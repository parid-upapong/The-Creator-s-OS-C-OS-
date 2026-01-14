from fastapi import APIRouter, Depends, BackgroundTasks
from ...agents.metadata_agent import MetadataAgent
from ...api.schemas import MetadataRequest

router = APIRouter(prefix="/metadata", tags=["Metadata Generation"])

@router.post("/generate/{hero_id}")
async def generate_platform_metadata(
    hero_id: str, 
    request: MetadataRequest,
    background_tasks: BackgroundTasks
):
    """
    Endpoint to trigger AI metadata generation for specific platforms.
    Runs as a background task because LLM calls can be slow.
    """
    agent = MetadataAgent(api_key="YOUR_OPENAI_KEY")
    
    # We trigger generation for each requested platform
    for platform in request.platforms:
        background_tasks.add_task(
            agent.generate_assets, 
            hero_id, 
            platform, 
            request.context_overrides
        )
        
    return {"message": f"Metadata generation started for {len(request.platforms)} platforms."}