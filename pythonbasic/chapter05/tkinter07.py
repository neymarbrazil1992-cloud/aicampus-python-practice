from tkinter import *

window = Tk()
'''
button1 = Button(window, text="버튼 1")
button2 = Button(window, text="버튼 2")
button3 = Button(window, text="버튼 3")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
'''

btnList = [""]*10

for i in range(0,10):
    btnList[i] = Button(window, text="버튼"+str(i+1))
    
for btn in btnList:
    btn.pack(side=LEFT)


window.mainloop()