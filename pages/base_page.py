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
    
    def verify_all_links(self):
        """
        Scans all links on the current page and verifies if they return a 200 OK status.
        """
        links = self.page.locator("a").all()

        excluded_domains = ["instagram.com", "facebook.com", "x.com", "tiktok.com"]
        
        for link in links:
            href = link.get_attribute("href")
            if href:
                # Resolve relative URLs to absolute ones using the current page's base URL
                full_url = self.page.evaluate("url => new URL(url, window.location.href).href", href)
                
                # Check only web links (ignore mailto:, tel:, etc.)
                if full_url.startswith("http"):
                    if any(domain in full_url for domain in excluded_domains):
                        continue

                        response = self.page.request.get(full_url)
                        assert response.ok, f"Link {full_url} is broken! Status: {response.status}"