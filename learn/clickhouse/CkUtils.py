import pandas as pd
from clickhouse_driver import Client
import configparser
from os import path as _path
import os as _os
import logging as _logging
import logging.handlers
from datetime import datetime

_logging.basicConfig(
    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=_logging.INFO)


class CKUtils:

    progress_timeout = 10
    progress_percent = 0.5

    def __init__(self, config_path="config.ini"):
        cf = configparser.ConfigParser()
        config_path = _path.join(_path.dirname(
            _os.path.realpath(__file__)), config_path)
        cf.read(config_path, "utf-8")
        self.settings = cf.items(section="Settings")
        self.db = cf.get("Clickhouse", 'database')
        self.host = cf.get("Clickhouse", 'host')
        self.user = cf.get("Clickhouse", 'user')
        self.password = cf.get("Clickhouse", 'password')
        self.port = cf.get("Clickhouse", 'port')
        self.url = "clickhouse://%s:%s@%s:%s/%s" % (
            self.user, self.password, self.host, self.port, self.db)
        if self.settings.count != 0:
            sets = ""
            for setting in self.settings:
                sets = sets + "&" + setting[0] + "=" + setting[1]
            sets = "?" + sets[1:]
            self.url = self.url + sets
        _logging.info(self.url)
        self.client = Client.from_url(url=self.url)
        self.tables = None

    def useDB(self, database):
        try:
            self.sql("USE "+database)
        except Exception as ex:
            _logging.error("self.useDB(): Database %s not exists" % database)

    def createDB(self, database):
        self.sql("CREATE DATABASE "+database)

    def data_migration(self, fromTable, toTable, fromColumns, toColumns):
        """
        Inserts data from one table into anothers
        
        :param fromTable: from table name
        :param toTable: to table or tables name can be str or list
        :param fromColumns: fields of the from table
        "param toColumns: fiedls of  the to table  

        :return: None
        """

        try:
            querys = []
            toCols = ""
            fromCols = ""
            if (type(toColumns) == list):
                toCols = ",".join(toColumns)
            else:
                toCols = toColumns
            if (type(fromColumns) == list):
                fromCols = ",".join(fromColumns)
            else:
                fromCols = fromColumns
            if type(toTable) == str:
                sql = "INSERT INTO " + toTable + \
                    "("+toCols + ") SELECT " + fromCols + " FROM " + fromTable
                querys.append(sql)
            elif type(toTable) == list:
                for table in toTable:
                    sql = "INSERT INTO " + table + \
                        "("+toCols + ") SELECT " + \
                          fromCols + " FROM " + fromTable
                    querys.append(sql)
            for query in querys:
                self.sql(query)
        except Exception:
            self.close()
            raise

    def drop_partition(self, table, partitions):
        for partition in partitions:
            self.sql("DROP TABLE %s PARTITION %s" % (table, partition))

    def query_all_table_name(self, table):
        """
        retrieve all table names in this DataBase
        """

        if self.tables == None:
            self.tables = self.client.execute("SHOW TABLES", columnar=True)
            if len(self.tables) > 0:
                self.tables = list(self.tables)

    def query_iter(self, query, with_column_types=True, convert_to_df=True):
        """
        Executes SELECT query with results streaming

        :param query: query that will be send to server.
        :param with_column_types: if specified column names and types will be
                                  returned alongside with result.
                                  Defaults to ``False``.
        :param: convert_to_df: if specified True will be returned DataFrame

        :return: * if with_column_types=False: iter-query-result can iterate
                 * if convert_to_df=False and with_column_types=True: iter-query-result without first column_with_type
                 * if convert_to_df=True and with_column_types=True: DataFrame
        """

        try:
            result = self.client.execute_iter(
                query, with_column_types=with_column_types)
            if with_column_types:
                for i in result:
                    column_with_type = i
                    break
                if convert_to_df:
                    columns = [i[0] for i in column_with_type]
                    result_list = []
                    for row in result:
                        result_list.append(row)
                    df = pd.DataFrame(data=result_list, columns=columns)
                    return df
                else:
                    return result
            else:
                return result
        except Exception as ex:
            self.close()
            raise

    def query_process(self, query, convert_to_df=True):
        """
        Executes SELECT query with progress information
        When select large dataset can retrieve part of the dataset
        
        DEFAULT:If 50 percent of the total data is not retrieved within 10s, 
        the following query is cancelled and the previously queried data is returned

        :param query: query that will be send to server.
        :param convert_to_df:  if specified True will be returned DataFrame

        :return: * if convert_to_df=True: (DataFrame, statistics) statistics: about last query execution
                 * if convert_to_df=False: (data, statistics) data: [(),()]


        """

        progress = self.client.execute_with_progress(
            query=query, with_column_types=True)
        started_at = datetime.now()
        for num_rows, total_rows in progress:
            if total_rows:
                done = float(num_rows) / total_rows
            else:
                done = total_rows
            now = datetime.now()
            elasped = (now - started_at).total_seconds()
            if elasped > self.progress_timeout and done < self.progress_percent:
                client.cancel()
                break
        rv = progress.get_result()
        att = statistics(self.client, rv[1])
        if convert_to_df:
            cols_and_type = rv[1]
            data = rv[0]
            columns = [i[0] for i in cols_and_type]
            df = pd.DataFrame(data=data, columns=columns)
            return (df, att)
        else:
            return (rv[0], att)

    def query(self, query, convert_to_df=True):
        """
        Executes SELECT query

        :param query: query that will be send to server.
        :param convert_to_df:  if specified True will be returned DataFrame

        :return: * if convert_to_df=True: (DataFrame, statistics) statistics: about last query execution
                 * if convert_to_df=False: (data, statistics) data: [(),()]

        """

        try:
            result = self.sql(query, with_column_types=True)
            if len(result) > 0:
                att = statistics(self.client, result[1])
                if convert_to_df:
                    cols_and_type = result[1]
                    data = result[0]
                    columns = [i[0] for i in cols_and_type]
                    df = pd.DataFrame(data=data, columns=columns)
                    return (df, att)
                else:
                    return (result, att)
            else:
                return None
        except Exception:
            self.close()
            raise

    def create_merge_tree(self, table_name, engine, columns, partition_column, order_column, extra_column=None, primary_key=None):
        cols = ""
        extra = ""
        for tup in columns:
            cols = cols + tup[0] + " " + tup[1] + ","
        cols = "(" + cols[0:-1] + ")"
        if extra_column is not None:
            if type(extra_column) == list:
                extra = "(" + ",".join(extra_column)+")"
            else:
                extra = extra_column
        if type(partition_column) == list:
            partition_column = "("+",".join(partition_column)+","
        if type(order_column) == list:
            order_column = "("+",".join(order_column)+")"
        query = "CREATE TABLE IF NOT EXISTS "+table_name + \
            cols+"ENGINE="+engine+"(" + extra+") PARTITION BY " \
            + partition_column + " ORDER BY "+order_column
        if primary_key is not None:
            if type(order_column) == list:
                primary_key = "("+",".join(primary_key)+")"
            query = sql + " PRIMARY KEY " + primary_key
        self.sql(query)

    def create_distribute(self, table_name, columns, cluster, database, table, split_shard_column=None):
        cols = ""
        for tup in columns:
            cols = cols + tup[0] + " " + tup[1] + ","
        cols = "(" + cols[0:-1] + ")"
        query = "CREATE TABLE IF NOT EXISTS "+table_name+cols+" ENGINE=Distributed(" \
            + cluster+","+database + "," + table
        if split_shard_column is None:
            query = query + ",rand())"
        else:
            query = query + split_shard_column + ")"
        self.sql(query)

    def create_tinylog(self, table_name, columns):
        cols = ""
        for tup in columns:
            cols = cols + tup[0] + " " + tup[1] + ","
        cols = "(" + cols[0:-1] + ")"
        query = "CREATE TABLE IF NOT EXISTS "+table_name + cols + "ENGINE=Memory"
        self.sql(query)

    def drop_table(self, table):
        query = "DROP TABLE IF EXISTS " + table
        self.sql(query)

    def data_export_csv(self, df, filepath):
        df.to_csv(path_or_buf=filepath, index=False)

    def insert(self, table, data, columns=None):
        """
        INSERT Data to table with type check

        :param table: table name
        :param data: insert Data like [[12,'da'],[231,'das']]
        :param columns: insert columns

        :return: insert counts

        """

        sql = "INSERT INTO %s " % table
        if columns is not None:
            sql = sql + "(" + ",".join(columns) + ") values "
        else:
            sql = sql + " values "
        _logging.info("INSERT SQL: "+sql)
        return self.client.execute(sql, data, types_check=True)

    def sql(self, query, with_column_types=False):
        """
        Execute all sql in clickhouse
        """

        try:
            _logging.info("QUERY: " + query)
            if with_column_types:
                return self.client.execute(query, with_column_types=with_column_types)
            else:
                return self.client.execute(query)
        except Exception as ex:
            self.close()
            raise

    def close(self):
        """
        Close the client 
        """
        self.client.disconnect()


class statistics:
    """
    statistics about last query execution.

    Attributes:
        rows: processed rows;
        byte: processed bytes;
        elapsed: elapsed time
        column_with_type: column_with_type like [(),()]
    """

    rows = 0
    byte = 0.0
    elapsed = 0.0
    column_with_type = None

    def __init__(self, client, column_with_type):
        self.rows = client.last_query.progress.rows
        self.byte = client.last_query.progress.bytes
        self.elapsed = client.last_query.elapsed
        self.column_with_type = column_with_type
