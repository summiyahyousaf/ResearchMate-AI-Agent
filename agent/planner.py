from agent.state import ResearchState

def plan_next_step(state:ResearchState)-> str:
    if not state.papers:
        return "search"
    if not state.ranked_papers:
        return "rank"

    if not state.report:
        return "generate_report"

    if not state.research_gaps:
        return "find_gaps"

    if not state.citations:
        return "citations"

    if not state.pdf_path:
        return "create_pdf"

    return "completed"