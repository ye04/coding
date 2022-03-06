from tkinter import *
root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

#스크롤바--> 한 프레임 안에 있는 어떤 위젯을 연결시켜 스크롤 가능하게 함

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") #y를 채움

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set) #스크롤 되는 대상의 y 를 scrollbar로 컨트롤함
for i in range(1,32):
    listbox.insert(END, i)
listbox.pack(side="left")

#listbox 와 scrollbar를 연결
scrollbar.config(command=listbox.yview) #리스트박스의 yview를 업데이트 함.
root.mainloop() #창이 닫히지 않게 함