# Chrome browser will open.
# Google website will load.
# Browser will remain open.
# Press Enter in the terminal to close the browser.


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open website
    page.goto("https://www.amazon.in/")

    # Keep browser open until manually closed
    input("Press Enter to close the browser...")

    browser.close()

