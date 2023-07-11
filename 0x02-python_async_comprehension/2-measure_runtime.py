#!/usr/bin/python3
"""Couroutine that will exercute async_comprehension asychronously"""


from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measuring time for for runs of async_comprehension"""
    start = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    return time() - start
