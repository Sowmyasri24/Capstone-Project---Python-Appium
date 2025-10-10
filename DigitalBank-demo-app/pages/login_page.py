"""Page Object for Login Page."""

from appium.webdriver.common.appiumby import AppiumBy
from utilities.logger import Logger
from config.config import Config


class LoginPage:
    """Page Object representing the Login screen for Android and iOS."""

    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(__name__)

        if Config.is_android():
            # Android locators
            self.locators = {
                "email": (AppiumBy.ACCESSIBILITY_ID, "Enter Email Address"),
                "password": (AppiumBy.ACCESSIBILITY_ID, "Enter Password"),
                "login_button": (AppiumBy.ACCESSIBILITY_ID, "Login Button"),
                "register_link": (AppiumBy.ACCESSIBILITY_ID, "Click here to Register new account"),
                "settings_icon": (AppiumBy.ACCESSIBILITY_ID, "Settings Cog Icon"),
                "error_message": (AppiumBy.ID, "xyz.digitalbank.demo:id/errorTextView"),
            }
        else:
            # iOS locators
            self.locators = {
                "username": (AppiumBy.ACCESSIBILITY_ID, "Enter UserName"),
                "continue_button": (AppiumBy.ACCESSIBILITY_ID, "continue"),
                "password": (AppiumBy.ACCESSIBILITY_ID, "Enter Password"),
                "login_button": (AppiumBy.ACCESSIBILITY_ID, "LogIn"),
                "settings_icon": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "      "`]'),
                "register_link": (AppiumBy.ACCESSIBILITY_ID, "Sign Up Here"),
                "error_message": (AppiumBy.ACCESSIBILITY_ID, "Error Message"),
            }

    # ---------------- ACTION METHODS ---------------- #

    def enter_username_or_email(self, value):
        """Enter username (iOS) or email (Android)."""
        locator = self.locators["username"] if not Config.is_android() else self.locators["email"]
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(value)
        self.logger.info(f"Entered username/email: {value}")

    def enter_password(self, value):
        """Enter password."""
        field = self.driver.find_element(*self.locators["password"])
        field.clear()
        field.send_keys(value)
        self.logger.info("Entered password")

    def click_login(self):
        """Click login button."""
        self.driver.find_element(*self.locators["login_button"]).click()
        self.logger.info("Clicked login button")

    def click_register_link(self):
        """Click link to navigate to registration."""
        self.driver.find_element(*self.locators["register_link"]).click()
        self.logger.info("Clicked Register link")

    def click_settings_icon(self):
        """Click the settings icon."""
        self.driver.find_element(*self.locators["settings_icon"]).click()
        self.logger.info("Clicked Settings icon")

    # ---------------- VALIDATION METHODS ---------------- #

    def is_field_present(self, field_name):
        """Check if the given field is visible."""
        try:
            return self.driver.find_element(*self.locators[field_name]).is_displayed()
        except Exception:
            return False

    def get_error_message(self):
        """Fetch visible error message text (if available)."""
        try:
            el = self.driver.find_element(*self.locators["error_message"])
            return el.text.strip()
        except Exception:
            return None
