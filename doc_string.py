import math
import inspect

# Спросим, что хорошего в этой библиотеке.
print(math.__doc__)

print('@@@@@@@@@@@@@@@@ print @@@@@@@@@@@@')
print(print.__doc__)

# Будет напечатано:
# This module provides access to the mathematical functions
# defined by the C standard. 

"""Документация модуля. Описывает работу классов и функций.
Размещается в верхней части файла (начиная с первой строки).
"""
# Импортируйте модуль inspect.



def tricky_func(self):
    """Описывает работу функции tricky_func."""
    ...


class Test:
    """Класс Test используется для демонстрации docstring."""

    def first(self):
        """Описывает метод first и демонстрирует перенос строки
        документации.
        """
        ...


print('Без применения cleandoc:')
print(Test.first.__doc__)
print('С применением cleandoc:')
print(inspect.cleandoc(Test.first.__doc__))  # Выведите докстринг, используя метод cleandoc().