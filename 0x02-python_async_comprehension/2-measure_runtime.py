#!/usr/bin/env python3
"""
module for task 2
"""
from time import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the total runtime and return it.
    """
    start = time()

    # run async_comprehension 4 time using gather.
    await gather(*(async_comprehension() for _ in range(4)))
    return time() - start
