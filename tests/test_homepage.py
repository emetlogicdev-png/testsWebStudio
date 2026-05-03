from pages.home_page import HomePage

def test_homepage_title(page, page_url):
    home_page = HomePage(page)
    home_page.navigate(page_url)
    
    # Sprawdzamy czy tytuł strony zawiera nazwę studia
    assert "Fajar Pertama" in page.title()

def test_navigation_to_projects(page, page_url):
    home_page = HomePage(page)
    home_page.navigate(page_url)
    
    # Klikamy w projekty
    home_page.click_projects()
    
    # Sprawdzamy czy URL zawiera projects.html
    # Używamy asercji, żeby potwierdzić, że automat tam dotarł
    assert "projects.html" in page.url