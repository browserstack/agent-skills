---
name: browserstack-app-automate-appium-javascript
description: |
  Generates and EXECUTES Appium mobile automation scripts in JavaScript (WebdriverIO) on
  BrowserStack App Automate real device cloud (3500+ devices). Use when the user asks to run
  Appium tests on BrowserStack with JavaScript, automate mobile apps using WebdriverIO/WDIO/Node.js,
  set up BrowserStack App Automate, configure wdio.conf.js, upload APK/IPA, or mentions
  BrowserStack, App Automate, real device cloud, bs://, WebdriverIO, WDIO, or @wdio/browserstack-service.
  Trigger keywords include BrowserStack, App Automate, JavaScript, Node.js, WDIO, WebdriverIO,
  run on real device, upload app, wdio.conf.js, BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY.
languages:
  - JavaScript
category: mobile-testing
license: MIT
user-invocable: true
metadata:
  author: BrowserStack
  version: "1.0"
---

# BrowserStack App Automate — Appium JavaScript (WebdriverIO) Skill

You are a senior mobile QA engineer with direct access to the user's shell and filesystem.
You DO NOT output code snippets for the user to copy-paste and run manually.
You USE your shell and file-editing tools to perform every action directly.

## Step 0: Install this skill (do this first, once)

Skip this step if a folder named `browserstack-app-automate-appium-javascript` already exists in your skills folder (for example `.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the project-level folder your agent uses).

1. Shallow-clone the repo at the release tag into a temporary folder:
   ```bash
   TMP=$(mktemp -d) && git clone --depth 1 --branch app-automate-v1.0.0 https://github.com/browserstack/agent-skills.git "$TMP/agent-skills"
   ```
2. Copy `app-automate/appium-javascript` from that clone into your skills folder, naming the destination folder `browserstack-app-automate-appium-javascript`.
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
Mentions Android / APK / Pixel / Samsung?  →  platformName: android
Mentions iOS / iPhone / IPA / iPad?        →  platformName: ios
Both?                                      →  add both capabilities in wdio.conf.js
```

---

## PATH A: Autonomous Sample App Run

**Trigger:** User mentions WebdriverIO, WDIO, or Node.js and wants a quickstart.

This path tests a pre-bundled Wikipedia sample app on a real BrowserStack device. After the user approves your plan (see Plan and approval), execute all steps without asking for confirmation on each one.

### WD-A1. Check prerequisites
```bash
node --version    # must be 20+
npm --version
git --version
```
If any are missing, tell the user what to install and stop.

### WD-A2. Clone the sample repo
```bash
git clone -b tra https://github.com/browserstack/webdriverio-appium-app-browserstack.git
```

### WD-A3. Install dependencies

**For Android:**
```bash
cd webdriverio-appium-app-browserstack/android
npm install
```

**For iOS:**
```bash
cd webdriverio-appium-app-browserstack/ios
npm install
```

### WD-A4. Write the config file

First, generate a unique build timestamp:
```bash
BUILD_TS=$(date +%Y%m%d-%H%M%S)
```

**For Android**, use your file-writing tool to create `webdriverio-appium-app-browserstack/android/examples/run-parallel-test/parallel.conf.js` (substitute actual timestamp for `<BUILD_TS>`):

```javascript
exports.config = {
  user: process.env.BROWSERSTACK_USERNAME,
  key: process.env.BROWSERSTACK_ACCESS_KEY,
  hostname: 'hub.browserstack.com',
  app: 'BrowserStack Sample App',
  specs: ['./examples/**/*.js'],
  capabilities: [{
    'bstack:options': {
      deviceName: 'Samsung Galaxy S23',
      osVersion: '13.0',
      platformName: 'android'
    }
  }],
  services: [['browserstack', {
    testObservabilityOptions: {
      projectName: 'Sample WDIO App Run',
      buildName: 'wdio-quickstart-<BUILD_TS>'
    }
  }]],
  framework: 'mocha',
  mochaOpts: { timeout: 60000 },
  maxInstances: 5
}
```

**For iOS**, use your file-writing tool to create `webdriverio-appium-app-browserstack/ios/examples/run-parallel-test/parallel.conf.js`:

```javascript
exports.config = {
  user: process.env.BROWSERSTACK_USERNAME,
  key: process.env.BROWSERSTACK_ACCESS_KEY,
  hostname: 'hub.browserstack.com',
  app: 'BrowserStack Sample App',
  specs: ['./examples/**/*.js'],
  capabilities: [{
    'bstack:options': {
      deviceName: 'iPhone 14',
      osVersion: '17',
      platformName: 'ios'
    }
  }],
  services: [['browserstack', {
    testObservabilityOptions: {
      projectName: 'Sample WDIO iOS App Run',
      buildName: 'wdio-ios-quickstart-<BUILD_TS>'
    }
  }]],
  framework: 'mocha',
  mochaOpts: { timeout: 60000 },
  maxInstances: 5
}
```

Do not hardcode credentials; the config reads them from the environment.

### WD-A5. Run the test

**For Android:**
```bash
cd webdriverio-appium-app-browserstack/android
npm run test
```

**For iOS:**
```bash
cd webdriverio-appium-app-browserstack/ios
npm run test
```

### WD-A6. Report outcome
Parse WDIO reporter output for pass/fail counts and extract the direct build URL printed by `@wdio/browserstack-service`:

```
============================================================
BrowserStack App Automate — Run Complete
------------------------------------------------------------
Result    : <X passing, Y failing — from WDIO reporter>
Device    : Samsung Galaxy S23 · Android 13
Build     : wdio-quickstart-<BUILD_TS>
Dashboard : https://app-automate.browserstack.com/dashboard/v2/builds/<id>
============================================================
```

Extract the URL from stdout with:
`grep -oE 'https://app-automate\.browserstack\.com/dashboard[^ ]+'`

---

## PATH B: Integrate User's Own App and Tests

**Trigger:** User has an existing WDIO project and their own APK/IPA.

If the user has not already provided both, ask ONE question:
> "Please share: (1) the path to your APK/IPA and (2) your project root directory. Which devices do you want to target?"

Once you have that information, show your plan and wait for the user's approval (see Plan and approval). After approval, execute the full sequence below **without asking for further confirmation at each step**. Report a single summary at the end.

### Automatic sequence (runs end-to-end)

**Step 1 — Inspect the project**
Run silently using your shell and file-reading tools. Do not ask the user before doing this.

```bash
find . -name "wdio.conf.*" -o -name "*.conf.js" | grep -i wdio
grep -n "capabilities\|app\|hostname\|services\|browserstack\|user\|key\|specs" \
  wdio.conf.js 2>/dev/null
cat package.json | grep -E "@wdio|browserstack|appium"
find . -path "*/specs/*.js" -o -path "*/test/*.js" | head -20
# Check if tests reference internal/localhost URLs (not port 4723 which is Appium server)
grep -rn "localhost\|127\.0\.0\.1\|192\.168\.\|10\.\|172\." . --include="*.js" | grep -viE "4723|//|appium|hub\." | head -10
```

Use your file-reading tool on the existing `wdio.conf.js` and apply fixes silently by editing:

| Finding | Fix (apply automatically) |
|---------|--------------------------|
| `app` set inside capabilities or at top level | Replace with `bs://` URL (set in service config, not capabilities) |
| `hostname` pointing at localhost or local Appium hub | Replace with `hub.browserstack.com` |
| `@wdio/browserstack-service` already in `services` | Skip Step 2 install; update service config block only |
| Flat capabilities (not `bstack:options`) | Migrate device fields into `bstack:options` by editing |
| `skipSessionStatus: true` in service config | Remove it — auto-marking is the default |
| Non-standard `specs` path | Preserve exact path in updated config |
| Internal URL in test/spec files (localhost, private IP, not port 4723) | Flag: set `browserstackLocal: true` in wdio.conf.js service config (Step 4), and tell user BrowserStack Local tunnel must be running before the test |

**Step 2 — Upload the app**
```bash
curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
  -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
  -F "file=@/path/to/app.apk" \
  -F "custom_id=UserApp"
```
Parse `app_url` (`bs://...`) from the JSON response.

**Step 3 — Install BrowserStack service (if not present)**
```bash
npm install @wdio/browserstack-service --save-dev
```

**Step 4 — Write/update wdio.conf.js**
Generate a unique build timestamp first:
```bash
BUILD_TS=$(date +%Y%m%d-%H%M%S)
```

If `wdio.conf.js` already exists (Step 1 found it), **edit it in place** — use your file-editing tool to update only `app`, `buildName`, and device fields while preserving all other settings. Only write a new file if none exists.

Set `deviceName`, `osVersion`, and `platformName` in `bstack:options` based on the user's target. Android example — for iOS replace with `deviceName: 'iPhone 14'`, `osVersion: '17'`, `platformName: 'ios'` (substitute actual timestamp for `<BUILD_TS>`):

```javascript
exports.config = {
  user: process.env.BROWSERSTACK_USERNAME,
  key: process.env.BROWSERSTACK_ACCESS_KEY,
  hostname: 'hub.browserstack.com',
  app: '<bs://app_url_from_upload>',
  capabilities: [{
    'bstack:options': {
      deviceName: 'Samsung Galaxy S23',
      osVersion: '13.0',
      platformName: 'android'
    }
  }],
  services: [['browserstack', {
    browserstackLocal: false,   // set to true if Step 1 detected internal URLs
    testObservabilityOptions: {
      projectName: 'My WDIO App Tests',
      buildName: 'build-<BUILD_TS>'
    }
  }]],
  framework: 'mocha',
  mochaOpts: { timeout: 60000 },
  maxInstances: 10,
  specs: ['./test/specs/**/*.js']   // preserve original path
}
```

If Step 1 detected internal/localhost URLs in the spec files, change `browserstackLocal: false` → `browserstackLocal: true` and notify the user:
> "Your tests reference an internal URL. I've enabled BrowserStack Local in the config. Before running, start the BrowserStack Local binary: `./BrowserStackLocal --key $BROWSERSTACK_ACCESS_KEY`"

Note: `@wdio/browserstack-service` marks session status automatically from spec names. No `executeScript` needed.

**Step 5 — Run the tests**
```bash
npx wdio run wdio.conf.js
```

**Step 6 — Report outcome**
Parse WDIO reporter output for pass/fail counts and extract the direct build URL from `@wdio/browserstack-service` stdout, then print:

```
============================================================
BrowserStack App Automate — Run Complete
------------------------------------------------------------
Inspected : <number of files scanned, issues fixed>
Result    : <X passing, Y failing — from WDIO reporter>
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

1. `$('~accessibilityId')` — cross-platform, most stable
2. `$('android=new UiSelector().text("Login")')` — Android UiAutomator
3. `$('-ios predicate string:label == "Login"')` — iOS predicate
4. `$('-ios class chain:**/XCUIElementTypeButton[`label == "Login"`]')` — iOS class chain
5. XPath — last resort only

---

## Wait Strategy

Use `waitForDisplayed` or `waitUntil` — never `browser.pause()`:

```javascript
const element = $('~dashboard');
element.waitForDisplayed({ timeout: 20000 });  // 20s minimum for real devices
```

---

## Session Status

`@wdio/browserstack-service` marks session status **automatically** from spec names. No `executeScript` needed.

---

## Anti-Patterns (never generate these)

| Bad | Good |
|-----|------|
| `browser.pause(5000)` | `element.waitForDisplayed({ timeout: 20000 })` |
| XPath for everything | `$('~accessibilityId')` first |
| Hardcoded credentials in config | Read from `process.env.BROWSERSTACK_USERNAME` |
| `app` set directly in capabilities | Set via service config or `bs://` URL |
| Uploading app on every run | Upload once, reuse `bs://` URL |

---

## Common Errors → Fixes

| Error | Fix |
|-------|-----|
| `ETIMEDOUT` / `hub.browserstack.com` unreachable | Corporate firewall or VPN is blocking outbound HTTPS. Whitelist `*.browserstack.com`. |
| Dashboard URL not in output | Search stdout for `app-automate.browserstack.com/dashboard`. If absent, use `https://app-automate.browserstack.com/dashboard/v2` and find the build by name. |
| `App not found` | Check file path; confirm `.apk`/`.ipa` is valid |
| `Invalid device/OS combination` | Cross-check at browserstack.com/list-of-browsers-and-platforms/app_automate |
| Session shows `Unknown` status | Check `@wdio/browserstack-service` is listed in `services`; remove `skipSessionStatus: true` if present |
| `browserstackLocal` not connecting | Start BrowserStackLocal binary before running tests: `./BrowserStackLocal --key $BROWSERSTACK_ACCESS_KEY` |
| App can't reach internal server / API during test | Set `browserstackLocal: true` in config and start the BrowserStackLocal binary first |
| `Cannot find module '@wdio/browserstack-service'` | Run `npm install @wdio/browserstack-service --save-dev` |

---

## Quick Reference

| Task | Command |
|------|---------|
| Install WDIO BrowserStack service | `npm install @wdio/browserstack-service --save-dev` |
| Run WDIO suite | `npx wdio run wdio.conf.js` |
| Upload APK/IPA | `curl -u "U:K" -X POST https://api-cloud.browserstack.com/app-automate/upload -F file=@app.apk` |
| Dashboard | https://app-automate.browserstack.com |
| Capability generator | https://www.browserstack.com/docs/app-automate/capabilities |
| Supported devices | https://www.browserstack.com/list-of-browsers-and-platforms/app_automate |
| Sample repo | https://github.com/browserstack/webdriverio-appium-app-browserstack (branch: tra) |
