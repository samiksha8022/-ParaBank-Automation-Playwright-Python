# https://demo.nopcommerce.com/register?returnUrl=%2F
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize(
    "username,password",
    [
        ("sunita", "123"),
        ("user1", "user123")
    ]
)
def test_verify_pwlocators(page: Page , username,password):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    title =page.get_by_text("Customer Login")
    expect(title).to_be_visible()
    print("title:",title.text_content())
    username1 = page.locator('input[name="username"]')
    username1.fill(username)
    password1 = page.locator('input[name="password"]')
    password1.fill(password)
    
    btn = page.locator('input[type="submit"]')
    btn.click()
    # page.wait_for_selector(btn)
    page.screenshot(path="homepage.png", full_page=True)



@pytest.mark.parametrize(
    "first_name,last_name,street,city,state,zip_code,ssn",
    [
        ("sunita", "chauhan", "akshnagar", "ghaziabad", "up", "1234", "1111"),
        ("user1", "kumar", "sector15", "noida", "up", "201301", "2222")
    ]
)
def test_forget(
    page: Page,
    first_name,
    last_name,
    street,
    city,
    state,
    zip_code,
    ssn
):
#  def test_forget(page:Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.get_by_text("Forgot login info?").click()
    expect(page.get_by_text("Customer Lookup")).to_be_visible()
    expect(page.get_by_text("Please fill out the following information in order to validate your account.")).to_be_visible()
    page.locator("input[name='firstName']").fill(first_name)
    page.locator("input[name='lastName']").fill(last_name)
    page.locator("input[name='address.street']").fill(street)
    page.locator("input[name='address.city']").fill(city)
    page.locator("input[name='address.state']").fill(state)
    page.locator("input[name='address.zipCode']").fill(zip_code)
    page.locator("input[name='ssn']").fill(ssn)
    page.get_by_role("button",name="Find My Login Info").click()
    error = page.locator("h1.title").text_content()
    print(error)
    error_msg = page.locator("p.error").text_content()

    # expect(error_msg).to_be_visible()
    print(error_msg)




    
  