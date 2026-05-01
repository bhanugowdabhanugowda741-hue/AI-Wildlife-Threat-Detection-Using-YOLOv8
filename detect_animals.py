import cv2
import torch
from ultralytics import YOLO
import pygame
import time

pygame.mixer.init()

device = "cuda" if torch.cuda.is_available() else "cpu"
model = YOLO("best.pt").to(device)

cap = cv2.VideoCapture(0)

SAFE_ANIMALS = {"eagle"}
WARNING_ANIMALS = {"tiger"}
DANGER_ANIMALS = {"elephant", "snake"}

last_alert_time = 0
alert_cooldown = 5

def play_alert(sound_file):
pygame.mixer.music.load(sound_file)
pygame.mixer.music.play()

while True:
ret, frame = cap.read()
if not ret:
break

```
results = model.predict(frame, conf=0.3)

alert_type = None

for result in results:
    for box in result.boxes:
        class_id = int(box.cls.item())
        confidence = float(box.conf.item())
        label = model.names[class_id].lower()

        if confidence > 0.5:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            color = (0,255,0)

            if label in WARNING_ANIMALS:
                alert_type = "warning"
                color = (0,255,255)

            elif label in DANGER_ANIMALS:
                alert_type = "danger"
                color = (0,0,255)

            cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)
            cv2.putText(frame,f"{label} {confidence:.2f}",(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,color,2)

if alert_type and (time.time() - last_alert_time > alert_cooldown):
    if alert_type == "danger":
        play_alert("danger.wav")
    else:
        play_alert("warning.wav")
    last_alert_time = time.time()

cv2.imshow("AI Wildlife Detector", frame)

if cv2.waitKey(1) & 0xFF == ord("q"):
    break
```

cap.release()
cv2.destroyAllWindows()
