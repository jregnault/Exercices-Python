1 - Les variables
=================

## 1. Définition
Une variable peut se représenter comme une boîte que l'on nomme et dans laquelle on peut mettre quelque chose pour s'en servir plus tard dans le code.

En Python, on utilise la syntaxe `nom = valeur` pour créer une variable.
Dans la suite de ce document, nous verrons quelques exemples de déclaration de variable avec les différents types de données que l'on peut rencontrer.

### 1.1 Les nombres
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