import sqlite3

#변수 
con, cur= None, None
data1, data2, data3, data4 ="","","",""
sql=""

#연결후 데이터 베이스 생성 
con=sqlite3.connect("C:/workspace/aicampus_python/sqlite/soldesk")
cur = con.cursor()

#테이블 생성 
cur.execute("create table userTable(id char(20), userName char(32), email char(32), birthYear int(20))")

ch = int(input("<입력>:1, <출력>:2 를 입력하세요"))

if ch == 1:
    while(True):
        data1 = input("사용자 이름 >>")
        if data1=="":
            break
        data2=input("사용자 이름 >> ")
        data3=input("사용자 이메일 >> ")
        data4=input("사용자 생년월일 >> ")
        sql = "insert into userTable values(?,?,?,?)"
        cur.execute(sql, (data1,data2,data3,data4))
        
    con.commit()
    print("데이터 입력 완료")
elif ch == 2:
    

cur.close()
con.close()