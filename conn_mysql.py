#!/usr/bin/python3
# Python manipulates MySQL CRUD operations

import pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     password = '12345678',
                     db = 'mysql'
                     )


cur = db.cursor()

#CRUD,create databas class
cur.execute('CREATE DATABASE class;')

cur.execute('USE class;')

#create table student
cur.execute('CREATE TABLE student(name VARCHAR(20),age TINYINT(3));')

#insert
sql = 'INSERT INTO student (name,age) VALUES (%s,%s)'
cur.execute(sql,('Selina',18))
db.commit()

#select 
cur.execute('SELECT * FROM student;')
print(cur.fetchone())


db.close()

cur.close()
