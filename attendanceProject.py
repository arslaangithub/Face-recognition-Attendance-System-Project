import cv2
import numpy as np
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = np.load("labels.npy", allow_pickle=True).item()

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

marked = set()

def markAttendance(name):
    if name in marked:
        return

    with open('Attendance.csv', 'a+') as f:
        now = datetime.now()
        f.write(f'{name},{now.strftime("%H:%M:%S")},{now.strftime("%d/%m/%Y")}\n')

    marked.add(name)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        id, confidence = recognizer.predict(face)

        if confidence < 70:
            name = labels[id].upper()
            color = (0, 255, 0)
            markAttendance(name)
        else:
            name = "UNKNOWN"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)
        cv2.putText(frame, f"{name} ({round(confidence,1)})",
                    (x, y-10), cv2.FONT_HERSHEY_COMPLEX,
                    0.8, color, 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()