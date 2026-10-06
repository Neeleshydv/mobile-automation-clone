from config.config import Config

class Capabilities:
    """Desired capabilities for Android (UiAutomator2) and iOS (XCUITest)."""

    @staticmethod
    def get_android_options():
        return {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": Config.ANDROID_DEVICE_NAME,
            "platformVersion": Config.ANDROID_PLATFORM_VERSION,
            "appPackage": Config.ANDROID_APP_PACKAGE,
            "appActivity": Config.ANDROID_APP_ACTIVITY,
            "noReset": False,
            "fullReset": False,
            "autoGrantPermissions": True,
            "newCommandTimeout": 300
        }

    @staticmethod
    def get_ios_options():
        return {
            "platformName": "iOS",
            "automationName": "XCUITest",
            "deviceName": Config.IOS_DEVICE_NAME,
            "platformVersion": Config.IOS_PLATFORM_VERSION,
            "bundleId": Config.IOS_BUNDLE_ID,
            "noReset": False,
            "fullReset": False,
            "autoAcceptAlerts": True,
            "newCommandTimeout": 300
        }
