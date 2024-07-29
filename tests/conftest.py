import pytest

def pytest_addoption(parser):
    parser.addoption("--num1", action="store", default=10, help="First number")
    parser.addoption("--num2", action="store", default=5, help="Second number")

@pytest.fixture
def numbers(request):
    num1 = int(request.config.getoption("--num1"))
    num2 = int(request.config.getoption("--num2"))
    return (num1, num2)

