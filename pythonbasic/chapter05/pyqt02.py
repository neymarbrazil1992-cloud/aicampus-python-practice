import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap

#QWidget(창) 안에 QVBoxLayout(배치판)을 넣고, 그 배치판 안에 QLabel(이미지 담는 라벨)을 넣는 박스안에 박스 구조 

app = QApplication(sys.argv)
#window(창) 만들기 -> 빈창을 하난 만들고, 제목을 "dog image로 설정해요"
window = QWidget()
window.setWindowTitle("Dog Image")
#배치 방식 정하기 -> 창안의 요소들을 세로로 쌀하 배치하는 레이아웃 객체를 만들어요
Layout = QVBoxLayout()
#이미지를 라벨에 담기 
Label1 = QLabel() #텍스트나 이미지를 담을수 있는 빈그릇을 만듬 
pixmap = QPixmap("C:/Users/soldesk/Desktop/resource/GIF/dog.gif") #경로
Label1.setPixmap(pixmap) #라벨 그릇에 이미지를 담음 
#조립하기 : 라벨을 레이아웃에 넣고, 그 레이우웃을 창에 붙인다 
Layout.addWidget(Label1)
window.setLayout(Layout)
#창 띄우고 실행 
window.show() #창을 화면에 보이게 하고 
sys.exit(app.exec_()) #프로그램이 계속 살아있게 만든다, 