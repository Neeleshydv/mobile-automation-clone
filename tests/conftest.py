import pytest
import os
from datetime import datetime
from drivers.driver_factory import DriverFactory
from config.config import Config

@pytest.fixture(scope="function")
def android_driver():
    """Provides an initialized Android Appium driver instance."""
    driver = DriverFactory.create_driver(platform="android")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def ios_driver():
    """Provides an initialized iOS Appium driver instance."""
    driver = DriverFactory.create_driver(platform="ios")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def mobile_driver(request):
    """Provides a dynamic driver based on the configured PLATFORM setting."""
    driver = DriverFactory.create_driver(platform=Config.PLATFORM)
    request.node.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.nodeid.replace("::", "_").replace(".py", "")
            shot_path = f"reports/screenshots/{test_name}_{ts}.png"
            try:
                driver.save_screenshot(shot_path)
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    extras.append(pytest_html.extras.image(shot_path))
            except Exception as e:
                print(f"Failed to save screenshot: {e}")
        report.extras = extras

def pytest_html_report_title(report):
    report.title = "LightX â€” Mobile Automation Test Report (Android & iOS)"

def pytest_configure(config):
    config._metadata = {
        "Project": "LightX Mobile App",
        "Framework": "Appium 2.x + PyTest + Mobile POM",
        "Target Platforms": "Android 14 (UiAutomator2) & iOS 17 (XCUITest)",
        "Device Names": "Pixel 8 Pro & iPhone 15 Pro",
        "App Version": "v2.4.0-RC1 (Build #4128)"
    }

