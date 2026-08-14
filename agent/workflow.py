from agent.state import ResearchState
from agent.planner import plan_next_step
from agent.memory import ResearchMemory

from services.search_service import search_all
from services.ranking_service import rank_papers
from services.report_service import generate_report
from services.gap_service import find_research_gaps
from services.pdf_service import create_pdf
from services.citation_service import generate_citations

from rag.retriever import Retriever


def run_agent(state: ResearchState):

    # Initialize memory and RAG retriever
    memory = ResearchMemory()
    retriever = Retriever()

    while True:

        # Ask the planner what the agent should do next
        action = plan_next_step(state)

        print(f"Agent Decided: {action}")

        # ==================================================
        # SEARCH
        # ==================================================

        if action == "search":

            print("Searching for Research Papers..")

            papers = search_all(
                state.topic,
                max_results=5
            )

            state.papers = papers

            # Prepare paper abstracts for RAG
            chunks = []

            for paper in papers:

                if paper.abstract:
                    chunks.append(paper.abstract)

            # Add abstracts to vector store
            if chunks:
                retriever.add_documents(chunks)

            # Remember research topic
            memory.remember(
                "topic",
                state.topic
            )

            print(f"Found {len(papers)} papers.")
            print(f"Added {len(chunks)} chunks to RAG.")

        # ==================================================
        # RANK
        # ==================================================

        elif action == "rank":

            print(
                "Ranking Papers by Relevance and Citation Count.."
            )

            ranked_papers = rank_papers(
                state.papers,
                state.topic
            )

            state.ranked_papers = ranked_papers

            print(
                f"Ranked {len(ranked_papers)} papers."
            )

        # ==================================================
        # GENERATE REPORT
        # ==================================================

        elif action == "generate_report":

            print("Generating research report...")

            # Retrieve the most relevant information
            # from the RAG system
            state.relevant_chunks = retriever.retrieve(
                state.topic,
                top_k=3
            )

            print(
                f"Retrieved {len(state.relevant_chunks)} "
                f"relevant chunks."
            )

            # Generate final research report
            report = generate_report(
                state.topic,
                state.ranked_papers,
                state.relevant_chunks
            )

            state.report = report

            # Store report in memory
            memory.remember(
                "report",
                state.report
            )

            print("Research report generated.")

        # ==================================================
        # CITATIONS
        # ==================================================

        elif action == "citations":

            print("Generating Citations..")

            citations = generate_citations(
                state.ranked_papers
            )

            state.citations = citations

            print(
                f"Generated citations for "
                f"{len(citations)} papers."
            )

        # ==================================================
        # RESEARCH GAPS
        # ==================================================

        elif action == "find_gaps":

            print("Generating research gaps..")

            gaps = find_research_gaps(
                state.topic,
                state.ranked_papers
            )

            state.research_gaps = gaps

            # Store research gaps in memory
            memory.remember(
                "research_gaps",
                state.research_gaps
            )

            print("Research gaps generated.")

        # ==================================================
        # CREATE PDF
        # ==================================================

        elif action == "create_pdf":

            print("Creating PDF..")

            pdf_path = create_pdf(
                state.topic,
                state.report,
                state.citations,
                state.research_gaps
            )

            state.pdf_path = pdf_path

            print(
                f"PDF Created: {pdf_path}"
            )

        # ==================================================
        # COMPLETED
        # ==================================================

        elif action == "completed":

            print("Research completed.")

            break