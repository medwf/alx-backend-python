#!/usr/bin/env python3
'''
import List, Union from typing.
function sum_mixed_list:
    mxd_lst: is a list of float.
return:
    (float) : sum of list[int | float].
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    method:
        Computes the sum of a list of integers and floating-point numbers.
    Args:
        mxd_lst: (list of float-int).
    return:
        (float) - sum of list of float-int
    '''
    return float(sum(mxd_lst))
