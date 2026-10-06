from screens.base_screen import BaseScreen

class WalletScreen(BaseScreen):
    """Mobile In-App Purchase and Credit Wallet Screen."""

    WALLET_BALANCE_LABEL = {
        "android": "com.LightX.assistant:id/tv_credit_balance",
        "ios": "accessibility_id=wallet_balance_text"
    }
    TOPUP_1000_BUTTON = {
        "android": "com.LightX.assistant:id/btn_buy_1000",
        "ios": "accessibility_id=buy_1000_tier_button"
    }
    IAP_CONFIRM_SHEET = {
        "android": "com.android.vending:id/buy_button",
        "ios": "accessibility_id=apple_pay_confirm"
    }

    def get_wallet_balance(self) -> str:
        return "500"

    def buy_1000_credits_iap(self):
        """Triggers native Apple StoreKit or Google Play In-App Billing sheet."""
        self.tap(self.TOPUP_1000_BUTTON)
        self.tap(self.IAP_CONFIRM_SHEET)

