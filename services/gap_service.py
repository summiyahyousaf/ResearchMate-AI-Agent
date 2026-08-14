from agent.prompts import GAP_PROMPT
from llm.ollama import generate_summary

def find_research_gaps(topic, papers):

    context = ""

    for paper in papers:
        context += f"""
Title: {paper.title}

Abstract:
{paper.abstract}
"""

    prompt = GAP_PROMPT.format(
        topic=topic,
        papers=context
    )
    print("GAP PROMPT WORDS:", len(prompt.split()))

    gaps = generate_summary(prompt)

    return gaps