from pages.projects_page import ProjectsPage

def test_homepage_title(projects_page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)
    
    # Sprawdzamy czy tytuł strony zawiera nazwę studia
    assert "Fajar Pertama" in projects_page.page.title()

def test_navigation_to_home(projects_page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)
    
    # Klikamy w projekty
    projects_page.click_home()
    
    # Sprawdzamy czy URL zawiera projects.html
    # Używamy asercji, żeby potwierdzić, że automat tam dotarł
    assert "index.html" in projects_page.page.url

def test_navigation_to_projects(projects_page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)
    
    # Klikamy w projekty
    projects_page.click_projects()
    
    # Sprawdzamy czy URL zawiera projects.html
    # Używamy asercji, żeby potwierdzić, że automat tam dotarł
    assert "projects.html" in projects_page.page.url

def test_navigation_to_about(projects_page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)
    
    # Klikamy w projekty
    projects_page.click_about()
    
    # Sprawdzamy czy URL zawiera projects.html
    # Używamy asercji, żeby potwierdzić, że automat tam dotarł
    assert "about_us.html" in projects_page.page.url

def test_navigation_to_youtube(projects_page, page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)

    with page.context.expect_page() as new_page_info:
        projects_page.click_youtube()

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

def test_navigation_to_x(projects_page, page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)

    with page.context.expect_page() as new_page_info:
        projects_page.click_x()

    # home_page.click_x()

    new_page = new_page_info.value
    new_page.wait_for_load_state()

    assert "x.com" in new_page.url

def test_navigation_to_instagram(projects_page, page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)

    with page.context.expect_page() as new_page_info:
        projects_page.click_instagram()

    # home_page.click_instagram()

    new_page = new_page_info.value
    new_page.wait_for_load_state()

    assert "instagram.com" in new_page.url

def test_navigation_to_tiktok(projects_page, page):
    # home_page = HomePage(page)
    # home_page.navigate(page_url)

    with page.context.expect_page() as new_page_info:
        projects_page.click_tiktok()

    # home_page.click_tiktok()

    new_page = new_page_info.value
    new_page.wait_for_load_state()


    assert "tiktok.com" in new_page.url

def test_footer_content(projects_page):
    # Sprawdzamy czy napis w stopce jest widoczny na stronie
    assert projects_page.get_footer_text_visibility() is True

def test_footer_actual_text(projects_page):
    # Pobieramy tekst, który RZECZYWIŚCIE jest na stronie w stopce
    actual_text = projects_page.footer_element.inner_text()
        
    # Sprawdzamy czy zawiera to, co chcemy
    assert "Fajar Pertama Studios" in actual_text
    assert "2026" in actual_text
    assert "©" in actual_text

def test_no_broken_links_on_projectspage(projects_page):

        """Verify that all links on the projectspage are functional."""
        projects_page.verify_all_links()