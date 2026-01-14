import os
import subprocess
import noisereduce as nr
import soundfile as sf
import pyloudnorm as pyln
import numpy as np

class AudioEnhancer:
    """
    Handles noise reduction and loudness normalization to ensure 
    content sounds professional across all device types.
    """
    
    def __init__(self, target_lufs: float = -14.0):
        self.target_lufs = target_lufs

    def reduce_noise(self, input_path: str, output_path: str):
        """Removes background noise using stationary noise masking."""
        data, rate = sf.read(input_path)
        
        # Perform noise reduction
        # stationary=True is faster for cloud processing
        reduced_noise = nr.reduce_noise(y=data, sr=rate, prop_decrease=0.8)
        
        sf.write(output_path, reduced_noise, rate)
        return output_path

    def normalize_loudness(self, input_path: str, output_path: str):
        """Ensures audio meets platform-standard LUFS levels."""
        data, rate = sf.read(input_path)
        
        # Peak normalize first
        peak_normalized = data / np.max(np.abs(data))
        
        # Measure and apply LUFS normalization
        meter = pyln.Meter(rate)
        loudness = meter.integrated_loudness(peak_normalized)
        loudness_normalized = pyln.normalize.loudness(peak_normalized, loudness, self.target_lufs)
        
        sf.write(output_path, loudness_normalized, rate)
        return output_path

    def process_pipeline(self, input_file: str):
        """Full enhancement pipeline."""
        base_name = os.path.splitext(input_file)[0]
        denoised = f"{base_name}_denoised.wav"
        final_master = f"{base_name}_mastered.wav"
        
        self.reduce_noise(input_file, denoised)
        self.normalize_loudness(denoised, final_master)
        
        return final_master