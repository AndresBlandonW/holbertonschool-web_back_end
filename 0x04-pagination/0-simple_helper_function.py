#!/usr/bin/env python3
"""Simple helper functionx"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a list for those particular pagination parameters"""
    start = (page * page_size) - page_size
    end = page * page_size

    return (start, end)
