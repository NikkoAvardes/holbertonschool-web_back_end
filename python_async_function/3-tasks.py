#!/usr/bin/env python3
"""
Ce module fournit une fonction utilitaire pour créer une tâche asynchrone
qui attend un délai aléatoire.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée et retourne une tâche asyncio pour exécuter wait_random
    avec un délai maximal donné.

    Args:
        max_delay (int): Le délai maximal en secondes pour l'attente aléatoire.

    Returns:
        asyncio.Task: La tâche asynchrone créée pour l'attente aléatoire.
    """
    return asyncio.create_task(wait_random(max_delay))
