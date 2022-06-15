#!/usr/bin/env python3
"""Hypermedia pagination"""
from typing import Dict, Tuple
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
        """Get page information a return the index of data"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page > 0

        self.dataset()
        if page * page_size > len(self.__dataset):
            return []

        res = index_range(page, page_size)

        data = [self.__dataset[i] for i in range(res[0], res[1])]

        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the following key-value pairs"""
        data = self.get_page(page, page_size)
        total_pages = round(len(self.__dataset) / page_size)

        size = page_size

        if page + 1 < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        if data == []:
            size = 0
            next_page = None
            prev_page = page - 1
            total_pages = math.floor(len(self.__dataset) / page_size) + 1

        returnDict = {'page_size': size, 'page': page, 'data': data,
                      'next_page': next_page, 'prev_page': prev_page,
                      'total_pages': total_pages}

        return returnDict
