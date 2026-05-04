import pytest
from pages.home_page import HomePage
from pages.projects_page import ProjectsPage

@pytest.fixture
def page_url():
    return "https://fajarpertamastudios.com/"

@pytest.fixture
def page_projects_url():
    return "https://fajarpertamastudios.com/projects.html"

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