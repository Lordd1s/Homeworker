import cv2
import numpy as np

cap = cv2.VideoCapture('0202.mp4')
face_find_alg = cv2.CascadeClassifier("haar.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_find_alg.detectMultiScale(gray, 1.3, 5)
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # this code rewrite the file(i don't understand what hapenned)
        face = frame[y:y + h, x:x + w]
        cv2.imwrite(f"face{i}.jpg", face)
        ############################################
    cv2.imshow('video', frame)
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

