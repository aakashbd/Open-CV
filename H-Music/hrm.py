import cv2
from cvzone.HandTrackingModule import HandDetector
from pygame import mixer
 
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
 
while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    mixer.init()
    
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                mixer.music.load("1.mp3")
                mixer.music.play()
            if fingerup == [0, 1, 1, 0, 0]:
                mixer.music.load("2.mp3")
                mixer.music.play()
            if fingerup == [0, 1, 1, 1, 0]:
                mixer.music.load("3.mp3")
                mixer.music.play()
            if fingerup == [0, 1, 1, 1, 1]:
                mixer.music.load("4.mp3")
                mixer.music.play()
            if fingerup == [1, 1, 1, 1, 1]:
                mixer.music.load("5.mp3")
                mixer.music.play()
            if fingerup == [0, 0, 0, 0, 0]:
                mixer.music.stop()

    cv2.imshow("Web-Cam", img)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
         
video.release()
cv2.destroyAllWindows()
