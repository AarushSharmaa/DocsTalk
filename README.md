# DocsTalk
## Overview
DocsTalk is an innovative application that allows you to converse with your documents using Large Language Models (LLMs). With DocsTalk, you can easily extract insights, answer questions, and interact with content from various file formats such as PDFs, PPTs, text documents and more.

### Introduction
Welcome to DocsTalk! We often find ourselves overwhelmed with information contained in PDFs, PowerPoint presentations, text documents, and more. Traditional methods of studying and synthesizing this content can be time-consuming and inefficient. DocsTalk aims to change that by leveraging the power of LLMs, making it easy to interact with your documents and obtain the information you need quickly and efficiently.

### Features
- Multi-format Support: Upload and process documents in various formats including .pdf, .pptx, .docx, and .txt.
- Conversational Interface: Ask questions about your documents and receive accurate, context-aware answers powered by Generative AI models.
- Content Extraction: Easily extract and process text from uploaded documents and web URLs.

### Tech Stack
Backend
- Flask: for API development
- FAISS: Facebook AI Similarity Search for efficient similarity search
- Large Language Model: gpt-4o

Frontend 
- Streamlit: for UI development
  
Data Processing
- LangChain: For chaining together the Language Models
- Pandas: For data manipulation and analysis.
- PyMuPDF: For handling PDF documents.
- Python-docx: For processing Word documents.
- python-pptx: For working with PowerPoint presentations.

