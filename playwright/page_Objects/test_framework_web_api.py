import json
import pytest
from playwright.sync_api import Playwright
from utils.apiBase import APIUtils

with open('../data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']




@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, user_credentials):
    # create order -> orderID
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill(user_credentials['userEmail'])
    page.locator("#userPassword").fill(user_credentials['userPassword'])
    page.locator("#login").click()


    #orders History Page ->

