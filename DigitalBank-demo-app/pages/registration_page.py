"""Page Object for Registration Page."""

from appium.webdriver.common.appiumby import AppiumBy
from utilities.logger import Logger
from config.config import Config


class RegistrationPage:
    """Page object representing the registration page for Android and iOS."""

    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(__name__)

        # Common locators
        if Config.is_android():
            self.locators = {
                "title": (AppiumBy.ACCESSIBILITY_ID, "Create a new account"),
                "title_spinner": (AppiumBy.ACCESSIBILITY_ID, "Select Title"),
                "first_name": (AppiumBy.ACCESSIBILITY_ID, "Enter First Name"),
                "last_name": (AppiumBy.ACCESSIBILITY_ID, "Enter Last Name"),
                "gender_male": (AppiumBy.ACCESSIBILITY_ID, "Select Male Gender"),
                "gender_female": (AppiumBy.ACCESSIBILITY_ID, "Select Female Gender"),
                "dob": (AppiumBy.ACCESSIBILITY_ID, "Date of Birth"),
                "ssn": (AppiumBy.ACCESSIBILITY_ID, "Social Security Number"),
                "email": (AppiumBy.ACCESSIBILITY_ID, "Email Address"),
                "password": (AppiumBy.ACCESSIBILITY_ID, "Enter Password"),
                "address": (AppiumBy.ACCESSIBILITY_ID, "Enter Address"),
                "region": (AppiumBy.ACCESSIBILITY_ID, "Enter Region"),
                "locality": (AppiumBy.ID, "xyz.digitalbank.demo:id/localityInput"),
                "register_button": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Register")'),
                "error_message": (AppiumBy.ID, "xyz.digitalbank.demo:id/errorTextView"),
            }
        else:  # iOS locators
            self.locators = {
                "title": (AppiumBy.ACCESSIBILITY_ID, "Create a new account"),
                "mr": (AppiumBy.ACCESSIBILITY_ID, "Mr."),
                "mrs": (AppiumBy.ACCESSIBILITY_ID, "Mrs."),
                "ms": (AppiumBy.ACCESSIBILITY_ID, "Ms."),
                "first_name": (AppiumBy.ACCESSIBILITY_ID, "First Name"),
                "last_name": (AppiumBy.ACCESSIBILITY_ID, "Last Name"),
                "male": (AppiumBy.ACCESSIBILITY_ID, "Male"),
                "female": (AppiumBy.ACCESSIBILITY_ID, "Female"),
                "dob": (AppiumBy.ACCESSIBILITY_ID, "Date Picker"),
                "password": (AppiumBy.ACCESSIBILITY_ID, "Password"),
                "email": (AppiumBy.ACCESSIBILITY_ID, "Email Address"),
                "ssn": (AppiumBy.ACCESSIBILITY_ID, "Social Security Number"),
                "address": (AppiumBy.ACCESSIBILITY_ID, "Address"),
                "locality": (AppiumBy.ACCESSIBILITY_ID, "Locality"),
                "region": (AppiumBy.ACCESSIBILITY_ID, "Region"),
                "zipcode": (AppiumBy.ACCESSIBILITY_ID, "Zip Code"),
                "phone": (AppiumBy.ACCESSIBILITY_ID, "Phone Number"),
                "agree_terms": (AppiumBy.ACCESSIBILITY_ID, "Agree to Term and Conditions"),
                "register_button": (AppiumBy.ACCESSIBILITY_ID, "Register"),
                "error_message": (AppiumBy.ACCESSIBILITY_ID, "Error Message"),
            }

    # ---------------- ACTION METHODS ---------------- #

    def enter_first_name(self, first_name):
        field = self.driver.find_element(*self.locators["first_name"])
        field.clear()
        field.send_keys(first_name)
        self.logger.info(f"Entered First Name: {first_name}")

    def enter_last_name(self, last_name):
        field = self.driver.find_element(*self.locators["last_name"])
        field.clear()
        field.send_keys(last_name)
        self.logger.info(f"Entered Last Name: {last_name}")

    def enter_email(self, email):
        field = self.driver.find_element(*self.locators["email"])
        field.clear()
        field.send_keys(email)
        self.logger.info(f"Entered Email: {email}")

    def enter_password(self, password):
        field = self.driver.find_element(*self.locators["password"])
        field.clear()
        field.send_keys(password)
        self.logger.info("Entered Password")

    def enter_ssn(self, ssn):
        field = self.driver.find_element(*self.locators["ssn"])
        field.clear()
        field.send_keys(ssn)
        self.logger.info("Entered SSN")

    def click_register(self):
        self.driver.find_element(*self.locators["register_button"]).click()
        self.logger.info("Clicked Register Button")

    # ---------------- VALIDATION METHODS ---------------- #

    def is_field_present(self, field_name):
        """Check whether a field is visible and accessible."""
        try:
            return self.driver.find_element(*self.locators[field_name]).is_displayed()
        except Exception:
            return False

    def get_error_message(self):
        """Fetch the visible error message text (if any)."""
        try:
            element = self.driver.find_element(*self.locators["error_message"])
            return element.text.strip()
        except Exception:
            return None
