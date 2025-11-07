from src.tracker import VehicleTracker
from src.density_analyzer import DensityAnalyzer
from src.utils import draw_text
from src.config import VIDEO_PATH, SHOW_WINDOW
import cv2

tracker = VehicleTracker()
analyzer = DensityAnalyzer()

cap = cv2.VideoCapture(VIDEO_PATH)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = tracker.detect_and_track(frame)
    count = analyzer.count_vehicles(results, tracker.model)
    analyzer.update(count)

    draw_text(frame, f"Vehicle Count: {count}")

    if SHOW_WINDOW:
        annotated = results[0].plot()
        cv2.imshow("Vehicle Tracking", annotated)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
analyzer.plot_density()
