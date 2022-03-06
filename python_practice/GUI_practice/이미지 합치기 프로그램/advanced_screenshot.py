from PIL import ImageGrab
import time
import keyboard

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S") #현재 년월일시분초를 가져옴
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("ctrl+q", screenshot) #어떤 키를 누르면 어떤 함수를 실행

keyboard.wait("esc") #사용자가 이 키를 누를 때까지 프로그램 수행