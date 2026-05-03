from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        # Tutaj definiujemy selektory (lokatory)
        self.projects_link = page.get_by_role("link", name="Projects")
        self.about_us_link = page.get_by_role("link", name="About Us")
        self.home_link = page.get_by_role("link", name="Home")

    def navigate(self, url: str):
        self.page.goto(url)

    def click_projects(self):
        self.projects_link.click()