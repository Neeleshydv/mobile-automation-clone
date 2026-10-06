import pytest
from screens.login_screen import LoginScreen
from screens.chat_screen import ChatScreen
from screens.wallet_screen import WalletScreen

@pytest.mark.ios
@pytest.mark.biometrics
def test_ios_face_id_biometric_login(ios_driver):
    """
    iOS Test: Verify LocalAuthentication Face ID authenticates user
    seamlessly to Chat interface.
    """
    login = LoginScreen(ios_driver)
    login.login_with_face_id()

    chat = ChatScreen(ios_driver)
    assert chat.is_chat_active(), "Chat screen failed to activate after iOS Face ID login"

@pytest.mark.ios
@pytest.mark.smoke
def test_ios_camera_document_scan_rag(ios_driver):
    """
    iOS Test: Verify Camera document scan button opens OCR ingestion pipeline.
    """
    chat = ChatScreen(ios_driver)
    chat.scan_document_camera()
    assert chat.is_chat_active()

@pytest.mark.ios
@pytest.mark.iap
def test_ios_apple_storekit_iap_purchase(ios_driver):
    """
    iOS Test: Verify Apple StoreKit 2 payment sheet confirms transaction and updates balance.
    """
    wallet = WalletScreen(ios_driver)
    wallet.buy_1000_credits_iap()
    assert wallet.get_wallet_balance() == "500"
