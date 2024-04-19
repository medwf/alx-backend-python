#!/usr/bin/env python3
'''
import List from typing.
function sum_list:
    input_list: is a list of float.
return:
    (float) : sum of list.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    method:
        Computes the sum of a list of floating-point numbers.
    Args:
        input_list: (list of float).
    return:
        (float) - sum of list of float.
    '''
    return float(sum(input_list))
