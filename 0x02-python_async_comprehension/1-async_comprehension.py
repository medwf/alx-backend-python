#!/usr/bin/env python3
"""
module for task 1
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    coroutine will collect 10 random numbers
        using an async comprehension over async_generator
    """
    return [number async for number in async_generator()]
