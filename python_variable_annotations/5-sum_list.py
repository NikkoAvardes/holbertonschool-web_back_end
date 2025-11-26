#!/usr/bin/env python3
"""
Ce module fournit une fonction pour calculer la somme d'une liste de flottants.
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    Calcule la somme des éléments d'une liste de nombres flottants.

    Args:
        input_list (list[float]): La liste des nombres à additionner.

    Returns:
        float: La somme des éléments de la liste.
    """
    return sum(input_list)
