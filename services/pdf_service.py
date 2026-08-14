from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

import os


def create_pdf(topic, report, citations, research_gaps):

    # -------------------------
    # Create reports folder
    # -------------------------

    os.makedirs("reports", exist_ok=True)

    # -------------------------
    # Create filename
    # -------------------------

    filename = f'reports/{topic.replace(" ", "_")}_Report.pdf'

    # -------------------------
    # Create PDF document
    # -------------------------

    doc = SimpleDocTemplate(filename)

    story = []

    # -------------------------
    # Styles
    # -------------------------

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading1"]
    body_style = styles["BodyText"]

    # Citation label style
    citation_label_style = ParagraphStyle(
        "CitationLabel",
        parent=body_style,
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        spaceBefore=5,
        spaceAfter=3
    )

    # Citation text style
    citation_body_style = ParagraphStyle(
        "CitationBody",
        parent=body_style,
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        spaceBefore=0,
        spaceAfter=6
    )

    # -------------------------
    # Title Style
    # -------------------------

    title_style.fontName = "Helvetica-Bold"
    title_style.fontSize = 20
    title_style.alignment = TA_CENTER
    title_style.spaceAfter = 20

    # -------------------------
    # Heading Style
    # -------------------------

    heading_style.fontName = "Helvetica-Bold"
    heading_style.fontSize = 15
    heading_style.spaceBefore = 12
    heading_style.spaceAfter = 8

    # -------------------------
    # Body Style
    # -------------------------

    body_style.fontName = "Helvetica"
    body_style.fontSize = 10.5
    body_style.leading = 15
    body_style.spaceAfter = 8

    # -------------------------
    # Title
    # -------------------------

    story.append(
        Paragraph(
            "ResearchMate AI",
            title_style
        )
    )

    # -------------------------
    # Research Topic
    # -------------------------

    story.append(
        Paragraph(
            f"Research Topic: {topic}",
            heading_style
        )
    )

    story.append(
        Spacer(1, 12)
    )

    # -------------------------
    # Research Report
    # -------------------------

    headings = [
        "Executive Summary",
        "Research Overview",
        "Main Findings",
        "Comparison of the Papers",
        "Research Gaps",
        "Future Research Directions",
        "Conclusion"
    ]

    for line in report.split("\n"):

        line = line.strip()

        if not line:

            story.append(
                Spacer(1, 6)
            )

            continue

        if line in headings:

            story.append(
                Paragraph(
                    line,
                    heading_style
                )
            )

        else:

            story.append(
                Paragraph(
                    line,
                    body_style
                )
            )

    # -------------------------
    # Research Gaps
    # -------------------------

    story.append(
        Paragraph(
            "Research Gaps",
            heading_style
        )
    )

    story.append(
        Spacer(1, 8)
    )

    for line in research_gaps.split("\n"):

        line = line.strip()

        if not line:

            story.append(
                Spacer(1, 5)
            )

            continue

        story.append(
            Paragraph(
                line,
                body_style
            )
        )

    story.append(
        Spacer(1, 15)
    )

    # -------------------------
    # References
    # -------------------------

    story.append(
        Paragraph(
            "References",
            heading_style
        )
    )

    story.append(
        Spacer(1, 8)
    )

    # -------------------------
    # Citations
    # -------------------------

    for citation in citations:

        # Paper title
        story.append(
            Paragraph(
                citation["title"],
                citation_label_style
            )
        )

        story.append(
            Spacer(1, 3)
        )

        # APA
        story.append(
            Paragraph(
                "APA:",
                citation_label_style
            )
        )

        story.append(
            Paragraph(
                citation["APA"],
                citation_body_style
            )
        )

        # IEEE
        story.append(
            Paragraph(
                "IEEE:",
                citation_label_style
            )
        )

        story.append(
            Paragraph(
                citation["IEEE"],
                citation_body_style
            )
        )

        # MLA
        story.append(
            Paragraph(
                "MLA:",
                citation_label_style
            )
        )

        story.append(
            Paragraph(
                citation["MLA"],
                citation_body_style
            )
        )

        # Space between papers
        story.append(
            Spacer(1, 10)
        )

    # -------------------------
    # Build PDF
    # -------------------------

    doc.build(story)

    return filename