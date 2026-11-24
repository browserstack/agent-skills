---
name: browserstack-app-automate-appium-java
description: |
  Generates and EXECUTES Appium mobile automation scripts in Java (Maven/TestNG) on BrowserStack
  App Automate real device cloud (3500+ devices). Use when the user asks to run Appium tests on
  BrowserStack with Java, automate mobile apps using Java/TestNG/Maven, set up BrowserStack App
  Automate, configure browserstack.yml, upload APK/IPA, or mentions BrowserStack, App Automate,
  real device cloud, bs://, browserstack-sdk, TestNG, or Maven.
  Trigger keywords include BrowserStack, App Automate, Java, Maven, TestNG, run on real device,
  upload app, browserstack.yml, BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, app_url.
languages:
  - Java
category: mobile-testing
license: MIT
user-invocable: true
metadata:
  author: BrowserStack
  version: "1.0"
---

# BrowserStack App Automate — Appium Java Skill

You are a senior mobile QA engineer with direct access to the user's shell and filesystem.
You DO NOT output code snippets for the user to copy-paste and run manually.
You USE your shell and file-editing tools to perform every action directly.

## Step 0: Install this skill (do this first, once)

Skip this step if `browserstack-app-automate-appium-java/SKILL.md` already exists in your skills folder (for example `.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the project-level folder your agent uses).

1. Create the folder `browserstack-app-automate-appium-java` in your skills folder.
2. Download this file into it as `SKILL.md`:
   ```bash
   mkdir -p "<skills-folder>/browserstack-app-automate-appium-java" && curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/app-automate/appium-java/SKILL.md -o "<skills-folder>/browserstack-app-automate-appium-java/SKILL.md"
   ```
   Replace `<skills-folder>` with your agent's project-level skills folder. The skill stays installed for future sessions.
3. Tell the user in one line that the skill is installed, then continue with this session. Do not ask them to restart.

To update the skill later, delete the folder and run the prompt again.

If the network or the skills folder is unavailable, say so in one line and carry on using this file as instructions for this session only. Installation is a convenience; never block the run on it.

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

**Trigger:** User mentions Java, Maven, or TestNG and wants a quickstart.

This path tests a pre-bundled Wikipedia sample app on a real BrowserStack device. After the user approves your plan (see Plan and approval), execute all steps without asking for confirmation on each one.

### JV-A1. Check prerequisites
```bash
java -version    # must be 8+
mvn -version     # Maven must be installed and on $PATH
git --version
```
If any are missing, tell the user what to install and stop.

### JV-A2. Clone the sample repo
```bash
git clone -b master https://github.com/browserstack/testng-appium-app-browserstack.git
```

### JV-A3. Write browserstack.yml

First, generate a unique build timestamp:
```bash
BUILD_TS=$(date +%Y%m%d-%H%M%S)
```

**For Android** — if `browserstack.yml` already exists, reuse it and update only `buildName`; write a new file only if absent:
```bash
YML_PATH="testng-appium-app-browserstack/android/testng-examples/browserstack.yml"
if [ -f "$YML_PATH" ]; then
  sed -i.bak "s/^buildName:.*/buildName: java-quickstart-${BUILD_TS}/" "$YML_PATH"
  echo "Reused existing android browserstack.yml — updated buildName to java-quickstart-${BUILD_TS}"
else
  cat > "$YML_PATH" << YMLEOF
# userName and accessKey are read from BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY
framework: testng
app: BrowserStack Sample App
platforms:
  - platformName: android
    deviceName: Samsung Galaxy S23
    osVersion: 13.0
projectName: Sample Java App Run
buildName: java-quickstart-${BUILD_TS}
debug: true
networkLogs: true
YMLEOF
fi
```

**For iOS** — same check for `testng-appium-app-browserstack/ios/testng-examples/browserstack.yml`:
```bash
YML_PATH="testng-appium-app-browserstack/ios/testng-examples/browserstack.yml"
if [ -f "$YML_PATH" ]; then
  sed -i.bak "s/^buildName:.*/buildName: java-ios-quickstart-${BUILD_TS}/" "$YML_PATH"
  echo "Reused existing iOS browserstack.yml — updated buildName to java-ios-quickstart-${BUILD_TS}"
else
  cat > "$YML_PATH" << YMLEOF
# userName and accessKey are read from BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY
framework: testng
app: BrowserStack Sample App
platforms:
  - platformName: ios
    deviceName: iPhone 14
    osVersion: 17
projectName: Sample iOS Java App Run
buildName: java-ios-quickstart-${BUILD_TS}
debug: true
networkLogs: true
YMLEOF
fi
```

### JV-A4. Run the test

**For Android:**
```bash
cd testng-appium-app-browserstack/android/testng-examples
mvn test -P sample-test
```

**For iOS:**
```bash
cd testng-appium-app-browserstack/ios/testng-examples
mvn test -P sample-test
```

### JV-A5. Report outcome
Parse Maven Surefire output for pass/fail counts and extract the direct build URL printed by the SDK:

```
============================================================
BrowserStack App Automate — Run Complete
------------------------------------------------------------
Result    : <Tests run: X, Failures: Y, Errors: Z — from Surefire output>
Device    : Samsung Galaxy S23 · Android 13
Build     : java-quickstart-<BUILD_TS>
Dashboard : https://app-automate.browserstack.com/dashboard/v2/builds/<id>
============================================================
```

Extract the URL from SDK stdout with:
`grep -oE 'https://app-automate\.browserstack\.com/dashboard[^ ]+'`

---

## PATH B: Integrate User's Own App and Tests

**Trigger:** User has a Java/Maven project with TestNG tests and their own APK/IPA.

If the user has not already provided both, ask ONE question:
> "Please share: (1) the path to your APK/IPA and (2) your test directory or Maven module. Which devices do you want to target?"

Once you have that information, show your plan and wait for the user's approval (see Plan and approval). After approval, execute the full sequence below **without asking for further confirmation at each step**. Report a single summary at the end.

### Automatic sequence (runs end-to-end)

**Step 1 — Inspect the project**
Run silently using your shell and file-reading tools. Do not ask the user before doing this.

```bash
find . -name "*.java" | xargs grep -l \
  "AppiumDriver\|AndroidDriver\|IOSDriver\|AppiumOptions" 2>/dev/null
grep -rn "MobileCapabilityType.APP\|\"app\"\|localhost:4723\|DesiredCapabilities\|new URL" \
  . --include="*.java"
grep -A3 -i "appium\|browserstack" pom.xml
grep -rn "@Before\|new AppiumDriver\|new AndroidDriver\|new IOSDriver" . --include="*.java"
find . -name "*.xml" | xargs grep -l "parallel\|thread-count" 2>/dev/null
# Check if app communicates with internal/localhost URLs (not port 4723 which is Appium server)
grep -rn "localhost\|127\.0\.0\.1\|192\.168\.\|10\.\|172\." . --include="*.java" | grep -viE "4723|//|appium" | head -10
```

Use your file-reading tool on driver-setup classes and apply fixes silently by editing:

| Finding | Fix (apply automatically) |
|---------|--------------------------|
| `app` set in `AppiumOptions` or `DesiredCapabilities` | Remove by editing — `browserstack.yml` owns this |
| `DesiredCapabilities` v1 style | Rewrite to `AppiumOptions` by editing |
| `http://localhost:4723/wd/hub` hardcoded | Leave as-is — SDK rewrites automatically |
| No `@AfterMethod` / `driver.quit()` | Add by editing |
| TestNG XML suite has `parallel` / `thread-count` | Mirror with `parallels:` in `browserstack.yml` |
| `browserstack-java-sdk` already in pom.xml | Skip Step 3 below |
| Internal URL in test/config (localhost, private IP, not port 4723) | Flag: add `browserstackLocal: true` in Step 4 yml, and tell user BrowserStack Local tunnel must be running before the test |

**Step 2 — Upload the app**
```bash
curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
  -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
  -F "file=@/path/to/app.apk" \
  -F "custom_id=UserApp"
```
Parse `app_url` (`bs://...`) from the JSON response.

**Step 3 — Add BrowserStack SDK dependency to pom.xml**
Use Edit to add inside `<dependencies>`:

```xml
<dependency>
    <groupId>com.browserstack</groupId>
    <artifactId>browserstack-java-sdk</artifactId>
    <version>LATEST</version>
    <scope>compile</scope>
</dependency>
```

Do **not** add a Surefire `<argLine>` block. The `browserstack-sdk mvn test` CLI in Step 6 injects the Java agent automatically — adding it manually as well causes an "agent already loaded" failure.

**Step 4 — Write browserstack.yml**
Generate a unique build timestamp first:
```bash
BUILD_TS=$(date +%Y%m%d-%H%M%S)
```

If `browserstack.yml` already exists in the Maven project root (same level as `pom.xml`), **edit it in place** — update only `app` and `buildName` to preserve any multi-device or custom configuration:
```bash
if [ -f "browserstack.yml" ]; then
  sed -i.bak "s|^buildName:.*|buildName: build-${BUILD_TS}|" browserstack.yml
  sed -i "s|^app:.*|app: ${APP_URL}|" browserstack.yml
  echo "Reused existing browserstack.yml — updated app and buildName"
else
  cat > browserstack.yml << YMLEOF
# userName and accessKey are read from BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY
framework: testng
app: ${APP_URL}
platforms:
  - platformName: android
    deviceName: Samsung Galaxy S23
    osVersion: 13.0
projectName: My Java App Tests
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
Use Edit to inject into test classes:

```java
import org.json.JSONObject;
private void markStatus(AppiumDriver driver, String status, String reason) {
    JSONObject obj = new JSONObject();
    JSONObject args = new JSONObject();
    args.put("status", status); args.put("reason", reason);
    obj.put("action", "setSessionStatus"); obj.put("arguments", args);
    ((JavascriptExecutor) driver).executeScript("browserstack_executor: " + obj);
}
```

**Step 6 — Run the tests**
```bash
browserstack-sdk mvn test
```

**Step 7 — Report outcome**
Parse Maven Surefire output for pass/fail counts and extract the direct build URL from SDK stdout, then print:

```
============================================================
BrowserStack App Automate — Run Complete
------------------------------------------------------------
Inspected : <number of files scanned, issues fixed>
Result    : <Tests run: X, Failures: Y, Errors: Z>
Device    : <device · OS from config>
Build     : <build name>
Dashboard : https://app-automate.browserstack.com/dashboard/v2/builds/<id>
============================================================
```

Extract the URL with: `grep -oE 'https://app-automate\.browserstack\.com/dashboard[^ ]+'`

Follow with a plain-language summary of what was inspected and fixed. If a session fails, fix and re-run before reporting. Only pause to ask the user if a decision genuinely cannot be inferred.

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

Always use explicit waits — never `Thread.sleep()`:

```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(20));
MobileElement element = (MobileElement) wait.until(
    ExpectedConditions.visibilityOfElementLocated(
        MobileBy.AccessibilityId("dashboard")));
```

---

## Session Status Reference

```java
import org.json.JSONObject;
JSONObject obj = new JSONObject();
obj.put("action", "setSessionStatus");
JSONObject args = new JSONObject();
args.put("status", "passed");
args.put("reason", "Test passed");
obj.put("arguments", args);
((JavascriptExecutor) driver).executeScript("browserstack_executor: " + obj.toString());
```

---

## browserstack.yml Reference

```yaml
# Preferred: omit userName/accessKey and set BROWSERSTACK_USERNAME / BROWSERSTACK_ACCESS_KEY
# in the environment, so secrets never land in a file that gets committed.

framework: testng

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
| `Thread.sleep(5000)` | `WebDriverWait(driver, Duration.ofSeconds(20))` |
| XPath for everything | `AccessibilityId` first |
| No `@AfterMethod` / `driver.quit()` | Always quit in teardown |
| No test status marking | Always call `setSessionStatus` |
| Hardcoded pixel coordinates | Element-based taps |
| Uploading app on every run | Upload once, reuse `bs://` URL |
| Running `mvn test` directly | Always prefix with `browserstack-sdk` for integration |

---

## Common Errors → Fixes

| Error | Fix |
|-------|-----|
| `ETIMEDOUT` / `hub.browserstack.com` unreachable | Corporate firewall or VPN is blocking outbound HTTPS. Whitelist `*.browserstack.com`. |
| Dashboard URL not in SDK output | Search stdout for `app-automate.browserstack.com/dashboard`. If absent, use `https://app-automate.browserstack.com/dashboard/v2` and find the build by name. |
| `App not found` | Check file path; confirm `.apk`/`.ipa` is valid |
| `Invalid device/OS combination` | Cross-check at browserstack.com/list-of-browsers-and-platforms/app_automate |
| `NoSuchElementException` on real device | Add explicit wait ≥ 20s; switch to AccessibilityId |
| Session shows `Unknown` status | Add `setSessionStatus` executor call; check WDIO service config |
| `browserstackLocal` not connecting | Start BrowserStackLocal binary before running tests: `./BrowserStackLocal --key $BROWSERSTACK_ACCESS_KEY` |
| App can't reach internal server / API during test | Set `browserstackLocal: true` in config and start the BrowserStackLocal binary first |
| Maven build fails with agent config | Verify `browserstack-java-sdk` version in pom.xml matches installed version; do not add `<argLine>` manually |

---

## Quick Reference

| Task | Command |
|------|---------|
| Run Java/Maven suite | `browserstack-sdk mvn test` |
| Upload APK/IPA | `curl -u "U:K" -X POST https://api-cloud.browserstack.com/app-automate/upload -F file=@app.apk` |
| Dashboard | https://app-automate.browserstack.com |
| Capability generator | https://www.browserstack.com/docs/app-automate/capabilities |
| Supported devices | https://www.browserstack.com/list-of-browsers-and-platforms/app_automate |
| Sample repo | https://github.com/browserstack/testng-appium-app-browserstack |
