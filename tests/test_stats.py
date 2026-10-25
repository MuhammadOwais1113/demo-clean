import pytest

from demo_clean import mean, normalize


def test_mean():
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


def test_normalize():
    assert normalize([0.0, 5.0, 10.0]) == [0.0, 0.5, 1.0]


def test_normalize_constant():
    assert normalize([4.0, 4.0]) == [0.0, 0.0]
