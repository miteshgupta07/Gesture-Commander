import cv2 
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import time

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=2)

new_dist=0

while True:
    
    success,img=cap.read()
    
    img=cv2.flip(img,1)
    
    if not success:
        break

    hands,img=detector.findHands(img,flipType=False)
    if hands:
        hand=hands[0]
        lmlist=hand["lmList"]
        bbox1=hand['bbox']
        center1=hand['center']
        handtype=hand['type']

# -----------------------------------------------------------------------------------------
       
        dist,info,img=detector.findDistance(lmlist[8],lmlist[12],img)
        old_dist=new_dist
        new_dist=info[5] # to get mid point's y axis value
        if new_dist<old_dist:
            print('Plus')
            time.sleep(0.05)
        elif new_dist>old_dist:
            print("Minus")
            time.sleep(0.05)
        else:
            print("Nothing")

# -----------------------------------------------------------------------------------------


    cv2.imshow('Image',img)

    if cv2.waitKey(1) & 0xFF==27:
        cv2.destroyAllWindows()
        cap.release()
        break