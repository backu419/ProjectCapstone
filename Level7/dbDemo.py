import sqlite3
connect = sqlite3.connect("C://sqlite//hcl.db")
cur = connect.cursor()
# sql = """insert into filelog values(?, ?);"""
# data = (100, 'C://jose1//demo.txt')
# cur.execute(sql,data)
# connect.commit()
#cur.execute("select * from filelog")
cur.execute("select * from filelog where id=100");
rows = cur.fetchall()
for r in rows:
    print(r)
