
import os
import pytest
from playwright.sync_api import sync_playwright, expect


BASE_URL = "https://www.saucedemo.com/"

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def browser_page():

    headless = os.getenv("CI", "false").lower() == "true"

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=headless,
            slow_mo=0 if headless else 1000
        )

        page = browser.new_page(
            viewport={"width": 1366, "height": 768}
        )

        yield page

        browser.close()


# TC001 - Valid Login

def test_valid_login(browser_page):

    page = browser_page

    print("\nTC001: Starting valid login test")

    page.goto(BASE_URL)

    page.locator('[data-test="username"]').fill(USERNAME)

    page.locator('[data-test="password"]').fill(PASSWORD)

    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(page.locator(".title")).to_have_text("Products")

    print("TC001: Login successful")


# TC002 - Invalid Password

def test_invalid_password(browser_page):

    page = browser_page

    print("\nTC002: Starting invalid password test")

    page.goto(BASE_URL)

    page.locator('[data-test="username"]').fill(USERNAME)

    page.locator('[data-test="password"]').fill(
        "wrong_password"
    )

    page.locator('[data-test="login-button"]').click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_contain_text(
        "Username and password do not match"
    )

    print("TC002: Invalid password correctly rejected")
