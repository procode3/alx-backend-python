#!usr/bin/env python3
"""finding time delta for the async functions"""

from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay:int) ->float:
    """Measuring the time difference between times"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time() - start
    return total_time / n
    
    

