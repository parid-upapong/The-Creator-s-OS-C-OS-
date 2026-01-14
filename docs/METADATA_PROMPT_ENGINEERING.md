# Documentation: Contextual Prompt Engineering for Metadata & Captioning

## 1. Objective
To transform raw "Hero" content (transcripts, visual cues, and audio sentiment) into platform-optimized text assets. This module ensures that a single piece of content speaks the "native language" of every social platform (TikTok, LinkedIn, YouTube, X) while maintaining the creator's unique voice.

## 2. The "Context Injection" Strategy
Instead of generic prompts, the Creator OS uses a **Multi-Layered Context Injection** approach:
1.  **Identity Layer:** The creator's persona, tone of voice, and historical "top-performing" keywords.
2.  **Content Layer:** High-fidelity transcript (Whisper), scene descriptions (CV Module), and sentiment analysis.
3.  **Platform Layer:** Specific constraints (character limits) and algorithmic preferences (hook types, hashtag density).

## 3. Platform Strategies
- **TikTok/Reels:** Focus on "The Hook" in the first 3 seconds. High-energy, emoji-rich, and trend-aligned.
- **LinkedIn:** Focus on "Insight-to-Action." Professional, structured with bullet points, and high-value takeaways.
- **YouTube Shorts:** Focus on curiosity-driven titles and loop-friendly descriptions.
- **X (Twitter):** Focus on "The Thread" or "Punchy Engagement." Concise, provocative, and conversational.

## 4. Prompt Versioning
All prompts are version-controlled to allow for A/B testing against platform performance metrics, creating a data-driven feedback loop for the LLM.