from tkinter import *

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

def create_new_file():
    print("create")
menu = Menu(root)
menu_file = Menu(menu, tearoff=0) #메인 윈도우가 아닌 menu 에 값을 만듦
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file) #제목은 file이고 그 안의 내용은 menu_file들임

menu.add_cascade(labe="Edit")
menu_language = Menu(menu, tearoff=0)
menu_language.add_radiobutton(label="Python")
menu_language.add_radiobutton(label="Java")
menu_language.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_language)

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)

root.mainloop() #창이 닫히지 않게 함