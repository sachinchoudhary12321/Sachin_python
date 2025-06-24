import sqlite3
name=input("enter the name")
id=input("enter the id ")
city=input("enter the city")
con=sqlite3.connect("sqlite.db")
ins='''INSERT INTO DATA values(?,?,?)'''#here we know the sequence of column name
con.execute(ins,(id,name,city))
con.commit()
con.close()
