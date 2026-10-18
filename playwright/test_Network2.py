import time


import page
from playwright.async_api import Playwright
from playwright.sync_api import Page, expect
from utils.apiBase import APIUtils


def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6ad409b493b084c41f56945f")
# above is another clients order
#network718@gmail.com
#imhere123!




def test_Network_2(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id*", interceptRequest)
    page.locator("#userEmail").fill("smarthq@gmail.com")
    page.locator("#userPassword").fill("Imhere123!")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(10)
    message = page.locator(".blink_me").text_content()
    print(message)




def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""") #f is for variable
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()