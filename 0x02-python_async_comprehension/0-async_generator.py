#!/usr/bin/env python3
"""Generators using yield"""
import asyncio
import random
from typing import List

async def async_generator() -> List[float]:
    """Coroutine will loop 10 times, each time asynchronously wait 1 second,"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
