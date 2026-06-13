# https://parabank.parasoft.com/parabank/register.htm
from playwright.sync_api import Page,expect
import random
import re

def test_register(page:Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.get_by_text("Register").click()
    expect(page.get_by_text("Signing up is easy!")).to_be_visible()
    expect(page.get_by_text("If you have an account with us you can sign-up for free instant online access.")).to_be_visible()
    username = f"user{random.randint(1000,9999)}"
    password = f"pass{random.randint(1000,9999)}"
    page.locator("input[name='customer.firstName']").fill("se")
    page.locator("input[name='customer.lastName']").fill("chauhan")
    page.locator("input[name='customer.address.street']").fill("akshnagar")
    page.locator("input[name='customer.address.city']").fill("ghazibad")
    page.locator("input[name='customer.address.state']").fill("up")
    page.locator("input[name ='customer.address.zipCode']").fill("1234")
    page.locator("input[name ='customer.phoneNumber']").fill("893657801")
    page.locator("input[name ='customer.ssn']").fill("hii")
    page.locator("input[name ='customer.username']").fill(username)
    page.locator("input[name ='customer.password']").fill(password)
    page.locator("input[name ='repeatedPassword']").fill(password)
    page.get_by_role("button", name="Register").click()
    succeful_msg =page.locator("h1.title").text_content()
    print(succeful_msg)


    success_msg = page.get_by_text("Your account was created successfully. You are now logged in.")

    expect(success_msg).to_be_visible()

    page.screenshot(path="screen.png")
    # page.get_by_role("link", name="Open New Account").click()

    page.wait_for_timeout(5000)
# account servces
    expect(page.get_by_text("Account Services")).to_be_visible()
    menu_items = page.locator("ul li a").all_text_contents()
    for item in menu_items:
     print(item)
    page.get_by_role("link", name="Open New Account").click()
#     # print(page.get_by_role("link", name="Open New Account").count())


    page.locator("#type").select_option(label="CHECKING")

    

   
    page.locator("#fromAccountId").select_option(index=0)


    page.get_by_role("button", name="Open New Account").click()
    # title =page.locator("h1.title").text_content()
    # print(title)
    # expect(title).to_be_visible()
   
    page.get_by_role("link", name='newAccountId').click()
    page.wait_for_timeout(50000)





def test_account(page:Page):
   page.goto("https://parabank.parasoft.com/parabank/openaccount.htm")
   username = f"user{random.randint(1000,9999)}"
   password = f"pass{random.randint(1000,9999)}"
   page.locator('input[name="username"]').fill(username)
   page.locator('input[name="password"]').fill(password)
   page.locator('input[type="submit"]').click()
  
   
#    page.wait_for_timeout(50000)
def test_bill_payment(page:Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    page.locator("input[name='username']").fill("john")
    page.locator("input[name='password']").fill("demo")

    page.get_by_role("button", name="Log In").click()

    page.get_by_role("link", name="Bill Pay").click()

    page.locator("input[name='payee.name']").fill("John Doe")
    page.locator("input[name ='payee.address.street']").fill("nehrunagar")
    page.locator("input[name ='payee.address.city']").fill("bihar")
    page.locator("input[name ='payee.address.state']").fill("up")
    page.locator("input[name ='payee.address.zipCode']").fill("101000")
    page.locator("input[name ='payee.phoneNumber']").fill("2345009960")
    page.locator("input[name ='payee.accountNumber']").fill("12sunita")
    page.locator("input[name ='verifyAccount']").fill("12sunita")
    page.locator("input[name ='amount']").fill("500000")
    page.locator("input[name ='fromAccountId']")
    page.get_by_role("button", name="Send Payment").click()
    expect(page.get_by_role("heading", name="Bill Payment Complete")).to_be_visible()   
  
    page.wait_for_timeout(50000)

   





