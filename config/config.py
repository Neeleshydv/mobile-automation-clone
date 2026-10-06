import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PLATFORM: str = os.getenv("PLATFORM", "android").lower()
    EMULATION_MODE: bool = os.getenv("EMULATION_MODE", "True").lower() in ("true", "1", "yes")
    APPIUM_SERVER_URL: str = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

    # Android Configuration
    ANDROID_DEVICE_NAME: str = os.getenv("ANDROID_DEVICE_NAME", "Pixel_8_Pro_API_34")
    ANDROID_PLATFORM_VERSION: str = os.getenv("ANDROID_PLATFORM_VERSION", "14.0")
    ANDROID_APP_PACKAGE: str = os.getenv("ANDROID_APP_PACKAGE", "com.LightX.assistant")
    ANDROID_APP_ACTIVITY: str = os.getenv("ANDROID_APP_ACTIVITY", ".ui.MainActivity")
    ANDROID_APP_PATH: str = os.getenv("ANDROID_APP_PATH", "./apps/LightX_ai_v2.4.apk")

    # iOS Configuration
    IOS_DEVICE_NAME: str = os.getenv("IOS_DEVICE_NAME", "iPhone 15 Pro")
    IOS_PLATFORM_VERSION: str = os.getenv("IOS_PLATFORM_VERSION", "17.4")
    IOS_BUNDLE_ID: str = os.getenv("IOS_BUNDLE_ID", "com.LightX.assistant")
    IOS_APP_PATH: str = os.getenv("IOS_APP_PATH", "./apps/LightX_ai_v2.4.app")

    # Credentials
    TEST_USER_EMAIL: str = os.getenv("TEST_USER_EMAIL", "alex@LightX.com")
    TEST_USER_PASSWORD: str = os.getenv("TEST_USER_PASSWORD", "SecretSauce@2026")

