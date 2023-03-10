import pytest
from testprogram.program5  import fact
@pytest.mark.parametrize("n,expected_output",[
    (2,2),
    (5,120),
    (8,40320),
])
def test_fact(n,expected_output):
    assert fact(n) == expected_output
