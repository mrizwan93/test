import calculator
import pytest
import sys

#orignal code
# @pytest.mark.skipif(sys.version_info >(3, 6), reason="not needed")
# def test_add():
#     assert calculator.add(3,5) == 8
#     assert calculator.add(20,10)== 30
#     assert calculator.add(100,20)== 120
#
# def test_multiply():
#     assert calculator.multiply(3,5)== 15
#     assert calculator.multiply(10,10)== 100
#     assert calculator.multiply(15,5)== 75
#
# def test_subtract():
#     assert calculator.subtract(5,3)== 2
#     assert calculator.subtract(3,5)== 2
#     assert calculator.subtract(10,3)== 7
#
# def test_division():
#     assert calculator.division(10,2)== 5
#     assert calculator.division(0,10)== None
#     assert calculator.division(2,30)== 15
#
# @pytest.mark.windows
# def test_window():
#     assert True


#compressed code
@pytest.mark.skipif(sys.version_info >(3, 6), reason="not needed")
@pytest.mark.parametrize("a, b, result", [(3, 5, 8), (20, 10, 30), (100, 20, 120)])
def test_add(a, b, result):
    assert calculator.add(a, b) == result

@pytest.mark.parametrize("a, b, result",[(3, 5, 15), (10, 10, 100), (15, 5, 75)])
def test_multiply(a, b, result):
    assert calculator.multiply(a, b)== result

@pytest.mark.parametrize("a, b, result",[(5, 3, 2), (3, 5, 2), (10, 3, 7)])
def test_subtract(a, b, result):
    assert calculator.subtract(a,b)== result

@pytest.mark.parametrize("a, b, result",[(10, 2, 5), (0, 10, None), (2, 30, 15)])
def test_division(a, b, result):
    assert calculator.division(a,b)== result

