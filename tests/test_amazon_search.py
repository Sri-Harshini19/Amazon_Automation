
import re
from playwright.sync_api import Page, expect


def test_amazon_search(page: Page):
    # Open Amazon India
    page.goto("https://www.amazon.in/")

    # Perform the actions recorded using Codegen
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill(
        "wireless headphones under 2000"
    )
    page.get_by_role("searchbox", name="Search Amazon.in").press("Enter")

    # Verify search results
    products = page.locator('[data-component-type="s-search-result"]')
    expect(products.first).to_be_visible(timeout=20000)

    # Open the first product in a new tab
    with page.expect_popup() as page1_info:
        page.locator(".a-link-normal.s-no-outline").first.click()

    page1 = page1_info.value
    expect(page1).to_have_url(re.compile(r"amazon\.in"), timeout=15000)

    print("Amazon search and product opening passed!")
