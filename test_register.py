# https://parabank.parasoft.com/parabank/register.htm
from playwright.sync_api import Page,expect
import random
import re
import pytest
import csv
data = []
with open("DDT_CSV_REG/data.csv",newline="") as file:
   reader =csv.DictReader(file)
   for row in reader:
         data.append(
            (
                row["firstName"],
                row["lastName"],
                row["address.street"],
                row["address.city"],
                row["address.state"],
                row["address.zipCode"],
                row["phoneNumber"],
                row["ssn"],
                row["username"],
                row["password"],
                row["repeatedPassword"],
            )
        )
@pytest.mark.parametrize(
    "firstName,lastName,street,city,state,zipCode,phoneNumber,ssn,username,password,repeatedPassword",
    data
)

def test_register(
    page:Page,
    firstName,
    lastName,
    street,
    city,
    state,
    zipCode,
    phoneNumber,
    ssn,
    username,
    password,
    repeatedPassword,

):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.get_by_text("Register").click()
    # expect(page.get_by_text("Signing up is easy!")).to_be_visible()
    # expect(page.get_by_text("If you have an account with us you can sign-up for free instant online access.")).to_be_visible()
    # username = f"user{random.randint(1000,9999)}"
    # password = f"pass{random.randint(1000,9999)}"
    page.locator("input[name='customer.firstName']").fill(firstName)
    page.locator("input[name='customer.lastName']").fill(lastName)
    page.locator("input[name='customer.address.street']").fill(street)
    page.locator("input[name='customer.address.city']").fill(city)
    page.locator("input[name='customer.address.state']").fill(state)
    page.locator("input[name ='customer.address.zipCode']").fill(zipCode)
    page.locator("input[name ='customer.phoneNumber']").fill(phoneNumber)
    page.locator("input[name ='customer.ssn']").fill(ssn)
    page.locator("input[name ='customer.username']").fill(username)
    page.locator("input[name ='customer.password']").fill(password)
    page.locator("input[name ='repeatedPassword']").fill(repeatedPassword)
    page.get_by_role("button", name="Register").click()
    page.screenshot(path="result.png")
    print(page.locator("body").text_content())

    expect(page.locator("#rightPanel h1")).to_be_visible()
    expect(page.locator("#rightPanel p")).to_have_text("Your account was created successfully. You are now logged in.")
    expect(page.get_by_text("Address is required.")).to_be_visible()
    expect(page.get_by_text("Zip Code is required.")).to_be_visible()

    # success_msg1 = page.get_by_text("Your account was created successfully. You are now logged in.")

    # expect(success_msg1).to_be_visible()

#     page.screenshot(path="screen.png")
    # page.get_by_role("link", name="Open New Account").click()








def test_account_serv(page:Page):
        # login page
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # existing valid user se login
    page.locator('input[name="username"]').fill("john")
    page.locator('input[name="password"]').fill("demo")
    page.locator('input[type="submit"]').click()


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
    title =page.locator("h1.title").nth(1).text_content()
    print(title)
    
    newAccountId = page.locator("#newAccountId").text_content()
    print(newAccountId)
    
    
    # page.get_by_role("link", name="Open New Account").click()




def test_transfer(page: Page):
    # login page
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # existing valid user se login
    page.locator('input[name="username"]').fill("john")
    page.locator('input[name="password"]').fill("demo")
    page.locator('input[type="submit"]').click()

    # transfer funds page
    page.get_by_role("link", name="Transfer Funds").click()
    page.locator("#amount").fill("50000")
    page.get_by_role("button", name="Transfer").click()
    # to check sucessfule msg show to display for print 
    


    
                 
    





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
    # expect(page.get_by_role("heading", name="Bill Payment Complete")).to_be_visible()  

  
   

   





