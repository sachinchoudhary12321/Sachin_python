import sqlite3
con=sqlite3.connect("sqlite.db")
m=con.execute("select * from data ")
for x in m:
    print(x)
a=input("delete by name : ")
m=con.execute("delete from data where st_name =?",(a,))
con.commit()
m=con.execute("select * from data ")
for x in m:
    print(x)
m=con.execute("select * from data ")
con.close()
