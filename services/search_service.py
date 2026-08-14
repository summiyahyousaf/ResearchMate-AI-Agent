from tools.arxiv_tool import search_arxiv
from tools.semantic_scholar_tool import search_semantic_scholar


def search_all(query: str, max_results: int = 5):

    arxiv_results = search_arxiv(query, max_results)

    semantic_results = search_semantic_scholar(query, max_results)

    results = (arxiv_results or []) + (semantic_results or [])

    unique_results = []

    seen_titles = set()


    for paper in results:

        title = paper.title

        if title not in seen_titles:
            seen_titles.add(title)
            unique_results.append(paper)


    return unique_results