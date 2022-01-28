"""Ce fichier contient les tests vérifiant
que les réponses aux questions sont correctes.
Ne pas modifier."""

import exercice as e

def print_error(variable, expected, actual):
    print(f"Erreur pour la variable {variable}:\n\
    attendu : {expected}\n\
    réponse donnée : {actual}\n")

def test1():
    a, b, c = e.exercice1()
    test_passed = True

    print("===== Exercice 1 =====")

    if a != 10:
        print_error('a', 10, a)
        test_passed = False

    if b != 2.21:
        print_error('b', 2.21, b)
        test_passed = False
    
    if c != 12.21:
        print_error('c', 12.21, c)
        test_passed = False
    
    if test_passed:
        print("Tout est correct, bravo!")


def runAllTests():
    test1()
    print("===== Fin des tests =====")