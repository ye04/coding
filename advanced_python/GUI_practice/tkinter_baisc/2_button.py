from tkinter import *

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

btn1 = Button(root, text ="button1") #메인 윈도우에 나오고 글자도 디스플레이
btn1.pack() #화면에 디스플레이

btn2 = Button(root, padx=5, pady=10, text="button2") #패딩 추가
btn2.pack()
btn3 = Button(root, padx=10, pady=5, text="button3")
btn3.pack()
btn4 = Button(root, width=10, height=3, text="button4") #버튼의 크기 추가 (유동적인 패딩과는 다르게 절대적인 크기를 고정함)
btn4.pack()
btn5 = Button(root, fg="red", bg="yellow", text="button5") #fg-->foregrond(text color) bg-->background
btn5.pack()

photo = PhotoImage(file="GUI_practice/image.png")

btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("button is clicked")

btn7 = Button(root, text="active", command=btncmd) #버튼을 눌렀을 때 command 에 해당하는 함수가 실행됨
btn7.pack()

root.mainloop() #창이 닫히지 않게 함