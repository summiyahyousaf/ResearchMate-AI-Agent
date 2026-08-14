from dataclasses import dataclass, field
from typing import Any


@dataclass
class ResearchState:

    # topic entered by user
    topic: str

    # papers discovered
    papers: list[Any] = field(default_factory=list)

    # papers after ranking/filtering
    ranked_papers: list[Any] = field(default_factory=list)

    # RAG-retrieved evidence
    relevant_chunks: list[str] = field(default_factory=list)

    # AI generated summaries of papers
    summarized_papers: list[Any] = field(default_factory=list)

    # final report
    report: str = ""

    # research gaps
    research_gaps: str = ""

    # citations
    citations: list[Any] = field(default_factory=list)

    # location of generated PDF
    pdf_path: str = ""

    # current stage of research workflow
    status: str = "initialized"