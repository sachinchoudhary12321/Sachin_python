import sqlite3
con=sqlite3.connect("sqlite.db")
m=con.execute("select * from data ")
for x in m:
    print(x)
a=input("enter the old name")
b=input("enter the new name")
m=con.execute("update data set st_name=? where st_name=?",(a,b,))
con.commit()
m=con.execute("select * from data ")
for x in m:
    print(x)
