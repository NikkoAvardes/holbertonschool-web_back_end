#!/usr/bin/env python3
"""
Module 3-tasks.py
-----------------
Ce module contient des fonctions asynchrones pour la gestion de tâches
avec asyncio en Python. Il permet de créer et d'exécuter des coroutines
de manière concurrente, en utilisant des tâches asyncio.

Fonctions principales :
- task_wait_random : Crée une tâche asynchrone qui attend un temps aléatoire.

"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
