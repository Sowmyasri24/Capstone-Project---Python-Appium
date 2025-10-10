from appium.webdriver.common.appiumby import AppiumBy
from utilities.logger import Logger

class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.log = Logger().get_logger()

        # Common locators (Android & iOS separated)
        self.locators = {
            "android": {
                "welcome_text": (AppiumBy.ID, "xyz.digitalbank.demo:id/welcomeText"),
                "my_dashboard": (AppiumBy.ACCESSIBILITY_ID, "My Dashboard"),
                "deposits": (AppiumBy.ACCESSIBILITY_ID, "Deposit's"),
                "atms": (AppiumBy.ACCESSIBILITY_ID, "ATM's NearMe"),
                "my_accounts": (AppiumBy.ACCESSIBILITY_ID, "My Accounts"),
                "toolbar_image": (AppiumBy.ID, "xyz.digitalbank.demo:id/toolbar_image"),
                "account_selection": (AppiumBy.ID, "xyz.digitalbank.demo:id/selectAccountText"),
                "balance_label": (AppiumBy.ID, "xyz.digitalbank.demo:id/balanceLabel")
            },
            "ios": {
                "welcome_label": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Welcome"`]'),
                "welcome_button": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Welcome"`]'),
                "chart_icon": (AppiumBy.ACCESSIBILITY_ID, "chart.pie.fill"),
                "transfer_button": (AppiumBy.ACCESSIBILITY_ID, "Transfer"),
                "atm_button": (AppiumBy.ACCESSIBILITY_ID, "ATM"),
                "tray_icon": (AppiumBy.ACCESSIBILITY_ID, "tray.fill"),
                "picker_wheel": (AppiumBy.CLASS_NAME, "XCUIElementTypePickerWheel")
            }
        }

    def click_element(self, platform, element_name):
        try:
            locator = self.locators[platform][element_name]
            self.driver.find_element(*locator).click()
            self.log.info(f"Clicked on {element_name}")
        except Exception as e:
            self.log.error(f"Unable to click {element_name}: {str(e)}")
            raise

    def is_element_displayed(self, platform, element_name):
        try:
            locator = self.locators[platform][element_name]
            element = self.driver.find_element(*locator)
            visible = element.is_displayed()
            self.log.info(f"{element_name} visible: {visible}")
            return visible
        except Exception as e:
            self.log.error(f"Element not found: {element_name}, Error: {str(e)}")
            return False
