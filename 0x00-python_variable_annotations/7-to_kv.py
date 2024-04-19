#!/usr/bin/env python3
'''
import List, Union from typing.
function to_kv:
    k: is a string.
    v: is a integer or float - using Union
return:
    (tuple) : (k: str, v^2: float)
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    method:
        Complex types - string and int/float to tuple
    Args:
        k: (str).
        v: int of float.
    return:
        (table) - have a k, v^2: float
    """
    return (k, float(v ** 2))
