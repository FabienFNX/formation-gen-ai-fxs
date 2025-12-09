import streamlit as st
import os
import time
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize ChatOpenAI
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# 1) Configurer le moteur d'embedding et la base de vecteurs


@st.cache_resource
def load_vectorstore():
    """Load and process the Git cheat sheet PDF into a vector store"""

    # 2) Charger le contenu du PDF

    # 3) Utiliser un splitter pour découper les documents

    # 4) Intégrer les chunks dans une base de vecteurs

# 5) Créer un retriever à partir de la base de vecteurs

# 6) Modifier le prompt pour inclure les informations récupérées depuis la base de données vectorielle

# Create a prompt template for technical interview evaluation
prompt = ChatPromptTemplate.from_messages([
    ("system", "Tu es un assistant expert en recrutement technique. Ton rôle est d'évaluer les compétences techniques des candidats en posant des questions pertinentes et en analysant leurs réponses. Sois professionnel, encourageant et constructif."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# 7) Modifier la chaîne pour utiliser le retriever et fournir des réponses basées sur les documents intégrés

# Create a simple chain using LCEL
chain = prompt | llm | StrOutputParser()

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
