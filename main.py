import cv2 
from pynput.keyboard import Controller
from cvzone.HandTrackingModule import HandDetector
import time
import warnings
warnings.filterwarnings('ignore')

controller=Controller()
cap=cv2.VideoCapture(0)
detector=HandDetector(maxHands=1,modelComplexity=1, detectionCon=0.8,minTrackCon=0.5)
vb_new_dist=0
fb_new_dist=0
pause_resume_flag=1
while True:
    
    success,img=cap.read()
    
    img=cv2.flip(img,1)
    
    if not success:
        break

    hands,img=detector.findHands(img,flipType=False)
    if hands:
        hand=hands[0]
        lmlist=hand["lmList"]
        bbox=hand['bbox']
        center=hand['center']
        handtype=hand['type']

# # -----------------------------------------------------------------------------------------
#     # Volume and Brightness
        # _,vb_info,_=detector.findDistance(lmlist[8][0:2],lmlist[12][0:2])
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
        # fb_dist,fb_info,_=detector.findDistance(lmlist[8][0:2],lmlist[4][0:2])
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
        # count=detector.fingersUp(hand)
        # finger_count=sum(count[1:])
        # if finger_count>0:
        #     speed=0.5*finger_count
        #     print("{}x".format(speed))

# -----------------------------------------------------------------------------------------
    
    # Pause and Resume
        # thumb_index_dist,_,_=detector.findDistance(lmlist[4][0:2],lmlist[8][0:2])
        # thumb_middle_dist,_,_=detector.findDistance(lmlist[4][0:2],lmlist[12][0:2])
        # thumb_ring_dist,_,_=detector.findDistance(lmlist[4][0:2],lmlist[16][0:2])
        # thumb_pinky_dist,_,_=detector.findDistance(lmlist[4][0:2],lmlist[20][0:2])

        # if (thumb_index_dist+thumb_middle_dist+thumb_pinky_dist+thumb_pinky_dist)<130:
        #     pause_resume_flag^=1
        #     time.sleep(0.5)
        # if pause_resume_flag==1:
        #     print('Resume')
        # else:
        #     print('Pause')

# -----------------------------------------------------------------------------------------

    cv2.imshow('Image',img)

    if cv2.waitKey(1) & 0xFF==27:
        cv2.destroyAllWindows()
        cap.release()
        break