---
transition: slide-left
class: text-center
layout: cover
background: ../images/16.png
---

# Prompt Engineering pour les développeurs

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Des bons principes pour écrire des prompts efficaces et des exemples d'utilisation des LLMs

## Principes

<v-clicks>

1. **Soyez <span v-mark.circle.red="1">clair</span> et précis**

    1. Utilisez des délimiteurs
    2. Demandez une sortie structurée
    3. Demandez au modèle de vérifier si les conditions sont satisfaites
    4. Donnez queques exemples

2. **Donnez du temps au LLM pour réfléchir**

    1. Spécifiez les étapes nécessaires pour accomplir la tâche
    2. Demandez au modèle d'élaborer sa propre solution avant de se précipiter vers une conclusion

3. **Adopter une démarche <span v-mark.underline.blue="3">itérative</span>**

</v-clicks>

---
transition: slide-left
layout: two-cols-header
---
# Prompt Engineering pour les développeurs

Soyez clair et précis

::left::
## #1 Utilisez des délimiteurs

- """
- \`\`\`
- \-\-\-
- <>
- \<tag\>\<\/tag\>

::right::

<div v-click>
```python
text = f"""Vous devez exprimer ce que vous voulez que le modèle 
fasse en fournissant des instructions aussi claires 
et spécifiques que possible.
Cela guidera le modèle vers la sortie souhaitée et 
réduira les risques de recevoir des réponses non 
pertinentes ou incorrectes.
Ne confondez pas la rédaction d'un prompt clair avec 
la rédaction d'un prompt court."""

prompt = f"""Résumez le texte suivant : ```{text}```"""

get_completion(prompt)
```
</div>

<div v-click>
```md
Pour obtenir une réponse pertinente, il est essentiel de formuler
des instructions claires et précises.
Cela oriente le modèle et diminue les risques d'erreurs.
Un prompt clair ne signifie pas nécessairement un prompt court.
```
</div>

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Soyez clair et précis

## #2 Demandez une sortie structurée

```python
prompt = f"""Générez une liste de deux titres de livres fictifs accompagnés de leurs auteurs et genres.
Présentez-les au format JSON avec les clés suivantes : book_id, title, author, genre."""
```
<div v-click>
```md
{
  "books": [
    {
      "book_id": 1,
      "title": "The Last Unicorn",
      "author": "Peter S. Beagle",
      "genre": "Fantasy"
    },
    {
      "book_id": 2,
      "title": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "genre": "Fantasy"
    }
  ]
}
```
</div>

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Soyez clair et précis

## #3 Demandez au modèle de vérifier si les conditions sont satisfaites

```python
prompt = f"""
Vous recevrez un texte délimité par des triples guillemets.
S'il contient une séquence d'instructions, 
reformulez ces instructions au format suivant :

Etape 1 - ...
Etape 2 - …
…
Etape N - …

Si le texte ne contient pas de séquence d'instructions, écrivez simplement 
\" Aucune étape fournie. \"

\"\"\"{text_1}\"\"\"
"""
```

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Soyez clair et précis

## #4 Donnez quelques exemples

```python
prompt = f"""
Votre tâche est de répondre dans un style cohérent.

<enfant>: Apprends-moi la patience.

<grandparent>: La rivière qui creuse la vallée la plus 
profonde coule d'une source modeste ; la symphonie la 
plus grandiose prend naissance d'une seule note ; la 
tapisserie la plus complexe commence par un fil solitaire.

<enfant>: Apprends-moi la résilience.
"""
```
<div v-click>
```md
<grandparent>: L'arbre plie sous la tempête mais ne rompt pas, car ses racines s'enfoncent profondément dans la terre. 
La mer caresse les falaises sans jamais les briser d'un coup, mais avec le temps, elle sculpte leur silhouette.
La résilience n'est pas de ne jamais tomber, mais de se relever chaque fois, plus fort, plus sage.
```
</div>

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Donnez du temps au LLM pour réfléchir

## #1 Spécifiez les étapes nécessaires pour accomplir la tâche

```python
prompt = f"""
Effectuez les actions suivantes :
1 - Résumez le texte suivant délimité par des triples accents graves en une seule phrase.
2 - Traduisez le résumé en anglais.
3 - Énumérez chaque nom dans le résumé anglais.
4 - Produisez un objet JSON qui contient les clés suivantes : french_summary, num_names.

Séparez vos réponses par des sauts de ligne.

texte :
<text>{text}</text>
"""
```

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Donnez du temps au LLM pour réfléchir

## #2 Demandez au modèle d'élaborer sa propre solution avant de se précipiter vers une conclusion

<div grid="~ cols-2 gap-2" m="-t-3">
```md
Déterminez si la solution de l'élève est correcte ou non.
Répondez par "correct" ou "incorrect" uniquement.

Question :
Je construis une installation solaire et j'ai besoin 
d'aide pour établir les aspects financiers."
- Le terrain coûte 100€ / mètre carré
- Je peux acheter des panneaux solaires 250€ / mètre carré
- J'ai négocié un contrat de maintenance qui me coûtera un 
montant forfaitaire de 100k € par an,
plus 10 € par mètre carré.

Quel est le coût total pour la première année d'exploitation 
en fonction du nombre de pieds carrés ?
```
<div v-click>
```md
La solution de l'étudiant :
Soit x la taille du terrain en mètre carré.
Coûts :
1. Coût du terrain : 100x
2. Coût des panneaux solaires : 250x
3. Coût de maintenance : 100 000 + 100x
Coût total : 100x + 250x + 100,000 + 100x = 450x + 100 000
```
</div>
</div>

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Adopter une démarche itérative

<v-clicks>

* Essayer une première approche
* Analyser les résultats et les erreurs
* Clarifier les instructions, donner plus de temps pour réfléchir
* Préciser le prompt avec plusieurs exemples

</v-clicks>

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Cas d'usage : résumer un texte

```python
prompt = f"""
Votre tâche est de générer un court résumé d'un avis sur un produit 
provenant d'un site de commerce électronique pour donner un retour 
au service des prix, responsable de la détermination du prix du produit.

Résumez l'avis ci-dessous, délimité par des triples accents graves, en 
au maximum 30 mots, en vous concentrant sur tous les aspects pertinents 
lié au prix et à la valeur perçue.

Avis : ```{prod_review}```
"""
```
<div v-click>
```md
La lampe offre un bon rapport qualité-prix avec un rangement supplémentaire.
Livraison rapide, mais un problème de cordon fragilisé.
Service client réactif pour le remplacement.
```
</div>

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Cas d'usage : analyser un texte

```python
prompt = f"""
Identifiez les éléments suivants à partir du texte de l'avis :
- Sentiment (positif ou négatif)
- L'évaluateur exprime-t-il de la colère ? (vrai ou faux)
- Article acheté par l'évaluateur
- Entreprise qui a fabriqué l'article

L'avis est délimité par des triples accents graves.
Formattez votre réponse en tant qu'objet JSON avec "Sentiment", "Anger", "Item" et "Brand" comme clés.
Si l'information n'est pas disponible, utilisez "unknown" comme valeur.
Rendez votre réponse aussi courte que possible.
Formatez la valeur Anger en tant que booléen.

Texte de l'avis : '''{lamp_review}'''
"""
```
<div v-click>
```json
{
  "Sentiment": "positif",
  "Anger": false,
  "Item": "lampe",
  "Brand": "unknown"
}
```
</div>

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Cas d'usage : transformer un texte

```python
user_messages = [
  "System performance is slower than normal.",
  "Mi monitor tiene píxeles que no se iluminan.",
  "Il mio mouse non funziona",
  "Mój klawisz Ctrl jest zepsuty",
  "我的屏幕在闪烁"
]
```
<div v-click>
```python
user_messages = [
  "Les performances du système sont plus lentes que la normale.",
  "Mon moniteur a des pixels qui ne s'allument pas.",
  "Ma souris ne fonctionne pas.",
  "Ma touche Ctrl est cassée.",
  "Mon écran clignote."
]
```
</div>

---
transition: slide-left
---
# Prompt Engineering pour les développeurs

Cas d'usage : personnaliser une réponse client

```python
prompt = f"""Vous êtes un assistant AI de service client. Vous devez envoyer une réponse par e-mail à un client important.
Étant donné l'e-mail du client, générez une réponse pour remercier le client pour son avis.
Si le sentiment est positif ou neutre, remerciez-les pour leur avis.
Si le sentiment est négatif, excusez-vous et suggérez-leur de contacter le service client.
Écrivez de manière concise et professionnelle. Signez l'e-mail en tant qu''agent client AI'.
Avis du client :  ```{review}``` Critique du sentiment : {sentiment}"""
```

<div v-click>
```md
Objet : Merci pour votre retour sur notre blender

Cher(e) client(e),

Merci d'avoir partagé votre expérience avec notre blender. Nous sommes désolés d'apprendre que vous avez rencontré
des préoccupations concernant l'évolution des prix et la qualité perçue du produit.

Nous comprenons l'importance d’un bon rapport qualité-prix et nous nous efforçons d’offrir les meilleurs produits
possibles. Si vous souhaitez discuter davantage de votre expérience ou explorer des solutions, nous vous encourageons
à contacter notre service client, qui sera ravi de vous aider.

Nous apprécions votre fidélité et restons à votre disposition pour toute assistance supplémentaire.

Cordialement,
Agent client AI
```
</div>

---
transition: slide-left
---

# Prompt Engineering pour les développeurs

Cas d'usage : créer un premier chatbot

```python
messages = [
  {'role':'system', 'content':'Vous êtes un assistant qui parle comme Shakespeare.'},
  {'role':'user', 'content':'Raconte moi une blague'},
  {'role':'assistant', 'content':'Pourquoi les poulets traversent-ils la rue ?'},
  {'role':'user', 'content':'Je ne sais pas'}
]
```
<div v-click>
Quelques remarques :
</div>

<v-clicks>

- Plusieurs types de rôles : system, user, assistant
- Ces rôles sont spécifiques à chaque modèle
- Il faut transmettre tous les messages précédents pour obtenir une réponse cohérente

</v-clicks>
