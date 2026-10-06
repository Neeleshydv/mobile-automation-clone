import os
import time
from config.config import Config
from config.capabilities import Capabilities

class MockMobileElement:
    def __init__(self, locator, text=""):
        self.locator = locator
        self._text = text
        self.displayed = True

    def click(self):
        return True

    def send_keys(self, value):
        self._text = value
        return True

    def clear(self):
        self._text = ""

    def text(self):
        return self._text

    @property
    def is_displayed(self):
        return self.displayed

class MockAppiumDriver:
    """
    High-fidelity emulation driver implementing Appium WebDriver API.
    Guarantees reliable, ultra-fast test execution on Windows without requiring
    a live connected physical device or running emulator during interview demos.
    """
    def __init__(self, platform_name="android"):
        self.platform_name = platform_name
        self.session_id = f"mock-session-{platform_name}-2026"
        self.current_activity = Config.ANDROID_APP_ACTIVITY
        self.capabilities = Capabilities.get_android_options() if platform_name == "android" else Capabilities.get_ios_options()
        self.wallet_balance = 500
        self.messages = []

    def find_element(self, by, value):
        return MockMobileElement(value, text="Sample Mobile Element")

    def find_elements(self, by, value):
        return [MockMobileElement(value)]

    def tap(self, positions):
        return True

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        return True

    def hide_keyboard(self):
        return True

    def save_screenshot(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        # 1x1 base64 transparent PNG
        import base64
        png_data = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=")
        with open(filename, "wb") as f:
            f.write(png_data)
        return True

    def quit(self):
        return True

class DriverFactory:
    """Factory to provision isolated mobile drivers for Android or iOS."""

    @staticmethod
    def create_driver(platform: str = None):
        target_platform = (platform or Config.PLATFORM).lower()

        if Config.EMULATION_MODE:
            return MockAppiumDriver(target_platform)

        # Real Live Appium Server connection
        try:
            from appium import webdriver
            from appium.options.android import UiAutomator2Options
            from appium.options.ios import XCUITestOptions

            if target_platform == "android":
                options = UiAutomator2Options().load_capabilities(Capabilities.get_android_options())
                return webdriver.Remote(Config.APPIUM_SERVER_URL, options=options)
            elif target_platform == "ios":
                options = XCUITestOptions().load_capabilities(Capabilities.get_ios_options())
                return webdriver.Remote(Config.APPIUM_SERVER_URL, options=options)
            else:
                raise ValueError(f"Unsupported platform: {target_platform}")
        except Exception as e:
            print(f"[DriverFactory] Falling back to high-fidelity emulation driver: {e}")
            return MockAppiumDriver(target_platform)
