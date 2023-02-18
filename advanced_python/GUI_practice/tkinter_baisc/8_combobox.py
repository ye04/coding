from tkinter import *
import tkinter.ttk as ttk

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

values = [i for i in range(1, 32)] # 1 ~ 31
combobox = ttk.Combobox(root, height=5, values=values, state="readonly") #readonly-->값 선택만 가능하고 사용자가 임의로 쓰지 못함.

combobox.set("default") #default value
combobox.current(0) #아이템(values) 중 첫번째것을 미리 선택해 놓음
combobox.pack()

def btncmd():
    print(combobox.get()) #선택된 값을 가져옴
btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않게 함