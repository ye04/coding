from tkinter import *
import tkinter.messagebox as msgbox

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

def info():
    msgbox.showinfo("notification", "just info message") #타이틀, 안의 내용

def warn():
    msgbox.showwarning("warning", "warning message ")

def error():
    msgbox.showerror("error", "error message")

def okcancel():
   msgbox.askokcancel("confirm / cancel", "are you going to do this?") #그냥 보여주는게 아닌 사용자한테 물음(확인) 박스에 들어갈 내용, 안의 콘텐츠 내용

def retrycancel():
    msgbox.askretrycancel("retry / cancel", "are you going to retry?")

def yesno():
    msgbox.askyesno("yes / no", "are you going to do this?")

def yesnocancel():
    response= msgbox.askyesnocancel(title=None, message="are you going to do this?") # title message를 키워드로 저장가능
    #응답을 변수에 저장하여 쓸 수 있게 함
    print(response) #yes--> True 1 no--> False 0 cancel--> None other #첫번째 아이템 --> 1 두번 째--> 0, 나머지

    if response ==1:
        print("yes")
    elif response == 0:
        print("no")
    else: 
        print("cancel")
Button(root, command=info, text="notification").pack()
Button(root, command=warn, text="warning").pack()
Button(root, command=error, text="error").pack()
Button(root, command=okcancel, text="confirm cancel").pack()
Button(root, command=retrycancel, text="retry cancel").pack()
Button(root, command=yesno, text="yes no").pack()
Button(root, command=yesnocancel, text="yes no cancel").pack()

root.mainloop() #창이 닫히지 않게 함