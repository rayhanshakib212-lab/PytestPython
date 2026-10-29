#Fixtures
import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("I set up browser instance")



@pytest.fixture
def browserInstance(playwright, request):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield browser
    browser.quit()
    browser.close()
