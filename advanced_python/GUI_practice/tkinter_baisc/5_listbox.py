from tkinter import *

root = Tk() #메인 윈도우
root.title("GUI") #제목
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표 (화면 기준으로)
#root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

listbox = Listbox(root, selectmode="extended", height=0) #selectmonde extended--> 여러아이템 복수선택 가능 single--> 하나만 선택 가능
                                                        #height-->한번에 보여질 아이템 갯수 (0이면 모두 보임)
listbox.insert(0, "apple") #첫번째 위치에
listbox.insert(1, "banana")
listbox.insert(2, "grape")
listbox.insert(END, "strawberry")
listbox.insert(END, "watermellon") #마지막 아이템 뒤에
listbox.pack()

def btncmd():
    print(listbox.size())
    print(listbox.get(0, 2)) #시작 인덱스의 항목부터 끝 인덱스 항목까지 가져옴
    print(listbox.curselection()) #선택된 값들을 가져옴 (인덱스로 반환함)
    listbox.delete(END) #맨 뒤의 항목 삭제, 0을 넣으면 앞에서부터 지워짐

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않게 함