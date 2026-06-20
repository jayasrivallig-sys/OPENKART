from playwright.sync_api import sync_playwright, expect, Playwright


def test_oramgehrm(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page =context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name = "Login").click()
    page.get_by_role("link", name="My Info").click()
    page.locator(".oxd-userdropdown-tab").select_option("Single")
    page.locator("span:has-text('Monkey Luffy')").click()
    page.get_by_text("Logout", exact=True).click()





