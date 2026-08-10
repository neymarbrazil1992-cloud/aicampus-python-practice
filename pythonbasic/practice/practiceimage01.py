import os
from tkinter import *
import tkinter.messagebox

folder_path = "C:/Users/soldesk/Desktop/resource/GIF"

window = Tk()
window.title("이미지 뷰어")

file_list = [f for f in os.listdir(folder_path) if f.endswith(".gif")]

listbox = Listbox(window, width=20, height=20)
listbox.pack(side=LEFT, fill=Y)

for name in file_list:
    listbox.insert(END, name)

image_label = Label(window)
image_label.pack(side=RIGHT)

current_photo = None

def on_select(event):
    global current_photo
    selection = listbox.curselection()
    if not selection:
        return
    filename = listbox.get(selection[0])
    full_path = os.path.join(folder_path, filename)
    current_photo = PhotoImage(file=full_path)
    image_label.config(image=current_photo)

    # 체크박스가 켜져 있으면 확인창 표시
    if chk.get() == 1:
        tkinter.messagebox.showinfo("알림", f"{filename} 을(를) 선택했습니다")

listbox.bind("<<ListboxSelect>>", on_select)

# 체크버튼: 선택 시 알림 켜기/끄기
chk = IntVar()
cb1 = Checkbutton(window, text="선택 시 알림 보기", variable=chk)
cb1.pack(side=BOTTOM)

window.mainloop()