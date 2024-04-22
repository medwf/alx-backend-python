#!/usr/bin/env python3
"""
module for task 1
"""
from asyncio import gather
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    Args:
        n: <int> repeat max_delay.
        max_delay: <int> max delay.
    return:
        <list[float]>: list of all the delays (float values) sorted.
    """
    return sorted(
        await gather(
            *list(
                map(lambda _: wait_random(max_delay), range(n))
            )
        )
    )
