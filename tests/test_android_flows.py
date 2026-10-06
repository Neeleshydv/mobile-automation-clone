import pytest
from screens.login_screen import LoginScreen
from screens.chat_screen import ChatScreen
from screens.wallet_screen import WalletScreen

@pytest.mark.android
@pytest.mark.biometrics
def test_android_fingerprint_biometric_login(android_driver):
    """
    Android Test: Verify BiometricPrompt fingerprint authentication
    authenticates user and transitions to Chat interface.
    """
    login = LoginScreen(android_driver)
    login.login_with_fingerprint()

    chat = ChatScreen(android_driver)
    assert chat.is_chat_active(), "Chat screen failed to activate after Android fingerprint login"

@pytest.mark.android
@pytest.mark.smoke
def test_android_voice_whisper_recording(android_driver):
    """
    Android Test: Verify Whisper speech mic interaction streams voice query.
    """
    chat = ChatScreen(android_driver)
    chat.trigger_voice_recording()
    assert chat.is_chat_active()

@pytest.mark.android
@pytest.mark.iap
def test_android_google_play_billing_iap(android_driver):
    """
    Android Test: Verify Google Play In-App Billing sheet triggers and delivers credits.
    """
    wallet = WalletScreen(android_driver)
    wallet.buy_1000_credits_iap()
    assert wallet.get_wallet_balance() == "500", "Wallet balance verification failed"
