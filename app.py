from ultralytics import YOLO
import cv2

# 1️⃣ Eğittiğin modeli yükle
model = YOLO("yolo11n.pt")  # kendi eğittiğin modelin yolu

# 2️⃣ Video kaynağını aç
cap = cv2.VideoCapture("test_videos/test.mp4")  # veya 0 -> webcam

# 3️⃣ Video çözünürlüğünü kontrol et
if not cap.isOpened():
    print("Video dosyası açılamadı!")
    exit()

# 4️⃣ Döngü: her karede tahmin yap ve çiz
while True:
    ret, frame = cap.read()
    if not ret:
        print("Video bitti veya kamera kapanmış.")
        break

    # YOLO tahmini
    results = model(frame, conf=0.3, verbose=False)

    # Sonuçları çiz
    annotated_frame = results[0].plot()

    # Görüntüyü göster
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    # ESC (27) tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 5️⃣ Temizlik
cap.release()
cv2.destroyAllWindows()
