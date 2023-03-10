import pytest


@pytest.fixture
def input_number():
    input=12
    return input
def test_divisible_by_3(input_number):
    assert input_number % 3 ==0
def test_divisible_by_6(input_number):
    assert input_number % 6 == 0

