import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

class ViralScoutAgent:
    def __init__(self, model_name="gpt-4o"):
        self.llm = ChatOpenAI(model=model_name, temperature=0.2)

    def identify_viral_moments(self, transcript_with_timestamps: str) -> list:
        """
        Analyzes transcript to find hooks, controversial statements, or high-value insights.
        """
        prompt = f"""
        Analyze the following transcript from a video. 
        Identify the 3 most engaging segments that would perform well as short-form content (TikTok/Reels).
        Provide the start and end timestamps and a reason for each choice.
        
        Transcript:
        {transcript_with_timestamps}
        
        Return ONLY a JSON list of objects:
        [{"start": 0.0, "end": 60.0, "hook": "...", "reason": "..."}]
        """
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        try:
            segments = json.loads(response.content)
            return segments
        except Exception as e:
            print(f"Error parsing segments: {e}")
            return []

    def process(self, state: dict):
        print("[ViralScout] Identifying key moments...")
        transcript = state.get("raw_transcript", "")
        segments = self.identify_viral_moments(transcript)
        state["segments"] = segments
        return state