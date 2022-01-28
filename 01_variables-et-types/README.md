1 - Variables et types de données
=================================

## 1. Variable: Définition et syntaxe
Une variable peut se représenter comme une boîte que l'on nomme et dans laquelle on peut mettre quelque chose pour s'en servir plus tard dans le code.

En Python, on utilise la syntaxe `nom = valeur` pour créer une variable.
Dans la suite de ce document, nous verrons quelques exemples de déclaration de variable avec les différents types de données que l'on peut rencontrer.

## 2. Types de données en Python

### 1. Les nombres
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

### 2. Le texte
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

#### 2.1 Opérations sur le texte
Dans certains cas, on veut ajouter des informations dans un texte pour les afficher à l'utilisateur.
On peut les imprimer les unes à la suite des autres avec des appels consécutifs à la fonction `print()`,
cependant en plus d'être fastidieux, chaque appel imprime sur une nouvelle ligne,
rendant la lecture compliquée.

Pour remédier à ce problème, on peut effectuer des opérations sur le texte pour accomplir ces tâches.

Supposons que l'on réalise un programme qui demande son prénom à l'utilisateur, puis l'affiche dans un message. Une approche naïve serait:

```python
name = input("Quel est votre prénom?: ")
print("Bonjour ")
print(name)
```

Ici, la première ligne stocke le prénom de l'utilisateur en utilisant la fonction `input()` permettant d'afficher le message fourni puis de récupérer ce qu'a entré l'utilisateur.

Si on s'intéresse à la sortie produite par ce programme, on obtient:

```
Quel est votre prénom?: John
Bonjour 
John
```

C'est un début, mais on voudrait afficher le prénom sur la même ligne. Il y a plusieurs façons de procéder:

```python
print("Bonjour " + name)
```

En utilisant le symbole `+` sur du texte, on effectue une **concaténation** (Attention à bien ajouter un espace à la fin de la première `string` pour éviter que les deux soient collés).

Cette méthode est efficace, mais elle a ses limites:
si on veut ajouter plus de variables avec du texte entre elles,
le code risque vite de devenir illisible.
C'est pour contourner cette limite qu'en python on utilise plus souvent les `f-strings`.

Il y a deux façons d'utiliser les `f-strings`, en raison d'une évolution de la syntaxe dans le temps.
Commençons par la plus récente, qui est aussi la plus simple à utiliser:

```python
print(f"Bonjour {name}")
```

Dans cet exemple, il y a deux choses à remarquer:
la première, c'est le 'f' placé avant le texte.
Il indique à python qu'il va devoir *formatter* des éléments dans le texte qui suit.
La deuxième, c'est les crochets autour de la variable `name`.
Cette syntaxe indique à python qu'il doit évaluer ce qui se trouve à l'intérieur, dans notre exemple le prénom de l'utilisateur.
