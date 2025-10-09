"""Device capabilities configuration for Android and iOS (Local + Perfecto setup)."""

from config.config import Config


class Capabilities:
    """Manages Android and iOS capabilities for both local and Perfecto environments."""

    @staticmethod
    def get_android_capabilities():
        """Get Android device capabilities."""
        return {
            "platformName": "Android",
            "platformVersion": Config.ANDROID_PLATFORM_VERSION,
            "deviceName": Config.ANDROID_DEVICE_NAME,
            "automationName": "UiAutomator2",
            "appPackage": Config.ANDROID_APP_PACKAGE,
            "appActivity": Config.ANDROID_APP_ACTIVITY,
            "newCommandTimeout": Config.COMMAND_TIMEOUT,
            "autoGrantPermissions": True,
            "noReset": False,
            # Include security token only if running on Perfecto
            **(
                {"securityToken": Config.PERFECTO_SECURITY_TOKEN}
                if Config.CLOUD_PROVIDER.lower() == "perfecto"
                else {}
            ),
        }

    @staticmethod
    def get_ios_capabilities():
        """Get iOS device capabilities."""
        return {
            "platformName": "iOS",
            "platformVersion": Config.IOS_PLATFORM_VERSION,
            "deviceName": Config.IOS_DEVICE_NAME,
            "automationName": "XCUITest",
            "bundleId": Config.IOS_BUNDLE_ID,
            "autoAcceptAlerts": True,
            "noReset": False,
            "newCommandTimeout": Config.COMMAND_TIMEOUT,
            # Include security token only if running on Perfecto
            **(
                {"securityToken": Config.PERFECTO_SECURITY_TOKEN}
                if Config.CLOUD_PROVIDER.lower() == "perfecto"
                else {}
            ),
        }

    @staticmethod
    def get_capabilities():
        """Return platform-specific capabilities."""
        return (
            Capabilities.get_android_capabilities()
            if Config.is_android()
            else Capabilities.get_ios_capabilities()
        )
