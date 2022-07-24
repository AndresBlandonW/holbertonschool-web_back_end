#!/usr/bin/env python3
"""Redis Cache module"""
from functools import wraps
import redis
from typing import Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Decorator to count number of times methods are called"""
    @wraps(method)
    def count_calls_wrapper(self, *args) -> bytes:
        """Counts number of calls wrapped function makes"""
        self._redis.incr(method.__qualname__)
        return method(self, *args)

    return count_calls_wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function"""
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def call_history_wrapper(self, *args) -> bytes:
        """Stores the history of inputs and outputs for a function"""
        self._redis.rpush(inputs, str(args))
        out = method(self, *args)
        self._redis.rpush(outputs, out)

        return out

    return call_history_wrapper


def replay(method: Callable) -> str:
    """Display the history of calls of a particular function"""
    name = method.__qualname__
    inputs = f"{name}:inputs"
    outputs = f"{name}:outputs"
    r = redis.Redis()
    data = r.get(name).decode('utf-8')
    input_list = r.lrange(inputs, 0, -1)
    output_list = r.lrange(outputs, 0, -1)

    print(f"{name} was called {data} times:")

    for ins, outs in zip(input_list, output_list):
        print(f"{name}(*{ins.decode('utf-8')}) -> {outs.decode('utf-8')}")


class Cache():
    """Redis cache object"""
    def __init__(self):
        """Initialize a Cache object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random uuid key, store data in key, return key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get data based on key, return data as specified type based on fn"""
        if fn:
            value = self._redis.get(key)
            return fn(value)

        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Typecast the key to a str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Typecast the key to an int"""
        return self.get(key, int)
