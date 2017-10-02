import pymysql

conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost')
cur = conn.cursor()
cur.execute('create table postTest (id varchar(20) primary key, name varchar(20))')
cur.execute('insert into postTest (id, name) values (%s, %s)', ['1', 'Micheal'])
conn.commit()
cur.close()