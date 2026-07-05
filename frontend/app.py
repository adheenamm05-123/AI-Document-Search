import streamlit as st
import requests

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Document Search",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Search (RAG Chatbot)")
st.write("Upload a PDF and ask questions about it.")

BACKEND_URL = "http://127.0.0.1:8000"

# -------------------------------
# PDF Upload Section
# -------------------------------
uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("📤 Upload PDF"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        with st.spinner("Uploading and processing PDF..."):

            response = requests.post(
                f"{BACKEND_URL}/upload",
                files=files
            )

        if response.status_code == 200:

            data = response.json()

            st.success("✅ PDF Uploaded Successfully!")

            if "filename" in data:
                st.write("**Filename:**", data["filename"])

            if "total_chunks" in data:
                st.write("**Total Chunks:**", data["total_chunks"])

        else:
            st.error("❌ Upload Failed")
            st.write(response.text)

# -------------------------------
# Chat Section
# -------------------------------
st.divider()

st.subheader("💬 Ask Questions")

question = st.text_input(
    "Ask anything about the uploaded PDF"
)

if st.button("🚀 Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={
                    "question": question
                }
            )

        if response.status_code == 200:

            result = response.json()

            st.success("Answer")

            st.write(result["answer"])

        else:
            st.error("❌ Error while getting answer")
            st.write(response.text)