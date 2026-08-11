import sqlite3


#연결후 데이터 베이스 생성 
con=sqlite3.connect("C:/workspace/aicampus_python/sqlite/soldesk")
cur = con.cursor()

#데이터 조회
cur.execute("select * from T_STU_INFO")

rows = cur.fetchall()
print(rows)

for r in rows : 
    print('ST_name:{0}, ST_code:{1}, ST_MAJ:{2}, ST_GRA:{3}, ST_PHO:{4}'.format(r[0], r[1], r[2], r[3], r[4]))

con.commit()

cur.close()
con.close()