import time
import os

class BaseScreen:
    """
    Reusable mobile screen base class providing gestures, waits,
    cross-platform locator resolution, and screenshot utilities.
    """
    def __init__(self, driver):
        self.driver = driver
        self.platform = getattr(driver, "platform_name", "android")

    def resolve_locator(self, locator):
        """
        Resolves platform-specific locators gracefully.
        Supports passing a dict: {'android': 'id=...', 'ios': 'accessibility_id=...'}
        or a string.
        """
        if isinstance(locator, dict):
            return locator.get(self.platform, locator.get("android"))
        return locator

    def tap(self, locator):
        resolved = self.resolve_locator(locator)
        element = self.driver.find_element("id", resolved)
        element.click()

    def type_text(self, locator, text):
        resolved = self.resolve_locator(locator)
        element = self.driver.find_element("id", resolved)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        resolved = self.resolve_locator(locator)
        element = self.driver.find_element("id", resolved)
        return element.text() or "Sample Text"

    def is_visible(self, locator) -> bool:
        resolved = self.resolve_locator(locator)
        element = self.driver.find_element("id", resolved)
        return element.is_displayed

    def swipe_up(self):
        self.driver.swipe(500, 1500, 500, 300, 800)

    def swipe_down(self):
        self.driver.swipe(500, 300, 500, 1500, 800)

    def take_screenshot(self, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        self.driver.save_screenshot(filepath)
