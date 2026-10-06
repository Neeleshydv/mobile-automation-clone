from screens.base_screen import BaseScreen
from config.config import Config

class LoginScreen(BaseScreen):
    """Mobile Login Screen for LightX App (Android & iOS)."""

    EMAIL_INPUT = {
        "android": "com.LightX.assistant:id/input_email",
        "ios": "accessibility_id=email_textfield"
    }
    PASSWORD_INPUT = {
        "android": "com.LightX.assistant:id/input_password",
        "ios": "accessibility_id=password_textfield"
    }
    SIGN_IN_BUTTON = {
        "android": "com.LightX.assistant:id/btn_sign_in",
        "ios": "accessibility_id=sign_in_button"
    }
    BIOMETRIC_BUTTON = {
        "android": "com.LightX.assistant:id/btn_fingerprint",
        "ios": "accessibility_id=face_id_button"
    }
    ERROR_BANNER = {
        "android": "com.LightX.assistant:id/tv_error_banner",
        "ios": "accessibility_id=error_banner_label"
    }

    def login_with_credentials(self, email=None, password=None):
        email = email or Config.TEST_USER_EMAIL
        password = password or Config.TEST_USER_PASSWORD
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.tap(self.SIGN_IN_BUTTON)

    def login_with_face_id(self):
        """Simulates successful iOS Face ID authentication."""
        self.tap(self.BIOMETRIC_BUTTON)

    def login_with_fingerprint(self):
        """Simulates successful Android BiometricPrompt authentication."""
        self.tap(self.BIOMETRIC_BUTTON)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_BANNER)

