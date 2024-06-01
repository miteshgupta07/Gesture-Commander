import cv2 
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import time

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=2)

vb_new_dist=0
fb_new_dist=0

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
    # Volume and Brightness
        # _,vb_info,img=detector.findDistance(lmlist[8],lmlist[12],img)
        # vb_old_dist=vb_new_dist
        # vb_new_dist=vb_info[5] # to get mid point's y axis value

        # if vb_new_dist<vb_old_dist-1: # subtracting 1 as a bias to gain stability
        #     if handtype=='Left':
        #         print('Brigthness Plus')
        #         time.sleep(0.05)
        #     else:
        #         print("Volume Plus")
        #         time.sleep(0.05)

        # elif vb_new_dist>vb_old_dist+1: # adding 1 as a bias to gain stability
        #     if handtype=="Left":
        #         print("Brightness Minus")
        #         time.sleep(0.05)
        #     else:
        #         print("Volume Minus")
        #         time.sleep(0.05)
        # else:
        #     print("Nothing")

# -----------------------------------------------------------------------------------------
    # Forward and Backward    
        # fb_dist,fb_info,img=detector.findDistance(lmlist[8],lmlist[4],img)
        # fb_old_dist=fb_new_dist
        # fb_new_dist=fb_info[4]

        # if fb_dist<20:
        #     if fb_new_dist>fb_old_dist+1:
        #         print('Forward')
        #         time.sleep(0.05)
        #     elif fb_new_dist<fb_old_dist-1:
        #         print('Backward')
        #         time.sleep(0.05)
        #     else:
        #         print('Nothing')

# -----------------------------------------------------------------------------------------
    
    # Speed
        

    cv2.imshow('Image',img)

    if cv2.waitKey(1) & 0xFF==27:
        cv2.destroyAllWindows()
        cap.release()
        break