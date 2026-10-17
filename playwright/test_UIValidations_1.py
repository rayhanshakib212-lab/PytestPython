from playwright.sync_api import Page, expect, Playwright
from playwright.async_api import Playwright


def test_UIValidationDynamicScript(page:Page):
    #iPhone x, Nokia Edge

    page.goto("https://www.rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()  # filtering more on get by role
    iPhoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iPhoneProduct.get_by_role("button").click()
    NokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    NokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)



def test_childwindow(page:Page):
    page.goto("https://www.rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText[href='https://rahulshettyacademy.com/documents-request']").click()
        childPage = newPage_info.value
        text=  childPage.locator("a[href='mailto:mentor@rahulshettyacademy.com']").text_content()
        print(text)
        words= text.split("@")
        email= words[1].split(" ")[0] # [0] is accessing the 0 index of the new split
        print(email)
        assert email == "rahulshettyacademy.com"

