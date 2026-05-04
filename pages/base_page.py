from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        # Tutaj definiujemy selektory (lokatory)
        self.home_link = page.get_by_role("link", name="Home")
        self.projects_link = page.get_by_role("link", name="Projects")
        self.about_us_link = page.get_by_role("link", name="About Us")

        #Follow Us
        self.youtube_link = page.get_by_role("link", name = "YOUTUBE")
        self.x_link = page.get_by_role("link", name = "TWITTER")
        self.instagram_link = page.get_by_role("link", name = "INSTAGRAM")
        self.tiktok_link = page.get_by_role("link", name = "TIKTOK")     

        self.footer_text = page.get_by_text("© 2026 Fajar Pertama Studios")
        self.footer_element = page.locator("footer")

    def navigate(self, url: str):
        self.page.goto(url)

    def click_home(self):
        self.home_link.click()

    def click_projects(self):
        self.projects_link.click()

    def click_about(self):
        self.about_us_link.click()

    def click_youtube(self):
        self.youtube_link.click()

    def click_x(self):
        self.x_link.click()

    def click_instagram(self):
        self.instagram_link.click()

    def click_tiktok(self):
        self.tiktok_link.click()

    def get_footer_text_visibility(self):
        return self.footer_text.is_visible()