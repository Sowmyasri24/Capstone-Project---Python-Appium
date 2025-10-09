"""Configuration management for test automation framework."""

import os
from enum import Enum


class Platform(Enum):
    """Supported mobile platforms."""
    ANDROID = "android"
    IOS = "ios"


class Config:
    """
    Central configuration class for framework settings.
    Manages all parameters including platform, timeouts, and app details.
    """

    # =========================================================
    # 🔹 Appium Server Configuration
    # =========================================================

    # Local Appium server (default)
    LOCAL_APPIUM_SERVER_URL = "http://127.0.0.1:4723/wd/hub"

    # Perfecto Cloud Appium server
    # Replace <your-cloud-name> with your Perfecto cloud name
    PERFECTO_SERVER_URL = os.getenv(
        "PERFECTO_SERVER_URL",
        "https://trail.perfectomobile.com/nexperience/perfectomobile/wd/hub"
    )

    # Authentication for Perfecto
    PERFECTO_SECURITY_TOKEN = os.getenv("PERFECTO_SECURITY_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2ZDM2NmJiNS01NDAyLTQ4MmMtYTVhOC1kODZhODk4MDYyZjIifQ.eyJpYXQiOjE3NTk3NTExMTMsImp0aSI6ImViNDJlMzBlLTg4MWMtNGJkZC05MmFhLTU4ODA3YmViYzExOCIsImlzcyI6Imh0dHBzOi8vYXV0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL3RyaWFsLXBlcmZlY3RvbW9iaWxlLWNvbSIsImF1ZCI6Imh0dHBzOi8vYXV0aDMucGVyZmVjdG9tb2JpbGUuY29tL2F1dGgvcmVhbG1zL3RyaWFsLXBlcmZlY3RvbW9iaWxlLWNvbSIsInN1YiI6IjcwMTI3NDY5LTRhMzMtNDIxYy1iMzlkLWYwZjAzNzExMWFhMCIsInR5cCI6Ik9mZmxpbmUiLCJhenAiOiJvZmZsaW5lLXRva2VuLWdlbmVyYXRvciIsIm5vbmNlIjoiZTFmZmFkNTEtNmEwMS00NTI0LTljMjQtMTkxNGNmODYxNzc5Iiwic2Vzc2lvbl9zdGF0ZSI6IjU4YmU4ODBjLTg2MjctNGE5Ni04ZTQyLWE0MmEwM2Q3NzRiZiIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI1OGJlODgwYy04NjI3LTRhOTYtOGU0Mi1hNDJhMDNkNzc0YmYifQ.sMMCTTlbMjZNwfqHUztBYxf4D7cohhP86mia6PUrbFk")

    # Choose which environment to use: 'local' or 'perfecto'
    CLOUD_PROVIDER = os.getenv("CLOUD_PROVIDER", "local")

    # Dynamically choose which Appium URL to use
    @classmethod
    def get_server_url(cls):
        """Return the correct Appium server URL based on cloud provider."""
        if cls.CLOUD_PROVIDER.lower() == "perfecto":
            return cls.PERFECTO_SERVER_URL
        return cls.LOCAL_APPIUM_SERVER_URL

    # =========================================================
    # 🔹 Platform Selection
    # =========================================================
    PLATFORM = os.getenv("PLATFORM", Platform.ANDROID.value)

    # =========================================================
    # 🔹 Timeout Configuration
    # =========================================================
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    COMMAND_TIMEOUT = int(os.getenv("COMMAND_TIMEOUT", "120"))

    # =========================================================
    # 🔹 Application Configuration
    # =========================================================
    ANDROID_APP_PACKAGE = "com.saucelabs.mydemoapp.android"
    ANDROID_APP_ACTIVITY = "com.saucelabs.mydemoapp.android.view.activities.MainActivity"

    IOS_BUNDLE_ID = "com.saucelabs.mydemoapp.ios"

    # =========================================================
    # 🔹 Device Configuration for local
    # =========================================================
    ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
    ANDROID_PLATFORM_VERSION = os.getenv("ANDROID_PLATFORM_VERSION", "13.0")

    IOS_DEVICE_NAME = os.getenv("IOS_DEVICE_NAME", "iPhone 14")
    IOS_PLATFORM_VERSION = os.getenv("IOS_PLATFORM_VERSION", "16.0")

    # =========================================================
    # 🔹 Test Data
    # =========================================================
    TEST_USERNAME = os.getenv("TEST_USERNAME", "john.doe@digitalbank.com")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "Test@1234")

    # Device Configuration for perfecto
    PERFECTO_ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "AndroidDevice1")
    PERFECTO_ANDROID_PLATFORM_VERSION = os.getenv("ANDROID_PLATFORM_VERSION", "13.0")

    PERFECTO_IOS_DEVICE_NAME = os.getenv("IOS_DEVICE_NAME", "iPhone 14 Pro")
    PERFECTO_IOS_PLATFORM_VERSION = os.getenv("IOS_PLATFORM_VERSION", "16.0")

    # 🔹 Test Data (Example login)
    PERFECTO_TEST_USERNAME = os.getenv("TEST_USERNAME", "john.doe@digitalbank.com")
    PERFECTO_TEST_PASSWORD = os.getenv("TEST_PASSWORD", "Test@1234")

    # =========================================================
    # 🔹 Reporting Configuration
    # =========================================================
    REPORTS_DIR = "reports"
    LOGS_DIR = "logs"
    SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")

    # =========================================================
    # 🔹 Platform helpers
    # =========================================================
    @classmethod
    def get_platform(cls):
        """Get the current platform."""
        return Platform(cls.PLATFORM.lower())

    @classmethod
    def is_android(cls):
        """Check if current platform is Android."""
        return cls.get_platform() == Platform.ANDROID

    @classmethod
    def is_ios(cls):
        """Check if current platform is iOS."""
        return cls.get_platform() == Platform.IOS
