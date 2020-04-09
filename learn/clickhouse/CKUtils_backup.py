from enum import Enum
import pandas as pd
from clickhouse_driver import Client
import configparser
from os import path as _path
import os as _os


class CKUtils:
    def __init__(self, config_path):
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
        print(self.url)
        self.client = Client.from_url(url=self.url)
        self.tables = None

    def useDB(self, database):
        try:
            self.sql("USE "+database)
        except Exception as ex:
            print("Database %s not exists" % database)

    def create_table(self, createTableBean):
        if createTableBean is not None:
            return self.client.execute(createTableBean.sql)
        return None

    def data_migration(self, fromTable, toTable):
        print("aa")

    def fetch_table_name(self, table):
        if self.tables == None:
            self.tables = self.client.execute("SHOW TABLES", columnar=True)
            if len(self.tables) > 0:
                self.tables = list(self.tables)

    def query(self, query):
        try:
            result = self.client.execute(query, with_column_types=True)
            if len(result) > 0:
                cols_and_type = result[1]
                data = result[0]
                columns = [i[0] for i in cols_and_type]
                df = pd.DataFrame(data=data, columns=columns)
            else:
                return None
            return df
        except MemoryError:
            print("data is too large please use self.query_large_data()")

    def query_large_data(self, query):
        result_iter = self.client.execute_iter(query, with_column_types=True)
        df = pd.DataFrame
        print("aa")

    
    def query_large_data_iter(self):
        print("hello")

    def insert_one(self, table, values, columns=None):
        print("das")

    def insert_many(self, table, values, columns=None):
        print("hello")

    def sql(self, query):
        return self.client.execute(query)

    def close(self):
        self.client.disconnect()


# CRUD
config_name = "source.ini"
ck = CKUtils(config_name)
print(ck.client.connection)
print(ck.client.execute("show tables"))
print(ck.useDB("system1"))
print(ck.client.execute("show tables"))
# print(ck.client.execute("select * from mt limit 1"))
# print(ck.settings)
print("\n\n\n")
print(ck.client.settings)
print(ck.client.execute("select * from mt limit 2", with_column_types=True)[0])


class createTableBean:
    table_name = None
    columns_and_type = None
    engine = None
    primary_key = None
    partition_columns = None
    order_columns = None
    sql = None

    def __init__(self):
        super().__init__()
        self.init_sql()

    def check_type(self):
        print("aa")

    def init_sql(self):
        print("aa")


class engine(Enum):
    merge_tree = "MergeTree"
    replacing_merge_tree = "ReplacingMergeTree"
    summing_merge_tree = "SummingMergeTree"
    aggreating_merge_tree = "AggreatingMergeTree"
    tiny_log = "TinyLog"
    distribute = "Distribute"
    memory = "Memory"


print(engine.merge_tree.value)
