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

Frontend 
- Streamlit: for UI development
  
Data Processing
- LangChain: For chaining together the Language Models
- Pandas: For data manipulation and analysis.
- PyMuPDF: For handling PDF documents.
- Python-docx: For processing Word documents.
- python-pptx: For working with PowerPoint presentations.


### Setting up the project

Preferred Python version: Python 3.9.13 (available to download at https://www.python.org/downloads/release/python-3913/)                                

Clone the Repository: Open your terminal. Run the following command to clone the repository 
```
git clone https://github.com/yourusername/your-repo-name.git
```

Navigate to the project directory:
```
cd DocsTalk
```

Set Up Virtual Environment
- Create a virtual environment:
```
python -m venv venv
```

- Activate the virtual environment:
```
On macOS/Linux:
source venv/bin/activate

On Windows:
venv\Scripts\activate
```


Install Dependencies: Run the following command to install all required dependencies
```
pip install -r requirements.txt
```

Note: If you encounter dependency issues, you may need to manually install specific versions as indicated in the error messages.

#### Add Environment Variables (please contact me at aarush.sharma6@gmail.com for needing the environment keys)
- Create a .env file in the root of your project directory and add the necessary environment variables.

#### Running the Application

Start the Flask API. In the terminal, run:
```
python api.py
```
This will start the Flask backend on http://localhost:5000.

In a new terminal (keeping the Flask API running), start the Streamlit application:
```
streamlit run app.py
```

This will open the Streamlit app in your web browser, typically at http://localhost:8501. You can now use the application.


### Usage
- Upload your documents or add URLs to process.
- Ask questions about the content, and get responses along with their sources.


