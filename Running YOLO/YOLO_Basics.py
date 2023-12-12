from ultralytics import YOLO
import cv2

model = YOLO('../YOLO_Weights/yolov8l.pt')
results = model("Images/cars.jpg", show=True)
cv2.waitKey(0)
