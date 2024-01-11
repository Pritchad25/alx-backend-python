#!/usr/bin/env python3
""" Returns sum of an input of floats and ints """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This function sums the list and returns float """
    total: float = 0
    for x in mxd_lst:
        total += x
    return total
