import sqlite3
con=sqlite3.connect("sqlite.db")
data=con.execute("select * from data where city!='jaipur'")
for m in data:
    print(m)
con.close