# LightX Mobile Automation Framework (Android & iOS)

A production-grade, unified Mobile Test Automation Framework supporting both **Android (UiAutomator2)** and **iOS (XCUITest)** using **Appium 2.x**, **Python 3.13**, and **PyTest**.

---

## ðŸ—ï¸ Architecture Overview

```
mobile-automation-suite/
â”‚
â”œâ”€â”€ config/
â”‚   â”œâ”€â”€ config.py              # Environment configuration (.env reader)
â”‚   â””â”€â”€ capabilities.py        # Desired Capabilities for Android & iOS
â”‚
â”œâ”€â”€ drivers/
â”‚   â””â”€â”€ driver_factory.py      # Unified driver factory (Android / iOS / Emulation)
â”‚
â”œâ”€â”€ screens/                   # Mobile Page Object Model (POM)
â”‚   â”œâ”€â”€ base_screen.py         # Mobile gestures: tap, swipe, wait, cross-platform locators
â”‚   â”œâ”€â”€ login_screen.py        # Biometric Face ID & Fingerprint login
â”‚   â”œâ”€â”€ chat_screen.py         # AI Assistant Chat, Whisper voice mic, Camera OCR RAG
â”‚   â””â”€â”€ wallet_screen.py       # In-App Purchases (StoreKit 2 & Google Play Billing v6)
â”‚
â”œâ”€â”€ tests/
â”‚   â”œâ”€â”€ conftest.py            # Appium lifecycle fixtures & screenshot failure hook
â”‚   â”œâ”€â”€ test_android_flows.py  # Android specific tests (Fingerprint, Whisper, Google Play)
â”‚   â”œâ”€â”€ test_ios_flows.py      # iOS specific tests (Face ID, Camera RAG, StoreKit)
â”‚   â””â”€â”€ test_cross_platform.py # Unified cross-platform test scenarios
â”‚
â”œâ”€â”€ reports/                   # Standalone HTML execution reports & failure screenshots
â”œâ”€â”€ .github/workflows/         # Multi-platform CI (Ubuntu for Android, macOS for iOS)
â”œâ”€â”€ Jenkinsfile                # Declarative Jenkins pipeline for Mobile
â””â”€â”€ run_mobile_tests.bat       # 1-Click execution script for local demonstration
```

---

## ðŸŽ¯ Interview Pitch: Android vs iOS in the Same Framework

### Q: *"How do you structure mobile testing for Android vs iOS?"*
> **Answer**:  
> *"We maintain both platforms in the **same unified framework**. The business logic, test cases, and user journeys are 95% identical. We abstract the platform differences in two key layers:*  
> *1. **Driver Factory**: Initializes `UiAutomator2Options` for Android `.apk` vs `XCUITestOptions` for iOS `.ipa` based on the `--platform` parameter.*  
> *2. **Screen Objects**: Use cross-platform Accessibility IDs or dictionary locators (`{'android': 'id=...', 'ios': 'accessibility_id=...'}`).*  
> *3. **CI/CD**: Android runs on standard Linux CI agents, while iOS runs on macOS runners (required for Xcode).*"

