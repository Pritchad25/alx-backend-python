#!/usr/bin/env python3
""" Takes as input float, returns func that multiplies """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function returns multiplier func """
    return (lambda x: multiplier*x)
