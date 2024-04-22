#!/usr/bin/env python3

"""
function:
    wait_random: an asynchronous coroutine that takes in an integer argument
"""
import random, asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    an asynchronous coroutine that takes in an integer argument
    Args:
        max_delay: (int) default take 10.
    return:
        random value between 0, max_delay.
    """
    waitInTell = random.uniform(0, max_delay)
    await asyncio.sleep(waitInTell)
    return waitInTell
