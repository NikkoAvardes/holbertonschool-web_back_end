#!/usr/bin/env python3
"""
Ce module fournit une fonction pour obtenir la partie entière inférieure
 d'un nombre flottant.
"""

import math


def floor(n: float) -> int:
    """
    Retourne la partie entière inférieure d'un nombre flottant.

    Args:
        n (float): Le nombre à arrondir vers le bas.

    Returns:
        int: La partie entière inférieure du nombre.
    """
    return math.floor(n)
