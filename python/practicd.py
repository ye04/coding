import cv2
import mediapipe as mp
import keyboard

cap = cv2.VideoCapture(0) #비디오 객체 생성 (0번 웹캠 사용-웹캠이 하나 있으면 0번 웹캠)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read() # 비디오객체에서 받아들이는 영상을 한 프레임씩 읽음.
                              # cap.read()는 튜플 형식으로 두 값을 받아들임
                              # 첫 번째(success)는 비디오 프레임을 잘 받아들였는지를 확인-True, False
                              # 두 번째(img)는 비디오 프레임 값
    #print(cap.read())
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                pass
                #print(id, lm)

            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS) #손에 선을 그려줌

    cv2.imshow("Image", img) #웹켐 띄우기
    cv2.waitKey(1)

    if keyboard.is_pressed("q"):
        break

cap.release()
cv2.destroyAllWindows()
