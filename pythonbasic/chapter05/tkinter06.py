from tkinter import*
import tkinter.messagebox

window = Tk()
window.geometry("400x400")
window.title("반려동물 선택하기")

#메서드
def myFun():
    if var.get() == 1:
        labelImage.configure(Image=photo1)
    elif var.get() == 2:
        labelImage.configure(image=photo2)
    else:
        labelImage.configure(image=photo3)
        
#메인 
labelText = Label(window, text="좋아하는 반려동물 투표", fg="blue", font=("궁서체, 20"))

var = IntVar()
rb1=Radiobutton(window, text="강아지", variable= var, value =1)
rb2=Radiobutton(window, text="고양이", variable= var, value =2)
rb3=Radiobutton(window, text="토끼", variable= var, value =3)
buttonOk=Button(window, text="사진보기", command= myFun)

photo1=PhotoImage(file="C:/Users/soldesk/Desktop/resource/GIF/dog4.gif")
photo2=PhotoImage(file="C:/Users/soldesk/Desktop/resource/GIF/cat.gif")
photo3=PhotoImage(file="C:/Users/soldesk/Desktop/resource/GIF/rabbit.gif")

photoinit = PhotoImage(file="C:/Users/soldesk/Desktop/resource/GIF/cat2.gif")

labelImage = Label(window, width=200, height=200, image=photoinit, bg="yellow")



labelText.pack(padx= 5, pady= 5)
rb1.pack()
rb2.pack()
rb3.pack()
buttonOk.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)
window.mainloop()