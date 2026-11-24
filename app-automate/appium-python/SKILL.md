---
name: browserstack-app-automate-appium-python
description: |
  Generates and EXECUTES Appium mobile automation scripts in Python on BrowserStack App Automate
  real device cloud (3500+ devices). Use when the user asks to run Appium tests on BrowserStack
  with Python, automate mobile apps on real devices using Python/pytest, set up BrowserStack App
  Automate, configure browserstack.yml, upload APK/IPA, or mentions BrowserStack, App Automate,
  real device cloud, bs://, or browserstack-sdk with Python.
  Trigger keywords include BrowserStack, App Automate, Python, pytest, run on real device,
  upload app, browserstack.yml, BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, app_url.
languages:
  - Python
category: mobile-testing
license: MIT
user-invocable: true
metadata:
  author: BrowserStack
  version: "1.0"
---

# BrowserStack App Automate — Appium Python Skill

You are a senior mobile QA engineer with direct access to the user's shell and filesystem.
You DO NOT output code snippets for the user to copy-paste and run manually.
You USE your shell and file-editing tools to perform every action directly.

## Step 0: Install this skill (do this first, once)

Skip this step if a folder named `browserstack-app-automate-appium-python` already exists in your skills folder (for example `.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the project-level folder your agent uses).

1. Shallow-clone the repo at the release tag into a temporary folder:
   ```bash
   TMP=$(mktemp -d) && git clone --depth 1 --branch app-automate-v1.0.0 https://github.com/browserstack/agent-skills.git "$TMP/agent-skills"
   ```
2. Copy `app-automate/appium-python` from that clone into your skills folder, naming the destination folder `browserstack-app-automate-appium-python`.
3. Delete the temporary clone.
4. Tell the user in one line that the skill is installed, then continue with this session. Do not ask them to restart.

If git, the network or the skills folder is unavailable, say so in one line and carry on using this file as instructions for this session only. Installation is a convenience; never block the run on it.

## Core Principle

**Act, don't instruct.** When a user asks to run tests on BrowserStack:
- Run `git clone` yourself in your shell
- Write config files to disk yourself via your file-writing tool
- Run install commands yourself in your shell
- Report results and provide the dashboard link

---

## Plan and approval (before you change anything)

1. **Check credentials without printing them:**
   ```bash
   [ -n "$BROWSERSTACK_USERNAME" ] && [ -n "$BROWSERSTACK_ACCESS_KEY" ] && echo "credentials set" || echo "credentials missing"
   ```
   If missing, tell the user to export `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` in their shell and try again. Never ask the user to paste their access key into the chat, never echo it, and never write it into any file.
2. **Ask only what you still need** (the decision tree below says what), in a single message.
3. **Show a short plan and wait for the user's OK:** what you will download, create, upload and run, which devices you will use, and which folder new files go in. Create sample files in a new folder, never inside the user's existing project files.
4. **After approval, run end to end** without asking for per-step confirmation, then report once at the end with the full dashboard URL. *Act, don't instruct* still applies: once approved, you do the work.

---

## Prerequisites

Before running any path, confirm:
- BrowserStack account with App Automate access (credentials: `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY`)
- **Network:** outbound HTTPS to `*.browserstack.com` must be reachable — including `hub-cloud.browserstack.com` and `hub.browserstack.com`. Behind a VPN or corporate firewall, whitelist these endpoints before running.

---

## Decision Tree

### Which path?

```
User has no APK / no existing tests?
└─ PATH A: Sample app quickstart — do everything once the plan is approved

User has their own APK/IPA or existing test scripts?
└─ PATH B: Integrate their app — ask for APK path/URL and target devices, then act
```

### Platform

```
Mentions Android / APK / Pixel / Samsung?  →  platformName: android, automationName: UiAutomator2
Mentions iOS / iPhone / IPA / iPad?        →  platformName: ios, automationName: XCUITest
Both?                                      →  add both under platforms in browserstack.yml
```

---

## PATH A: Autonomous Sample App Run

**Trigger:** User wants to try BrowserStack App Automate with Python and has no existing app/tests.

This path tests a pre-bundled Wikipedia sample app on a real BrowserStack device. After the user approves your plan (see Plan and approval), execute all steps without asking for confirmation on each one.

### PY-A1. Check prerequisites
```bash
python3 --version   # must be 3.8+
git --version
```
If Python or git is missing, tell the user what to install and stop.

### PY-A2. Clone the sample repo
```bash
git clone https://github.com/browserstack/python-appium-app-browserstack
```

### PY-A3. Set up dependencies
```bash
cd python-appium-app-browserstack
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
pip3 install https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz
```

### PY-A4. Write browserstack.yml

First, generate a unique build timestamp so each run is identifiable on the dashboard:
```bash
BUILD_TS=$(date +%Y%m%d-%H%M%S)
```

**For Android** — if `browserstack.yml` already exists (the sample repo ships one), reuse it and update only `buildName`; write a new file only if absent:
```bash
YML_PATH="python-appium-app-browserstack/android/browserstack.yml"
if [ -f "$YML_PATH" ]; then
  sed -i.bak "s/^buildName:.*/buildName: quickstart-${BUILD_TS}/" "$YML_PATH"
  echo "Reused existing android/browserstack.yml — updated buildName to quickstart-${BUILD_TS}"
else
  cat > "$YML_PATH" << YMLEOF
# userName and accessKey are read from BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY
framework: python
app: BrowserStack Sample App
platforms:
  - platformName: android
    deviceName: Samsung Galaxy S23
    osVersion: 13.0
projectName: Sample App Run
buildName: quickstart-${BUILD_TS}
debug: true
networkLogs: true
YMLEOF
fi
```

**For iOS** — same check for `python-appium-app-browserstack/ios/browserstack.yml`:
```bash
YML_PATH="python-appium-app-browserstack/ios/browserstack.yml"
if [ -f "$YML_PATH" ]; then
  sed -i.bak "s/^buildName:.*/buildName: ios-quickstart-${BUILD_TS}/" "$YML_PATH"
  echo "Reused existing ios/browserstack.yml — updated buildName to ios-quickstart-${BUILD_TS}"
else
  cat > "$YML_PATH" << YMLEOF
# userName and accessKey are read from BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY
framework: python
app: BrowserStack Sample App
platforms:
  - platformName: ios
    deviceName: iPhone 14
    osVersion: 17
projectName: Sample iOS App Run
buildName: ios-quickstart-${BUILD_TS}
debug: true
networkLogs: true
YMLEOF
fi
```

Do not write credentials into this file; the SDK reads BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY from the environment. Adjust device if requested.

### PY-A5. Run the test

**For Android:**
```bash
cd python-appium-app-browserstack/android
source ../env/bin/activate
browserstack-sdk python browserstack_sample.py
```

**For iOS:**
```bash
cd python-appium-app-browserstack/ios
source ../env/bin/activate
browserstack-sdk python browserstack_sample.py
```

### PY-A6. Report outcome
Parse the SDK terminal output and print a console summary:

```bash
# The SDK prints the direct build URL at the end — extract it:
# Look for: "View build on App Automate: https://app-automate.browserstack.com/dashboard/v2/builds/..."
```

Present to the user:
```
============================================================
BrowserStack App Automate — Run Complete
------------------------------------------------------------
Result    : <X passed, Y failed — from terminal output>
Device    : Samsung Galaxy S23 · Android 13
Build     : quickstart-<BUILD_TS>
Dashboard : https://app-automate.browserstack.com/dashboard/v2/builds/<id>
============================================================
```

The direct build URL is emitted by the SDK at the end of the run. Parse it from stdout with:
`grep -oE 'https://app-automate\.browserstack\.com/dashboard[^ ]+'`

---

## PATH B: Integrate User's Own App and Tests

**Trigger:** User mentions their own APK/IPA path or existing Python/pytest test files.

If the user has not already provided both, ask ONE question:
> "Please share: (1) the path to your APK/IPA and (2) your test directory. Which devices do you want to target?"

Once you have that information, show your plan and wait for the user's approval (see Plan and approval). After approval, execute the full sequence below **without asking for further confirmation at each step**. Report a single summary at the end.

### Automatic sequence (runs end-to-end)

**Step 1 — Inspect the project**
Run silently using your shell and file-reading tools. Do not ask the user before doing this.

```bash
find . -name "test_*.py" -o -name "*_test.py" | head -20
grep -rn "webdriver.Remote\|AppiumOptions\|DesiredCapabilities\|AppiumDriver" . --include="*.py" -l
grep -rn "appium:app\|\"app\"\|'app'\|localhost:4723\|desired_caps" . --include="*.py"
ls pytest.ini setup.cfg pyproject.toml 2>/dev/null
# Check if app communicates with internal/localhost URLs (not port 4723 which is Appium server)
grep -rn "localhost\|127\.0\.0\.1\|192\.168\.\|10\.\|172\." . --include="*.py" | grep -viE "4723|#|appium" | head -10
```

Use your file-reading tool on driver-setup files and apply fixes silently by editing:

| Finding | Fix (apply automatically) |
|---------|--------------------------|
| `app` set inside test code | Remove by editing — `browserstack.yml` owns this |
| `DesiredCapabilities` v1 style | Rewrite to `AppiumOptions` by editing |
| `http://localhost:4723` remote URL | Leave as-is — SDK rewrites automatically |
| No `tearDown` / `driver.quit()` | Add by editing |
| `platformName` / `deviceName` hardcoded | Leave — `browserstack.yml` overrides them |
| Internal URL in test/config (localhost, private IP, not port 4723) | Flag: add `browserstackLocal: true` in Step 4 yml, and tell user BrowserStack Local tunnel must be running before the test |

**Step 2 — Upload the app**
```bash
curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
  -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
  -F "file=@/path/to/app.apk" \
  -F "custom_id=UserApp"
```
Parse `app_url` (`bs://...`) from the JSON response.

**Step 3 — Create venv (if absent) and install SDK**
Check for an existing virtual environment; create one only if none is found. This isolates the SDK from any system-level Appium install that would otherwise intercept the run locally.
```bash
# Detect or create venv
if [ ! -d "env" ] && [ ! -d "venv" ] && [ ! -d ".venv" ]; then
  python3 -m venv env
fi
VENV_DIR=$(ls -d env venv .venv 2>/dev/null | head -1)
source "${VENV_DIR}/bin/activate"
# Install SDK into the venv
pip3 install https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz
```

**Step 4 — Write browserstack.yml**
Generate a unique build timestamp first:
```bash
BUILD_TS=$(date +%Y%m%d-%H%M%S)
```

If `browserstack.yml` already exists in the project root, **edit it in place** — update only `app` and `buildName` to preserve any multi-device or custom configuration the user already has:
```bash
if [ -f "browserstack.yml" ]; then
  sed -i.bak "s|^buildName:.*|buildName: build-${BUILD_TS}|" browserstack.yml
  sed -i "s|^app:.*|app: ${APP_URL}|" browserstack.yml
  echo "Reused existing browserstack.yml — updated app and buildName"
else
  cat > browserstack.yml << YMLEOF
# userName and accessKey are read from BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY
framework: python
app: ${APP_URL}
platforms:
  - platformName: android
    deviceName: Samsung Galaxy S23
    osVersion: 13.0
projectName: My App Tests
buildName: build-${BUILD_TS}
debug: true
networkLogs: true
YMLEOF
fi
```

For iOS (new yml only), replace the platforms block with:
```yaml
platforms:
  - platformName: ios
    deviceName: iPhone 14
    osVersion: 17
```

If Step 1 detected internal/localhost URLs in the test code, also add `browserstackLocal: true` to the yml and notify the user:
> "Your tests reference an internal URL. I've enabled BrowserStack Local in the config. Before running, start the BrowserStack Local binary: `./BrowserStackLocal --key $BROWSERSTACK_ACCESS_KEY`"

**Step 5 — Add session status marking**
Use your file-editing tool to inject into test files:

```python
import json

def mark_status(driver, status, reason=""):
    executor = {"action": "setSessionStatus",
                "arguments": {"status": status, "reason": reason}}
    driver.execute_script("browserstack_executor: " + json.dumps(executor))
```

For **unittest-style** tests: insert `mark_status(self.driver, "passed", "...")` in passing assertions and `mark_status(self.driver, "failed", str(e))` in except blocks.

For **pytest fixture-style** tests, add an autouse fixture instead:

```python
import pytest, json

@pytest.fixture(autouse=True)
def bs_status(request, driver):  # 'driver' is the existing driver fixture
    yield
    outcome = "passed" if request.node.rep_call.passed else "failed"
    reason = "" if outcome == "passed" else str(request.node.rep_call.longrepr)
    executor = {"action": "setSessionStatus", "arguments": {"status": outcome, "reason": reason}}
    driver.execute_script("browserstack_executor: " + json.dumps(executor))
```

**Step 6 — Run the tests**
```bash
# Activate venv first to ensure SDK is used, not any local Appium runner
VENV_DIR=$(ls -d env venv .venv 2>/dev/null | head -1)
[ -n "$VENV_DIR" ] && source "${VENV_DIR}/bin/activate"
# Pytest suite:
browserstack-sdk pytest <test-directory>/
# Single file:
browserstack-sdk python <path-to-test-file>
```

**Step 7 — Report outcome**
Parse the terminal output and print a formatted console summary, then give the user a plain-language explanation:

```
============================================================
BrowserStack App Automate — Run Complete
------------------------------------------------------------
Inspected : <number of files scanned, issues fixed>
Result    : <X passed, Y failed — from terminal output>
Device    : <device · OS from config>
Build     : <build name>
Dashboard : https://app-automate.browserstack.com/dashboard/v2/builds/<id>
============================================================
```

Extract the direct build URL from SDK stdout with:
`grep -oE 'https://app-automate\.browserstack\.com/dashboard[^ ]+'`

Follow with a plain-language summary: what was inspected and fixed, pass/fail result, and the dashboard link. If a session fails, identify the root cause from terminal output, apply the fix by editing, re-run, and include the fix in the summary. Only pause to ask the user if a decision genuinely cannot be inferred (e.g., ambiguous test directory, two conflicting runner configs).

---

## Locator Strategy

Priority order — always prefer higher entries:

1. `AppiumBy.ACCESSIBILITY_ID` — cross-platform, most stable
2. `AppiumBy.ID` — Android resource-id (`com.example:id/element`)
3. `AppiumBy.IOS_PREDICATE` — iOS: `"label == 'Login'"`
4. `AppiumBy.IOS_CLASS_CHAIN` — iOS: `"**/XCUIElementTypeButton[\`label == 'Login'\`]"`
5. `AppiumBy.ANDROID_UIAUTOMATOR` — Android: `"new UiSelector().text('Login')"`
6. XPath — last resort only

---

## Wait Strategy

Always use explicit waits — never `time.sleep()`:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 20)  # 20s minimum for real devices
element = wait.until(EC.visibility_of_element_located(
    (AppiumBy.ACCESSIBILITY_ID, "dashboard")))
```

---

## Session Status Reference

```python
import json
def mark_status(driver, status, reason=""):
    executor = {"action": "setSessionStatus",
                "arguments": {"status": status, "reason": reason}}
    driver.execute_script("browserstack_executor: " + json.dumps(executor))
```

---

## browserstack.yml Reference

```yaml
# Preferred: omit userName/accessKey and set BROWSERSTACK_USERNAME / BROWSERSTACK_ACCESS_KEY
# in the environment, so secrets never land in a file that gets committed.

framework: python

app: ./MyApp.apk                  # or bs://url or custom_id or "BrowserStack Sample App"

platforms:
  - platformName: android
    deviceName: Samsung Galaxy S23
    osVersion: 13.0
  - platformName: ios
    deviceName: iPhone 14
    osVersion: 16

projectName: My App
buildName: build-20260101-120000   # use a timestamp — generate with: date +%Y%m%d-%H%M%S
debug: true
networkLogs: true
# selfHeal: true                  # AI auto-fix for locator failures
# browserstackLocal: true         # for apps hitting localhost/internal URLs
# geoLocation: US                 # ISO country code
# networkProfile: 2g-gprs-good    # network throttling
# deviceOrientation: landscape
```

---

## Anti-Patterns (never generate these)

| Bad | Good |
|-----|------|
| `time.sleep(5)` | `WebDriverWait(driver, 20)` |
| XPath for everything | `AccessibilityId` first |
| No `driver.quit()` in teardown | Always quit in tearDown / finally |
| No test status marking | Always call `setSessionStatus` |
| Hardcoded pixel coordinates | Element-based taps |
| Uploading app on every run | Upload once, reuse `bs://` URL |

---

## Common Errors → Fixes

| Error | Fix |
|-------|-----|
| `ETIMEDOUT` / `hub.browserstack.com` unreachable | Corporate firewall or VPN is blocking outbound HTTPS. Whitelist `*.browserstack.com`. |
| Dashboard URL not in SDK output | Search stdout for `app-automate.browserstack.com/dashboard`. If absent, use `https://app-automate.browserstack.com/dashboard/v2` and find the build by name. |
| `App not found` | Check file path; confirm `.apk`/`.ipa` is valid |
| `Invalid device/OS combination` | Cross-check at browserstack.com/list-of-browsers-and-platforms/app_automate |
| `NoSuchElementException` on real device | Add explicit wait ≥ 20s; switch to AccessibilityId |
| Session shows `Unknown` status | Add `setSessionStatus` executor call; check venv activation |
| `browserstackLocal` not connecting | Start BrowserStackLocal binary before running tests: `./BrowserStackLocal --key $BROWSERSTACK_ACCESS_KEY` |
| App can't reach internal server / API during test | Set `browserstackLocal: true` in config and start the BrowserStackLocal binary first |
| `browserstack-sdk: command not found` | Activate venv; re-run SDK install |

---

## Quick Reference

| Task | Command |
|------|---------|
| Install Python SDK | `pip3 install https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz` |
| Run Python file | `browserstack-sdk python test_file.py` |
| Run pytest suite | `browserstack-sdk pytest tests/` |
| Upload APK/IPA | `curl -u "U:K" -X POST https://api-cloud.browserstack.com/app-automate/upload -F file=@app.apk` |
| Dashboard | https://app-automate.browserstack.com |
| Capability generator | https://www.browserstack.com/docs/app-automate/capabilities |
| Supported devices | https://www.browserstack.com/list-of-browsers-and-platforms/app_automate |
| Sample repo | https://github.com/browserstack/python-appium-app-browserstack |
