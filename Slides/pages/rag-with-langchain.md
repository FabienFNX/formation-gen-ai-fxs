---
transition: slide-left
---

# Mettre en place un RAG avec Langchain

Présentation du framework Langchain

<v-clicks>

- **Contexte et Historique** :
  - Framework créé en 2021
  - Besoin d'orchestrer des pipelines de NLP complexes
- **Principales composantes** :
  - Prompt Templates (gérer le texte envoyé au LLM),
  - Chains (enchaîner plusieurs étapes de traitement),
  - Agents (rendre un LLM interactif avec des “tools”),
  - Memory (stockage du contexte conversationnel), etc.

</v-clicks>

---
transition: slide-left
---

# Mettre en place un RAG avec Langchain

Premier exemple de code 

```python {1-2|4-5|6-11|13-14|all}
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

# Initialisation d'un LLM (OpenAI) :
llm = OpenAI(temperature=0.7)

# Création d'un prompt template simple
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Réponds en français : {question}"
)

# Assemblage dans une chaine
chain = LLMChain(llm=llm, prompt=prompt_template)

# Test
print(chain.run("Quel est le principe de LangChain ?"))
```

---
transition: slide-left
---

# Mettre en place un RAG avec Langchain

Concepts clés

<v-clicks>

- **Prompt Templates avancés**
  - Utiliser des placeholders et variables (ex. `{context}`, `{user_input}`, `{style}`, etc.).
  - Personnaliser le prompt pour ajuster le ton, la langue, le format de la réponse.
- **Memory**
  - Short-Term Memory : stocker les dernières interactions.
  - Long-Term Memory : référencer des conversations plus anciennes.
- **Agents et Tools**
  - Agent : Un LLM capable de planifier et choisir des outils pour effectuer des actions (par ex. requête sur le web, calcul, base de données, etc.).
  - Tools : Fonctions ou API spécifiques (Recherche, calcul, etc.).

</v-clicks>

---
transition: slide-left
---

# LangChain - Chat with Document (RAG)

Utilisation de Langchain pour un contexte de RAG <span v-mark.red="3">(Retrieval Advanced Generation)</span>

<img src="../images/rag.png" width="70%" alt="RAG" />


---
transition: slide-left
---

# Mettre en place un RAG avec Langchain

Décomposition de la chaîne : indexation des documents

```python {1-3|5-7|9-|all}
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Chargement des documents
loader = TextLoader("document.txt")
docs = loader.load()

# Création du moteur d'embeddings et du vecteur store
embedding_fn = OpenAIEmbeddings()
vector_store = Chroma.from_documents(documents=docs, embedding=embedding_fn, collection_name="mon_index")
```

---
transition: slide-left
---

# Mettre en place un RAG avec Langchain

Décomposition de la chaîne : requête et génération

```python {1|4|6-12|13-14|all}
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

llm = OpenAI(temperature=0.0)
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff", 
    retriever=retriever
)

query = "Quelle est la définition de LangChain ?"
response = rag_chain.run(query)
print(response)
```

<!--
Recherche des 3 documents les plus pertinents.

chain_type="stuff" : simple concaténation des documents dans le prompt (d’autres stratégies existent, ex. “map_reduce”).

La chaîne va retrouver les documents correspondants à la question puis les injecter dans le prompt du LLM.
-->

---
transition: slide-left
---

# Mettre en place un RAG avec Langchain

Décomposition de la chaîne : personnalisation du prompt

```python {all|5-12|all}
from langchain.prompts import PromptTemplate

custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    Tu es un assistant expert. 
    Utilise le contexte ci-dessous pour répondre à la question suivante.
    Contexte: {context}

    Question: {question}
    Réponse en français :
    """
)

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": custom_prompt}
)
```
