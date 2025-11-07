import cv2

def draw_text(frame, text, position=(20, 50), color=(0, 255, 0), size=1.2):
   
    cv2.putText(
        frame,
        text,
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        size,
        color,
        2
    )

def apply_roi_mask(frame, roi=None):
  
    if roi is None:
        return frame
    x1, y1, x2, y2 = roi
    mask = frame.copy()
    cv2.rectangle(mask, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return mask
