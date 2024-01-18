#!/usr/bin/env python3
""" asyncio.gather """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension four times in
    parallel using asyncio.gather.
    measure total runtime and return it.
    """
    start = time.time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    return ((time.time()) - start)
