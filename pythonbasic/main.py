# -*- coding: utf-8 -*-
"""
main.py
- 프로그램 진입점
- QuizDatabase(DB 담당)와 각 Screen(화면 담당) 객체를 생성하고 연결한다.

실행 전 설치:
    pip install PyQt5

실행:
    python main.py

"""

import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget

from database import QuizDatabase
from screens import StartScreen, QuizScreen, RankingScreen

def main():
    db = QuizDatabase("quiz.db")
    
    app = QApplication(sys.argv)
    
    stack = QStackedWidget() #화면 생성시 인덱스 번호 생성 스택 구조 
    
    #스크린 화면 클래스 
    start_screen = StartScreen(stack)
    quiz_screen = QuizScreen(stack, db)
    ranking_screen = RankingScreen(stack, db)
    
    stack.addWidget(start_screen)
    stack.addWidget(quiz_screen)
    stack.addWidget(ranking_screen)
    
    stack.setWindowTitle("상식 퀴즈 게임 - PyQt5 + SQLite")
    stack.resize(420,400)
    stack.show()
    
    sys.exit(app.exec_())
    
#메인 메서드 생성 

if __name__ == "__main__":
    main()