#!/usr/bin/env python3
"""
Module : 0-simple_helper_function
Ce module fournit une fonction utilitaire pour la pagination.

Fonction :
    index_range(page: int, page_size: int) -> Tuple[int, int]
        Calcule les indices de début et de fin pour une page donnée.
"""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
    Calcule les indices de début et de fin pour une pagination.

    Args:
        page (int): Le numéro de la page (commence à 1).
        page_size (int): Le nombre d'éléments par page.

    Returns:
        Tuple[int, int]: Un tuple (start, end) où start est l'indice de début
        (inclus) et end est l'indice de fin (exclu).
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
