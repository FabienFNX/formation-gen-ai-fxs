---
transition: slide-left
---

# Introduction au RAG

Concept général

<v-clicks>

- **RAG** : *Retrieval-Augmented Generation*  
- **Idée-clé** : Combiner la **recherche d’information** (retrieval) avec un **modèle génératif** (generation)  
- **Objectif** : produire un texte ou une réponse plus **pertinente**, en se basant sur des **sources externes**  
- **Utilité** :
  - S’appuyer sur du **contenu validé** (documents, base de connaissances)  
  - Réduire les hallucinations du modèle génératif

</v-clicks>

<!--
L’intuition est que le modèle génératif seul peut parfois “inventer” des faits. Avec RAG, on lui fournit du contenu récupéré depuis une base de données ou un index afin d’ancrer la génération sur des informations véridiques.
-->

---
transition: slide-left
---

# Introduction au RAG

Pourquoi le RAG ?

<v-clicks>

- **Hallucinations** : Les grands modèles de langage (LLMs) peuvent générer des informations fausses ou biaisées  
- **Dynamisme** : Les modèles pré-entraînés possèdent des connaissances “figées” à la date de leur entraînement  
- **Spécificité** : L’accès à des bases de connaissances spécialisées (médical, juridique, technique) permet de donner des réponses plus précises

</v-clicks>

---
transition: slide-left
---

# Introduction au RAG

Exemple d'applications

<v-clicks>

- **Chatbot de support client**  
   - Accès à une documentation produit / FAQ  
- **Agent conversationnel pour la recherche académique**  
   - Interrogation d’articles scientifiques ou d’archives  
- **Systèmes d’assistance à l’expertise**  
   - Médecine, droit, finance, etc.

</v-clicks>

---
transition: slide-left
---

# Introduction au RAG

Etapes clés

<v-clicks>

- **Indexation du corpus**
  - Extraction des embeddings (ex: Sentence-BERT, MiniLM …)
  - Stockage dans un moteur de recherche (Elasticsearch, FAISS …)
- **Requête/Prompt**
  - L'utilisateur pose une question
- **Retrieval**
  - Le système compare la requête aux documents (via similarité cosinus, BM25 …)
  - Retourne les K documents les plus pertinents
- **Génération**
  - Le modèle LLM prend la question + les documents comme contexte 
  - Produit une réponse contextualisée

</v-clicks>

<!--
Une étape intermédiaire de “pré-traitement” des documents peut inclure le split en passages (chunking), la normalisation du texte, etc

BM25 : Best Matching 25
BM25 scores documents based on their relevance to a query. It considers:
Term Frequency (TF): How often a term appears in a document.
Inverse Document Frequency (IDF): How unique or important a term is across all documents.
Document Length Normalization: Adjusts scores so longer documents don’t get unfair advantages.

FAISS : Facebook AI Similarity Search
FAISS is designed for Approximate Nearest Neighbor (ANN) Search and uses optimized indexing structures to speed up searches in high-dimensional spaces.
-->

---
transition: slide-left
---

# Introduction au RAG

Avantages

<v-clicks>

- **Pertinence accrue**
  - La réponse est ancrée sur des documents existants
  - Réduction du risque d’hallucinations
- **Maintenance des connaissances**
  - Pas besoin de ré-entraîner le modèle à chaque mise à jour de la base documentaire
  - Gestion plus facile du contenu dynamique
- **Adaptation à des domaines spécialisés**
  - Ajout ou suppression de documents / corpus spécifiques
  - S’adapte à divers cas d’usage (médical, juridique…)
- **Réduction de la taille du LLM**
  - On peut recourir à un générateur plus “léger” si on dispose d’une bonne base de connaissances

</v-clicks>

<!--
Cette approche permet aux entreprises de gérer leur propre base documentaire, tout en utilisant un modèle générique pré-entraîné pour la génération
-->

---
transition: slide-left
---

# Introduction au RAG

Limites et défis

<v-clicks>

- **Qualité de la base de connaissances**
  - Si les données sont obsolètes, incomplètes ou biaisées, la réponse le sera aussi
  - Nécessité de la curation et la mise à jour du corpus
- **Complexité de l’infrastructure**
  - Mise en place d’un moteur de recherche (indexation, pipeline, scoring)
- **Coût de l’inférence**
  - Double ou triple étape : encodage de la question, recherche de documents, génération
  - Besoin d’optimiser le pipeline pour répondre en temps réel
- **Problèmes de privacy et de propriété intellectuelle**
  - Les documents indexés peuvent contenir des données sensibles
  - Respecter les contraintes légales (RGPD, NDA…)
- **Méthodes d’évaluation**

</v-clicks>

<!--
La mise en place de RAG requiert un écosystème plus large que le simple fine-tuning d’un LLM. Les problématiques de données, de maintenance et de performance en temps réel sont cruciales
-->

---
transition: slide-left
---

# Introduction au RAG

La notion de RAG avancé

<img src="../images/advanced_RAG.png" width="60%" alt="RAG avancé" />
