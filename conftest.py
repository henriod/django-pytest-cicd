from datetime import datetime, timedelta
from time import time
from typing import Callable

import pytest


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"\n runtime {diff.total_seconds()}")


def PerformanceException(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit

    def __str__(self) -> str:
        return f"Performance test failed, runtime: {self.runtime.total_second()}, limi: {self.limit.total_second()}"


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_function_and_variables_runtime(*args, **kw):
        tick = datetime.now()
        result = method(*args, *kw)
        tock = datetime.now()
        runtime = tock - tick
        print(f"\n runtime {runtime.total_seconds()}")

        if runtime > runtime_limit:
            raise PerformanceException(runtime=runtime, limit=runtime_limit)

        return result

    return run_function_and_variables_runtime
