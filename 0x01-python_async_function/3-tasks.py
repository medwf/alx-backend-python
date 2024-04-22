#!/usr/bin/env python3
"""
module for task 3
"""
from asyncio import create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    DOC
    """
    return create_task(wait_random(max_delay))
