def generate_citations(papers):

    citations = []

    for paper in papers:

        apa = (
            f"{', '.join(paper.authors)} "
            f"({paper.year}). "
            f"{paper.title}. "
            f"{paper.url}"
        )

        ieee = (
            f"{', '.join(paper.authors)}, "
            f"\"{paper.title},\" "
            f"{paper.year}. "
            f"Available: {paper.url}"
        )

        mla = (
            f"{', '.join(paper.authors)}. "
            f"\"{paper.title}.\" "
            f"{paper.year}. "
            f"{paper.url}"
        )

        citations.append({

            "title": paper.title,

            "APA": apa,

            "IEEE": ieee,

            "MLA": mla

        })

    return citations