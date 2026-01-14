# Developer Notes: Auto-Framing Module

## Integration with Rendering Pipeline
The output of this module is a `crop_metadata.json`. This is decoupled from the actual video rendering to allow for:
1.  **Manual Overrides:** A UI can visualize the `crop_x` and allow a creator to drag the window if the AI misses the target.
2.  **High Performance:** Rendering can be done via FFmpeg using the `crop` filter or a specialized GPU shader (using the metadata provided).

## Future Improvements (Roadmap)
- **Multi-Subject Logic:** Implement a "Wide-Shot" heuristic when two people are talking.
- **Cinematic Panning:** Instead of linear smoothing, use cubic splines for "Ease-in/Ease-out" camera movements.
- **Action Recognition:** Increase the crop speed dynamically during high-action scenes (e.g., sports, dance).