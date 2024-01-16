#!/usr/bin/env python3
""" A coroutine that takes an int arg and
waits for random delay """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ An asynce that waits for random delay between 0
    nd max_delay, returns that """
    actual_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
