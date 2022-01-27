1 - Les variables
=================

## 1. Définition
Une variable peut se représenter comme une boîte que l'on nomme et dans laquelle on peut mettre quelque chose pour s'en servir plus tard dans le code.

En Python, on utilise la syntaxe `nom = valeur` pour créer une variable.
Dans la suite de ce document, nous verrons quelques exemples de déclaration de variable avec les différents types de données que l'on peut rencontrer.

## 2. Les nombres
De manière générale, on distingue 2 types de nombres : les nombres entiers et les nombres à virgule flottante, nommés simplements nombres flottants.

En Python, on les retrouvent sous la forme des types `int` et `float`, et on passe souvent de l'un à autre de manière transparente, sans action supplémentaire.

Pour la syntaxe, on note:

Pour un `int`:
```python
a = 10
```

Et pour un `float`:
```python
b = 10.0
```

Il est également tout à fait possible de stocker le résultat d'un calcul directement dans la variable, par exemple:
```python
resultat = 10 + 20 * (4 / 2)
```

Enfin, on peut utiliser le contenu d'autres variables dans le calcul:
```python
a = 10
b = 5
c = a + b
```

## 3. Le texte
Dans la plupart des langages, le texte est divisé en 2 catégories : les caractères et les chaînes de caractères.
Ces 2 catégories sont représentées par les types `char` et `string`.

En python, il n'y a pas de distinction entre les deux.
Ainsi, un caractère sera définit comme une chaîne de caractères de longueur 1.

Cette particularité se retrouve dans la syntaxe utilisée:
on peut employer à loisir la `single quote (')` ou la `double quote (")` pour déclarer une `string`, là où d'autres langages employent la première pour représenter un `char`.

Les deux lignes suivantes sont donc équivalentes:
```python
a = "text"
a = 'text'
```

L'idéal est de choisir l'une des deux notations pour garder une certaine uniformité dans le code.

### 3.1 Opérations sur le texte
Le texte est l'un des moyens les plus simple de communiquer avec l'utilisateur:
on peut présenter de manière élégante le résultat d'un calcul,
afficher le contenu d'une variable pour trouver l'origine d'un bug,
ou plus simplement connaître la progression de son programme.

Python offre des fonctionnalités intéressantes qui facilitent la mise en place des cas de figures cités ci-dessus.