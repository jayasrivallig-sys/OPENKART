
from playwright.sync_api import sync_playwright, Playwright


def test_mobile(playwright:Playwright):
    iphone = playwright.devices["iPhone 13"]
    # for device in playwright.devices:
    #     print(device)
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(**iphone)

    page = context.new_page()
    page.goto("https://www.google.com")

    browser.close()


# def test_mobile2(playwright:Playwright):
#     android = playwright.devices["Pixel 7"]
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(**android)
#     page = context.new_page()
#     print(page.viewport_size)
#     page.goto("https://www.amazon.com")
#     page.screenshot(path = "amazon.png")
#     browser.close()