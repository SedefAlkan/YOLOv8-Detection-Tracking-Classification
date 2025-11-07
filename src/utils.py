import cv2

def draw_text(frame, text, position=(20, 50), text_color=(0, 255, 0), font_scale=1.2, thickness=2):

    (text_w, text_h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    x, y = position
    cv2.rectangle(frame,
                  (x - 10, y - text_h - 10),
                  (x + text_w + 10, y + 10),
                  (0, 0, 0),  
                  -1)        
    cv2.putText(frame,
                text,
                position,
                cv2.FONT_HERSHEY_SIMPLEX,
                font_scale,
                text_color,
                thickness,
                cv2.LINE_AA)


def apply_roi_mask(frame, roi=None):
  
    if roi is None:
        return frame
    x1, y1, x2, y2 = roi
    mask = frame.copy()
    cv2.rectangle(mask, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return mask
