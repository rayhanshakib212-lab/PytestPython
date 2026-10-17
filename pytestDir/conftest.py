#Fixtures
import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("I set up browser instance")