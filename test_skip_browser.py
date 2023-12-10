import pytest

@pytest.mark.skip_browser("chromium")
def test_visit_youtube(page, browser_type):
    browser_type.launch(headless=False, slow_mo=2000)
    page.goto("https://youtube.com")