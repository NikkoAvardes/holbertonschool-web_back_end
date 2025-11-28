#!/usr/bin/env python3
"""
Ce module fournit une fonction qui utilise une compréhension asynchrone
pour collecter les valeurs générées par async_generator.
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collecte 10 nombres flottants générés de façon asynchrone par async_generator.

    Returns:
        list[float]: Liste des 10 nombres générés.
    """
    result = [i async for i in async_generator()]
    return result
