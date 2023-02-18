from tkinter import *

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

options_var = IntVar() #라디오버튼은 여러 개 중에서 하나만 선택가능하기에 변수는 하나만 있어도 됨
                       #만약 value가 문자로 하고 싶을 경우 StringVar()로 지정하면 됨
option1 = Radiobutton(root, text="option1", value=1, variable=options_var)
option1.select()
option2 = Radiobutton(root, text="option2", value=2, variable=options_var)
option3 = Radiobutton(root, text="option3", value=3, variable=options_var)

option1.pack()
option2.pack()
option3.pack()

def btncmd():
    print(options_var.get()) #선택된 라디오 항목의 값(value)을 출력
btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않게 함