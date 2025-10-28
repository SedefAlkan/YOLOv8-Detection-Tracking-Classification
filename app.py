from ultralytics import YOLO
import cv2


model = YOLO("yolov8.pt") 

cap = cv2.VideoCapture("test_videos/test.mp4") 

if not cap.isOpened():
    print("Video dosyası açılamadı!")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print("Video bitti veya kamera kapanmış.")
        break

 
    results = model(frame, conf=0.3, verbose=False)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Detection", annotated_frame)

   
    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
