#!/usr/bin/env python3
"""
this module for task 0
"""

from asyncio import sleep
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    yield a random number between 0 and 10.
    """
    for _ in range(0, 10):
        await sleep(1)
        yield uniform(0, 10)
