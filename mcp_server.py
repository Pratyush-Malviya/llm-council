"""Model Context Protocol (MCP) Server for Karpathy's LLM Council.
Exposes prompts and tools so that LLM Council appears natively in Antigravity IDE's '/' menu.
"""

from mcp.server.fastmcp import FastMCP
import asyncio
import os
import sys

# Ensure backend can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend.council import run_full_council

mcp = FastMCP("llm-council")

@mcp.prompt()
def deliberate(topic: str = "Describe your architecture, workflow, or problem to debate") -> str:
    """Multi-model council deliberation across Claude, GPT-4o, Gemini, and Llama."""
    return f"""Please consult the LLM Council on the following topic:

Topic: {topic}

Follow the 3-stage deliberation pipeline:
1. Stage 1: Independent proposals from Claude 3.5 Sonnet, GPT-4o, Gemini 2.0 Flash, and Llama 3.3 70B.
2. Stage 2: Blind peer-review and ranking.
3. Stage 3: Chairman synthesis into a single battle-tested blueprint."""

@mcp.prompt()
def workflow_design(workflow_goal: str = "Describe the n8n automation workflow you want to create") -> str:
    """Design and stress-test an n8n automation workflow with the LLM Council."""
    return f"""Consult the LLM Council to architect a production-grade n8n automation workflow.

Goal: {workflow_goal}

Requirements:
- Detailed node topology (triggers, transformers, AI chains, error routers)
- Strict payload schemas between nodes to avoid runtime breaks
- Failure modes & automated retry / fallback logic
- Consolidated Chairman architecture blueprint"""

@mcp.tool()
async def consult_council(query: str) -> str:
    """Run the 3-stage multi-model council deliberation pipeline on any technical problem or workflow goal."""
    stage1, stage2, stage3, meta = await run_full_council(query)
    
    lines = [f"# LLM Council Deliberation Report\n**Query**: {query}\n"]
    lines.append("## Stage 1: Individual Model Proposals")
    for item in stage1:
        lines.append(f"\n### {item['model']}\n{item['response']}\n")
        
    lines.append("\n## Stage 2: Anonymized Peer Rankings")
    for r in meta.get("aggregate_rankings", []):
        lines.append(f"- **{r['model']}**: Average Rank {r['average_rank']}")
        
    lines.append(f"\n## Stage 3: Chairman Synthesis ({stage3.get('model', 'Chairman')})")
    lines.append(stage3.get("response", "No response generated."))
    
    return "\n".join(lines)

if __name__ == "__main__":
    mcp.run(transport="stdio")
