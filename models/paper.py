class Paper:
    def __init__(
        self,
        title,
        authors,
        year,
        abstract,
        citation_count,
        url
    ):

        self.title = title
        self.authors = authors
        self.year = year
        self.abstract = abstract
        self.citation_count = citation_count
        self.url = url



    def __str__(self):

        return f"""
Title: {self.title}

Authors: {", ".join(self.authors)}

Year: {self.year}

Citations: {self.citation_count}

URL: {self.url}
"""

