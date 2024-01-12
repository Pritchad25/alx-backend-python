#!/usr/bin/env python3
""" Annotates the function parameters and returns values """

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function performs Duck-typing """
    return [(i, len(i)) for i in lst]
