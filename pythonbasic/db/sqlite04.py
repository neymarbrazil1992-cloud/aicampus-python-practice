import sqlite3


#연결후 데이터 베이스 생성 
con=sqlite3.connect("C:/workspace/aicampus_python/sqlite/soldesk")
cur = con.cursor()



con.commit()

cur.close()
con.close()