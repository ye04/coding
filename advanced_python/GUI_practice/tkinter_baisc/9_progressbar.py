from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")#maximum--> 퍼센티지
                                                                    #indeterminate-->언제 로딩 끝날지 모름 determinate--> 끝이 있고 점점 차오름
progressbar.start(10) #10ms 마다 움직임
progressbar.pack()
#progressbar.stop()은 움직임을 멈추고 값을 삭제

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd():
    for i in range(1, 101):
        time.sleep(0.01) #0.01초 대기
        p_var2.set(i) #직접 프로그레스 바의 value를 정해주는 것임 (1부터 올리면서 반복)
        progressbar2.update() #어떤 동작을 할 떄마다 gui가 업데이트 됨.
        

btn14 = Button(root, text="start", command=btncmd)
btn14.pack()

root.mainloop() #창이 닫히지 않게 함