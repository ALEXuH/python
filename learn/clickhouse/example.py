# from CKUtils import *

# CRUD
from learn.clickhouse.CkUtils import CKUtils

ck = CKUtils()
print(ck.client.connection)
print(ck.client.execute("show tables"))
print(ck.useDB("system1"))
print(ck.client.execute("show tables"))
# print(ck.client.execute("select * from mt limit 1"))
# print(ck.settings)
print("\n\n\n")
print(ck.client.settings)
print(ck.client.execute("select * from mt limit 2", with_column_types=True)[0])
print("--------")
print(ck.data_migration("user",["user1","user2"],["id","username","password","gender","createAt"],["id","username","password","gender","createAt"]))
print("---------------")
print(ck.insert("driver", data=[[400, "xzc"], [
      13000, "dasd"]], columns=["x", "name"]))
print(ck.insert("driver", data=[[400, "xzc"], [13000, "dasd"]]))

# print("\n\n")
# result = ck.query_iter("select * from mt", with_column_types=True)

# print(result[1])
# for i in result[0]:
#     print(i)

#ck.create_merge_tree(table_name="cc",engine="SummingMergeTree",columns=[('id', 'UInt16'), ('name', 'String'), ('age', 'UInt16'), ('birthDay', 'DateTime')], partition_column="birthDay", order_column=["id","name"], extra_column=["age","birthDay"])
#ck.client.execute("CREATE TABLE user3 (`id` Nullable(UInt16), `username` Nullable(String), `password` Nullable(String), `gender` Nullable(String), `createAt` Nullable(DateTime)) ENGINE = TinyLog")
#ck.create_distribute(table_name="dd",columns=[('id', 'UInt16'), ('name', 'String'), ('age', 'UInt16'), ('birthDay', 'DateTime')], cluster="test_unavailable_shard",database="click", table="t")
# result = ck.query_process("select * from user1")
# print(result[0])
# print(result[1].byte)
# print(result[1].rows)
# print(result[1].elapsed)
# for row in result[0]:
#     print(row)

# print(ck.query_panda_df("select * from mt limit 2"))
# result1 = ck.query_panda_df("select * from mt limit 2")
# result2 = ck.query_panda_df("select * from mt limit 2")

# print(pd.concat([result1, result2]))

# print("\n\n\n")
# print(ck.query("select * from mt limit 2"))
# print("\n")
# print(ck.query_iter("select * from mt limit 2"))
# print("\n")
# print(ck.query_process("select * from mt limit 2"))

r1 = ck.query("select * from mt limit 2")
r2 = ck.query_iter("select * from mt limit 2")
r3 = ck.query_process("select * from mt limit 2")

# print(r1[1].column_with_type)
# print(r1[1].rows)
# print(r1[1].byte)
# print(r1[1].elapsed)

# print("\n")
# print(r2)
# print("\n")
# print(r3[1].column_with_type)
# print(r3[1].rows)
# print(r3[1].byte)
# print(r3[1].elapsed)

# pd.DataFrame.to_json(index=)
# print(r1[0])
# print(r1[0].to_csv(path_or_buf="ccc", index=False ))
r1 = pd.read_csv("ccc")
print(r1)
print("\n")
print(r1.values.tolist())
print(r1.columns.values.tolist())
print("\n")

# print(ck.data_load_csv("ccc","mt"))
print(ck.insert("driver", data=[[400, "xzc"], [
      13000, "dasd"]], columns=["x", "name"]))
