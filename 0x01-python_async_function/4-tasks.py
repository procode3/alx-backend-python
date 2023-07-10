#!/usr/bin/env python3
"""concurrent execution"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """concurrent execution"""
    delays = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
