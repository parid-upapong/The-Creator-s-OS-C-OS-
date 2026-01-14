from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(String)
    title = Column(String)
    hero_video_url = Column(String)
    target_platforms = Column(JSON) # List of strings
    status = Column(String, default="queued") # queued, processing, completed, failed
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Relationship to detailed sub-tasks (one per adaptation)
    tasks = relationship("AdaptationTask", back_populates="project")

class AdaptationTask(Base):
    __tablename__ = "adaptation_tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    platform = Column(String) # e.g., 'tiktok'
    status = Column(String) # pending, framing, tts_generating, rendering, ready
    output_url = Column(String, nullable=True)
    
    project = relationship("Project", back_populates="tasks")