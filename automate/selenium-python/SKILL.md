---
name: browserstack-automate-selenium-python
description: >-
  Runs Selenium tests written in Python on BrowserStack Automate (real desktop browsers and real mobile devices)
  from one pasted prompt: either BrowserStack's official Selenium Python sample build, or the user's own
  Selenium Python tests with no changes to their test logic. Checks credentials without printing them,
  shows a plan and waits for approval, runs the build, confirms it on the BrowserStack API and
  returns the dashboard link. Use when the user asks to run Selenium Python tests on BrowserStack, set up
  BrowserStack Automate for a Selenium Python project, or mentions Selenium with Python, pytest, unittest, behave, browserstack-sdk or browserstack.yml. Not for other languages
  or frameworks: it names the right skill instead.
languages:
  - Python
category: e2e-testing
license: MIT
user-invocable: true
metadata:
  author: BrowserStack
  version: "1.0"
---

<!-- Generated from automate/_source by build.py. Edit the source, not this file. -->

# BrowserStack Automate — Selenium Python skill

You are a senior QA automation engineer with access to the user's shell and files. Do the work
yourself (clone, install, edit, run) instead of handing commands to the user, but only after the
user approves your plan.

## Step 0: Install this skill (do this first, once)

Skip this step if `browserstack-automate-selenium-python/SKILL.md` already exists in your skills folder (for example
`.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the
project-level folder your agent uses).

1. Create the folder `browserstack-automate-selenium-python` in your skills folder.
2. Download this file into it as `SKILL.md`:
   ```bash
   mkdir -p "<skills-folder>/browserstack-automate-selenium-python" && curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-python/SKILL.md -o "<skills-folder>/browserstack-automate-selenium-python/SKILL.md"
   ```
   Replace `<skills-folder>` with your agent's project-level skills folder. The skill stays
   installed for future sessions.
3. Tell the user in one line that the skill is installed, then continue in this session. Do not
   ask them to restart.

To update the skill later, delete the folder and run the prompt again. If the network or the
skills folder is unavailable, say so in one line and carry on using this file for this session
only. Installing is a convenience; never block the run on it.

## Is this the right skill? (check before anything else)

Look at the folder the user is in (read-only). This skill is for **Selenium Python**: `requirements.txt`, `pyproject.toml` or `.py` tests that import `selenium`.

- Empty folder, or the user asked for the sample build → right skill, continue.
- A Selenium Python project → right skill, continue.
- A project in another language or framework → stop. Tell the user in one line what you found and
  that this skill is for Selenium Python, then give them the prompt for the right skill:

  - **Selenium Java** (`pom.xml` or `build.gradle` that depends on `selenium-java`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-java/SKILL.md, then follow that skill to run my own Selenium Java tests on BrowserStack Automate.`
  - **Selenium JavaScript** (`package.json` that depends on `selenium-webdriver` (Mocha or Jest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-javascript/SKILL.md, then follow that skill to run my own Selenium JavaScript tests on BrowserStack Automate.`
  - **Playwright JavaScript** (`package.json` that depends on `@playwright/test` (JavaScript or TypeScript)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-javascript/SKILL.md, then follow that skill to run my own Playwright JavaScript tests on BrowserStack Automate.`

  For anything else (C#, Ruby, PHP, WebdriverIO, Nightwatch, Cypress, Playwright with Python, Java
  or C#) there is no skill yet: point the user to https://www.browserstack.com/docs/automate and stop.
- A mixed project (for example Java and Python tests): work only on the Selenium Python part, and name the
  skill that covers the rest.

## Ground rules

- **Credentials come from `$BROWSERSTACK_USERNAME` and `$BROWSERSTACK_ACCESS_KEY` only.** Never ask
  the user to paste the access key into the chat, never print it, never write it into a file.
- **The SDK itself can write the key to disk.** It has been seen in `log/sdk-cli-debug.log` inside
  the project, so any project you wire for BrowserStack must list `log/` in `.gitignore`. Before you
  quote any SDK output or log, mask the key: `sed "s/$BROWSERSTACK_ACCESS_KEY/<ACCESS_KEY>/g"`.
- **Never write a test yourself.** The sample build uses BrowserStack's official sample repo; the
  other path runs the user's own tests.
- **Never commit, push or open a pull request.** Leave changes in the working tree for the user.
- **Stay in scope:** BrowserStack wiring and the fixes listed in this skill. Don't refactor app code.
- **Data:** a cloud run uploads the page URL, page content and a session video to BrowserStack.
  For a private or internal app, use BrowserStack Local and say so in your plan.

## Plan and approval (before you change anything)

1. **Check credentials without printing them:**
   ```bash
   [ -n "$BROWSERSTACK_USERNAME" ] && [ -n "$BROWSERSTACK_ACCESS_KEY" ] && echo "credentials set" || echo "credentials missing"
   ```
   If they are missing, ask the user to export both variables in their shell and run the prompt
   again, then stop.
2. **Read-only checks (no approval needed):**
   - Toolchain: `python3 --version` (3.8+), `git --version`. If something is missing, say what to install and stop. Never
     install system tools yourself.
   - Free parallel sessions:
     ```bash
     curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" https://api.browserstack.com/automate/plan.json
     ```
     Free = the smaller of `parallel_sessions_max_allowed` and `team_parallel_sessions_max_allowed`,
     minus `parallel_sessions_running`. If it is lower than the number of platforms, trim the plan or
     say the run will queue.
   - For your own tests: the project assessment in Path B, step B1.
3. **Ask only what you still need, in one message.** The sample build usually needs nothing. For
   your own tests, ask only if it is unclear which tests to run.
4. **Show a short plan and wait for the user's OK.** List what you will clone, install or create,
   every existing file you will change (with the diff), the browsers and devices with the session
   count, the folder you will work in, and the command you will run. In the same message, invite
   changes: "Reply OK to start, or tell me which browsers or devices to change."
5. **After approval, run end to end** without asking again at each step, then report once.

## Which path?

- The prompt says **"sample build"**, or the folder has no Selenium Python tests → **Path A: sample build**.
- The prompt says **"my own Selenium Python tests"**, or the folder has Selenium Python tests → **Path B: your own tests**.
  If the user asked for their own tests but you find none, say so, offer the sample build and stop.

## Path A: sample build

This runs BrowserStack's official Selenium Python sample (`browserstack/python-selenium-browserstack`, branch
`main`), the same one the BrowserStack docs use, on the platforms it ships with.

### A1. Prerequisites

```bash
python3 --version   # 3.8 or newer
git --version
```
If either is missing, tell the user what to install and stop.

### A2. Clone the official sample into a new folder

```bash
git clone -b main https://github.com/browserstack/python-selenium-browserstack.git
cd python-selenium-browserstack
```

If `python-selenium-browserstack` already exists, clone into `python-selenium-browserstack-$(date +%Y%m%d-%H%M%S)` instead.
Never overwrite a folder the user may have changed.

### A3. Point `browserstack.yml` at this run

Change only these, and leave everything else as BrowserStack ships it:

```bash
BUILD_NAME="bsk-automate-selenium-python-sample-$(date +%Y%m%d-%H%M%S)"
sed -i.bak -e "s/^buildName:.*/buildName: ${BUILD_NAME}/" \
           -e "s/^browserstackLocal:.*/browserstackLocal: false/" browserstack.yml && rm -f browserstack.yml.bak
```

- **`buildName`** gets a unique name, so the API check below finds exactly this run. Keep the
  `bsk-` prefix: it marks builds started by a skill.
- **`browserstackLocal: false`**: the sample tests a public site, and the Local tunnel is only
  needed for private apps (its binary can also fail to start, which drops every session).
- **Credentials:** leave the `userName`/`accessKey` placeholders alone. The environment variables
  take precedence. Never write real credentials into the file.
- **Real devices** in the file can be retired over time. If it lists any, check them against the
  live catalog and swap a stale one for the closest current device (same OS family), noting it in
  your report:
  ```bash
  curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" https://api.browserstack.com/automate/browsers.json \
    | python3 -c "import sys,json; d=json.load(sys.stdin); print(sorted({(b['device'],b['os_version']) for b in d if b.get('device')}))"
  ```

### A4. Install and run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt   # includes the current BrowserStack SDK from BrowserStack's server
.venv/bin/browserstack-sdk ./tests/test.py
```

On Windows use `.venv\Scripts\pip` and `.venv\Scripts\browserstack-sdk`. The SDK runs
`tests/test.py` (adds a product to the cart on bstackdemo.com and checks it is there) on every
platform in `browserstack.yml`, in parallel, and the test reports its own pass/fail to BrowserStack.

Then go to **Confirm the run on BrowserStack** and **Report**.

## Path B: your own tests

Run the user's existing Selenium Python tests on BrowserStack with no changes to their test logic.

### B1. Assess the project (read-only, before your plan)

Note these in a short Assessment block at the top of your plan:

- **Test runner:** pytest (`conftest.py`, `pytest.ini`, `test_*.py`), unittest, behave, or plain scripts.
- **Dependencies:** `requirements.txt` or `pyproject.toml`, and the Selenium version (4.x is required).
- **Framework clash:** if `playwright` or `pytest-playwright` is installed or listed, the SDK may
  patch Playwright instead of Selenium and the tests silently run on the local machine. Use a
  separate virtual environment with only the Selenium stack (B2).
- **How the driver is created:** `webdriver.Chrome()` and similar are intercepted by the SDK. If a
  helper builds the driver some other way, check after the run that sessions appear on the API.
- **`maximize_window()` calls:** real Android phones reject them, so they matter only if the plan
  includes phones.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test, pick the test whose name is the nearest step in that flow, and if two are equally close,
  the first by file path. State the pick and why.

### B2. Changes to put in your plan (each one shown as a diff)

1. **A virtual environment with only the Selenium stack** (a new folder, `.venv`): the user's own
   `selenium` and test-runner versions plus the current BrowserStack SDK from BrowserStack's server.
   PyPI's `browserstack-sdk` lags well behind, so don't install it from there:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install "selenium==<their version>" "pytest==<their version>" \
     https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz
   .venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"
   ```
2. **Pin the SDK by URL in `requirements.txt`** (diff), so the next install gets the same version
   (`browserstack-sdk==<version>` doesn't exist on PyPI):
   ```
   browserstack-sdk @ https://sdk-assets.browserstack.com/python/browserstack_sdk-<version>.tar.gz
   ```
3. **Don't run `browserstack-sdk setup`**: it writes `browserstack.yml` with the credentials inline.
   Use the file below instead.
4. **`maximize_window()` on real phones** (only if the plan includes phones): run it on desktop only:
   ```python
   if str(driver.capabilities.get("platformName", "")).lower() not in ("android", "ios"):
       driver.maximize_window()
   ```

Add a `browserstack.yml` next to the project's build file (a new file, so no diff needed). By
default it runs on Windows 11 Chrome, macOS Sequoia Safari, a real Samsung Galaxy S23 (Chrome) and a real iPhone 15 (Safari); the user can change this when approving the plan:

```yaml
# userName and accessKey are read from BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY
platforms:
  - os: Windows
    osVersion: 11
    browserName: chrome
    browserVersion: latest
  - os: OS X
    osVersion: Sequoia
    browserName: safari
    browserVersion: latest
  - deviceName: Samsung Galaxy S23
    osVersion: 13.0
    browserName: chrome
  - deviceName: iPhone 15
    osVersion: 17
    browserName: safari
parallelsPerPlatform: 1
projectName: My Selenium Python Tests
buildName: bsk-automate-selenium-python-<timestamp>   # unique per run; keep the bsk- prefix
buildIdentifier: '#${BUILD_NUMBER}'
browserstackLocal: false   # true only for localhost, staging or a private app
debug: true
networkLogs: true
consoleLogs: info
testObservability: true
```

Check the real-device rows against the live catalog as in step A3, and set `browserstackLocal: true`
only when the tests open `localhost`, a private IP or a staging host (say so in the plan; the SDK
starts the tunnel itself).

Add `log/` to the project's `.gitignore` (create the file if needed) in the same diff.

### B3. Run

- **pytest:** `.venv/bin/browserstack-sdk pytest <tests>` (never bare `pytest`).
- **unittest:** `.venv/bin/browserstack-sdk python -m unittest <module>`.
- **behave:** `.venv/bin/browserstack-sdk behave`.
- **Plain script:** `.venv/bin/browserstack-sdk python <script>.py`.

These lines also appear on genuine BrowserStack runs and are harmless: `[SDKCLI][ERROR] - Failed
to patch pytest selenium … No module named 'pytest_selenium'`, `failed to setup playwright: No
module named 'playwright'`, "Please install pytest-selenium package", and Selenium's
`DeprecationWarning: setting remote_server_addr …`. Don't install packages to silence them.

Then go to **Confirm the run on BrowserStack** and **Report**.

## Confirm the run on BrowserStack

The test runner's "passed" and the dashboard link the SDK prints are **not proof**: the SDK can
print a link when no session was created. Check the BrowserStack API yourself:

```bash
BUILD_NAME="<the buildName you set>"
curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" "https://api.browserstack.com/automate/builds.json?limit=100" \
  | python3 -c "import sys,json; n=sys.argv[1]; [print(b['automation_build']['hashed_id'], b['automation_build']['name']) for b in json.load(sys.stdin) if b['automation_build']['name'].startswith(n)]" "$BUILD_NAME"
curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" "https://api.browserstack.com/automate/builds/<hashed_id>/sessions.json" \
  | python3 -c "import sys,json; [print(s['automation_session'].get('os'), s['automation_session'].get('browser') or '', s['automation_session'].get('device') or '', '|', s['automation_session']['status'], '|', s['automation_session'].get('name')) for s in json.load(sys.stdin)]"
```

- Match the build by **prefix**: the SDK appends an identifier, so `bsk-…-0930` shows up as
  `bsk-…-0930  1`. Ask for `limit=100`, since a busy account fills the default 10 within minutes.
- **No matching build, or 0 sessions** → the tests did not reach BrowserStack. Read the SDK's own
  logs in the project's `log/` folder (mask the key first) before guessing; then see Troubleshooting.
- **Each session's `status`:** `passed` or `failed` means the result reached the dashboard.
  **`done` means the session ran but nobody reported pass or fail**: never report it as a pass.
  - pytest sessions are marked and named by the SDK. Plain scripts and unittest may not be: if
    their sessions show `done`, mark them from the runner's result as shown below. (The official
    sample reports its own status.)
- To mark a session yourself from the test runner's own result (use the assertion message as the
  reason for a failure, and say in your report that you marked it):
  ```bash
  curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" -X PUT -H "Content-Type: application/json" \
    -d '{"status":"passed","reason":"Marked from the test runner result"}' \
    "https://api.browserstack.com/automate/sessions/<session_hashed_id>.json"
  ```
  Only do this when you can tell which test result belongs to which session (for example one test
  per platform). Otherwise report the runner's result and explain that the dashboard shows `done`.

## Report

Print one summary block, then one line on what the test does and where it came from:

```
============================================================
BrowserStack Automate — Run Complete
------------------------------------------------------------
Ran       : [Sample build: browserstack/python-selenium-browserstack] or [Your tests: <path>]
Result    : <N> of <M> sessions passed (from the BrowserStack API)
Platforms : <browser · OS — passed/failed, one per line>
Build     : <build name>
Dashboard : https://automate.browserstack.com/dashboard/v2/builds/<hashed_id>
============================================================
```

Each session on the dashboard has its video, text logs, network logs and console logs.

## What I can do next

After a successful run, offer three or four of these, one line each, then wait for the user's
answer (extra sessions and devices use plan minutes):

- **Run faster:** "Your plan allows N parallel sessions and M are free. I can set
  `parallelsPerPlatform: K` so a full suite finishes up to K× faster." K = max(1, ⌊free ÷
  platforms⌋), no higher than the number of tests. After a one-test run, frame it for their full suite.
- **Wider coverage:** add browsers, OS versions or real devices (for example Firefox, an older
  Safari, a Pixel or an iPad).
- **Your own app:** after the sample build, run their own Selenium Python tests; for localhost or staging,
  turn on BrowserStack Local.
- **On every push:** add a CI job (GitHub Actions, Jenkins, GitLab) that runs this on BrowserStack.

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| Tests pass locally but the API shows no build | The run did not go through the BrowserStack SDK. Check the run command and wiring below, and read `log/sdk-cli.log` (mask the key) |
| Every session fails to start with `[browserstack.local] is set to true but local testing through BrowserStack is not connected` | The Local binary could not start (in `log/sdk-cli.log`: `Local.start … spawn …`; error `-86` = an Intel binary on Apple silicon without Rosetta). Public site → `browserstackLocal: false`. Private app → ask the user before installing Rosetta or a native binary |
| `All parallel tests are currently in use` | The plan's parallel limit is reached; lower `parallelsPerPlatform` or wait |
| `Browser/OS combination not supported` | A retired device or OS version: re-check the catalog (step A3), swap to the closest current one and re-run once |
| Session fails to start with a connect timeout while parallels are free | Usually transient: re-run once. If it repeats, the network may block `*.browserstack.com` (allow outbound HTTPS) |
| Logs show `unpatched method: new_page/launch/connect`; a browser opens locally | The SDK patched Playwright instead of Selenium: use a virtual environment without `playwright`/`pytest-playwright` (B2, step 1) |
| Old SDK behaviour, or `pip` installs `browserstack-sdk` 1.51.x | PyPI's copy is stale: install from `https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz` |
| Android: `Unable to maximize window` | `maximize_window()` on a real phone: guard it as in B2, step 4 |
| `browserstack-sdk: command not found` | Use the virtual environment's copy: `.venv/bin/browserstack-sdk` |

## Quick reference

| Task | Command |
| --- | --- |
| Sample build | `git clone -b main https://github.com/browserstack/python-selenium-browserstack.git && cd python-selenium-browserstack && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt && .venv/bin/browserstack-sdk ./tests/test.py` |
| Your tests (pytest) | `.venv/bin/browserstack-sdk pytest tests/` |
| Install the current SDK | `pip install https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz` |
| SDK version installed | `python -c "import browserstack_sdk._version as v; print(v.__version__)"` |
| Docs | https://www.browserstack.com/docs/automate/selenium/getting-started/python |
