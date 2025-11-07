
from ultralytics import YOLO
from src.config import MODEL_PATH, TRACKER_CFG, CONF_THRES

class VehicleTracker:
   
    def __init__(self):
        print("[INFO] YOLO modeli yükleniyor...")
        self.model = YOLO(MODEL_PATH)
        print("[INFO] Model yüklendi.")

    def detect_and_track(self, frame):
       
        results = self.model.track(
            frame,
            persist=True,
            conf=CONF_THRES,
            tracker=TRACKER_CFG,
            verbose=False,
            
        )
        return results
