from playwright.sync_api import Page

class ListProjectsPage():
    page:Page

    # Tutaj definiujemy selektory (lokatory)
    @property
    def aethelgard_link(self):
        return self.page.get_by_role("link", name="The Chronicles of Aethelgard")

    @property
    def silence_link(self):
        return self.page.get_by_role("link", name="The Silence Between")

    @property
    def mow_link(self):
        return self.page.get_by_role("link", name="MOW OR MOW")

    @property
    def you_link(self):
        return self.page.get_by_role("link", name="You Didn't Buy Me")

    
    def click_aethelgard(self):
        self.aethelgard_link.click()

    def click_silence(self):
        self.silence_link.click()

    def click_mow(self):
        self.mow_link.click()

    def click_you(self):
        self.you_link.click()