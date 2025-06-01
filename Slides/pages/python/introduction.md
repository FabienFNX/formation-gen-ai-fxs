---
transition: slide-left
class: text-center
layout: cover
background: ../images/16.png
---

# Introduction au langage Python

---
transition: slide-left
---
# Introduction au langage Python (philosophie, écosystème, usages)

* **Un langage polyvalent et mature** : Python est un langage de programmation interprété, orienté objet et à typage dynamique, créé en 1991 (soit 4 ans avant Java).
* **Philosophie “Zen of Python”** : La philosophie de Python se résume en 19 principes. En pratique, Python favorise un code clair et lisible, en privilégiant l’indentation pour structurer les blocs plutôt que des symboles encombrants. Cette clarté donne souvent l’impression de lire du pseudo-code.
* **Écosystème riche (“batteries incluses”)** : Python fournit une vaste bibliothèque standard prête à l’emploi, couvrant la majorité des besoins courants (traitement texte, fichiers, web, etc.)
* **Usages principaux** : Initialement utilisé pour le scripting et l’automatisation, Python est aujourd’hui très présent en **scientifique/data**, en **web back-end** (frameworks Django, Flask, FastAPI…), mais aussi pour des outils d’administration, du prototypage rapide, etc.

Sa syntaxe accessible en fait également un choix populaire pour l’enseignement et les débutants.

<!--

* **Un langage polyvalent et mature** : Python est un langage de programmation interprété, orienté objet et à typage dynamique, créé en 1991 (soit 4 ans avant Java). Conçu par Guido van Rossum, il met l’accent sur la lisibilité et la concision du code.
* **Philosophie “Zen of Python”** : La philosophie de Python se résume en 19 principes (importez le module `this` pour les lire). Par exemple : *« Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex... Readability counts. »*. En pratique, Python favorise un code clair et lisible, en privilégiant l’indentation pour structurer les blocs plutôt que des symboles encombrants. Cette clarté donne souvent l’impression de lire du pseudo-code.
* **Écosystème riche (“batteries incluses”)** : Python fournit une vaste bibliothèque standard prête à l’emploi, couvrant la majorité des besoins courants (traitement texte, fichiers, web, etc.). De plus, un écosystème florissant de bibliothèques externes est disponible via le *Python Package Index* (PyPI) et gérable avec l’outil `pip`. On trouve des modules pour à peu près tout (API web, accès BDD, science des données, tests…), ce qui évite de “réinventer la roue” et accélère le développement.
* **Usages principaux** : Initialement utilisé pour le scripting et l’automatisation, Python est aujourd’hui très présent en **scientifique/data** (analyses, IA/ML, où il domine grâce à des libs comme NumPy, pandas, TensorFlow…), en **web back-end** (frameworks Django, Flask, FastAPI…), mais aussi pour des outils d’administration, du prototypage rapide, etc. Sa syntaxe accessible en fait également un choix populaire pour l’enseignement et les débutants.

-->

---
transition: slide-left
---
# Syntaxe de base : différences clés avec Java

* **Indentation au lieu des accolades** : *“Readability counts”*.

  ```python
  # Exemple Python
  if x > 0:
      print("Positif")
  else:
      print("Non positif")
  ```

  ```java
  // Exemple Java équivalent
  if (x > 0) {
      System.out.println("Positif");
  } else {
      System.out.println("Non positif");
  }
  ```

* **Pas de point-virgule ni de type explicite** : le langage est *dynamiquement typé* mais *fortement typé*

* **Types de base et collections** : `int`de taille arbitraire, *collections* (list, tuples, dictionnaires), *Tout est objet*

---
transition: slide-left
---
# Ecrire du code élégant en Python


**Philosophie : Le Zen of Python**
```python
import this
```

Extraits clés :
- Beautiful is better than ugly.
- Simple is better than complex.
- Readability counts.
- There should be one — and preferably only one — obvious way to do it.

---
transition: slide-left
---
# Ecrire du code élégant en Python

**Structures idiomatiques**

| Objectif | Pythonic ✅ | Moins Pythonic ❌ |
|---------|-------------|-------------------|
| **Boucle avec index** | `for i, v in enumerate(items):` | `i = 0; for v in items:` |
| **Parcours d’un dictionnaire** | `for k, v in d.items():` | `for k in d: v = d[k]` |
| **Compréhensions** | `[x**2 for x in range(10)]` | `for x in range(10): ... append(x**2)` |
| **Conditions courtes** | `if x:` ou `if not x:` | `if x == True:` ou `if len(x) == 0:` |
| **Appartenance** | `if x in my_list:` | `for y in my_list: if x == y:` |

---
transition: slide-left
---
# Ecrire du code élégant en Python

**Gestion des ressources**

```python
with open("data.txt") as f:
    content = f.read()
```
✅ Automatiquement fermé, même en cas d'erreur.

---
transition: slide-left
---
# Ecrire du code élégant en Python

**Exceptions plutôt que codes d’erreurs**

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

*"It's easier to ask for forgiveness than permission" (EAFP)*


  <!--
  Python n’utilise pas `{}` pour délimiter les blocs de code. L’indentation (retraits) est *significative* et sert à grouper les instructions. Par exemple, un `if` en Python s’écrit sans parenthèses et avec un `:` puis un bloc indenté, au lieu d’accolades. Cette contrainte de formatage rend le code plus uniforme et lisible, conformément à la maxime *“Readability counts”*.

  **Pas de point-virgule ni de type explicite** : En Python, chaque fin d’instruction est implicite (pas besoin de `;`), et il n’y a pas de mot-clé comme `public`/`static`. Surtout, on ne déclare pas le type des variables ou des paramètres : le langage est *dynamiquement typé*. Par exemple `count = 10` suffit pour créer un entier. Le type de `count` pourra changer plus tard (c’est autorisé) et sera vérifié *à l’exécution* seulement. En contrepartie, Python est **fortement typé** : une opération entre types incompatibles provoquera une exception (par ex. additionner un entier et une chaîne sans conversion). Il n’y a pas de conversion implicite silencieuse, ce qui évite des résultats incohérents.
  **Types de base et collections** : Python offre des types built-in équivalents à ceux de Java, mais utilisables plus simplement : entiers (`int` de taille arbitraire), flottants (`float` en double précision), booléens (`True/False`), chaînes de caractères (`str`), et des **collections** puissantes en standard : listes (`list`) dynamiques, tuples (immuables), dictionnaires (`dict` pour des paires clé-valeur, équivalent des maps), ensembles (`set`)… Ces types disposent de méthodes natives utiles (par ex. `len(obj)` pour la taille, `mylist.append(x)` pour ajouter, etc.), et supportent des **opérateurs** intuitifs (concatenation de listes par `+`, appartenance avec `in`, répétition d’une chaîne par `*`, etc.). **Tout est objet** en Python : même les nombres ou fonctions sont des objets offrant des attributs ou méthodes.
  -->

---
transition: slide-left
---
# Structures de contrôle : conditions et boucles

* **Conditions (`if/elif/else`)** : 

  ```python
  if score >= 60:
      grade = "Passed"
  elif score >= 50:
      grade = "Rattrapage"
  else:
      grade = "Failed"
  ```

  En Python, toute valeur peut servir de condition (y compris `None`, listes vides, etc., qui sont considérées comme *False* si vide/zéro). Pas besoin d’écrire `if (obj != null)` : on fait simplement `if obj:` pour tester la présence d’un objet.


<!--
* **Conditions (`if/elif/else`)** : La syntaxe conditionnelle est proche de Java en logique, mis à part l’absence de parenthèses et l’indentation à la place des accolades. On utilise `if`, `elif` (contraction de “else if”) et `else`. Exemple :

  ```python
  if score >= 60:
      grade = "Passed"
  elif score >= 50:
      grade = "Rattrapage"
  else:
      grade = "Failed"
  ```

  En Python, toute valeur peut servir de condition (y compris `None`, listes vides, etc., qui sont considérées comme *Falsey* si vide/zéro). Pas besoin d’écrire `if (obj != null)` : on fait simplement `if obj:` pour tester la présence d’un objet.
-->

---
transition: slide-left
---
# Structures de contrôle : conditions et boucles

* **Boucles** : Python propose la boucle `while` (semblable à Java) et surtout la boucle **`for`** de haute niveau. Un `for` Python itère directement sur les éléments d’une séquence (liste, tuple, chaîne, etc.) ou tout itérable, plutôt que d’utiliser un index numérique explicite. Par exemple :

  ```python
  fruits = ["pomme", "banane", "cerise"]
  for fruit in fruits:
      print(fruit)  # affiche chaque fruit
  ```

Pour des itérations numérotées, on utilise *range* (ex: `for i in range(5):` boucle de 0 à 4). 

Il n’existe pas de boucle `for` style C (`for(int i=0; i<…; i++)`) directement, ni de `do/while` en Python (on utilise `while True` avec break si besoin).


<!--
  Pour des itérations numérotées, on utilise la fonction *range* (ex: `for i in range(5):` boucle de 0 à 4). Cela simplifie des boucles qui seraient plus verbeuses en Java. À noter qu’il n’existe pas de boucle `for` style C (`for(int i=0; i<…; i++)`) directement, ni de `do/while` en Python (on utilise `while True` avec break si besoin).
-->

---
transition: slide-left
---
# Fonctions et classes en Python

* **Définition de fonction** : On déclare une fonction avec le mot-clé `def`. Il n’est pas requis d’indiquer le type de retour ni le type des paramètres. Exemple :

  ```python
  def greet(name):
      return f"Hello, {name}!"
  ```

  En l’absence de `return`, une fonction retourne implicitement `None`. Python permet aussi des paramètres optionnels avec des valeurs par défaut (`def foo(x, debug=False): ...`) et un nombre variable d’arguments (`*args`, `**kwargs`).
  
  Il n’y a pas de surcharge de fonctions par signature différente comme en Java : on gère les variantes via les paramètres par défaut ou en testant les types à l’exécution.

---
transition: slide-left
---
# Fonctions et classes en Python

* **Programmation orientée objet** : Python prend en charge la POO avec des **classes** et **héritage** (simple ou multiple).

  ```python
  class Animal:
      def __init__(self, nom):
          self.nom = nom
      def parle(self):
          print("Je suis un animal.")

  class Chien(Animal):              # Hérite de Animal
      def parle(self):             # redéfinition de la méthode
          print("Woof! Je m’appelle", self.nom)

  rex = Chien("Rex")
  rex.parle()  # Woof! Je m’appelle Rex
  ```

  Pas de `public/private` sur les attributs : par convention, un nom commençant par `_` indique une variable interne. 
  Tous les membres sont accessibles par défaut, Python s’en remet au discernement du développeur (*“we are all consenting adults here”*). 
  
  Le polymorphisme est naturel (typage dynamique + duck typing).

  <!-- 
   La syntaxe est concise : `class MaClasse(ParentClass):` puis des méthodes indentées. Le constructeur s’appelle `__init__(self, ...)`. Par exemple :
  -->

---
transition: slide-left
---
# Modules, import et organisation du code

* **Modules et packages** :

En Python, chaque fichier `.py` est un **module** pouvant être importé.

Les modules sont organisés en **packages** (répertoires avec un fichier `__init__.py`).

* **Bibliothèques tierces** : Grâce à l’écosystème Python, on peut installer des packages externes via **pip** (gestionnaire de paquets Python). 

* **environnement virtuel** isolé par projet pour installer ces dépendances (voir bonnes pratiques).

<!--
* **Modules et packages** : En Python, chaque fichier `.py` est un **module** pouvant être importé. On utilise l’instruction `import` pour réutiliser du code d’un module (standard ou tiers) dans un autre. Par exemple, `import math` donne accès aux fonctions mathématiques du module standard *math*, et `import monmodule` importe le fichier `monmodule.py` local. On peut aussi écrire `from monmodule import une_fonction` pour importer un membre spécifique. Les modules sont organisés en **packages** (répertoires avec un fichier `__init__.py`). Cette modularité encourage le principe *DRY* (Don’t Repeat Yourself) en réutilisant le code. *Note:* Les “packages” Python diffèrent des packages Java : il s’agit concrètement de dossiers de modules, sans lien avec le concept de classpath du JVM.
* **Bibliothèques tierces** : Grâce à l’écosystème Python, on peut installer des packages externes via **pip** (gestionnaire de paquets Python). Par exemple `pip install requests` installe la lib `requests` pour faire des appels HTTP. Ces modules tiers s’importent ensuite comme les autres (`import requests`). Il est recommandé d’utiliser un **environnement virtuel** isolé par projet pour installer ces dépendances (voir bonnes pratiques).
-->

---
transition: slide-left
---

# Modules, import et organisation du code

## Pourquoi utiliser un environnement virtuel ?
- Éviter les conflits entre projets
- Ne pas polluer le Python système
- Répliquer facilement un environnement de développement ou production

## Comparatif rapide

| Outil      | Inclus par défaut | Isolation | Gestion des dépendances | Verrouillage | Simplicité |
|------------|-------------------|-----------|--------------------------|--------------|------------|
| `venv`     | ✅ Oui             | ✅ Oui     | ❌ Manuelle (`pip`)       | ❌ Optionnel  | ✅ Facile   |
| `pipenv`   | ❌ Non             | ✅ Oui     | ✅ Pipfile               | ✅ Pipfile.lock | ⚠️ Moyenne |
| `poetry`   | ❌ Non             | ✅ Oui     | ✅ pyproject.toml        | ✅ poetry.lock | ✅ Moderne  |


---
transition: slide-left
---
# Modules, import et organisation du code

## Structure typique d’un package

```
mon_package/
├── mon_package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   └── test_module1.py
├── pyproject.toml
├── README.md
```

Depuis PEP 518, c'est le format standard pour décrire un projet Python [Poetry] :
```toml
[tool.poetry]
name = "mon_package"
version = "0.1.0"
description = "Une super librairie Python"
authors = ["Votre Nom <email@example.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.8"
```

---
transition: slide-left
---
# Gestion des exceptions (erreurs)

* **Modèle d’exception** : Python utilise des exceptions pour signaler les erreurs, tout comme Java, mais *toutes* les exceptions sont non vérifiées (*unchecked*).
* **`try/except/finally`**

  ```python
  try:
      f = open("data.txt", "r")
      data = int(f.read())
  except FileNotFoundError as e:
      print("Fichier introuvable:", e)
  except ValueError as e:
      print("Donnée non valide:", e)
  else:
      print("Lecture réussie, nombre =", data)
  finally:
      if f:
          f.close()
  ```

* **Lever des exceptions** : Comme en Java avec `throw`, on peut déclencher une exception via l’instruction `raise`. Python possède de nombreuses exceptions intégrées (ValueError, TypeError, IOError, etc.), et on peut définir des exceptions personnalisées en créant des classes héritant de `Exception`.

<!--
 C’est-à-dire qu’on n’est pas forcé de déclarer ou capturer une exception donnée. Si une exception n’est pas interceptée, le programme interrompra son exécution et affichera une trace (*stack trace*).
 La syntaxe pour gérer les exceptions en Python ressemble à Java avec quelques mots-clés différents. On enclôt le code à risque dans un bloc `try:`, puis on ajoute des clauses `except ExcepType as e:` pour chaque type d’erreur à gérer. Le bloc `finally:` (optionnel) s’exécute dans tous les cas, que l’exception soit levée ou non, typiquement pour faire du nettoyage. Il existe aussi un bloc `else:` (optionnel) qui s’exécute si aucune exception n’est levée dans le try. Exemple :
 
  Ici on gère deux exceptions spécifiques (fichier non trouvé, et conversion invalide). Le `finally` ferme le fichier dans tous les cas Cette structure est l’équivalent de `try-catch-finally` en Java. À noter que grâce au mot-clé `with` utilisé plus haut, on évite souvent d’avoir à écrire manuellement le finally pour les fichiers.
-->