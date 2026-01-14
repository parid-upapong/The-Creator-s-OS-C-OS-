import openai
from .prompt_engine import PromptEngine
from ..models import ContentAsset

class MetadataAgent:
    """
    AI Agent responsible for calling LLMs to generate 
    metadata, captions, and tags.
    """
    
    def __init__(self, api_key: str):
        self.engine = PromptEngine()
        self.client = openai.OpenAI(api_key=api_key)

    async def generate_assets(self, hero_content_id: str, platform: str, context_data: dict):
        """
        Orchestrates the LLM call and returns structured metadata.
        """
        # 1. Construct the Contextual Prompt
        prompt = self.engine.generate_prompt(platform, context_data)
        
        # 2. Call the LLM (Using GPT-4o for high-quality creative writing)
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a specialized content adaptation assistant."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"} if "JSON" in prompt else {"type": "text"}
        )
        
        content = response.choices[0].message.content
        
        # 3. Process and return (In a real app, this would save to DB)
        return {
            "platform": platform,
            "generated_text": content,
            "status": "completed"
        }