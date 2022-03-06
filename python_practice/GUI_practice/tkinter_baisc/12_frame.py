from tkinter import *
root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

Label(root, text="top").pack(side="top")
Button(root, text="bottom").pack(side="bottom")
frame = Frame(root, relief="solid", bd=1) #relief--> 테두리 스타일
frame.pack(side="left", fill="both", expand=True) #디스플레이 할 때 정렬, 자기 칼럼을 꽉 채움, 화면 전체 꽉 채움
Button(frame, text="1").pack() #메인 윈도우가 아닌 프레임 안에 버튼을 넣음
Button(frame, text="2").pack()
Button(frame, text="3").pack()

frame2 = LabelFrame(root, text="frame2")
frame2.pack(side="right", fill="both", expand=True)
Button(frame2, text="1").pack()
Button(frame2, text="2").pack()
Button(frame2, text="3").pack()

root.mainloop() #창이 닫히지 않게 함