from tkinter import *
import tkinter.messagebox

window = Tk()

#메서드 
def myfun():
    if chk.get() == 0:
        tkinter.messagebox.showinfo("", "CheckButton is OFF")
    else:
        tkinter.messagebox.showinfo("", "CheckButton is ON")
        
# main
chk = IntVar() #정수값 반환 
cb1 = Checkbutton(window, text="Click this Button", variable=chk, command=myfun)

cb1.pack()
window.mainloop()