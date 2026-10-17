from playwright.sync_api import Playwright

from utils.apiBase import APIUtils

def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill("smarthq@gmail.com")
    page.locator("#userPassword").fill("Imhere123!")
    page.locator("#login").click()

    #create order -> orderID
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)