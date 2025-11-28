#!/usr/bin/env python3
"""
Ce module mesure le temps d'exécution pour lancer 4 fois
la fonction async_comprehension en parallèle.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure le temps nécessaire pour exécuter
    4 fois async_comprehension en parallèle.

    Returns:
        float: Durée totale d'exécution en secondes.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
