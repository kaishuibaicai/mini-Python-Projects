import pymysql

conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost',charset='utf8')
cur = conn.cursor()

cur.execute(drop table znenpost)

createTable = """CREATE TABLE znenpost (
		 id INT UNSIGNED AUTO_INCREMENT NOT NULL,
		 postTitle VARCHAR(50) NOT NULL, 
		 EnText TEXT,
		 ZnText TEXT,
		 UNIQUE (id, postTitle))"""

cur.execute(createTable)

conn.commit()
cur.close()