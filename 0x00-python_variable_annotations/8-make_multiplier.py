#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a Callable, multiplies multiplier by a float"""
    return lambda x: x * multiplier
