#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 0) -> int:
    """that waits for a random delay"""
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return ran
