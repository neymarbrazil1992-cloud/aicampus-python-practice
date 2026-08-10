from tkinter import *
import tkinter.messagebox

#메서드 
def keyEvent(event):
    tkinter.messagebox.showinfo("키보드 이벤트", "눌린 키: " + chr(event.keycode))

#메인 
window=Tk()
window.bind("<Key>",keyEvent)
window.mainloop()