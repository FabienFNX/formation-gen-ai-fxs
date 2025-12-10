import streamlit as st
import os
import asyncio
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

# Load environment variables
load_dotenv()

# Initialize embeddings
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize RAG components
@st.cache_resource
def load_vectorstore():
    """Load and process the Git cheat sheet PDF into a vector store"""
    # Load the PDF
    pdf_path = os.path.join(os.path.dirname(__file__), "github-git-cheat-sheet.pdf")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(documents)
    
    # Create vector store
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    return vectorstore

# Load the vectorstore
vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

def format_docs(docs):
    """Format retrieved documents for context"""
    return "\n\n".join(doc.page_content for doc in docs)

# 1) Créer une fonction qui appelle le  RAG tool
@function_tool
def search_git_documentation(query: str) -> str:
    ## A définir
    print("Hello")

# 2) Créer un agent qui appelle le RAG tool
 

st.write("ChatBot permettant d'évaluer les compétences techniques des candidats lors d'entretiens.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Quelles compétences techniques souhaitez-vous évaluer ?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Async function to run the agent
async def run_agent(user_input: str, chat_history: list) -> str:
    """Run the SkillsAgent with the given input and chat history"""
    # Format conversation history for context
    history_context = ""
    if chat_history:
        history_context = "\n\nHistorique de la conversation:\n"
        for msg in chat_history:
            role = "Utilisateur" if msg["role"] == "user" else "Assistant"
            history_context += f"{role}: {msg['content']}\n"
    
    full_input = f"{history_context}\n\nNouvelle question de l'utilisateur: {user_input}"
    
    result = await Runner.run(skills_agent, full_input)
    return result.final_output

# Accept user input
if prompt := st.chat_input("Saisissez votre texte ici..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Prepare chat history for the agent (exclude the current message)
        chat_history = [
            {"role": msg["role"], "content": msg["content"]} 
            for msg in st.session_state.messages[:-1]
        ]
        
        # Run the agent asynchronously
        with st.spinner("Recherche en cours..."):
            full_response = asyncio.run(run_agent(prompt, chat_history))
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
