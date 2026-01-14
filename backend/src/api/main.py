from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine
from .orchestrator import ContentOrchestrator

# Initialize DB
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Creator OS - Core API",
    description="The central nervous system for automated content adaptation.",
    version="0.1.0"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/projects/", response_model=schemas.Project, tags=["Projects"])
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    """
    Initializes a new content project. 
    This represents the 'Hero Content' entry point.
    """
    return crud.create_project(db=db, project=project)

@app.post("/projects/{project_id}/process", tags=["Orchestration"])
async def trigger_adaptation_pipeline(
    project_id: int, 
    background_tasks: BackgroundTasks, 
    db: Session = Depends(get_db)
):
    """
    Triggers the AI Multi-Agent Workflow to transform Hero content.
    """
    project = crud.get_project(db, project_id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    orchestrator = ContentOrchestrator(db)
    # Move to background to keep API responsive
    background_tasks.add_task(orchestrator.start_pipeline, project_id)
    
    return {"message": "Adaptation pipeline initiated", "status": "processing"}

@app.get("/projects/{project_id}/status", response_model=schemas.ProjectStatus, tags=["Projects"])
def get_project_status(project_id: int, db: Session = Depends(get_db)):
    return crud.get_project_status(db, project_id=project_id)