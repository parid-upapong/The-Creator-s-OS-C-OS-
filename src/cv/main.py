import json
import argparse
from detectors.subject_detector import SubjectDetector
from processors.auto_framing import AutoFramingEngine

def main():
    parser = argparse.ArgumentParser(description="Creator OS: Auto-Framing Engine")
    parser.add_argument("--input", required=True, help="Path to input hero video")
    parser.add_argument("--output_meta", default="crop_metadata.json", help="Path to save crop JSON")
    args = parser.parse_args()

    detector = SubjectDetector()
    engine = AutoFramingEngine(target_ratio=(9, 16))

    print(f"[*] Processing: {args.input}")
    
    metadata = []
    for frame_idx, crop_data in enumerate(engine.process_video_metadata(detector, args.input)):
        crop_data['frame'] = frame_idx
        metadata.append(crop_data)
        
        if frame_idx % 100 == 0:
            print(f"[*] Processed {frame_idx} frames...")

    with open(args.output_meta, 'w') as f:
        json.dump(metadata, f)
        
    print(f"[+] Success: Metadata saved to {args.output_meta}")

if __name__ == "__main__":
    main()