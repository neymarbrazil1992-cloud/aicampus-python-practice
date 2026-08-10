import sqlite3

# "D:/AI_Campus_2026/aicampu_python"
#"C:/workspace/aicampus_python/pythonbasic/sqlite"

#연결후 데이터 베이스 생성 
con=sqlite3.connect("C:/workspace/aicampus_python/sqlite/soldesk")
cur = con.cursor()

#데이터베이스에 테이블 생성 
cur.execute("create table T_STU_INFO(ST_name char(32), ST_code char(32), ST_MAJ char(32), ST_GRA char(32), ST_PHO char(32))")

con.commit() #완료

cur.close()
con.close()