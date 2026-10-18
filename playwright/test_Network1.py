from playwright.sync_api import Page


fakePayloadOrderResponse = {"data": [],"message": "No Orders"} # the call that is made for orders is gutted to represent no orders



def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )




def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/user/get-cart-count/*",intercept_response)
    page.locator("#userEmail").fill("smarthq@gmail.com")
    page.locator("#userPassword").fill("Imhere123!")
    page.locator("#login").click()

    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)


