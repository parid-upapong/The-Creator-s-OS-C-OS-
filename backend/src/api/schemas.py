from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class ProjectBase(BaseModel):
    title: str
    hero_video_url: HttpUrl
    target_platforms: List[str] # e.g., ["tiktok", "instagram_reels", "youtube_shorts"]

class ProjectCreate(ProjectBase):
    creator_id: str

class Project(ProjectBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True

class ProjectStatus(BaseModel):
    id: int
    overall_status: str
    agent_logs: List[dict]
    generated_assets: List[str]