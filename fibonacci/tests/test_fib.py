from typing import Callable
import pytest
from fibonacci.dynamic import fibonacii_dynamic, fibonacii_dynamic_v2

# from fibonacci.my_decorators import my_parametrized
from fibonacci.naive import fibonacci_naive
from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
from fibonacci.conftest import time_tracker


@pytest.mark.parametrize(
    "fib_func",
    [
        fibonacci_naive,
        fibonacci_cached,
        fibonacci_lru_cached,
        fibonacii_dynamic,
        fibonacii_dynamic_v2,
    ],
)
@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
# @my_parametrized(identifiers="n,expected", values=[(0,0),(1,1),(2,1),(20,6765)])
def test_fibonacci(
    time_tracker, fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    res = fib_func(n)
    assert res == expected
