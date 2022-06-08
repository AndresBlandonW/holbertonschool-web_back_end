#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random

async def wait_random(max_delay = 0):
    """that waits for a random delay"""
    return random.uniform(0, max_delay)
