import dask.dataframe as dd
import datetime
import json
import os
import re
import pandas as pd
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from infi.clickhouse_orm.database import Database
from sqlalchemy import create_engine
from time import sleep


class clickpandas:
    
    def __init__(self, config_path):
        
        self.config_path = config_path
        
        with open(os.path.expanduser(self.config_path), 'r') as fp:
            self.config = json.load(fp)
        
        self.db_name = self.config['db_name']
        self.db_url = self.config['db_url']
        self.username = self.config['username']
        self.password = self.config['password']
        self.uri = 'clickhouse://' + self.username + ':' + self.password + '@' + self.db_url.split('//')[1] + '/' + self.db_name
        self.db = Database(self.db_name, db_url=self.db_url, username=self.username, password=self.password)
        
        self.technical_attr = {'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
                               '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
                               '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
                               '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
                               '__subclasshook__', '__weakref__', '_database', '_fields', '_writable_fields', 
                               'create_table_sql', 'drop_table_sql', 'engine', 'from_tsv', 'get_database', 
                               'get_field', 'objects_in', 'readonly', 'set_database', 
                               'system', 'table_name', 'to_dict', 'to_tsv'}
        
        self.dt_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
        self.col_pattern = r'select(.*?)from'
        self.table_pattern = r'from (.*?) '

    def insert_rows(self, data_buffer, datamodel):
        
        self.db.create_table(datamodel)
        try:
            self.db.insert(data_buffer)
        except:
            traceback.print_exc()

    def execute_query(self, f, **kwargs):
        
        data_buffer = []
        
        for row in self.db.select(f(**kwargs)):
            quoted_attributes = [getattr(row, attr) for attr in dir(row) if attr not in self.technical_attr]
            data_buffer.append(quoted_attributes)
        
        if 'row' in dir():
            columns = [attr for attr in dir(row) if attr not in self.technical_attr]
        else:
            columns = ['no_data']
        
        return pd.DataFrame(data_buffer, columns=columns)
   
    def proxy_execute(self, template, start, end):
        
        def fill_template(template, start, end):
            
            return template.format(start, end)
            
        result = self.execute(fill_template, template=template, start=start, end=end)
        
        return result 

    def __get_time_splits(self, query, n_splits=2):
        
        timestamps = [datetime.datetime.strptime(x.group(), "%Y-%m-%d %H:%M:%S") \
        for x in re.finditer(self.dt_pattern, query)]
        template = re.sub(self.dt_pattern, '{}', query)
        start = min(timestamps)
        diff = (max(timestamps)-start) / n_splits
        diff -= datetime.timedelta(microseconds=diff.microseconds)
        
        for i in range(1, n_splits+1):
            
            yield (template, start + diff * (i-1), start + diff * i)

    def parallel_execute(self, f, n_splits=2, **kwargs):
        
        query = f(**kwargs)
        executor = ProcessPoolExecutor(n_splits)
        futures = [executor.submit(self.proxy_execute, date_range[0], date_range[1], date_range[2]) \
        for date_range in self.__get_time_splits(query, n_splits)]
        
        df = pd.DataFrame()
        for proc in as_completed(futures):
            df = pd.concat([df, proc.result()])
        
        return df

    def out_of_core_execute(self, timestamp_column, f, blocksize=268435456, **kwargs):
        
        query = f(**kwargs)
        timestamps = [[str(date_range[1]), str(date_range[2])] for date_range in self.__get_time_splits(query, 1)][0]
        columns = re.findall(self.col_pattern, query)[0].replace(' ', '').split(',')
        table = re.findall(self.table_pattern, query)[0].split('.')[1]
        df = dd.read_sql_table(table=table, divisions=timestamps, uri=self.uri, columns=columns,
                               index_col=timestamp_column, bytes_per_chunk=blocksize)
        
        return df