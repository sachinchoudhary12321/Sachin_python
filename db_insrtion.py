import sqlite3
con=sqlite3.connect("sqlite.db")

con.execute('''
create table data(
st_id VARCHAR(100),
st_name VARCHAR(100),
city VARCHAR(100))
''')
con.close