#!/usr/bin/env python3
"""
module for task 3
"""
from asyncio import create_task, Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    create task py using create_task().
    """
    return create_task(wait_random(max_delay))
