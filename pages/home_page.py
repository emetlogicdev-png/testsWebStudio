from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.listprojects_page import ListProjectsPage

class HomePage(BasePage, ListProjectsPage):
    def __init__(self, page: Page):
        super().__init__(page)

    