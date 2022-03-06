import time
from PIL import ImageGrab

time.sleep(5) #사용자가 대기하는 시간

for i in range(1, 11): 
    img = ImageGrab.grab() #현재 스크린 이미지를 가져옴
    img.save("auto_screenshot_image{}.png".format(i))
    time.sleep(2) #2초 간격