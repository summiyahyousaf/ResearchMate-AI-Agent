from agent.prompts import REPORT_PROMPT
from llm.ollama import generate_summary


def generate_report(topic, papers, relevant_chunks):

    # Use RAG results as the main research context
    rag_context = "\n\n".join(relevant_chunks)

    prompt = REPORT_PROMPT.format(
        topic=topic,
        papers=rag_context,
        relevant_chunks=rag_context
    )

    print("========== REPORT PROMPT ==========")
    print("REPORT PROMPT WORDS:", len(prompt.split()))
    print("REPORT PROMPT CHARACTERS:", len(prompt))
    print("===================================")

    report = generate_summary(prompt)

    return report