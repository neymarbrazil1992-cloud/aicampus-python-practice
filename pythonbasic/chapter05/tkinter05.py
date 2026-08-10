from tkinter import*
import tkinter.messagebox
window=Tk()

#함수 
def myFun():
    if var.get() == 1:
        label1.configure(text="Python")
    elif var.get() == 2:
        label1.configure(text="Springboot")
    else: 
        label1.configure(text="BigData")
        
#메인 
var = IntVar()
rb1 = Radiobutton(window, text="Python", variable=var, value=1, command=myFun)
rb2 = Radiobutton(window, text="SpringBoot", variable=var, value=2, command=myFun)
rb3 = Radiobutton(window, text="BigData", variable=var, value=3, command=myFun)

label1= Label(window, text="선택한 강좌: ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()

label1.pack()
window.mainloop()



