#!/usr/bin/env python3
"""
Ce module fournit une fonction asynchrone pour attendre un délai aléatoire.
"""
import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """
    Attend un délai aléatoire compris entre 0 et max_delay secondes.

    Args:
        max_delay (int, optional): Le délai maximal en secondes. Par défaut 10.

    Returns:
        float: Le délai effectivement attendu en secondes.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

asyncio.run(wait_random())
