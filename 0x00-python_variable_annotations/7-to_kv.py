!/usr/bin/env python3
from typing import Union, Tuple
""" Takes as input a str and int or float, returns tuple """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ This function returns tuple """
    new_tup: Tuple[str, Union[int, float]] = (k, v**2)
    return new_tup
