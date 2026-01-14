# AI Agent Workflow Specification: Content Transformation Pipeline

## 1. Overview
This document defines the interaction model between specialized AI agents within the Creator OS. The goal is to move from a single "Hero" asset to multiple platform-optimized "Sub-assets" through a coordinated multi-agent system.

## 2. Agent Roles & Responsibilities

| Agent Name | Role | Core AI Capability |
| :--- | :--- | :--- |
| **Ingestion Sentinel** | Content Validation | Signal processing, metadata extraction, format verification. |
| **Contextual Analyst** | Narrative Understanding | Transcription (Whisper), diarization, and semantic topic modeling. |
| **Viral Scout** | Segment Extraction | Predictive virality scoring, hook detection, and scene boundary analysis. |
| **Platform Stylist** | Creative Adaptation | LLM-based copywriting (hooks, captions, hashtags) and visual layout logic. |
| **The Conductor** | Orchestration | State management, error handling, and parallel task dispatching. |

## 3. The "Hero-to-Multi" Workflow
1. **Trigger:** User uploads Hero Video (e.g., 60-min Podcast).
2. **Analysis Phase:**
    - `Contextual Analyst` generates a full transcript and summary.
    - `Viral Scout` identifies 5-10 "high-impact" segments based on emotional peaks and information density.
3. **Transformation Phase:**
    - `The Conductor` spawns parallel tasks for each identified segment.
    - `Platform Stylist` generates:
        - **TikTok/Shorts:** 9:16 crop, burnt-in captions, high-energy hook.
        - **LinkedIn:** 1:1 crop, professional summary, "Key Takeaway" bullets.
        - **X (Twitter):** Thread structure + 15-second teaser.
4. **Review Phase:** Drafts are pushed to the Creator Dashboard for final approval.
5. **Distribution:** Approved assets are scheduled to respective platform APIs.