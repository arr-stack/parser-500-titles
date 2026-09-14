from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.film.ru/compilation/500-luchshih-filmov")

    scroll_count = 0
    max_count = 100

    height = -1
    while scroll_count < max_count:
        page.mouse.wheel(0, 15000)
        page.wait_for_timeout(4000)
        new_height = page.evaluate('document.body.scrollHeight')
        if new_height == height:
            break
        height = new_height
        scroll_count += 1

    list1 = []
    u = page.locator("//div[@class='redesign_afisha_movie_main_title']//a")
    for item in u.all_text_contents():
        film = {'contents': {"title": item.strip()}}
        list1.append(film)

    with open('movie_titles500.json', 'w', encoding='utf8') as f:
        json.dump(list1, f, indent=2, default=lambda x: list(x), ensure_ascii=False)



    browser.close()