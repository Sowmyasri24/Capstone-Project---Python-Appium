import pytest
from pages.transferpage import TransferPage
from utilities.driverfactory import DriverFactory

@pytest.fixture(scope="function")
def transfer_page(request):
    driver = DriverFactory.get_driver()
    page = TransferPage(driver)
    yield page
    driver.quit()

# ---------------------- Field Presence Tests ----------------------
def test_fields_presence(transfer_page):
    assert transfer_page.account_dropdown.is_displayed(), "Account dropdown not present"
    assert transfer_page.amount_field.is_displayed(), "Amount field not present"
    assert transfer_page.description_field.is_displayed(), "Description field not present"
    assert transfer_page.credit_radio.is_displayed(), "Credit radio button not present"
    assert transfer_page.submit_button.is_displayed(), "Submit button not present"

# ---------------------- Valid Tests ----------------------
@pytest.mark.parametrize("account, amount, description", [
    ("Individual Savings - 1000393.0", "1000", "Salary Deposit"),
    ("Individual Savings - 1000393.0", "500", "Gift Transfer")
])
def test_valid_transaction(transfer_page, account, amount, description):
    transfer_page.select_account(account)
    transfer_page.enter_amount(amount)
    transfer_page.enter_description(description)
    transfer_page.select_credit()
    transfer_page.submit_transaction()
    # add assertion here based on toast/message/confirmation element after submit

# ---------------------- Negative Tests ----------------------
@pytest.mark.parametrize("amount, description", [
    ("", "Salary Deposit"),       # Empty amount
    ("abc", "Salary Deposit"),    # Invalid amount
    ("100", ""),                  # Empty description
])
def test_invalid_transaction(transfer_page, amount, description):
    transfer_page.enter_amount(amount)
    transfer_page.enter_description(description)
    transfer_page.select_credit()
    transfer_page.submit_transaction()
    # add assertion here for validation message or error
