#!/usr/bin/env python3
"""concurrent execution"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """concurrent execution"""
    delays = []
    returns = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    for i in delays:
        returns.append(sorted(i))
    return returns
