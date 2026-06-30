# Find Transactions
from playwright.sync_api import Page,expect
import random
import re


def test_transaction(page:Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
       # existing valid user se login
    page.locator('input[name="username"]').fill("john")
    page.locator('input[name="password"]').fill("demo")
    page.locator('input[type="submit"]').click()
    # transaction option
    page.get_by_role("link", name ="Find Transactions").click()


    page.locator("#accountId").select_option(index=1)
    page.locator("#transactionId").fill("14787")

    page.get_by_role("button", name="Find Transactions").nth(0).click() 
    title = page.get_by_role("heading",name="Transaction Results")
    expect(title).to_be_visible()
    page.get_by_role("link", name ="Find Transactions").click()

    
    page.locator("input#transactionDate").fill("06-25-2026")
    page.locator("#findByDate").click()
    expect(page.get_by_role("heading", name="Transaction Results")).to_be_visible()




# this testcase update the infomation ,and to check the vaild or invalid data

def test_update_info(page:Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # existing valid user se login
    page.locator('input[name="username"]').fill("john")
    page.locator('input[name="password"]').fill("demo")
    page.locator('input[type="submit"]').click()
   #  update contact info
    page.get_by_role("link",name="Update Contact Info").click()
    page.locator('[id="customer.firstName"]').fill("samiksha")

    page.get_by_role("button", name="Update Profile").click()
    expect(page.locator("#updateProfileResult")).to_be_visible()



def test_request_loan(page:Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # existing valid user se login
    page.locator('input[name="username"]').fill("john")
    page.locator('input[name="password"]').fill("demo")
    page.locator('input[type="submit"]').click()


    page.get_by_role("link",name="Request Loan").click()
    page.locator("#amount").fill("50000")
    page.locator("#downPayment").fill("20000")
    page.get_by_role("button",name="Apply Now").click()

