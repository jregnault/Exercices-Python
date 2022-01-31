"""Ce fichier contient les tests vérifiant
que les réponses aux questions sont correctes.
Ne pas modifier."""
from sys import stderr
from unittest import TestCase, mock
import unittest

import exercice as e

import inspect
from textwrap import dedent
import re


class MockFunction:
    """ Defines a Mock for functions to explore the details on their execution.
    """
    def __init__(self, func):
        self.func = func

    def __call__(mock_instance, *args, **kwargs):
        # Add locals() to function's return
        code = re.sub('[\\s]return\\b', ' return locals(), ', dedent(
            inspect.getsource(mock_instance.func)))
        code = code + f'\nloc, ret = {mock_instance.func.__name__}(*args, **kwargs)'
        loc = {'args': args, 'kwargs': kwargs}
        exec(code, mock_instance.func.__globals__, loc)
        # Put execution locals into mock instance
        for l,v in loc['loc'].items():
            setattr(mock_instance, l, v)
        return loc['ret']


class ExerciceTest(TestCase):

    @mock.patch(f'exercice.exercice1', autospec=True, side_effect=MockFunction(e.exercice1))
    def test1(self, mocked):
        ret = e.exercice1()

        self.assertEqual(10, mocked.side_effect.a)
        self.assertEqual(2.21, mocked.side_effect.b)
        self.assertEqual(12.21, mocked.side_effect.c)
    
    def test2(self):
        with mock.patch('builtins.input', return_value="Johan") as mocked_input:
            with mock.patch('builtins.print') as mocked_print:
                e.exercice2()
                mocked_input.assert_called_with("Quel est votre nom?: ")
                mocked_print.assert_called_with("Bonjour Johan.")


if __name__ == "__main__":
    unittest.main()
