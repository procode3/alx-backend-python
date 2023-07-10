#!/usr/bin/env python3
"""Creates an function that returns an asyncio.Task"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returning an async task"""
    return asyncio.create_task(wait_random(max_delay))
