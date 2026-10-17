#Fixtures
import pytest

@pytest.fixture(scope="module")
def preWork():
    print("I set up browser instance as module")
    return "fail"


@pytest.fixture(scope="function")
def secondWork():
    print("I set up browser instance as module")
    yield #pause
    print("this is a teardown")



def test_initialise():
    print("Testing initialCheck")

def test_initialise2(preWork):
    print("Testing initialCheck2")
    assert preWork == "fail"