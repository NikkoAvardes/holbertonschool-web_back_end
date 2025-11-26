#!/usr/bin/env python3
"""
Ce module fournit une fonction pour mesurer le temps moyen d'exécution
 de plusieurs coroutines asynchrones.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps moyen d'exécution de n coroutines wait_n.

    Args:
        n (int): Le nombre de coroutines à lancer.
        max_delay (int): Le délai maximal pour chaque attente.

    Returns:
        float: Le temps moyen d'exécution par coroutine.
    """
    t1 = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t2 = time.perf_counter()
    total_time = t2 - t1
    return total_time / n
