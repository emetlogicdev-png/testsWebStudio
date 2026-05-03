from pages.home_page import HomePage

def test_homepage_title(home_page, page_url):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)
    
    # Sprawdzamy czy tytuł strony zawiera nazwę studia
    assert "Fajar Pertama" in home_page.page.title()

def test_navigation_to_home(home_page, page_url):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)
    
    # Klikamy w projekty
    home_page.click_home()
    
    # Sprawdzamy czy URL zawiera projects.html
    # Używamy asercji, żeby potwierdzić, że automat tam dotarł
    assert "index.html" in home_page.page.url

def test_navigation_to_projects(home_page, page_url):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)
    
    # Klikamy w projekty
    home_page.click_projects()
    
    # Sprawdzamy czy URL zawiera projects.html
    # Używamy asercji, żeby potwierdzić, że automat tam dotarł
    assert "projects.html" in home_page.page.url

def test_navigation_to_about(home_page, page_url):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)
    
    # Klikamy w projekty
    home_page.click_about()
    
    # Sprawdzamy czy URL zawiera projects.html
    # Używamy asercji, żeby potwierdzić, że automat tam dotarł
    assert "about_us.html" in home_page.page.url

def test_navigation_to_youtube(home_page, page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)

    with page.context.expect_page() as new_page_info:
        home_page.click_youtube()

    # home_page.click_youtube()

    new_page = new_page_info.value
    # Używamy wait_until="networkidle", żeby przeczekać przekierowania RODO
    # new_page.wait_for_load_state("networkidle") # Czekamy aż YT się załaduje
    # 1. Czekamy na załadowanie (nawet jeśli to strona zgody)
    new_page.wait_for_load_state("domcontentloaded")

    # 2. Jeśli pojawi się przycisk zgody, klikamy go
    # Szukamy przycisku, który ma tekst "Accept all" lub "Zaakceptuj wszystko"
    # Używamy fragmentu tekstu, bo język zależy od lokalizacji serwera (np. na GitHub będzie to angielski)
    consent_button = new_page.get_by_role("button", name="Accept all")

    if consent_button.is_visible(timeout=5000): # Czekaj max 5 sek
        consent_button.click()

    assert "youtube.com" in new_page.url

def test_navigation_to_x(home_page, page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)

    with page.context.expect_page() as new_page_info:
        home_page.click_x()

    # home_page.click_x()

    new_page = new_page_info.value
    new_page.wait_for_load_state()

    assert "https://x.com/FajarPertamaStd" in new_page.url

def test_navigation_to_instagram(home_page, page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)

    with page.context.expect_page() as new_page_info:
        home_page.click_instagram()

    # home_page.click_instagram()

    new_page = new_page_info.value
    new_page.wait_for_load_state()

    assert "https://www.instagram.com/fajarpertamastudios/" in new_page.url

def test_navigation_to_tiktok(home_page, page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)

    with page.context.expect_page() as new_page_info:
        home_page.click_tiktok()

    # home_page.click_tiktok()

    new_page = new_page_info.value
    new_page.wait_for_load_state()


    assert "https://www.tiktok.com/@fajarpertamastudios" in new_page.url