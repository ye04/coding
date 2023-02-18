from tkinter import *

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

label1 = Label(root, text="hello") 
label1.pack()

photo2 = PhotoImage(file="GUI_practice/image.png")
label2 = Label(root, image=photo2)
label2.pack()

def change():
    label1.config(text="bye") #속성을 바꿈

    global photo2 #garbage collection 이 쓸데없는 변수라고 처리하지 않도록 이미지를 할 때는 전역변수로 만들어줌
    photo3 = PhotoImage(file="GUI_practice/image2.png")
    label2.config(image=photo3)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop() #창이 닫히지 않게 함
