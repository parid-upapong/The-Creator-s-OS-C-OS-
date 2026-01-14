# Core API & Orchestration Specification

## Overview
The Core API serves as the entry point for the Creator OS ecosystem. It implements an asynchronous, event-driven architecture to handle long-running AI video processing tasks.

## Endpoint Lifecycle

1. **POST `/projects/`**: The client (Dashboard) uploads metadata and the URL of the "Hero" content.
2. **POST `/projects/{id}/process`**: Triggers the `ContentOrchestrator`. 
    - Orchestrator creates a task chain in Celery.
    - Redis tracks the message passing between distributed workers.
3. **Worker Execution**:
    - **Worker A (CPU)**: Ingestion & Analysis (Whisper, NLP).
    - **Worker B (GPU)**: CV Auto-framing (YOLOv8/MediaPipe) and FFmpeg Rendering.
4. **Status Polling**: The client polls `/status` or waits for a Webhook/WebSocket notification (to be implemented) when `status == "completed"`.

## Scaling Strategy
- **API Nodes**: Stateless FastAPI instances scaled horizontally behind Nginx.
- **Worker Nodes**: Separated into `cpu-queue` and `gpu-queue`.
- **Database**: PostgreSQL for relational state; Redis for transient task coordination.