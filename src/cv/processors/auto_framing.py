import numpy as np
from collections import deque

class AutoFramingEngine:
    """
    Core engine that calculates the dynamic crop window for a video stream.
    Includes smoothing logic to prevent jerky camera movements.
    """
    def __init__(self, target_ratio=(9, 16), smoothing_window=15):
        self.target_ratio = target_ratio
        self.history = deque(maxlen=smoothing_window)
        self.dead_zone_threshold = 0.05  # 5% movement allowed before camera follows

    def calculate_crop_window(self, frame_w, frame_h, coi_x, coi_y):
        """
        Determines the [x1, y1, x2, y2] crop coordinates.
        """
        target_w = int(frame_h * (self.target_ratio[0] / self.target_ratio[1]))
        target_h = frame_h

        # Center the window on COI_X
        ideal_x = coi_x - (target_w // 2)

        # Apply smoothing via moving average
        self.history.append(ideal_x)
        smoothed_x = int(np.mean(self.history))

        # Clamp to frame boundaries
        final_x = max(0, min(smoothed_x, frame_w - target_w))
        final_y = 0 # Usually 0 for 16:9 to 9:16 conversions

        return {
            "x": final_x,
            "y": final_y,
            "w": target_w,
            "h": target_h
        }

    def process_video_metadata(self, detector, video_path):
        """
        Generator yielding crop metadata for each frame.
        """
        import cv2
        cap = cv2.VideoCapture(video_path)
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            f_h, f_w, _ = frame.shape
            coi_x, coi_y = detector.get_center_of_interest(frame)
            crop_data = self.calculate_crop_window(f_w, f_h, coi_x, coi_y)
            
            yield crop_data
            
        cap.release()