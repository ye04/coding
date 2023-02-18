from tkinter import *

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)



root.mainloop() #창이 닫히지 않게 함