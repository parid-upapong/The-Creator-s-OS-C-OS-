# Technical Stack Recommendation

## Frontend
- **Framework:** Next.js 14 (App Router)
- **Styling:** Tailwind CSS + Shadcn UI
- **State Management:** TanStack Query (React Query)

## Backend & AI
- **Primary Language:** Python (FastAPI) for AI orchestration.
- **Orchestration:** LangChain / LangGraph for complex AI workflows.
- **Transcription:** OpenAI Whisper (Large-v3).
- **LLM:** GPT-4o for text adaptation and metadata.
- **Computer Vision:** MediaPipe (for face tracking and auto-reframing).

## Infrastructure
- **Database:** PostgreSQL (Supabase) + Vector Store (Pinecone) for content memory.
- **Storage:** AWS S3 (for video files).
- **Video Processing:** FFmpeg (Worker nodes) or Cloudinary.
- **Deployment:** Vercel (Frontend) + AWS ECS/Lambda (Backend/Heavy Processing).