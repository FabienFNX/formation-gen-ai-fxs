---
transition: slide-left
---

# Considérations générales sur l'évaluation d'un RAG

Evaluation de la phase de retrieval

<v-clicks>

- **Métriques de base** : 
  - **Recall@K** :
      - Pourcentage de cas où la “bonne” réponse (ou le document correct) fait partie des k résultats renvoyés.
      - Permet de mesurer la couverture : est-ce que le système récupère généralement la bonne information ?
  - **Precision@K** :
      - Pourcentage de cas où les documents renvoyés sont réellement pertinents.
      - Permet de mesurer la qualité des k résultats : combien sont justes parmi ceux présentés ?
- **Métriques avancées** :
  - **Mean Average Precision** : Moyenne des précisions à chaque document pertinent. Donne un score global (entre 0 et 1) qui reflète l’exactitude sur un ensemble de requêtes.
  - **Mean Reciprocal Rank** : Se focalise sur la position du premier document pertinent. Plus ce document apparaît tôt dans la liste, plus le score est élevé.

</v-clicks>

---
transition: slide-left
---

# Considérations générales sur l'évaluation d'un RAG

Evaluation de la phase de génération

<v-clicks>

- **Métriques de base** :
  - **BLEU** (Bilingual Evaluation Understudy) : Mesure la similarité entre la réponse générée et une réponse de référence (ou plusieurs).
  - **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) : Mesure la similarité entre les n-grammes de la réponse générée et ceux de la référence.
  - **METEOR** : Mesure la similarité en tenant compte de la synonymie et de la paraphrase.
- **Evaluation de la factualité**
- **Evaluation humaine** : 
  - **Annotation** : Faire annoter les réponses par des humains pour évaluer la qualité et la pertinence.
  - **Crowdsourcing** : Utiliser des plateformes de crowdsourcing pour évaluer les réponses.

</v-clicks>

<!--
BLEU donnera une idée de la précision (à quel point on retrouve des séquences de mots identiques à la référence), tandis que ROUGE donnera une idée du rappel (à quel point le texte généré couvre l’essentiel de la réponse de référence).
Limites : Ni BLEU ni ROUGE ne mesurent directement la justesse factuelle ou la qualité sémantique profonde. Un modèle peut avoir un bon score s’il copie littéralement certaines parties attendues, mais il pourrait manquer d’exactitude sur le fond (hallucinations, omissions d’informations critiques, etc.). Pour évaluer un RAG, on complète souvent ces métriques avec d’autres mesures (par exemple des évaluations humaines ou des scores d’exactitude factuelle).
-->
