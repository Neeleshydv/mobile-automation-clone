# LightX Mobile Test Automation Framework (Android & iOS)

A production-grade, unified Mobile Test Automation Framework for **LightX** supporting both **Android (UiAutomator2)** and **iOS (XCUITest)** using **Appium 2.x**, **Python 3.13**, and **PyTest**.

---

## 🏗️ Architecture & Directory Structure

```
mobile-automation-suite/
│
├── config/
│   ├── config.py              # Environment configuration (.env reader)
│   └── capabilities.py        # Desired Capabilities for Android & iOS
│
├── drivers/
│   └── driver_factory.py      # Unified driver factory (Android / iOS / Emulation)
│
├── screens/                   # Mobile Page Object Model (POM)
│   ├── base_screen.py         # Mobile gestures: tap, swipe, wait, cross-platform locators
│   ├── login_screen.py        # Biometric Face ID & Fingerprint authentication
│   ├── chat_screen.py         # AI Assistant Chat, Whisper voice mic, Camera OCR RAG
│   └── wallet_screen.py       # In-App Purchases (StoreKit 2 & Google Play Billing v6)
│
├── tests/                     # Automated Test Scenarios
│   ├── conftest.py            # Appium lifecycle fixtures & screenshot failure hook
│   ├── test_android_flows.py  # Android specific tests (Fingerprint, Whisper, Google Play)
│   ├── test_ios_flows.py      # iOS specific tests (Face ID, Camera RAG, StoreKit)
│   └── test_cross_platform.py # Unified cross-platform test scenarios
│
├── reports/                   # Standalone HTML execution reports & failure screenshots
├── .github/workflows/         # Multi-platform CI (Ubuntu for Android, macOS for iOS)
├── Jenkinsfile                # Declarative Jenkins pipeline for Mobile
├── pytest.ini                 # PyTest configuration & platform markers
├── requirements.txt           # Python dependencies
└── run_mobile_tests.bat       # 1-Click local test execution runner
```

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10+ (Tested on Python 3.13)
* Appium 2.x (`npm install -g appium`)
* Appium Drivers:
  * Android: `appium driver install uiautomator2`
  * iOS: `appium driver install xcuitest`
* Android SDK (for Android Emulators & Devices) / Xcode (for iOS Simulators)

### 2. Installation
```powershell
# Clone the repository
git clone https://github.com/Neeleshydv/mobile-automation-clone.git
cd mobile-automation-clone

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Executing Tests

### Quick Execution
Double-click `run_mobile_tests.bat` or run via PowerShell:
```powershell
.\run_mobile_tests.bat
```

### Targeted Execution via Platform Markers
```bash
# Run Android test suite
python -m pytest -m android -v

# Run iOS test suite
python -m pytest -m ios -v

# Run Mobile Biometric flows (Face ID & Fingerprint)
python -m pytest -m biometrics -v

# Run Mobile In-App Purchase flows (StoreKit & Google Play)
python -m pytest -m iap -v

# Run full cross-platform regression
python -m pytest -v
```

---

## 🔄 Cross-Platform Architectural Design

1. **Unified Driver Factory**:
   * Uses `config/capabilities.py` to abstract Appium options between Android (`UiAutomator2Options`) and iOS (`XCUITestOptions`).
   * Switch platforms dynamically via `.env` (`PLATFORM=android` or `PLATFORM=ios`) or command-line parameters.

2. **Screen Object Model (POM)**:
   * `screens/base_screen.py` handles cross-platform locator resolution (`{'android': 'id=...', 'ios': 'accessibility_id=...'}`) while providing reusable touch gestures like vertical swipes, taps, and keyboard dismissal.

3. **CI/CD Pipeline Matrix**:
   * Android test jobs execute on Linux runners (Ubuntu).
   * iOS test jobs execute on macOS runners (required for Xcode and iOS Simulators).
