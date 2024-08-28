import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

# Load the API key for Groq
groq_api_key = os.getenv('GROQ_API_KEY')

st.title("GroqChat with Llama3⚡")

st.markdown("""
* Click on "Process and Embed PDFs" to prepare the system.
* Enter your question in the input box below.
* View the answer and related document segments.
""")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only. Please provide the most accurate response based on the question
    <context>
    {context}
    </context>
    Question: {input}
    """
)

def vector_embedding():
    if "vectors" not in st.session_state:
        # Use HuggingFaceEmbeddings instead of OpenAIEmbeddings
        st.session_state.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        st.session_state.loader = PyPDFDirectoryLoader("./pdfs")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

if st.button("Process and Embed PDFs"):
    vector_embedding()
    st.success("Documents processed successfully and the Vector Store DB is ready! You can now ask questions.")

st.subheader("Get your thinking cap on & ask!🧠")

prompt1 = st.text_input("Enter your question about the documents")

if prompt1 and "vectors" in st.session_state:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    print("Response time:", time.process_time() - start)
    
    st.subheader("Answer:")
    st.write(response['answer'])
    
    # With a streamlit expander
    with st.expander("Related Document Segments"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.markdown(f"**Segment {i+1}:**")
            st.write(doc.page_content)
            st.markdown("---")
elif prompt1:
    st.warning("Please process the documents first by clicking the 'Process Documents' button.")