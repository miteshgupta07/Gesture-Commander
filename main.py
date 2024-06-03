# Import necessary libraries
import cv2 
from pynput.keyboard import Controller
from cvzone.HandTrackingModule import HandDetector
from Key_Control import *

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize the hand detector
detector = HandDetector(maxHands=2, modelComplexity=1, detectionCon=0.8, minTrackCon=0.5)

# Variables to store distances for volume and playback control
vb_new_dist = 0
fb_new_dist = 0

# Start the video capture loop
while True:
    
    # Read a frame from the webcam
    success, img = cap.read()
    
    # Flip the image horizontally for a mirror effect
    img = cv2.flip(img, 1)
    
    # Break the loop if the frame was not read successfully
    if not success:
        break

    # Detect hands in the frame
    hands, img = detector.findHands(img, flipType=False)
    
    # If hands are detected
    if hands:
        # If one hand is detected
        if len(hands) == 1:
            hand = hands[0]
            lmlist = hand["lmList"]  # Landmark list
            bbox = hand['bbox']       # Bounding box
            center = hand['center']   # Center of the hand
            handtype = hand['type']   # Type of hand (Left or Right)

            # Volume control for the right hand
            if handtype == 'Right':
                # Calculate the distance between the index and middle finger
                v_dist, v_info, _ = detector.findDistance(lmlist[8][0:2], lmlist[12][0:2])
                if v_dist < 25:
                    vb_old_dist = vb_new_dist
                    vb_new_dist = v_info[5]  # Midpoint's y-axis value
                    # Increase volume if the distance decreases
                    if vb_new_dist < vb_old_dist - 1:  # Bias for stability
                        Volume_Up()
                    # Decrease volume if the distance increases
                    elif vb_new_dist > vb_old_dist + 1:  # Bias for stability
                        Volume_Down()

                # Forward and backward control
                fb_dist, fb_info, _ = detector.findDistance(lmlist[8][0:2], lmlist[4][0:2])
                if fb_dist < 25:
                    fb_old_dist = fb_new_dist
                    fb_new_dist = fb_info[4]
                    # Move forward if the distance increases
                    if fb_new_dist > fb_old_dist + 1:
                        Forward()
                    # Move backward if the distance decreases
                    elif fb_new_dist < fb_old_dist - 1:
                        Backward()
                    
            # Pause and resume control for the left hand
            elif handtype == 'Left':
                thumb_index_dist, _, _ = detector.findDistance(lmlist[4][0:2], lmlist[8][0:2])
                thumb_middle_dist, _, _ = detector.findDistance(lmlist[4][0:2], lmlist[12][0:2])
                thumb_ring_dist, _, _ = detector.findDistance(lmlist[4][0:2], lmlist[16][0:2])
                thumb_pinky_dist, _, _ = detector.findDistance(lmlist[4][0:2], lmlist[20][0:2])
                # Pause or resume if the sum of distances is less than a threshold
                if (thumb_index_dist + thumb_middle_dist + thumb_pinky_dist + thumb_pinky_dist) < 90:
                    Pause_Resume()

    # Display the image
    cv2.imshow('Gesture Detection', img)

    # Break the loop if the escape key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
