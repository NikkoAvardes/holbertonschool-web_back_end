#!/usr/bin/env python3
"""
Ce module fournit une fonction pour calculer la somme d'une liste d'entiers
 et de flottants.
"""

import typing


def sum_mixed_list(
    mxd_lst: typing.List[typing.Union[int, float]]
) -> float:
    """
    Calcule la somme des éléments d'une liste d'entiers et de flottants.

    Args:
        mxd_lst (List[Union[int, float]]): La liste des nombres à additionner.

    Returns:
        float: La somme des éléments de la liste.
    """
    return sum(mxd_lst)
