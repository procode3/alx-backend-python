#!/usr/bin/env python3
from typing import Union, Tuple
"""return a tuple"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple"""
    return (k, v ** 2)
