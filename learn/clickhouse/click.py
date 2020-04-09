from clickhouse_driver import Client
import pandas as pd

# Client
settings = {'max_block_size': 100000,'max_threads': 2}
client = Client(host='192.168.62.134',password='123456',settings=settings,compression=True)
print(client.execute("show databases"))
print(client.execute("select * from click.mt limit 2"))
print(client.execute("use click"))
print(client.execute("create table if Not Exists driver(x Int16,name String)ENGINE=TinyLog"))

# print(client.execute("insert into driver values",[{'x':2,'name':'xxx'},{'x':2,'name':'xxx'}]))

# print(client.execute("insert into driver(x) values",[[100],[200]]))

print(client.execute("insert into driver (x,name) values",[[1000,"xz"],[2000,"dasd"]]))
# print(client.execute("insert into driver values",[[200,'xzc']]))
# print(client.execute("select sum(x) from driver", with_column_types=True))

# settings = {'max_block_size': 100000}
# rows_gen = client.execute_iter('QUERY WITH MANY ROWS', settings=settings)
# data = client.execute_iter("select * from ontime limit 10000000")
# for i in data:
#     print(i)
#print(data)

#print(data.columnar)
# data = client.execute("select * from mt limit 2", with_column_types=True, columnar=True)
# columns = []
# for i in data[1]:
#     columns.append(i[0])
# print(data[0])
# print(columns)
# df1 = pd.DataFrame(data[0],dtype=["int64","string"], columns=columns)
# print(df1)

# print(client.execute("show tables", with_column_types=True, columnar=True))
# print(client.execute("show tables", columnar=True))
# print(list(client.execute("show tables", columnar=True)[0]))

# df2 = pd.DataFrame()
# df2.append
# print(df2)

# pd.concat()

# print(df1.dtypes)
# settings = {'max_block_size': 100000}
# rows_gen = client.execute_iter('QUERY WITH MANY ROWS', settings=settings)
# for row in rows_gen:
#     print(row)


from datetime import datetime

progress = client.execute_with_progress("select * from mt", with_column_types=True)
timeout = 0.3

started_at = datetime.now()

for num_rows, total_rows in progress:
    print(num_rows)
    print(total_rows)
    if total_rows:
        done = float(num_rows) / total_rows
    else:
        done = total_rows

    now = datetime.now()
    
    print(done)
    elasped = (now - started_at).total_seconds()
    print(elasped)
    if elasped > timeout and done < 0.5:
        client.cancel()
        break

print("\n\n")
rv = progress.get_result()
print(rv)
# print("\n\n")
# for i in rv:
#     print(i)

    