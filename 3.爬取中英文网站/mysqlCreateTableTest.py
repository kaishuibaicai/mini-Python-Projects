import pymysql

conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost')
cur = conn.cursor()
cur.execute('create table znEnPostTest (id integer unsigned auto_increment, postTitle varchar(50), primary key id)')
cur.execute('insert into znEnPostTest (postTitle) values (%s)', ['post1'])
conn.commit()
cur.close()