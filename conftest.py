import pytest
from pages.home_page import HomePage
from pages.projects_page import ProjectsPage
from pages.about_page import AboutPage

@pytest.fixture
def page_url():
    return "https://fajarpertamastudios.com/"

@pytest.fixture
def page_projects_url():
    return "https://fajarpertamastudios.com/projects.html"

@pytest.fixture
def page_about_url():
    return "https://fajarpertamastudios.com/about_us.html"

@pytest.fixture
def home_page(page, page_url):
    hp = HomePage(page)
    hp.navigate(page_url)
    return hp

@pytest.fixture
def projects_page(page, page_projects_url):
    pp = ProjectsPage(page)
    pp.navigate(page_projects_url)
    return pp

@pytest.fixture
def about_page(page, page_about_url):
    ap = AboutPage(page)
    ap.navigate(page_about_url)
    return ap