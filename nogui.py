import cv2
import atexit

cap = cv2.VideoCapture(1)
atexit.register(lambda: cap.release())
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 60)
print(f"{cap.get(cv2.CAP_PROP_FOURCC )}")
cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)

while True:
    cap.grab()
    _, frame = cap.retrieve()
    #_, frame = cap.read()
    #cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    #img = Image.fromarray(cv2image) #Pillow.Image
    cv2.imshow("camCapture", frame)
    cv2.waitKey(1)

