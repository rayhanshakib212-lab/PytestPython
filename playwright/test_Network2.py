import time

from playwright.sync_api import Page


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