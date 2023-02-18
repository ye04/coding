from tkinter import *
import os

root = Tk()
root.title("Untitled - Notepad")
root.geometry("640x480")

frame = Frame(root)
frame.pack(fill="both", expand=True)
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
txt = Text(frame, yscrollcommand = scrollbar.set)
txt.pack(fill="both", expand=True)
scrollbar.config(command=txt.yview)

#open, save file
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): #파일이 있으면 True 없으면 False
        with open(filename, "r") as file: #파일 열기/file이라는 변수로 변환
            txt.delete("1.0", END) #원래 있던 내용은 삭제하고 불러오기
            txt.insert(END, file.read())  #파일의 내용(file.read)을 텍스트 엔트리 마지막에 더해서 텍스트 창에 표시되게 함

def save_file():
    with open(filename, "w") as file:
        file.write(txt.get("1.0", END)) #텍스트에서 쓰여진 모든 내용 (처음부터 끝까지) 가져와서 파일에 내용을 넣음
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New")
menu_file.add_command(label="New Window")
menu_file.add_command(label="Open...", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Save As")
menu_file.add_separator()
menu_file.add_command(label="Page Setup...")
menu_file.add_command(label="Print...")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Undo", state="disable")
menu_edit.add_separator()
menu_edit.add_command(label="Cut", state="disable")
menu_edit.add_command(label="Copy", state="disable")
menu_edit.add_command(label="Paste", state="disable")
menu_edit.add_command(label="Delete", state="disable")
menu_edit.add_separator()
menu_edit.add_command(label="Search with Bing...", state="disable")
menu_edit.add_command(label="Find", state="disable")
menu_edit.add_command(label="Find Next", state="disable")
menu_edit.add_command(label="Find Previous", state="disable")
menu_edit.add_command(label="Replace...")
menu_edit.add_command(label="Go To...")
menu_edit.add_separator()
menu_edit.add_command(label="Select All")
menu_edit.add_command(label="Time/Date")
menu.add_cascade(label="Edit", menu=menu_edit)

menu_format = Menu(menu, tearoff=0)
menu_format.add_checkbutton(label="Word Wrap")
menu_format.add_command(label="Font...")
menu.add_cascade(label="Format", menu=menu_format)

menu_view = Menu(menu, tearoff=0)
menu_view.add_command(label="Zoom")
menu_view.add_checkbutton(label="Status Bar")
menu.add_cascade(label="View", menu=menu_view)

menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label="View Help")
menu_help.add_command(label="Send Feedback")
menu_edit.add_separator()
menu_help.add_command(label="About Notepad")
menu.add_cascade(label="Help", menu=menu_help)

root.config(menu=menu)







root.mainloop()