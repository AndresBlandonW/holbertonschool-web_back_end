#!/usr/bin/env python3
"""Tasks"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    array = []
    for x in range(n):
        array.append(task_wait_random(max_delay))

        result = []
    for task in asyncio.as_completed(array):
        result.append(await task)

    return sorted(result)
