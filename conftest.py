import pytest
from pages.home_page import HomePage

@pytest.fixture
def page_url():
    return "https://fajarpertamastudios.com/"

@pytest.fixture
def home_page(page, page_url):
    hp = HomePage(page)
    hp.navigate(page_url)
    return hp