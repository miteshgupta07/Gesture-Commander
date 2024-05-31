import cv2 
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=2)


while True:
    
    success,img=cap.read()
    
    img=cv2.flip(img,1)
    
    if not success:
        break

    hands,img=detector.findHands(img,flipType=False)
    [{'lmList': [[183, 419], [217, 405], [236, 368], [242, 337], [250, 310], [212, 342], [220, 320], [221, 342], [217, 363], [191, 343], [201, 320], [203, 352], [199, 373], [170, 346], [182, 323], [187, 356], [185, 378], [146, 353], [159, 329], [169, 349], [171, 368]], 'bbox': (146, 310, 104, 109), 'center': (198, 364), 'type': 'Left'}]
    [{'lmList': [[436, 472], [392, 452], [367, 394], [365, 353], [368, 317], [410, 352], [386, 337], [379, 377], [379, 410], [441, 356], [411, 351], [406, 402], [409, 437], [470, 370], [441, 363], [433, 411], [433, 443], [497, 388], [473, 379], [460, 409], [455, 431]], 'bbox': (365, 317, 132, 155), 'center': (431, 394), 'type': 'Right'}, {'lmList': [[122, 456], [166, 435], [194, 385], [195, 343], [195, 307], [160, 350], [164, 320], [163, 358], [161, 388], [129, 356], [129, 336], [134, 383], [136, 414], [99, 367], [102, 350], [111, 394], [114, 425], [70, 380], [71, 355], [81, 381], [86, 403]], 'bbox': (70, 307, 125, 149), 'center': (132, 381), 'type': 'Left'}]
    if hands:
        hand=hands[0]
        lmlist=hand["lmList"]
        bbox1=hand['bbox']
        center1=hand['center']
        handtype=hand['type']

        dist,info,img=detector.findDistance(lmlist[8],lmlist[12],img)
        print(type(info))

    cv2.imshow('Image',img)

    if cv2.waitKey(1) & 0xFF==27:
        cv2.destroyAllWindows()
        cap.release()
        break