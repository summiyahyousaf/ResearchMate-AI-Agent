import arxiv
from models.paper import Paper


def search_arxiv(query: str, max_results: int = 5):

    if not query.strip():
        raise ValueError("Search query cannot be empty!")

    search = arxiv.Search(
        query=f'all:"{query}"',
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []

    client = arxiv.Client(
        page_size=max_results,
        delay_seconds=3,
        num_retries=3
    )

    try:

        for result in client.results(search):

            paper = Paper(
                title=result.title,
                authors=[
                    author.name
                    for author in result.authors
                ],
                year=result.published.strftime("%Y-%m-%d"),
                abstract=result.summary,
                citation_count=0,
                url=result.entry_id
            )

            papers.append(paper)

        print(
            f"arXiv returned {len(papers)} papers."
        )

        return papers

    except Exception as e:

        print(
            "Unable to connect to arXiv:",
            e
        )

        return []