import cv2
import numpy as np
from detectObjAndRunRasp.servo import runServo

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   
    
    blue_lower = np.array([75,100,100], np.uint8)
    blue_upper = np.array([130,255,255], np.uint8)
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    
    kernel = np.ones((5, 5), np.uint8)
    blue_mask = cv2.erode(blue_mask, kernel)
    blue_result = cv2.bitwise_and(frame, frame, mask = blue_mask)
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_COMPLEX
    colorPix = (0, 0, 255)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        x = approx.ravel () [0]
        y = approx.ravel () [1]
        locations = (x, y)

        if area > 3000:
            cv2.drawContours(frame, [cnt], 0, (0, 0 , 255), 5)
            
        if len(approx) == 3:
            detected = "ucgen-mavi"
            cv2.putText(frame, detected, locations, font, 1, colorPix)
            runServo(x, y)
        elif len(approx) == 4:
            detected = "dikdortgen-mavi"
            cv2.putText(frame, detected, locations, font, 1, colorPix)
            runServo(x, y)
        elif 9 < len(approx) < 30:
            detected = "daire-mavi"
            cv2.putText(frame, detected, locations, font, 1, colorPix)
            runServo(x, y)
    
    lower_red = np.array([161, 100, 100])
    upper_red = np.array([180, 255 , 255])
    
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.erode(red_mask, kernel)
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        x = approx.ravel () [0]
        y = approx.ravel () [1]
        locations = (x, y)

        if area > 3000:
            cv2.drawContours(frame, [cnt], 0, colorPix, 5)
            
        if len(approx) == 3:
            detected = "ucgen-kirmizi"
            cv2.putText(frame, detected, locations, font, 1, colorPix)
            runServo(x, y)

        elif len(approx) == 4:
            detected = "dikdortgen-kirmizi"
            cv2.putText(frame, detected, locations, font, 1, colorPix)
            runServo(x, y)
            
        else :
            detected = "daire-kirmizi"
            cv2.putText(frame, detected, locations, font, 1, colorPix)
            runServo(x, y)
                
    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()