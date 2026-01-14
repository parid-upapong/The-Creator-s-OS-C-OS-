import yaml
from typing import Dict, Any

class PromptEngine:
    """
    The Brain of Contextual Adaptation. 
    Hydrates prompt templates with dynamic content and creator-specific context.
    """
    
    def __init__(self, template_path: str = "prompts/templates.yaml"):
        with open(template_path, 'r') as f:
            self.templates = yaml.safe_load(f)

    def generate_prompt(self, platform: str, context: Dict[str, Any]) -> str:
        """
        Merges system instructions with platform-specific templates.
        """
        system_msg = self.templates['system_base'].format(
            creator_name=context.get('creator_name', 'a Professional Creator'),
            tone_description=context.get('tone', 'informative and engaging'),
            target_audience=context.get('audience', 'general interest')
        )
        
        if platform not in self.templates:
            raise ValueError(f"Platform {platform} template not found.")
            
        template = self.templates[platform]['prompt']
        
        # Hydrate the template with transcript and other data
        specific_prompt = template.format(**context)
        
        return f"{system_msg}\n\nTask:\n{specific_prompt}"

# Example Usage:
# engine = PromptEngine()
# prompt = engine.generate_prompt("tiktok_caption", {
#     "transcript": "Today I'm showing you how to build an AI agent in 5 minutes...",
#     "tone": "energetic and fast-paced",
#     "creator_name": "TechWithAlex"
# })