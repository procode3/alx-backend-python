#!/usr/bin/env python3
from typing import List, Union
"""sum of mixed types of floats and ints"""


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """sum of mixed types of floats and ints"""
    return sum(mxd_lst)
