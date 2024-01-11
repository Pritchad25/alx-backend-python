#!/usr/bin/env python3
""" Returns sum of an input of floats """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ This function sums the list of floats """
    total: float = 0
    for x in input_list:
        total += x
    return total
