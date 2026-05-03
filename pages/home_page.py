from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        # Tutaj definiujemy selektory (lokatory)
        self.home_link = page.get_by_role("link", name="Home")
        self.projects_link = page.get_by_role("link", name="Projects")
        self.about_us_link = page.get_by_role("link", name="About Us")
        

    def navigate(self, url: str):
        self.page.goto(url)

    def click_home(self):
        self.home_link.click()

    def click_projects(self):
        self.projects_link.click()

    def click_about(self):
        self.about_us_link.click()