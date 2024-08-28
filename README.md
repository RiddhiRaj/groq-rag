# ⚡GroqChat with Llama3-8B⚡
This project is a Streamlit-based web application that leverages the power of Groq's Llama3 model and HuggingFace embeddings to create an intelligent document assistant. Users can upload PDFs, ask questions, and receive accurate answers based on the content of their documents.

## 🚀 Features

- 🧩 **Document Vectorization**
- ❓ **Question Answering with your PDFs**
- 🔍 **Document Similarity Search**
- 📖 **Pre-loaded Classics**: *Kabuliwala* by Rabindranath Tagore and *The Alchemist* by Paulo Coelho

## 🛠️ Technologies Used

- Streamlit
- Langchain
- Groq API (Llama3-8B model)
- HuggingFace Embeddings
- FAISS for vector storage
- PyPDF for PDF processing

## ⚙️ Prerequisites

- Python 3.7+
- Groq API key

## 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RiddhiRaj/groq-rag.git
   ```
   ```bash
   cd groq-llama3-assistant
   ```

2. Install the required packages:
   
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your `Groq API` key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Create a directory named `pdfs` in the project root and place your PDF files there.

## 🚀 Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. It should automatically open the browser but if it doesn't, then open it manually and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Click on `Process and Embed PDFs` to process and vectorize your documents.

4. Enter your question in the text input field and press Enter to get an answer.

5. Explore the Document Similarity Search results to see related content from your PDFs.