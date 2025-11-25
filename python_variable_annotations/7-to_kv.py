#!/usr/bin/env python3
"""
Ce module fournit une fonction pour créer un tuple à partir d'une chaîne
 et d'un nombre, en élevant le nombre au carré.
"""

import typing


def to_kv(
    k: str,
    v: typing.Union[int, float]
) -> typing.Tuple[str, float]:
    """
    Crée un tuple contenant une chaîne et le carré d'un nombre.

    Args:
        k (str): La chaîne à inclure dans le tuple.
        v (Union[int, float]): Le nombre à élever au carré.

    Returns:
        Tuple[str, float]: Le tuple contenant la chaîne et le carré du nombre.
    """
    return k, v**2
