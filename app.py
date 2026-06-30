import gradio as gr

from rag import (
    ask_ai,
    generate_sprint_summary,
    generate_jira_ticket,
    TOPICS,
    ISSUE_MATRIX
)

# --------------------------------------------------
# Gradio UI
# --------------------------------------------------

with gr.Blocks(
    title="AI Product Feedback Intelligence Platform",
    theme=gr.themes.Soft()
) as demo:

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    gr.Markdown(
        """
# 🤖 AI Product Feedback Intelligence Platform
Analyze customer feedback using **LangChain**, **FAISS**, **Groq LLM** and **RAG**.
This application helps Product Managers:
- Understand customer issues
- Generate Sprint Summaries
- Generate Jira Tickets
- Explore AI-discovered trends
"""
    )

    # --------------------------------------------------
    # Dashboard
    # --------------------------------------------------

    with gr.Accordion("📊 Product Dashboard", open=True):

        gr.Markdown("## 📈 Issue Prioritization Matrix")

        gr.Markdown(ISSUE_MATRIX)

        gr.Markdown("---")

        gr.Markdown("## 🔥 AI-Discovered Trending Topics")

        gr.Markdown(TOPICS)

    # --------------------------------------------------
    # Tabs
    # --------------------------------------------------

    with gr.Tab("💬 Ask AI"):

        gr.Markdown(
            """
### Ask questions about your customer reviews.
Example Questions
- What are users saying about Memory?
- What are the biggest customer complaints?
- Summarize negative reviews.
- What feature requests are customers asking for?
- What are users saying about Voice Mode?
"""
        )

        question = gr.Textbox(
            label="Ask a Question",
            placeholder="Example: What are users saying about memory?",
            lines=2
        )

        answer = gr.Markdown()

        ask_btn = gr.Button(
            "🚀 Generate Answer",
            variant="primary"
        )

        ask_btn.click(
            fn=ask_ai,
            inputs=question,
            outputs=answer
        )

    # --------------------------------------------------

    with gr.Tab("📑 Sprint Summary"):

        gr.Markdown(
            """
Generate an AI-powered sprint summary
from customer feedback.
"""
        )

        sprint_query = gr.Textbox(
            value="overall customer feedback",
            label="Sprint Context"
        )

        sprint_output = gr.Markdown()

        sprint_btn = gr.Button(
            "🚀 Generate Sprint Summary",
            variant="primary"
        )

        sprint_btn.click(
            fn=generate_sprint_summary,
            inputs=sprint_query,
            outputs=sprint_output
        )

    # --------------------------------------------------

    with gr.Tab("📝 Jira Ticket Generator"):

        gr.Markdown(
            """
Generate a professional Jira ticket
from customer feedback.
"""
        )

        jira_query = gr.Textbox(
            value="memory issues",
            label="Issue"
        )

        jira_output = gr.Markdown()

        jira_btn = gr.Button(
            "🚀 Generate Jira Ticket",
            variant="primary"
        )

        jira_btn.click(
            fn=generate_jira_ticket,
            inputs=jira_query,
            outputs=jira_output
        )

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    gr.Markdown("---")

    gr.Markdown(
        """
Built using:
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq LLM
- Gradio
Developed as an AI Product Intelligence Platform.
"""
    )

# --------------------------------------------------

if __name__ == "__main__":
    demo.launch()
