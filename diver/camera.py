# Camera module for Flaskplay

import cv2, os
from datetime import datetime

def is_okay() -> bool:
    """Runs a check to see if the primary camera is running."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return False
    
    ret, frame = cap.read()
    cap.release()
    return ret and frame is not None

def take_screenshot():
    """Captures a frame from the camera, saves it locally as a JPEG."""
    save_dir = os.path.expanduser(save_dir)
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Camera not available.")

    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise RuntimeError("Failed to capture image.")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(save_dir, f"screenshot_{timestamp}.jpg")
    cv2.imwrite(filepath, frame)
    print(f"Screenshot saved to {filepath}")
    return filepath

def record_clip(): ...

def start_camera():
    if not is_okay():
        raise SystemError("Camera module is non-functional!")
    
    print("Camera module appear to be online.")
    

