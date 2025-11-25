#!/usr/bin/env python3
"""
Ce module fournit une fonction pour obtenir la longueur de chaque élément
 d'un itérable de séquences.
"""

import typing


def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Retourne une liste de tuples contenant chaque élément et sa longueur.

    Args:
        lst (Iterable[Sequence]): L'itérable de séquences à traiter.

    Returns:
        List[Tuple[Sequence, int]]: Liste de tuples (élément, longueur).
    """
    return [(i, len(i)) for i in lst]
