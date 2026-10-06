import pytest
from screens.login_screen import LoginScreen
from screens.chat_screen import ChatScreen
from screens.wallet_screen import WalletScreen

@pytest.mark.smoke
def test_unified_login_and_token_streaming(mobile_driver):
    """
    Cross-Platform Test: Runs on Android or iOS dynamically depending on config.
    Validates credential login and AI prompt submission.
    """
    login = LoginScreen(mobile_driver)
    login.login_with_credentials("alex@LightX.com", "SecretSauce@2026")

    chat = ChatScreen(mobile_driver)
    assert chat.is_chat_active()

    chat.send_prompt("Explain quantum computing in 1 sentence")
    assert chat.is_chat_active()

@pytest.mark.regression
def test_unified_credit_wallet_balance_inquiry(mobile_driver):
    """
    Cross-Platform Test: Verifies wallet balance retrieval and credit display.
    """
    wallet = WalletScreen(mobile_driver)
    assert int(wallet.get_wallet_balance()) > 0

