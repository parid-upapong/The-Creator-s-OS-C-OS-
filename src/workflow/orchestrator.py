from langgraph.graph import StateGraph, END
from .state_definition import AgentState
from src.agents.viral_scout_agent import ViralScoutAgent

class CreatorWorkflowOrchestrator:
    def __init__(self):
        self.scout = ViralScoutAgent()
        self._build_graph()

    def _analysis_node(self, state: AgentState):
        # Mocking transcription for brevity
        state["raw_transcript"] = "[00:00] Hello world [00:10] This is a breakthrough in AI."
        return state

    def _segmentation_node(self, state: AgentState):
        # Delegate to Viral Scout
        return self.scout.process(state)

    def _adaptation_node(self, state: AgentState):
        print("[Conductor] Dispatching to Platform Stylist...")
        # Logic to generate TikTok/LinkedIn copy
        state["platform_outputs"] = {
            "tiktok": {"caption": "The future is here! #AI #Tech", "crop": "9:16"},
            "linkedin": {"post": "I recently discussed the evolution of AI...", "crop": "1:1"}
        }
        return state

    def _build_graph(self):
        workflow = StateGraph(AgentState)

        # Define Nodes
        workflow.add_node("analyze", self._analysis_node)
        workflow.add_node("segment", self._segmentation_node)
        workflow.add_node("adapt", self._adaptation_node)

        # Define Edges
        workflow.set_entry_point("analyze")
        workflow.add_edge("analyze", "segment")
        workflow.add_edge("segment", "adapt")
        workflow.add_edge("adapt", END)

        self.app = workflow.compile()

    def run(self, video_path: str):
        initial_state = {
            "hero_video_path": video_path,
            "raw_transcript": "",
            "segments": [],
            "platform_outputs": {},
            "status": "started",
            "error_log": []
        }
        return self.app.invoke(initial_state)

if __name__ == "__main__":
    orchestrator = CreatorWorkflowOrchestrator()
    result = orchestrator.run("path/to/hero_video.mp4")
    print("Final Output Platform Strategy:", result["platform_outputs"])