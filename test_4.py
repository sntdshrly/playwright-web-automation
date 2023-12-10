from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://morning.maranatha.edu/")
    # tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("2072025")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("12345*")
    page.get_by_role("button", name="Log in").click()

    # ---------------------
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)