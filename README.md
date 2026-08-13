#  ResearchMate AI Agent

> **An autonomous AI research assistant that discovers academic papers, ranks relevant research, analyzes findings using RAG, identifies research gaps, generates citations, and produces downloadable research reports.**

ResearchMate AI Agent is an AI-powered research assistant designed to simplify the process of academic research.

Instead of manually searching through papers, comparing sources, extracting information, identifying research gaps, formatting citations, and preparing a report, ResearchMate coordinates these tasks through an automated research workflow.

---

##  Table of Contents

* [Overview](#-overview)
* [Purpose](#-purpose)
* [Objective](#-objective)
* [Key Features](#-key-features)
* [How ResearchMate Works](#-how-researchmate-works)
* [Architecture](#-architecture)
* [Project Structure](#-project-structure)
* [Research Workflow](#-research-workflow)
* [RAG Pipeline](#-rag-pipeline)
* [LLM Integration](#-llm-integration)
* [Academic Sources](#-academic-sources)
* [Citation Generation](#-citation-generation)
* [PDF Report Generation](#-pdf-report-generation)
* [Web Interface](#-web-interface)
* [Technology Stack](#-technology-stack)
* [Installation](#-installation)
* [Running Locally](#-running-locally)
* [Docker](#-docker)
* [Environment Variables](#-environment-variables)
* [Example Workflow](#-example-workflow)
* [Project Goals](#-project-goals)
* [Future Improvements](#-future-improvements)
* [Limitations](#-limitations)
* [Author](#-author)

---

#  Overview

ResearchMate AI Agent is an autonomous research workflow built with Python and Flask.

A user provides a research topic such as:

> **"Generative AI in healthcare"**

ResearchMate then coordinates multiple stages of research:

```text
Research Topic
      ↓
Academic Paper Search
      ↓
Paper Ranking
      ↓
RAG Retrieval
      ↓
Research Analysis
      ↓
Research Gap Identification
      ↓
Citation Generation
      ↓
Research Report
      ↓
PDF Generation
```

The objective is to turn a simple research topic into a structured research report with supporting academic references.

---

#  Purpose

Academic research often requires repetitive tasks such as:

* finding relevant papers
* comparing research
* reading abstracts
* identifying important findings
* finding research gaps
* formatting citations
* organizing information into a report

ResearchMate was created to explore how an AI agent can coordinate these tasks automatically.

The project combines:

* AI agents
* LLMs
* Retrieval-Augmented Generation (RAG)
* vector search
* academic APIs
* ranking
* citation generation
* PDF generation
* Flask
* Docker

into one research workflow.

---

#  Objective

The main objective of ResearchMate is to build an AI research assistant capable of moving beyond simple question-answering.

Instead of only generating an answer, the system is designed to:

1. Search academic sources.
2. Collect relevant research papers.
3. Rank papers based on relevance and citation information.
4. Store research information for retrieval.
5. Retrieve relevant information using RAG.
6. Generate research analysis.
7. Identify potential research gaps.
8. Generate citations in multiple formats.
9. Produce a structured research report.
10. Generate a downloadable PDF.

---

#  Key Features

| Feature                  | Description                                                   |
| -------------------------| -----------------------------------------------------------   |
|  Academic Search         | Searches research papers from academic sources                |
|  Paper Ranking           | Ranks papers using relevance and citation information         |
|  AI Research Analysis    | Uses an LLM to analyze collected research                     |
|  RAG                     | Retrieves relevant research information from stored documents |
|  Research Gap Detection  | Identifies potential gaps and future research directions      |
|  Report Generation       | Produces a structured research report                         |
|  Citation Generation     | Generates APA, IEEE and MLA citations                         |
|  PDF Generation          | Creates a downloadable research report                        |
|  Web Interface           | Provides a simple browser-based interface                     |
|  Docker Support          | Packages the application into a reproducible environment      |

---

#  How ResearchMate Works

The system follows an agent-based workflow.

```text
                     ┌──────────────────┐
                     │   Research Topic │
                     └────────┬─────────┘
                              ↓
                     ┌──────────────────┐
                     │     Planner      │
                     └────────┬─────────┘
                              ↓
                     ┌──────────────────┐
                     │  Search Papers   │
                     └────────┬─────────┘
                              ↓
                     ┌──────────────────┐
                     │ Rank Papers      │
                     └────────┬─────────┘
                              ↓
                     ┌──────────────────┐
                     │   RAG Retrieval  │
                     └────────┬─────────┘
                              ↓
                     ┌──────────────────┐
                     │ Generate Report  │
                     └────────┬─────────┘
                              ↓
                     ┌──────────────────┐
                     │ Research Gaps    │
                     └────────┬─────────┘
                              ↓
                     ┌──────────────────┐
                     │    Citations     │
                     └────────┬─────────┘
                              ↓
                     ┌──────────────────┐
                     │    PDF Report    │
                     └──────────────────┘
```

---

#  Architecture

ResearchMate is organized into several layers.

```text
                    ┌───────────────────────┐
                    │      Web Interface    │
                    │       HTML + CSS      │
                    └───────────┬───────────┘
                                │
                                ↓
                    ┌───────────────────────┐
                    │        Flask API      │
                    │      flask_app.py     │
                    └───────────┬───────────┘
                                │
                                ↓
                    ┌───────────────────────┐
                    │    Agent Workflow     │
                    │ planner + state       │
                    │ memory + reasoning    │
                    └───────────┬───────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ↓                 ↓                 ↓
        Search Services     Ranking          RAG System
              │                 │                 │
              ↓                 ↓                 ↓
       Academic APIs      Relevance +       Embeddings
       arXiv/S2           citations         Vector Store
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ↓
                         LLM Processing
                                ↓
                    ┌───────────────────────┐
                    │ Report + Gap Analysis │
                    └───────────┬───────────┘
                                ↓
                    ┌───────────────────────┐
                    │ Citations + PDF       │
                    └───────────────────────┘
```

---

#  Project Structure

```text
ResearchMate-AI-Agent/
│
├── agent/
│   ├── __init__.py
│   ├── memory.py
│   ├── planner.py
│   ├── prompts.py
│   ├── reasoning.py
│   ├── state.py
│   └── workflow.py
│
├── assets/
│   └── styles.css
│
├── frontend/
│   ├── __init__.py
│   └── index.html
│
├── llm/
│   ├── __init__.py
│   ├── huggingface.py
│   └── ollama.py
│
├── models/
│   ├── citation.py
│   ├── paper.py
│   └── report.py
│
├── rag/
│   ├── __init__.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
│
├── services/
│   ├── citation_service.py
│   ├── gap_service.py
│   ├── pdf_service.py
│   ├── ranking_service.py
│   ├── report_service.py
│   ├── search_service.py
│   └── summary_service.py
│
├── tools/
│   ├── __init__.py
│   ├── arxiv_tool.py
│   └── semantic_scholar_tool.py
│
├── app.py
├── flask_app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── README.md
└── test.py
```

---

#  Agent Workflow

The core workflow is controlled by the agent.

The planner determines what action should happen next.

Typical actions include:

```text
search
   ↓
rank
   ↓
generate_report
   ↓
find_research_gaps
   ↓
generate_citations
   ↓
create_pdf
```

The workflow maintains the research state throughout the process.

This allows different components to operate on the same research task.

---

#  RAG Pipeline

ResearchMate uses Retrieval-Augmented Generation to provide the language model with relevant research information.

The pipeline is:

```text
Research Papers
      ↓
Paper Abstracts
      ↓
Document Chunks
      ↓
Embeddings
      ↓
Vector Store
      ↓
Similarity Retrieval
      ↓
Relevant Context
      ↓
LLM
      ↓
Research Analysis
```

The current implementation uses a vector retrieval system to store and retrieve research information.

This reduces the need to rely only on the language model's internal knowledge.

---

#  LLM Integration

ResearchMate currently integrates with local LLM inference through Ollama.

The current model configuration is:

```text
llama3.2:1b
```

The application communicates with Ollama through its local API.

```text
ResearchMate
      ↓
HTTP Request
      ↓
Ollama API
      ↓
llama3.2:1b
      ↓
Generated Response
```

This allows the research workflow to use an LLM locally during development.

---

#  Academic Sources

ResearchMate currently integrates academic search through:

### arXiv

Used for discovering research papers available through the arXiv API.

### Semantic Scholar

Used for academic paper search and metadata such as:

* title
* authors
* abstract
* publication year
* citation count
* paper URL

The search service combines results from the available academic sources.

---

#  Paper Ranking

After collecting papers, ResearchMate ranks them according to research relevance and available citation information.

The ranking layer is separated into:

```text
services/ranking_service.py
```

This separation allows the ranking strategy to be improved independently from the search system.

---

#  Research Gap Identification

ResearchMate analyzes the collected research to identify potential areas where additional research may be valuable.

The generated gap analysis can include:

* underexplored areas
* limitations
* missing perspectives
* potential future directions

The gap analysis is generated as part of the research workflow rather than being a separate manual step.

---

#  Citation Generation

ResearchMate generates citations in multiple academic formats.

Currently supported formats include:

* **APA**
* **IEEE**
* **MLA**

Example:

```text
Research Paper
      ↓
Metadata
      ↓
Citation Service
      ↓
APA
IEEE
MLA
```

---

#  PDF Report Generation

After completing the research workflow, ResearchMate generates a PDF report using ReportLab.

The generated report can contain:

* Research topic
* Executive summary
* Research overview
* Main findings
* Paper comparison
* Research gaps
* Future research directions
* Conclusion
* References
* APA citations
* IEEE citations
* MLA citations

Users can download the generated PDF directly from the web interface.

---

#  Web Interface

ResearchMate provides a Flask-powered web interface.

The interface allows users to:

1. Enter a research topic.
2. Start the research workflow.
3. Wait while ResearchMate processes the topic.
4. View the generated report.
5. Review research gaps.
6. View citations.
7. Download the generated PDF.

---

# 🛠️ Technology Stack

| Category         | Technology                      |
| ---------------- | ------------------------------- |
| Language         | Python                          |
| Backend          | Flask                           |
| LLM Runtime      | Ollama                          |
| LLM              | Llama 3.2 1B                    |
| RAG              | Custom retrieval pipeline       |
| Vector Search    | FAISS                           |
| Embeddings       | Python-based embedding pipeline |
| Academic Search  | arXiv                           |
| Academic Search  | Semantic Scholar                |
| PDF Generation   | ReportLab                       |
| Frontend         | HTML, CSS, JavaScript           |
| Containerization | Docker                          |
| Version Control  | Git + GitHub                    |

---

#  Installation

Clone the repository:

```bash
git clone https://github.com/summiyahyousaf/ResearchMate-AI-Agent.git
```

Move into the project:

```bash
cd ResearchMate-AI-Agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

#  Running Locally

Make sure Ollama is installed and running.

Verify Ollama:

```bash
ollama --version
```

Verify that Ollama is running:

```bash
curl http://localhost:11434
```

Make sure the required model is available:

```bash
ollama list
```

Then run:

```bash
python flask_app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

#  Docker

ResearchMate includes Docker support for reproducible application environments.

Build the Docker image:

```bash
docker build -t researchmate-ai .
```

Run the container:

```bash
docker run -p 5000:5000 researchmate-ai
```

Then access the application at:

```text
http://localhost:5000
```

> **Note:** The current local development architecture uses Ollama running outside the Flask application. A production deployment therefore requires an appropriate LLM hosting strategy rather than assuming the cloud container can access the developer's local Ollama instance.

---

#  Environment Variables

Sensitive credentials should not be committed to GitHub.

Store secrets in a local `.env` file when required.

Example:

```env
SEMANTIC_SCHOLAR_API_KEY=your_api_key
```

The `.env` file should remain excluded through `.gitignore`.

---

#  Example Workflow

A typical ResearchMate session looks like:

```text
User enters:

"Generative AI in healthcare"

             ↓

ResearchMate searches academic sources

             ↓

Relevant papers collected

             ↓

Papers ranked

             ↓

Research abstracts added to retrieval system

             ↓

Relevant information retrieved

             ↓

LLM analyzes research

             ↓

Research gaps identified

             ↓

Citations generated

             ↓

Structured report generated

             ↓

PDF created

             ↓

User downloads report
```

---

#  Project Goals

ResearchMate was developed as a practical exploration of how autonomous AI systems can coordinate multiple tools and services to accomplish a larger task.

The project focuses on understanding and implementing:

* AI agents
* agent planning
* state management
* memory
* LLM integration
* RAG
* vector databases
* academic APIs
* information retrieval
* ranking
* report generation
* citation generation
* PDF generation
* Flask APIs
* Docker

Rather than building a simple chatbot, the project explores how multiple components can work together as an autonomous research workflow.

---

#  Future Improvements

Planned improvements include:

* [ ] More academic databases
* [ ] PubMed integration
* [ ] Google Scholar-compatible research discovery
* [ ] Improved paper ranking
* [ ] Better semantic similarity
* [ ] Full paper PDF ingestion
* [ ] More advanced RAG
* [ ] Improved research-gap detection
* [ ] User research history
* [ ] Multi-topic research
* [ ] Research comparison mode
* [ ] Authentication
* [ ] Cloud-based LLM infrastructure
* [ ] Production deployment
* [ ] Custom domain
* [ ] More advanced agent planning
* [ ] Improved observability and logging

---

# Limitations

ResearchMate is currently a project under active development.

Research results should be reviewed by the user before being used in academic or professional work.

AI-generated research analysis can contain errors, incomplete interpretations, or unsupported conclusions.

The system should therefore be treated as a **research assistance tool**, not as a replacement for reading and evaluating the original academic sources.

---

#  Author

**Summiya Yousaf**

BSAI Student | AI & Machine Learning Enthusiast

GitHub:

https://github.com/summiyahyousaf

---

#  Project Status

**ResearchMate AI Agent is actively under development.**

The current version demonstrates an end-to-end research workflow:

```text
Search
  ↓
Rank
  ↓
Retrieve
  ↓
Analyze
  ↓
Find Gaps
  ↓
Citations
  ↓
Report
  ↓
PDF
```

The project will continue evolving toward a more autonomous, scalable, and production-ready AI research system.
