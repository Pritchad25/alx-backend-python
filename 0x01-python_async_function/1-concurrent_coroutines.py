#!/usr/bin/env python3
""" Takes in two int arguments and waits for
random delay """


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random



async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Async that waits for ran delay until max_delay,
    returns list of actual delays """.

    values = []

    for _ in range(n):
        values.append(await asyncio.create_task(wait_random(max_delay)))
    return sorted(values)
