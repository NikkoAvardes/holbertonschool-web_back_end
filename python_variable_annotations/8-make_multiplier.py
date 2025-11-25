#!/usr/bin/env python3
"""
Ce module fournit une fonction pour créer
un multiplicateur sous forme de fonction.
"""

import typing


def make_multiplier(
    multiplier: float
) -> typing.Callable[[float], float]:
    """
    Retourne une fonction qui multiplie son argument par
    un multiplicateur donné.

    Args:
        multiplier (float): Le facteur de multiplication.

    Returns:
        Callable[[float], float]: Une fonction qui multiplie
        un nombre par le multiplicateur.
    """
    def make_function(x: float) -> float:
        """
        Multiplie un nombre flottant par le multiplicateur.

        Args:
            x (float): Le nombre à multiplier.

        Returns:
            float: Le résultat de la multiplication.
        """
        return x * multiplier
    return make_function
