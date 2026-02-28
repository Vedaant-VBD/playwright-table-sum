from playwright.sync_api import sync_playwright

urls = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=25",
    "https://sanand0.github.io/tdsdata/js_table/?seed=26",
    "https://sanand0.github.io/tdsdata/js_table/?seed=27",
    "https://sanand0.github.io/tdsdata/js_table/?seed=28",
    "https://sanand0.github.io/tdsdata/js_table/?seed=29",
    "https://sanand0.github.io/tdsdata/js_table/?seed=30",
    "https://sanand0.github.io/tdsdata/js_table/?seed=31",
    "https://sanand0.github.io/tdsdata/js_table/?seed=32",
    "https://sanand0.github.io/tdsdata/js_table/?seed=33",
    "https://sanand0.github.io/tdsdata/js_table/?seed=34"
]

total_sum = 0

with sync_playwright() as p:

    browser = p.chromium.launch()
    page = browser.new_page()

    for url in urls:

        page.goto(url)

        page.wait_for_selector("table")

        numbers = page.locator("td").all_text_contents()

        for n in numbers:
            try:
                total_sum += float(n)
            except:
                pass

    browser.close()

print("FINAL TOTAL =", total_sum)
