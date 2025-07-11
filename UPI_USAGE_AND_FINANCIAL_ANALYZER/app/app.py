# app.py

import gradio as gr
from extract import extract_pdf_data
from process import clean_and_categorize
from analyze import summarize

def analyze_pdf(pdf_file, password):
    try:
        df = extract_pdf_data(pdf_file.name, password)
        df = clean_and_categorize(df)
        result = summarize(df)
        # You can integrate LLM recommendation here if needed
        return result, "📌 Financial advice will appear here (LLM integration pending)"
    except Exception as e:
        return f"❌ Error: {str(e)}", ""

interface = gr.Interface(
    fn=analyze_pdf,
    inputs=[
        gr.File(label="Upload UPI PDF"),
        gr.Textbox(label="PDF Password", type="password")
    ],
    outputs=["text", "text"],
    title="🧾 Personal UPI Analyzer",
    description="Upload your UPI statement to get monthly financial summaries and advice."
)

interface.launch()
