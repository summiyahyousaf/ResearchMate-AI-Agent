import re


def calculate_relevance(topic, paper):

    # Combine title and abstract
    text = f"{paper.title} {paper.abstract}".lower()

    # Extract words from the topic
    topic_words = re.findall(r"\b[a-zA-Z]{3,}\b", topic.lower())

    if not topic_words:
        return 0

    # Count how many topic words appear
    matches = 0

    for word in topic_words:

        if word in text:
            matches += 1

    # Relevance percentage
    relevance_score = matches / len(topic_words)

    return relevance_score


def rank_papers(papers, topic):

    scored_papers = []

    for paper in papers:

        relevance = calculate_relevance(
            topic,
            paper
        )

        citation_score = paper.citation_count

        scored_papers.append(
            (
                relevance,
                citation_score,
                paper
            )
        )

    # First relevance, then citations
    scored_papers.sort(
        key=lambda item: (
            item[0],
            item[1]
        ),
        reverse=True
    )

    return [
        item[2]
        for item in scored_papers
    ]