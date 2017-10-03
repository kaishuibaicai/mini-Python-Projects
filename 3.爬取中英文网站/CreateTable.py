import pymysql

conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost')
cur = conn.cursor()


createTable = """CREATE TABLE znEnPost (
		 id INT UNSIGNED AUTO_INCREMENT NOT NULL,
		 postTitle VARCHAR(50) NOT NULL, 
		 EnText TEXT,
		 ZnText TEXT,
		 PRIMARY KEY (id, postTitle) )"""

cur.execute(createTable)

conn.commit()
cur.close()