from typing import List, TypedDict, Optional

class ContentSegment(TypedDict):
    id: str
    start_time: float
    end_time: float
    transcript: str
    virality_score: float
    suggested_title: str

class AgentState(TypedDict):
    """
    Represents the internal state of the transformation workflow.
    """
    hero_video_path: str
    raw_transcript: str
    segments: List[ContentSegment]
    platform_outputs: dict # platform_name -> list of assets
    status: str # 'analyzing', 'transforming', 'review_pending', 'completed'
    error_log: List[str]