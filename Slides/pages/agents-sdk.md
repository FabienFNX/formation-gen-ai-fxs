---
transition: slide-left
title: Présentation du framework Agents SDK
subtitle: Un framework simple de création d'agents
---

# Qu'est-ce que Agents SDK ?

<v-clicks>

- Un framework créé par OpenAI (suite de Swarm)
- Uniquement en Python
- Simple d'utilisation

</v-clicks>

<v-clicks>

Quelques composants clés :
- Gestionnaire d'exécution des agents
- Délégation des tâches (handoff)
- Pipelines de validation (guardrails)
- Observabilité (tracing)

</v-clicks>

---
transition: slide-left
---

# Worflow de traitement

![Agents SDK Worflow](../images/agents/agents_sdk_workflow.png)

---
transition: slide-left
---

# Comparaison avec les autres frameworks

| **Fonctionalités** | <span class="text-blue-500">**Agents SDK**</span> | <span class="text-blue-500">**LangGraph**</span> | <span class="text-blue-500">**Crew.AI**</span> |
| --------- | ----------- | ------ | --------------- |
| **Paradigme** | Orchestration d'agents | Composants | Gestion des rôles |
| **Validation** | Pydantic | Spécifiques | Tâches définies |
| **Intégration** | Flexible, OpenAI | Ecosystème | LangChain |
| **Observabilité** | Intégré | LangSmith | Limité | 
| **Apprentissage** | Facile | Difficile | Modéré |
| **Cas d'usage** | Centré sur OpenAI | Systèmes complexes | Tâches nécessitant des spécialistes |