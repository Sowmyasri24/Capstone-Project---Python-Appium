"""Welcome page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class WelcomePage(BasePage):
    """
    Welcome page object for My Demo App.

    Contains all locators and methods related to the welcome screen.
    """

    # Android Locators
    ANDROID_WELCOME_TITLE = (
        By.ACCESSIBILITY_ID,
        "Welcome"  # Update this value if Android accessibility ID differs
    )

    # iOS Locators
    IOS_WELCOME_TITLE = (
        AppiumBy.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`name == "Welcome"`]'
    )

    def __init__(self, driver):
        """
        Initialize WelcomePage.

        Args:
            driver (webdriver.Remote): Appium driver instance
        """
        super().__init__(driver)

    def is_welcome_title_displayed(self):
        """
        Check if the Welcome title is displayed.

        Returns:
            bool: True if Welcome title is displayed, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_WELCOME_TITLE,
            self.IOS_WELCOME_TITLE
        )
        return self.actions.is_displayed(locator, timeout=5)

    def get_welcome_text(self):
        """
        Get the text of the Welcome title.

        Returns:
            str: The welcome title text or empty string if not found
        """
        locator = self.get_locator(
            self.ANDROID_WELCOME_TITLE,
            self.IOS_WELCOME_TITLE
        )
        return self.actions.get_text(locator)

