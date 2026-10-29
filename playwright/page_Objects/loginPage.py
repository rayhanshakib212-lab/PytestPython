from playwright.sync_api import Playwright


class LoginPage:
    def __init__(self, playwright:Playwright):
        self.playwright = playwright