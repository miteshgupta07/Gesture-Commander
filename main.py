import cv2 
from pynput.keyboard import Controller
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key,Controller
import time

sleep_time=0.025
cap=cv2.VideoCapture(0)
controller=Controller()
detector=HandDetector(maxHands=2,modelComplexity=1, detectionCon=0.8,minTrackCon=0.5)
vb_new_dist=0
fb_new_dist=0
pause_resume_flag=1

def Volume_Up():
    controller.press(Key.up)
    controller.release(Key.up)
    time.sleep(sleep_time)

def Volume_Down():
    controller.press(Key.down)
    controller.release(Key.down)
    time.sleep(sleep_time)

def Forward():
    controller.press(Key.shift)
    controller.press(Key.right)
    controller.release(Key.shift)
    controller.release(Key.right)
    time.sleep(sleep_time)

def Backward():
    controller.press(Key.shift)
    controller.press(Key.left)
    controller.release(Key.shift)
    controller.release(Key.left)
    time.sleep(sleep_time)

def Pause_Resume():
    controller.press(Key.space)
    controller.release(Key.space)
    time.sleep(0.5)

while True:
    
    success,img=cap.read()
    
    img=cv2.flip(img,1)
    
    if not success:
        break

    hands,img=detector.findHands(img,flipType=False)
    if hands:
        if len(hands)==1:
            hand=hands[0]
            lmlist=hand["lmList"]
            bbox=hand['bbox']
            center=hand['center']
            handtype=hand['type']

# -----------------------------------------------------------------------------------------
    #     # Volume
            if handtype=='Right':
                v_dist,v_info,_=detector.findDistance(lmlist[8][0:2],lmlist[12][0:2])
                if v_dist<25:
                    vb_old_dist=vb_new_dist
                    vb_new_dist=v_info[5] # to get mid point's y axis value
                    if vb_new_dist<vb_old_dist-1: # subtracting 1 as a bias to gain stability
                        Volume_Up()

                    elif vb_new_dist>vb_old_dist+1: # adding 1 as a bias to gain stability
                        Volume_Down()

# -----------------------------------------------------------------------------------------
        # Forward and Backward    
                fb_dist,fb_info,_=detector.findDistance(lmlist[8][0:2],lmlist[4][0:2])
                if fb_dist<25:
                    fb_old_dist=fb_new_dist
                    fb_new_dist=fb_info[4]
                    if fb_new_dist>fb_old_dist+1:
                        Forward()
                    elif fb_new_dist<fb_old_dist-1:
                        Backward()
                    

# -----------------------------------------------------------------------------------------
        
        # Pause and Resume
            elif handtype=='Left':
                thumb_index_dist,_,_=detector.findDistance(lmlist[4][0:2],lmlist[8][0:2])
                thumb_middle_dist,_,_=detector.findDistance(lmlist[4][0:2],lmlist[12][0:2])
                thumb_ring_dist,_,_=detector.findDistance(lmlist[4][0:2],lmlist[16][0:2])
                thumb_pinky_dist,_,_=detector.findDistance(lmlist[4][0:2],lmlist[20][0:2])
                if (thumb_index_dist+thumb_middle_dist+thumb_pinky_dist+thumb_pinky_dist)<90:
                    Pause_Resume()
# -----------------------------------------------------------------------------------------

    cv2.imshow('Image',img)

    if cv2.waitKey(1) & 0xFF==27:
        cv2.destroyAllWindows()
        cap.release()
        break