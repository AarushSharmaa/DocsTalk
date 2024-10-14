# summary of the codebase below #
#1. This file implements a Streamlit application called "DocsTalk," which allows users to upload documents, process URLs, and ask questions about the content.
#2. The app interacts with a backend API (api.py) to handle file uploads, extract text from provided URLs, and retrieve answers based on user queries.
#3. It features a simple user interface with clear instructions and feedback for a seamless experience.
#################################
import streamlit as st
import requests
from io import BytesIO

# Initialize session state variable to track document uploads
if 'documents_uploaded' not in st.session_state:
    st.session_state['documents_uploaded'] = False

# Streamlit UI
st.title("DocsTalk: Talk to your documents")

# Add custom CSS for background color and image
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f8ff; /* Light background color */
        }
        h5 {
            text-align: left;
            color: #008080;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h5>Welcome to the DocsTalk! Upload your files to start interacting with them.</h5>", unsafe_allow_html=True)

st.header("How to Use This App in 3 Simple Steps")
st.markdown("""
    <strong>Upload Documents</strong> ➡️ <strong>Process URLs if you need to</strong> ➡️ <strong>Ask Questions to Language Model</strong>
""", unsafe_allow_html=True)

# File upload section
st.header("Upload Documents")
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=['txt', 'docx', 'xlsx', 'pptx', 'pdf'])

if uploaded_files:
    for file in uploaded_files:
        st.session_state['documents_uploaded'] = True  # Set state to true when documents are uploaded
        file_content = BytesIO(file.read())
        files = {'file': (file.name, file_content, file.type)}
        response = requests.post('http://localhost:5000/upload', files=files)
        if response.status_code == 200:
            st.success(f"File {file.name} uploaded and processed successfully!")
        else:
            error_message = response.json().get('error', 'Error uploading file.')
            st.error(f"Error uploading file {file.name}: {error_message}")

# URL input section
st.header("Add URLs")
url_input = st.text_input("Enter URLs (comma-separated)")
if st.button("Process URLs"):
    urls = [url.strip() for url in url_input.split(',') if url.strip()]
    if urls:
        st.session_state['documents_uploaded'] = True  # Set state to true when URLs are uploaded
        response = requests.post('http://localhost:5000/process_urls', json={'urls': urls})
        if response.status_code == 200:
            st.success("All URLs processed successfully!")
        else:
            error_message = response.json().get('error', 'Error processing URLs.')
            for error in error_message:
                st.error(error)
    else:
        st.warning("Please enter at least one URL.")

# Q&A section
st.header("Ask a Question")
question = st.text_input("Enter your question")
if st.button("Get Answer"):
    if question:
        if not st.session_state['documents_uploaded']:
            st.info("Note: Since no documents are uploaded, the response will be generated without any custom context.")
        response = requests.post('http://localhost:5000/ask', json={'question': question})
        if response.status_code == 200:
            answer = response.json()['answer']
            sources = response.json().get('sources', [])  # Get the sources from the response
            st.write("Answer:", answer)
            if sources:
                st.write("Sources:")
                for source in sources:
                    st.write(f"- {source}")  # Display each source
        else:
            error_message = response.json().get('error', 'Error getting answer.')
            st.error(error_message)
    else:
        st.warning("Please enter a question.")


