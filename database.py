# -*- coding: utf-8 -*-
"""
database.py
- SQLite 연결 및 쿼리를 전담하는 QuizDatabase 클래스
- 화면(UI) 코드는 이 클래스의 메서드만 호출해서 DB에 접근한다.
"""

import sqlite3
import random

class QuizDatabase:
    
    #생성자 db_path = ""
    def __init__(self, db_path="quiz.db"): #데이터베이스 생성 및 연결 + 테이블 까지 자동으로 끝남
        self.db_path = db_path
        self.init_db() #생성
        
    def get_connection(self): #연결 
        return sqlite3.connect(self.db_path)
    
    def init_db(self): #실행
        con = self.get_connection()
        cur = con.cursor() #--> 연결후 실행
        
         #primary key, autoincrement(++), NOT NULL(반드시 입력칸)
         
        cur.execute("""
            CREATE TABLE IF NOT EXISTS QUIZ (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                choice1 TEXT NOT NULL,
                choice2 TEXT NOT NULL,
                choice3 TEXT NOT NULL,
                choice4 TEXT NOT NULL,
                answer INTEGER NOT NULL
            )
        """)
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS SCORE (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                played_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # executemany --> (한번에) 데이터의 중복을 막아줌 
        cur.execute("SELECT COUNT(*) FROM QUIZ")
        if cur.fetchone()[0] == 0:
            sample_questions = [
                ("대한민국의 수도는?", "부산", "서울", "인천", "대구", 2),
                ("파이썬에서 리스트를 만드는 기호는?", "{}", "()", "[]", "<>", 3),
                ("1년은 몇 개월?", "10", "11", "12", "13", 3),
                ("HTTP 상태코드 중 '찾을 수 없음'은?", "200", "301", "404", "500", 3),
                ("SQLite는 어떤 종류의 DB?", "서버형", "파일형(경량)", "그래프형", "메모리 전용", 2),
                ("파이썬 리스트의 인덱스는 몇 번부터 시작?", "0", "1", "-1", "2", 1),
                ("물의 화학식은?", "CO2", "O2", "H2O", "NaCl", 3),
                ("자바에서 클래스를 만드는 키워드는?", "def", "class", "func", "struct", 2),
            ]
            cur.executemany( # executemany: 데이터의 중복을 막아줌
                """INSERT INTO QUIZ
                   (question, choice1, choice2, choice3, choice4, answer)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                sample_questions
            )

        con.commit()
        con.close()
        
    def fetch_random_qustions(self, n=5):
        con = self.get_connection()
        cur = con.cursor()
        cur.execute("SELECT id, question, choice1, choice2, choice3, choice4, answer from QUIZ")
        rows = cur.fetchall() #db 문제 전체를 가져옴
        con.close()
        
        random.shuffle(rows) # 데이터를 섞은 뒤 자르기 (다른 sql에서는 Order by random() 사용)
        return rows[:n] #섞은 리스트에서 앞 5개만 반환
    
    def save_score(self, name, score):
        con = self.get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO SCORE (name, score) VALUES (?,?)", (name, score))
        con.commit()
        con.close()
        
    def fetch_ranking(self, top=10):
        con = self.get_connection()
        cur = con.cursor()
        cur.execute(
            "SELECT name, score, played_at FROM SCORE ORDER BY score DESC, played_at ASC LIMIT ?",
            (top,)
            )
        rows = cur.fetchall()
        con.close()
        