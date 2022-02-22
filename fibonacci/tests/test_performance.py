import pytest
from fibonacci.dynamic import fibonacii_dynamic_v2
from conftest import track_performance


@pytest.mark.performance
@track_performance
def test_performance():
    fibonacii_dynamic_v2(1000)
