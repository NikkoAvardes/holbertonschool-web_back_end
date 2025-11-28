#!/usr/bin/env python3
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
	result = [i async for i in range(10)]
