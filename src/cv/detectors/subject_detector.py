import cv2
import mediapipe as mp
import numpy as np

class SubjectDetector:
    """
    Identifies the primary subject in a frame using a combination of 
    Face Detection and Pose Estimation.
    """
    def __init__(self, min_detection_confidence=0.5):
        self.mp_face_detection = mp.solutions.face_detection
        self.detector = self.mp_face_detection.FaceDetection(
            model_selection=1, # 1 for far-range (full frame)
            min_detection_confidence=min_detection_confidence
        )

    def get_center_of_interest(self, frame):
        """
        Returns the (x, y) coordinate of the most likely subject.
        """
        results = self.detector.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        h, w, _ = frame.shape
        
        if not results.detections:
            # Fallback to center of screen if no subject found
            return w // 2, h // 2

        # Select the detection with the largest bounding box (likely the primary subject)
        primary_subject = max(results.detections, key=lambda d: d.location_data.relative_bounding_box.width)
        bbox = primary_subject.location_data.relative_bounding_box
        
        # Calculate center
        center_x = int((bbox.xmin + bbox.width / 2) * w)
        center_y = int((bbox.ymin + bbox.height / 2) * h)
        
        return center_x, center_y

    def release(self):
        self.detector.close()