from agent.prompts import SUMMARY_PROMPT
from llm.ollama import generate_summary


def summarize_papers(papers):

    summarized = []

    for paper in papers:

        prompt = SUMMARY_PROMPT.format(
            paper=paper.abstract
        )

        summary = generate_summary(prompt)

        summarized.append({
            "title": paper.title,
            "summary": summary,
            "authors": paper.authors,
            "year": paper.year,
            "citation_count": paper.citation_count,
            "url": paper.url
        })

    return summarized