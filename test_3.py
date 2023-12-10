from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("http://youtube.com/")
    page.screenshot(path="example.png")
    browser.close()