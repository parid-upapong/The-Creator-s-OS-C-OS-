import os
from typing import Optional
from openai import OpenAI
import requests

class NeuralTTSService:
    """
    Orchestrates multiple TTS backends. 
    Prioritizes ElevenLabs for high-fidelity/cloning, 
    OpenAI for cost-effective rapid iterations.
    """
    
    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.eleven_api_key = os.getenv("ELEVENLABS_API_KEY")

    def synthesize_speech(self, text: str, voice_id: str, provider: str = "openai") -> str:
        """
        Synthesizes text to speech and returns the file path.
        """
        output_path = "output_speech.mp3"
        
        if provider == "openai":
            return self._synthesize_openai(text, voice_id, output_path)
        elif provider == "elevenlabs":
            return self._synthesize_eleven(text, voice_id, output_path)
        else:
            raise ValueError(f"Unsupported TTS provider: {provider}")

    def _synthesize_openai(self, text: str, voice: str, path: str) -> str:
        # Voice options: alloy, echo, fable, onyx, nova, shimmer
        response = self.openai_client.audio.speech.create(
            model="tts-1-hd",
            voice=voice,
            input=text
        )
        response.stream_to_file(path)
        return path

    def _synthesize_eleven(self, text: str, voice_id: str, path: str) -> str:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.eleven_api_key
        }
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        response = requests.post(url, json=data, headers=headers)
        with open(path, "wb") as f:
            f.write(response.content)
        return path