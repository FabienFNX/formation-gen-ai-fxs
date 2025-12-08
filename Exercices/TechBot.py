import streamlit as st
import os
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize ChatOpenAI
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

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

# Create a prompt template for technical interview evaluation with RAG
prompt = ChatPromptTemplate.from_messages([
    ("system", """Tu es un assistant expert en recrutement technique spécialisé en Git/GitHub. 
    Ton rôle est d'évaluer les compétences techniques des candidats en posant des questions pertinentes 
    et en analysant leurs réponses en les comparant avec la documentation officielle fournie.
    
    Utilise le contexte suivant pour vérifier la précision des réponses des candidats:
    {context}
    
    Sois professionnel, encourageant et constructif. Si la réponse du candidat est correcte, 
    félicite-le. Si elle est incorrecte ou incomplète, fournis des corrections basées sur la documentation."""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Create RAG chain using LCEL
chain = (
    {
        "context": lambda x: format_docs(retriever.invoke(x["input"])),
        "chat_history": lambda x: x["chat_history"],
        "input": lambda x: x["input"]
    }
    | prompt 
    | llm 
    | StrOutputParser()
)

st.write("ChatBot permettant d'évaluer les compétences techniques des candidats lors d'entretiens.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Quelles compétences techniques souhaitez-vous évaluer ?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

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
        full_response = ""
        
        # Prepare chat history for the chain (exclude the current message)
        chat_history = [
            {"role": msg["role"], "content": msg["content"]} 
            for msg in st.session_state.messages[:-1]
        ]
        
        # Use the chain to get response with streaming
        for chunk in chain.stream({
            "chat_history": chat_history,
            "input": prompt
        }):
            full_response += chunk
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
