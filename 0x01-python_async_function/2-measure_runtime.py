#!/usr/bin/env python3
"""
module for task 2
"""
import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure the Total execution time
    """
    start = time.time()
    run(wait_n(n, max_delay))
    end = time.time()
    return end - start
