import sqlite3 as sql

print("STUDENT DATABASE!!")
con=sql.connect('student_database.db')
print ("Database Created Successfully!!")
cur=con.cursor()
cur.execute("create table login_data (enrollment numeric,username text,password text)")
print("Table login_data created successfully!!")
cur.execute("create table user_data (enrollment numeric,name text, phone numeric, user_pass text )")
print("Table user_data created successfulyy!!")
print("All operations done Successfully!!")

print("FACULTY DATABASE!!")
con=sql.connect('faculty_database.db')
print ("Database Created Successfully!!")
cur=con.cursor()
cur.execute("create table login_data (id integer primary key,username text,password text)")
print("Table login_data created successfully!!")
cur.execute("create table user_data (id integer primary key, name text, phone numeric, user_pass text )")
print("Table user_data created successfulyy!!")
con.commit()
con.close()
print("All operations done Successfully!!")
