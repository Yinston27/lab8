import cv2
import random
import numpy as np



def unit1(level):
    img = cv2.imread('image.jpg')
    layer = img.copy()
    gaussian_pyramid = [layer]
    for i in range(level):
        layer = cv2.pyrDown(layer)
        gaussian_pyramid.append(layer)
        cv2.imshow(f'Level {i}', layer)

xor, yor, xyt = 0, 0, 0
def unit2():
        global xor, yor, xyt
        cap = cv2.VideoCapture(0)
        down_points = (640, 480)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
            contours, hierarchy = cv2.findContours(thresh, 
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_NONE)

            if len(contours) > 0:
                c = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 250, 0), 3)
                cv2.putText(frame, f'{x+w//2}, {y+h//2}', (50, 400), cv2.FONT_ITALIC, 3, (0, 0, 255), 2, cv2.LINE_AA)
                xor += x+w//2
                yor += y+h//2
                xyt += 1
            cv2.imshow('vid', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()


unit1(5)
unit2()

cv2.waitKey(0)
cv2.destroyAllWindows()
print('Средние координаты центра:')
print(f'x = {xor // xyt}, y = {yor // xyt}')