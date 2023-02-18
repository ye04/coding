from tkinter import *

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

checkvar = IntVar() #체그바에 int형으로 값을 저장한다 --> 나의 변수의 값들은 int 가 될 것이다
checkbox = Checkbutton(root, text="check", variable=checkvar) #체크 되었을 떄와 해제되었을 떄의 값을 변수에 저장
checkbox.select() #미리 선택해놓기
checkbox.deselect()
checkbox.pack()

checkvar2 = IntVar() #서로 다른 체크박스는 서로 다른 값을 저장하므로 변수도 각각 지정되어야함
checkbox2 = Checkbutton(root, text="check2", variable=checkvar2)
checkbox2.pack()

def btncmd():
    print(checkvar.get()) #값이 0이면 체크해제 1이면 체크됨
    print(checkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않게 함



