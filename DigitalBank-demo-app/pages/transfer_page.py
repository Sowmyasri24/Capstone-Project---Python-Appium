from appium.webdriver.common.mobileby import MobileBy
from utilities.driverfactory import DriverFactory

class TransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.platform = driver.capabilities['platformName'].lower()

    # ---------------------- Locators ----------------------
    @property
    def account_dropdown(self):
        if self.platform == 'android':
            return self.driver.find_element(MobileBy.ID, "xyz.digitalbank.demo:id/accountSpinner")
        else:
            return self.driver.find_element(MobileBy.IOS_CLASS_CHAIN,
                                            '**/XCUIElementTypePickerWheel[`value == "Individual Savings = 1000393.0"`]')

    @property
    def amount_field(self):
        if self.platform == 'android':
            return self.driver.find_element(MobileBy.ID, "xyz.digitalbank.demo:id/amountEditText")
        else:
            return self.driver.find_element(MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeTextField" AND value=="Enter Amount"')

    @property
    def description_field(self):
        if self.platform == 'android':
            return self.driver.find_element(MobileBy.ID, "xyz.digitalbank.demo:id/descriptionEditText")
        else:
            return self.driver.find_element(MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeTextField" AND value=="Enter Description"')

    @property
    def credit_radio(self):
        if self.platform == 'android':
            return self.driver.find_element(MobileBy.ID, "xyz.digitalbank.demo:id/creditRadioButton")
        else:
            return self.driver.find_element(MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeSwitch"')

    @property
    def submit_button(self):
        if self.platform == 'android':
            return self.driver.find_element(MobileBy.ID, "xyz.digitalbank.demo:id/submitButton")
        else:
            return self.driver.find_element(MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeButton" AND name=="Submit "')

    # ---------------------- Actions ----------------------
    def select_account(self, account_name=None):
        self.account_dropdown.click()
        if self.platform == 'android' and account_name:
            self.driver.find_element(MobileBy.XPATH, f"//android.widget.TextView[@text='{account_name}']").click()
        # iOS picker wheel auto selects, handled by setting value if needed

    def enter_amount(self, amount):
        self.amount_field.clear()
        self.amount_field.send_keys(amount)

    def enter_description(self, description):
        self.description_field.clear()
        self.description_field.send_keys(description)

    def select_credit(self):
        if not self.credit_radio.is_selected():
            self.credit_radio.click()

    def submit_transaction(self):
        self.submit_button.click()
