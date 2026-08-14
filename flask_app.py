from flask import Flask, jsonify, request, render_template, send_file
from agent.state import ResearchState
from agent.workflow import run_agent


app = Flask(
    __name__,
    template_folder="frontend",
    static_folder="assets"
)


# Store the latest research state
current_state = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/research", methods=["POST"])
def research():

    global current_state

    data = request.get_json()
    topic = data.get("topic")

    if not topic:
        return jsonify({
            "error": "Research Topic is Required!"
        }), 400

    # Create research state
    state = ResearchState(topic=topic)

    # Run ResearchMate
    run_agent(state)

    # Store latest state
    current_state = state

    return jsonify({
        "message": "Research completed.",
        "topic": state.topic,
        "report": state.report,
        "citations": state.citations,
        "research_gaps": state.research_gaps,
        "pdf_path": state.pdf_path
    })


# PDF download
@app.route("/download.pdf")
def download_pdf():

    if current_state is None:
        return jsonify({
            "error": "No research report available."
        }), 404

    if not current_state.pdf_path:
        return jsonify({
            "error": "PDF has not been generated."
        }), 404

    return send_file(
        current_state.pdf_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)