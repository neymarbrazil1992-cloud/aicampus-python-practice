# -*- coding: utf-8 -*-
"""
screens.py
- 화면(위젯) 클래스들만 모아둔 파일
- DB 접근은 직접 하지 않고, main.py에서 주입받은 QuizDatabase 객체를 통해서만 처리한다.
"""

from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout,
    QLineEdit, QMessageBox, QListWidget
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


# ---------------------------------------------------------
# 화면 1: 시작 화면
# ---------------------------------------------------------

class StartScreen(QWidget): #상속
    
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("🧠 상식 퀴즈 게임")
        title.setFont(QFont("맑은 고딕", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("이름을 입력하세요")
        self.name_input.setFixedWidth(200)

        start_btn = QPushButton("퀴즈 시작")
        start_btn.clicked.connect(self.start_quiz)

        rank_btn = QPushButton("랭킹 보기")
        rank_btn.clicked.connect(self.go_ranking)

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(self.name_input, alignment=Qt.AlignCenter)
        layout.addSpacing(10)
        layout.addWidget(start_btn, alignment=Qt.AlignCenter)
        layout.addWidget(rank_btn, alignment=Qt.AlignCenter)
        self.setLayout(layout)
        
    def start_quiz(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "입력 오류", "이름을 입력해주세요!")
            return
        quiz_screen = self.stack.widget(1)
        quiz_screen.start(name)
        self.stack.setCurrentIndex(1)

    def go_ranking(self):
        ranking_screen = self.stack.widget(2)
        ranking_screen.load_ranking()
        self.stack.setCurrentIndex(2)
        
# ---------------------------------------------------------
# 화면 2: 퀴즈 진행 화면
# ---------------------------------------------------------
class QuizScreen(QWidget):
    def __init__(self, stack, db):  #의존성 주입 : 화면 전환
        super().__init__()
        self.stack = stack #바뀐 화면  Q StackedWidgt
        self.db = db # 데이터 

        self.questions = [] # 5개의 셔플 문제 
        self.current_idx = 0 # 문제 카운트 
        self.score = 0 # 맞춘 갯수 
        self.player_name = "" # 화면에서 입력받은 이름 

        layout = QVBoxLayout()
        self.progress_label = QLabel()
        self.progress_label.setAlignment(Qt.AlignRight)

        self.question_label = QLabel()
        self.question_label.setFont(QFont("맑은 고딕", 16, QFont.Bold))
        self.question_label.setWordWrap(True)

        self.choice_buttons = []
        btn_layout = QVBoxLayout()
        for i in range(4):
            btn = QPushButton()
            btn.clicked.connect(lambda checked, idx=i: self.check_answer(idx))
            btn_layout.addWidget(btn)
            self.choice_buttons.append(btn)

        layout.addWidget(self.progress_label)
        layout.addWidget(self.question_label)
        layout.addSpacing(10)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def start(self, name): #5개의 문제 가져오기 
        self.player_name = name
        self.questions = self.db.fetch_random_questions(5)
        self.current_idx = 0
        self.score = 0
        self.show_question()

    def show_question(self): #화면에 그리기 
        q = self.questions[self.current_idx]
        _, question, c1, c2, c3, c4, answer = q
        self.progress_label.setText(
            f"문제 {self.current_idx + 1} / {len(self.questions)}   점수: {self.score}"
        )
        self.question_label.setText(question)
        for btn, choice in zip(self.choice_buttons, [c1, c2, c3, c4]):
            btn.setText(choice)
            btn.setStyleSheet("")

    def check_answer(self, idx): # 버튼 클릭시 정답 채점 
        _, question, c1, c2, c3, c4, answer = self.questions[self.current_idx]
        correct_idx = answer - 1

        if idx == correct_idx:
            self.score += 1
            self.choice_buttons[idx].setStyleSheet("background-color: #a5d6a7;")
        else:
            self.choice_buttons[idx].setStyleSheet("background-color: #ef9a9a;")
            self.choice_buttons[correct_idx].setStyleSheet("background-color: #a5d6a7;")

        for btn in self.choice_buttons:
            btn.setEnabled(False) #  오답은 비활성화 

        QTimer.singleShot(700, self.next_question) # 700: 0.7초

    def next_question(self): #다음문제로 넘어감 
        for btn in self.choice_buttons:
            btn.setEnabled(True)

        self.current_idx += 1
        if self.current_idx < len(self.questions):
            self.show_question()
        else:
            self.db.save_score(self.player_name, self.score)
            QMessageBox.information(
                self, "결과",
                f"{self.player_name}님, 최종 점수: {self.score} / {len(self.questions)}"
            )
            ranking_screen = self.stack.widget(2)
            ranking_screen.load_ranking()
            self.stack.setCurrentIndex(2)       
            
            
# ---------------------------------------------------------
# 화면 3: 랭킹 화면
# ---------------------------------------------------------
class RankingScreen(QWidget):
    def __init__(self, stack, db):
        super().__init__()
        self.stack = stack
        self.db = db

        layout = QVBoxLayout()

        title = QLabel("🏆 랭킹")
        title.setFont(QFont("맑은 고딕", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.rank_list = QListWidget()

        back_btn = QPushButton("처음으로")
        back_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(title)
        layout.addWidget(self.rank_list)
        layout.addWidget(back_btn)
        self.setLayout(layout)

    def load_ranking(self):
        self.rank_list.clear()
        rows = self.db.fetch_ranking()
        if not rows:
            self.rank_list.addItem("아직 기록이 없습니다.")
            return
        for i, (name, score, played_at) in enumerate(rows, start=1):
            self.rank_list.addItem(f"{i}위  {name}  -  {score}점  ({played_at})")