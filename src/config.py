
MODEL_PATH = "weights/best.pt" 
VIDEO_PATH = "test_videos/cars.mp4"  
TRACKER_CFG = "ultralytics/cfg/trackers/bytetrack.yaml"
CONF_THRES = 0.3  
SHOW_WINDOW = True  

VEHICLE_CLASSES = {
    "car", "bus", "truck", "van",
    "motor", "tricycle", "awning-tricycle"
}

MAX_HISTORY = 200 
PLOT_COLOR = "orange"
