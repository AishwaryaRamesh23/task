import pytest
from source.calculator import add,subtract,multiply,divide

# @pytest.fixture
# def numbers(request):
#     num1= int(request.config.getoption("--num1"))
#     num2= int(request.config.getoption("--num2"))
#     return (num1,num2)

# Define a fixture with scope
@pytest.fixture(scope="module")
def numbers():
    return (10, 5)

@pytest.mark.math
def test_add(numbers):
    a,b=numbers
    assert add(a,b)==a+b

@pytest.mark.math
def test_subtract(numbers):
    a,b=numbers
    if b>a:
        a,b=b,a
    assert subtract(a,b)==a-b

@pytest.mark.math
def test_multiplication(numbers):
    a,b=numbers
    assert multiply(a,b)==a*b

@pytest.mark.math
def test_divide(numbers):
    a,b=numbers
    assert divide(a,b)==a/b

@pytest.mark.exception
def test_divide_by_zero():
    with pytest.raises(ValueError,match="Cannot divide by zero"):
        divide(10,0)



