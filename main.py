import cv2
import os
import numpy as np

dataset_path = "dataset"

faces = []
labels = []
names = {}
label_id = 0

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    names[label_id] = person

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        img = cv2.imread(img_path, 0)

        faces.append(img)
        labels.append(label_id)

    label_id += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))

recognizer.save("trainer.yml")
np.save("labels.npy", names)

print("✅ Training Complete")