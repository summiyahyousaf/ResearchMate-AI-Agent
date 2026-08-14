from services.search_service import search_all
from services.ranking_service import rank_by_citation
from services.summary_service import summarize_papers
from services.report_service import generate_report
from services.gap_service import find_research_gaps
from services.citation_service import generate_citations
from services.pdf_service import create_pdf


# ==========================================
# User Input
# ==========================================

topic = input("Enter Research Topic: ")
num_papers = int(input("How many research papers do you want? "))

print("\nSearching papers...\n")

papers = search_all(topic, num_papers)

print(f"Found {len(papers)} papers.\n")


# ==========================================
# Rank Papers
# ==========================================

ranked_papers = rank_by_citation(papers)

print("Top Research Papers Found:\n")

for i, paper in enumerate(ranked_papers, start=1):
    print(f"{i}. {paper.title}")


# ==========================================
# Generate Summaries
# ==========================================

print("\nGenerating summaries...\n")

summarized_papers = summarize_papers(ranked_papers)


# ==========================================
# Generate Research Report
# ==========================================

print("Generating research report...\n")

report = generate_report(
    topic,
    ranked_papers
)

print("\n================ RESEARCH REPORT ================\n")
print(report)


# ==========================================
# Print Paper Summaries
# ==========================================

print("\n================ PAPER SUMMARIES ================\n")

for paper in summarized_papers:

    print("=" * 70)

    print("Title:")
    print(paper["title"])

    print()

    print("Authors:")
    print(", ".join(paper["authors"]))

    print()

    print("Citations:")
    print(paper["citation_count"])

    print()

    print("Summary:")
    print(paper["summary"])

    print()


# ==========================================
# Generate Research Gaps
# ==========================================

print("\nGenerating Research Gaps...\n")

research_gaps = find_research_gaps(
    topic,
    ranked_papers
)

print("\n================ RESEARCH GAPS ================\n")

print(research_gaps)


# ==========================================
# Generate Citations
# ==========================================

print("\nGenerating Citations...\n")

citations = generate_citations(ranked_papers)

print("\n================ CITATIONS ================\n")

for citation in citations:

    print("=" * 70)

    print("Paper:")
    print(citation["title"])

    print()

    print("APA")
    print(citation["APA"])

    print()

    print("IEEE")
    print(citation["IEEE"])

    print()

    print("MLA")
    print(citation["MLA"])

    print()


# ==========================================
# Create PDF (LAST STEP)
# ==========================================

print("\nCreating PDF Report...\n")

pdf_path = create_pdf(
    topic,
    report,
    summarized_papers,
    citations,
    research_gaps
)

print("Report saved successfully!")

print(pdf_path)