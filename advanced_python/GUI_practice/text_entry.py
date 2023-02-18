from tkinter import *

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

txt = Text(root, width=30, height=5)
txt.insert(END, "Type your text") #기본으로 적용될 글자를 적용함
txt.pack()

e = Entry(root, width=30) #줄바꿈 안됨 
e.insert(0, "hello") #end를 써도 괜찮음
e.pack()

def btncmd():
    print(txt.get("1.0", END)) #1번째 라인의 0번째 칼럼부터 끝까지의 텍스트 값 가져오기
    print(e.get()) #엔트리는 그냥 이렇게만 써주면 됨

    #내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)
    
btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않게 함