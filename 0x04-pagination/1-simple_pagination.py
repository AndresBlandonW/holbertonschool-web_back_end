#!/usr/bin/env python3
"""Simple helper functionx"""
from tracemalloc import start
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a list for those particular pagination parameters"""
    start = (page * page_size) - page_size
    end = page * page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page > 0

        self.dataset()
        if page * page_size > len(self.__dataset):
            return []

        res = index_range(page, page_size)

        data = [self.__dataset[i] for i in range(res[0], res[1])]

        return data
        
