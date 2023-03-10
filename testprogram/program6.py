import pytest
def add(n):
    a=0

    for i in n:
        a=a+i
    return a
# print(add(a))

@pytest.mark.parametrize("n,expected_output",[
    ([1,2,3,4,5,],15),
    ([2,2,2,2,2],10),
    ([1.2,2.2,3.2,5.5,2.1],14.2)
])
def test_add(n,expected_output):
    assert add(n) == expected_output