from llm.huggingface import generate_summary
from agent.prompts import RESEARCH_AGENT_PROMPT
from agent.state import ResearchState
from agent.memory import ResearchMemory


def agent_reason(state: ResearchState, memory: ResearchMemory):

    prompt = f"""
{RESEARCH_AGENT_PROMPT}

Current Research State:

Topic: {state.topic}

Papers found: {len(state.papers)}

Report generated: {bool(state.report)}

Research gaps generated: {bool(state.research_gaps)}

Citations generated: {len(state.citations)}

PDF created: {bool(state.pdf_path)}

Previous memory:

Topic: {memory.recall("topic")}

Report: {memory.recall("report")}

Research gaps: {memory.recall("research_gaps")}


Based on the current state and memory, decide the single next action.

Choose ONLY ONE of these actions:

search
rank
summarize
generate_report
find_gaps
citations
create_pdf
completed

Return ONLY the action name.
Do not explain your answer.
Do not use Markdown.
"""

    response = generate_summary(prompt)

    return response