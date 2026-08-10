import os 
from tkinter import*
from time import *

print("현재 작업 디렉터리 : ",  os.getcwd)

current_dir = os.path.dirname(os.path.abspath(__file__))
fnameList = [os.path.join(current_dir, f"jeju{i}.gif") for i in range (1,10)]
# print(fnameList)

#이미지 목록 확인 

for f in fnameList:
    if not os.path.exists(f):
        print("이미지 파일이 존재하지 않습니다.")
        
photoList = [None]*9
num=0

def clickPrev():
    global num 
    num -= 1
    
    if num < 0:
        num = len(fnameList)-1 # 8
        
    photo=PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo) 
    pLabel.image=photo
    
def pageDown(event):
    clickPrev()


#메인 
window = Tk()
window.geometry("700x500")
window.title("디지털 앨범")

#키보드 이벤트1
window.bind("<Next>", pageDown) #pgDn

#키보드 이벤트2
window.bind("<Left>", pageDown) # <- 이전 이미지 


#마우스 이벤트 
btnprev = Button(window, text="<<이전", command= clickPrev)
btnprev.place(x=250, y=10)


#첫 번째 이미지 적용 
photo = PhotoImage(file= fnameList[num])
pLabel = Label(window, image=photo)

pLabel.place(x=15, y=50)

window.mainloop()
