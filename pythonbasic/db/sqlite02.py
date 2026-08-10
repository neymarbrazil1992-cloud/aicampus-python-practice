import sqlite3


#연결후 데이터 베이스 생성 
con=sqlite3.connect("C:/workspace/aicampus_python/sqlite/soldesk")
cur = con.cursor()

#데이터 삽입 
cur.execute("insert into T_STU_INFO values('soldesk','160322','SW','4','010-1111-3333')")
cur.execute("insert into T_STU_INFO values('parksu','150321','SYSTEM','3','010-8888-7777')")
cur.execute("insert into T_STU_INFO values('kimchi','140321','Secure','2','010-9999-3333')")

id = cur.lastrowid #튜플의 수 
print(id)

con.commit()

cur.close()
con.close()