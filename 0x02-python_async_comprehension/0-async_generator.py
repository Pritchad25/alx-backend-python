#!/usr/bin/env python3
""" A coroutine that takes no arguments """

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ Async loops 10 times asyncronously, yielding random num """

    for i in range(10):
        yield random.random()
        await asyncio.sleep(1)
