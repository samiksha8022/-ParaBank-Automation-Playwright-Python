# https://demo.nopcommerce.com/register?returnUrl=%2F
from playwright.sync_api import Page, expect

def test_verify_pwlocators(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    title =page.get_by_text("Customer Login")
    expect(title).to_be_visible()
    print("title:",title.text_content())
    username = page.locator('input[name="username"]')
    username.click()
    username.fill("samta")
    password = page.locator('input[name="password"]')

    password.click()
    password.fill("sunita23")
    btn = page.locator('input[type="submit"]')
    btn.click()
    # page.wait_for_selector(btn)
    page.screenshot(path="homepage.png", full_page=True)




def test_forget(page:Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.get_by_text("Forgot login info?").click()
    expect(page.get_by_text("Customer Lookup")).to_be_visible()
    expect(page.get_by_text("Please fill out the following information in order to validate your account.")).to_be_visible()
    page.locator("input[name='firstName']").fill("sunita ")
    page.locator("input[name='lastName']").fill("chauhan ")
    page.locator("input[name='address.street']").fill("akshnagar ")
    page.locator("input[name='address.city']").fill("ghazibad ")
    page.locator("input[name='address.state']").fill("up ")
    page.locator("input[name='address.zipCode']").fill("1234 ")
    page.locator("input[name='ssn']").fill("my good job playwright ")
    page.get_by_role("button",name="Find My Login Info").click()
    error = page.locator("h1.title").text_content()
    print(error)
    error_msg = page.locator("p.error").text_content()

    # expect(error_msg).to_be_visible()
    print(error_msg)




    
  