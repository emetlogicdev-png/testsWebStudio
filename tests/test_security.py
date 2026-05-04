from playwright.sync_api import Page

def test_http_to_https_redirection(page):

    page.goto("http://fajarpertamastudios.com/")

    page.wait_for_load_state("networkidle")

    assert page.url.startswith("https://")