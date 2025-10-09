"""Driver factory for creating Appium driver instances (Local + Perfecto)."""

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from config.config import Config
from config.capabilities import Capabilities
from utilities.logger import Logger


class DriverFactory:
    """
    Factory class for creating and managing Appium driver instances.

    Supports:
    - Local Android/iOS emulators or real devices
    - Perfecto cloud devices
    """

    logger = Logger.get_logger(__name__)

    @staticmethod
    def create_driver():
        """Create and return Appium driver based on platform and environment."""

        try:
            DriverFactory.logger.info(
                f"Creating driver for platform: {Config.PLATFORM}, "
                f"Environment: {Config.CLOUD_PROVIDER}"
            )

            # Load capabilities based on platform
            if Config.is_android():
                options = UiAutomator2Options().load_capabilities(
                    Capabilities.get_android_capabilities()
                )
            else:
                options = XCUITestOptions().load_capabilities(
                    Capabilities.get_ios_capabilities()
                )

            # Create Appium driver
            driver = webdriver.Remote(
                Config.get_server_url(),
                options=options
            )

            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            DriverFactory.logger.info("Driver created successfully")
            return driver

        except Exception as e:
            DriverFactory.logger.error(f"Failed to create driver: {e}")
            raise

    @staticmethod
    def quit_driver(driver):
        """Quit the Appium driver and clean up resources."""
        if driver:
            try:
                DriverFactory.logger.info("Quitting driver")
                driver.quit()
                DriverFactory.logger.info("Driver quit successfully")
            except Exception as e:
                DriverFactory.logger.error(f"Error while quitting driver: {e}")
