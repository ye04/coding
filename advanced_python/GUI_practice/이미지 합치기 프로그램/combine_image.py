from tkinter import *
import os
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Nado GUI")

#파일 추가/삭제
def add_file():
    files = filedialog.askopenfilenames(title="Select image file", #선택된 파일을 열어 변수에 저장함 \ 
        filetypes=(("PNG File", "*.png"), ("All file", "*.*")), #어떤 타입의 파일을 보여줄 것인지 \
        initialdir="C:/") #최초에 어느 경로에 저장되어있는 파일들을 띄울 것인지 
    
    #사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

def del_file(): #지울 때는 뒷 인덱스부터 (앞에서부터 지우면 0을 지우면 그 다음 인덱스가 다시 0이 되기에 지정한 것처럼 지워지지 x)
    for index in reversed(list_file.curselection()): #reversed 를 사용하면 실제 인덱스에 영향을 미치진 않고 뒤집어진 값을 던져줌 / curselection --> 선택된 값들
        list_file.delete(index)

#저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory() #사용자가 선택한 경로를 변수에 저장
    if folder_selected == '': #사용자가 취소를 누를 때 (변수에 저장된 게 없을 때)
        return

    txt_dest_path.delete(0,END) #저장경로에 띄워져있는 게 있었다면 없애기
    txt_dest_path.insert(0, folder_selected)

#이미지 통합
def merge_image():
    #print("width: ", cmb_width.get())
    #print("spacing: ", cmb_space.get())
    #print("format: ", cmb_format.get())

    try:
        img_width = cmb_width.get()
        if img_width == "Original":
            img_width = -1 #-1일때는 원본 기준으로
        else:
            img_width = int(img_width)

        img_space = cmb_space.get()

        if img_space == "narrow":
            img_space = 30
        elif img_space == "normal":
            img_space = 60
        elif img_space == "wide":
            img_space = 90
        else:
            img_space = 0

        img_format = cmb_format.get().lower()



        #print(list_file.get(0,END))  #모든 파일 목록을 가지고 오기
        images = [Image.open(x) for x in list_file.get(0, END)]

        image_sizes = [] #[(width1, height1), (width2, height2)...]

        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        #size[0] --> width size[1]--> height
        #widths = [x.size[0] for x in images]
        #heights = [x.size[1] for x in images]
        
        widths, heights = zip(*(image_sizes))

        max_width, total_height = max(widths), sum(heights) #리스트에서 가장 큰 가로, 모든 세로의 합-->사진을 세로로 붙이는 것이기 때문

        if img_space > 0:
            total_height += (img_space * (len(images) -1)) # 배경 만들때 간격이 사진 사이에 있는 칸 개수 (개수 -1) 만큼 곱해진 길이를 더해줌

        result_img = Image.new("RGB", (max_width, total_height), (255,255,255)) #새 이미지 만들기
        y_offset = 0 # y 위치

        for idx, img in enumerate(images):
            #width 가 원본이 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx]) #image_sizes 는 각 사진의 가로 세로 튜플을 가지고 있음

            result_img.paste(img, (0, y_offset)) #만들어놓은 배경에 images 에 있는 사진들을 붙여넣기
            y_offset += (img.size[1] + img_space) #높이 + 간격 만큼 y를 시프트함

            progress = (idx + 1) / len(images) * 100 #index + 1 (0부터 시작이라 몇 번째 사진인지 알려면 1을 더함) / 총 사진이 몇 개 있는지 * 100 실제 퍼센티지로 변환
            p_var.set(progress)
            progress_bar.update()

        file_name = "result_image." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("Notification", "Your images had been successfully saved")
    except Exception as err:
        msgbox.showerror("error", err)


#시작
def start():
    #각 옵션들 값을 확인
    #print("width: ", cmb_width.get())
    #print("spacing: ", cmb_space.get())
    #print("format: ", cmb_format.get())
    
    #파일 목록 확인
    if list_file.size() == 0: #선택되어 리스트 박스에 올라간 이미지 개수가 0일 때
        msgbox.showwarning("Warning", "Add image files")
        return
    
    #저장 경로 확인
    if len(txt_dest_path.get()) == 0: #저장 경로 문자열의 개수가 0일 때
        msgbox.showwarning("Warning", "Select where to save")
        return
    
    #이미지 통합 작업
    merge_image()

#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) #가로로 쫙 펴짐 (이 프레임을 기준으로 안의 버튼들이 가장 왼쪽 오른쪽으로 정렬하게 됨)/간격 띄우기

btn_add_file = Button(file_frame, text="Add File", padx=5, pady=5, width=12, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="Select delete", padx=5, pady=5, width=12, command=del_file)
btn_del_file.pack(side="right")

#리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill=Y)

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)\

# 저장 경로 프레임
path_frame = LabelFrame(root, text="Saving Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #높이 변경

btn_dest_path = Button(path_frame, text="Search", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx=5, pady=5, ipady=5)

#1.가로 넓이 옵션
lbl_width = Label(frame_option, text="Width")
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width) # values-->안에 들어갈 옵션들(리스트로 넣어놓으면 편리)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5) #전에 있던 아이템 중 left가 또 있었다면 그 다음으로 가장 왼쪽으로 정렬


#2.간격 옵션
lbl_space = Label(frame_option, text="Spacing")
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["None", "narrow", "normal", "wide"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space) 
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5) 



#3.파일 포맷 옵션
lbl_format = Label(frame_option, text="FIle Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10) 
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5) 


#진행 상황 Progress bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var) #백개로 나눠서 일씩 올라감
progress_bar.pack(fill="x")

#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5) #둘 다 오른쪽으로 정렬하고 싶을 때 가장 오른쪽으로 놓을 것을 먼저 만들어야 오른쪽부터 왼쪽 방향으로 차례대로 쌓이게 됨

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5) 






root.resizable(False, False)
root.mainloop()

