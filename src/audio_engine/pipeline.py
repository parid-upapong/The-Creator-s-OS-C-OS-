from .enhancer import AudioEnhancer
from .tts_service import NeuralTTSService

class AudioProductionPipeline:
    """
    The main entry point for the Creator OS Audio Engine.
    Coordinates between TTS generation and post-production enhancement.
    """
    
    def __init__(self):
        self.enhancer = AudioEnhancer()
        self.tts = NeuralTTSService()

    def generate_dubbed_asset(self, script: str, voice_profile: str, target_lang: str):
        """
        Workflow:
        1. Synthesize localized speech
        2. Enhance and Master (Loudness/Noise)
        3. Ready for video muxing
        """
        print(f"Synthesizing script for language: {target_lang}")
        raw_audio = self.tts.synthesize_speech(
            text=script, 
            voice_id=voice_profile, 
            provider="elevenlabs"
        )
        
        print("Mastering audio for social distribution...")
        final_audio = self.enhancer.process_pipeline(raw_audio)
        
        return {
            "status": "success",
            "audio_url": final_audio,
            "meta": {
                "provider": "elevenlabs",
                "standard": "ITU-R BS.1770-4"
            }
        }