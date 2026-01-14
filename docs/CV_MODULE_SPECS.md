# Module Specification: Intelligent Auto-Framing (IAF)

## 1. Objective
The IAF module is responsible for converting landscape "Hero" content (16:9) into platform-specific vertical formats (9:16, 4:5) by dynamically tracking the most relevant subject (the "Center of Interest") to ensure they remain in frame without manual keyframing.

## 2. Technical Stack
- **Engine:** Python 3.9+
- **Inference:** ONNX Runtime / OpenVINO (for CPU optimization) or TensorRT (for GPU).
- **Computer Vision Libraries:** OpenCV, MediaPipe (Face/Pose), YOLOv8 (Object Detection).
- **Smoothing:** Kalman Filtering / Savitzky-Golay Filter for jitter reduction.

## 3. Computer Vision Pipeline
1.  **Scene Change Detection:** Segment the video into shots to reset tracking and avoid "sliding" transitions between different camera angles.
2.  **Saliency & Subject Detection:** 
    - Priority 1: Active Speaker (Face + Lip movement).
    - Priority 2: Human Figures (Pose).
    - Priority 3: Salient Objects (via Saliency Mapping).
3.  **Temporal Tracking:** Maintain subject ID across frames even during brief occlusions.
4.  **Optimal Window Calculation:** Calculate the `x-coordinate` of the crop window while maintaining the target aspect ratio.
5.  **Damping & Smoothing:** Apply a "Virtual Cameraman" logic to allow the subject to move within a "dead zone" before the camera follows, creating natural movement.

## 4. Output API
The module returns a metadata JSON containing the `crop_x`, `crop_y`, `width`, and `height` for every frame, which is then passed to the FFmpeg Rendering Engine.