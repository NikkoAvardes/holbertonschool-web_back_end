#!/usr/bin/env python3
"""
Ce module fournit un générateur asynchrone qui produit 10 nombres.
entre 0 et 10, avec une pause d'une seconde entre chaque génération.
"""
import asyncio
import random


async def async_generator():
    """
    Génère 10 nombres flottants aléatoires entre 0 et 10.

    Yields:
        float: Un nombre flottant aléatoire entre 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

x = [async_generator()]
