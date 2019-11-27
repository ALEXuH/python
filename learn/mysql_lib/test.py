import pymysql
conn = pymysql.connect(
    host='localhost', user='root', passwd='123456', db='bilibili', charset='utf8')

cur = conn.cursor()
cur.execute("sql")
conn.commit()