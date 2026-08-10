import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QKeyEvent
from PyQt5.QtCore import Qt

print("현재 작업 디렉터리 :", os.getcwd())

current_dir = os.path.dirname(os.path.abspath(__file__))
fnameList = [os.path.join(current_dir, f"jeju{i}.gif") for i in range(1, 10)]

# 이미지 목록 확인
for f in fnameList:
    if not os.path.exists(f):
        print(f"이미지 파일이 존재하지 않습니다: {f}")


class PhotoAlbum(QWidget):
    
    # 생성자
    def __init__(self):
        super().__init__()
        self.num = 0
        self.initUI() # 생성자에서 전체 프로그램을 호출

    def initUI(self):
        self.setWindowTitle("디지털 앨범")
        self.setGeometry(100, 100, 700, 500)

        # 이미지 라벨 (place 대응 -> setGeometry로 절대좌표 배치)
        self.pLabel = QLabel(self)
        self.pLabel.setGeometry(20, 50, 670, 400)
        self.updateImage()

        # 이전/다음 버튼
        self.btnPrev = QPushButton("<<이전", self)
        self.btnPrev.setGeometry(220, 10, 100, 30)
        self.btnPrev.clicked.connect(self.clickPrev)

        self.btnNext = QPushButton("다음<<", self)
        self.btnNext.setGeometry(400, 10, 100, 30)
        self.btnNext.clicked.connect(self.clickNext)

        # 키보드 이벤트를 받으려면 포커스 필요
        self.setFocusPolicy(Qt.StrongFocus)

    def updateImage(self):
        pixmap = QPixmap(fnameList[self.num])
        self.pLabel.setPixmap(pixmap)

    def clickPrev(self):
        self.num -= 1
        if self.num < 0:
            self.num = len(fnameList) - 1
        self.updateImage()

    def clickNext(self):
        self.num += 1
        if self.num >= len(fnameList):
            self.num = 0
        self.updateImage()

    # 키보드 이벤트 (tkinter의 bind 대응)
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_PageUp:
            self.clickNext()
        elif event.key() == Qt.Key_PageDown:
            self.clickPrev()
        elif event.key() == Qt.Key_Left:
            self.clickNext()
        elif event.key() == Qt.Key_Right:
            self.clickPrev()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhotoAlbum() # PhotoAlbum window=new PhotoAlbum()
    window.show()
    sys.exit(app.exec_())