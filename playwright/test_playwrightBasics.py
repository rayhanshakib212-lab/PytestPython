import time

from playwright.async_api import Playwright
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page


def test_playwrightBasic(playwright):
    print("test_playwrightBasic")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com")


#chromium headless mode, 1 single context
def test_playwrightShortCut(page:Page):
    page.goto("https://www.rahulshettyacademy.com")



def test_coreLocators(page:Page):
    page.goto("https://www.rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click() # filtering more on get by role
    time.sleep(5)
    expect(page.get_by_text("incorrect username/password.")).to_be_visible()



def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()  # filtering more on get by role
    time.sleep(5)
    expect(page.get_by_text("incorrect username/password.")).to_be_visible()


def test_newloginpagepractice(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill("smarthq@gmail.com")
    page.locator("#userPassword").fill("Imhere123!")
    page.locator("#login").click()

    pageTitle = page.locator("#h3").get_text()
    assert "Automation" == pageTitle

   # page.get_by_role("button", name="login").click() h3
    time.sleep(5)

