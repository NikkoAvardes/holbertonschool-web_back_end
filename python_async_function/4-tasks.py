#!/usr/bin/env python3
"""
Ce module fournit une coroutine pour exécuter plusieurs attentes asynchrones
et retourner leurs délais.
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Lance n coroutines de wait_random et retourne la liste des délais obtenus.

    Args:
        n (int): Le nombre de coroutines à lancer.
        max_delay (int): Le délai maximal pour chaque attente.

    Returns:
        List[float]: Liste des délais attendus pour chaque coroutine.
    """
    coroutine = [wait_random(max_delay) for _ in range(n)]
    delay = []
    for x in asyncio.as_completed(coroutine):
        result = await x
        delay.append(result)
    return delay
