import pytest
def numfact(num):
    list1=[]

    for i in range(2,num):
        if num%i==0:
            list1.append(i)
            print(list1)
        continue
    return list1
# numfact(10)
@pytest.mark.parametrize("num,expected_output",[
    (10,[2,5]),
    (12,[2,3,4,6]),
])
def test_numfact(num,expected_output):
    assert numfact(num) == expected_output



