import requests
import os
from dotenv import load_dotenv
from models.paper import Paper

load_dotenv()

API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"


def search_semantic_scholar(query: str, max_results: int = 5):

    if not query.strip():
        raise ValueError("Search query cannot be empty!")

    params = {
        "query": query,
        "limit": max_results,
        "fields": "title,authors,year,abstract,url,citationCount"
    }

    headers = {}

    if API_KEY:
        headers["x-api-key"] = API_KEY

    try:

        response = requests.get(
            BASE_URL,
            params=params,
            headers=headers,
            timeout=30
        )

        print("Semantic Scholar Status:", response.status_code)

        if response.status_code != 200:

            print("Semantic Scholar Error:")
            print(response.text)

            return []

        data = response.json()

        papers = data.get("data", [])

        formatted_papers = []

        for paper in papers:

            authors = []

            for author in paper.get("authors", []):
                authors.append(
                    author.get("name", "Unknown Author")
                )

            formatted_paper = Paper(
                title=paper.get(
                    "title",
                    "Untitled Paper"
                ),

                authors=authors,

                year=paper.get("year"),

                abstract=paper.get(
                    "abstract"
                ) or "No abstract available.",

                citation_count=paper.get(
                    "citationCount",
                    0
                ),

                url=paper.get(
                    "url",
                    ""
                )
            )

            formatted_papers.append(
                formatted_paper
            )

        print(
            f"Semantic Scholar returned "
            f"{len(formatted_papers)} papers."
        )

        return formatted_papers

    except requests.exceptions.RequestException as e:

        print(
            "Semantic Scholar connection error:",
            e
        )

        return []