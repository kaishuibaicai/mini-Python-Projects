import pymysql

conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost')
cur = conn.cursor()


createTable = """CREATE TABLE znEnPostTest (
		 id INT UNSIGNED AUTO_INCREMENT,
		 postTitle VARCHAR(50), 
		 PRIMARY KEY (id) )"""
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
#cur.execute(createTable)
#cur.execute(sql) 
cur.execute('insert into znEnPostTest (postTitle) values (%s)', ['post1'])
cur.execute('insert into znEnPostTest (postTitle) values (%s)', ['post1'])
conn.commit()
cur.close()