#!/usr/bin/env python3
"""
module for task 4
"""
from typing import List
from asyncio import gather
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
                map(lambda _: task_wait_random(max_delay), range(n))
            )
        )
    )
