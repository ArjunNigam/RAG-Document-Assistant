import gradio as gr
from backend.rag_pipeline import (
    build_index,
    ask_question,
)




def upload(pdf):
    build_index(pdf.name)
    return "✅ PDF indexed! Ask me anything about it."


def chat(message, history):
    return ask_question(message)


def create_ui():
    with gr.Blocks(title="📄 Chat with your PDF") as demo:
        gr.Markdown("## 📄 Chat with your PDF (powered by RAG)")

        pdf = gr.File(
            label="Upload a PDF",
            file_types=[".pdf"]
        )

        status = gr.Markdown()

        pdf.upload(
            upload,
            inputs=pdf,
            outputs=status
        )

        gr.ChatInterface(fn=chat)

    return demo