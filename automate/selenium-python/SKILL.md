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

## Step 1: Is this the right skill? (before anything else)

Look at the folder the user is in and its subfolders (read-only). This skill is for
**Selenium Python**: `requirements.txt`, `pyproject.toml` or `.py` tests that import `selenium`.

- Empty folder, or the user asked for the sample build → right skill, continue.
- A Selenium Python project → right skill, continue.
- A project in another language or framework → stop without changing anything. If you already
  saved this skill into the project's skills folder, remove that folder again. Tell the user in one
  line what you found and that this skill is for Selenium Python, then give them the prompt for the right
  skill:

  - **Selenium Java** (`pom.xml` or `build.gradle` that depends on `selenium-java`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-java/SKILL.md, then follow that skill to run my own Selenium Java tests on BrowserStack Automate.`
  - **Selenium JavaScript** (`package.json` that depends on `selenium-webdriver` (Mocha or Jest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-javascript/SKILL.md, then follow that skill to run my own Selenium JavaScript tests on BrowserStack Automate.`
  - **Selenium C#** (a `.csproj` that references `Selenium.WebDriver` (NUnit, xUnit or MSTest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-csharp/SKILL.md, then follow that skill to run my own Selenium C# tests on BrowserStack Automate.`
  - **Playwright JavaScript** (`package.json` that depends on `@playwright/test` (JavaScript or TypeScript)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-javascript/SKILL.md, then follow that skill to run my own Playwright JavaScript tests on BrowserStack Automate.`
  - **Playwright Python** (`requirements.txt` or `pyproject.toml` with `playwright` or `pytest-playwright`, or `.py` tests that import `playwright`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-python/SKILL.md, then follow that skill to run my own Playwright Python tests on BrowserStack Automate.`
  - **Playwright Java** (`pom.xml` or `build.gradle` that depends on `com.microsoft.playwright`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-java/SKILL.md, then follow that skill to run my own Playwright Java tests on BrowserStack Automate.`
  - **Playwright C#** (a `.csproj` that references `Microsoft.Playwright` (NUnit, MSTest or xUnit)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-csharp/SKILL.md, then follow that skill to run my own Playwright C# tests on BrowserStack Automate.`

  For anything else (Ruby, PHP, WebdriverIO, Nightwatch or Cypress) there is no skill yet: point
  the user to https://www.browserstack.com/docs/automate and stop.
- A mixed project (for example Java and Python tests): work only on the Selenium Python part, and name the
  skill that covers the rest.

## Step 2: Install this skill (once)

Skip this step if `browserstack-automate-selenium-python/SKILL.md` already exists in your skills folder (for example
`.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the
project-level folder your agent uses).

1. Create the folder `browserstack-automate-selenium-python` in your skills folder and download this file into it as `SKILL.md`:
   ```bash
   mkdir -p "<skills-folder>/browserstack-automate-selenium-python" && curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-python/SKILL.md -o "<skills-folder>/browserstack-automate-selenium-python/SKILL.md" || rmdir "<skills-folder>/browserstack-automate-selenium-python"
   ```
   Replace `<skills-folder>` with your agent's project-level skills folder. The skill stays
   installed for future sessions.
2. Tell the user in one line that the skill is installed, then continue in this session. Do not
   ask them to restart.

If the download fails for any reason (no network, an HTTP error such as 404, or no writable
skills folder), say so in one line and carry on using this file for this session only. Installing
is a convenience; never block the run on it. To update the skill later, delete the folder and run
the prompt again.

## Ground rules

- **Credentials come from `$BROWSERSTACK_USERNAME` and `$BROWSERSTACK_ACCESS_KEY` only.** Never ask
  the user to paste the access key into the chat, never print it, never write it into a file.
- **The SDK itself can write the key to disk.** It has been seen in `log/sdk-cli-debug.log` inside
  the project, so any project you run on BrowserStack must list `log/` in `.gitignore`. Before you
  quote any SDK output or log, mask the key: `sed "s/$BROWSERSTACK_ACCESS_KEY/<ACCESS_KEY>/g"`.
- **Never write a test yourself.** The sample build uses BrowserStack's official sample repo; the
  other path runs the user's own tests.
- **Never commit, push or open a pull request.** Leave changes in the working tree for the user.
- **Stay in scope:** BrowserStack wiring and the fixes listed in this skill. Don't refactor app code.
- **Never install system software** (runtimes, Rosetta, browsers, build tools). Tell the user what
  to install and stop. Project-local packages (a virtual environment, `node_modules`, Maven or
  NuGet dependencies) are fine.
- **Data:** a cloud run uploads the page URL, page content and a session video to BrowserStack.
  For a private or internal app, use BrowserStack Local and say so in your plan.

## Plan and approval (before you change anything)

1. **Check credentials without printing them:**
   ```bash
   [ -n "$BROWSERSTACK_USERNAME" ] && [ -n "$BROWSERSTACK_ACCESS_KEY" ] && echo "credentials set" || echo "credentials missing"
   ```
   If they are missing, ask the user to export both variables in their shell (both are on
   https://www.browserstack.com/accounts/settings) and run the prompt again, then stop.
2. **Read-only checks (no approval needed):**
   - Toolchain: `python3 --version` (3.8+), `git --version`. If something is missing, say what to install and stop.
   - Free parallel sessions:
     ```bash
     curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" https://api.browserstack.com/automate/plan.json
     ```
     Free = the smaller of `parallel_sessions_max_allowed` and `team_parallel_sessions_max_allowed`,
     minus `parallel_sessions_running`. If it is lower than the number of platforms, trim the plan or
     say the run will queue.
   - For the sample build: read the platforms it ships with, without cloning yet, and check any real
     devices against the live catalog (step A3):
     ```bash
     curl -fsSL https://raw.githubusercontent.com/browserstack/python-selenium-browserstack/main/browserstack.yml
     ```
   - For your own tests: the project assessment in Path B, step B1.
3. **Ask only what you still need, in one message.** The sample build usually needs nothing. For
   your own tests, ask only if it is unclear which tests to run.
4. **Show a short plan and wait for the user's OK.** List what you will clone, install or create,
   every existing file you will change (with the diff) and any file the install itself updates,
   the browsers and devices with the session count, the folder you will work in, and the command
   you will run. In the same message, invite changes: "Reply OK to start, or tell me which
   browsers or devices to change."
5. **After approval, run end to end** without asking again at each step, then report once. If the
   user asked you to set things up without running, stop after the changes, give them the run
   command and the build name it will use, and don't run anything.

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

Change only these two lines of `browserstack.yml`, and leave the rest as BrowserStack ships it:

```bash
BUILD_NAME="bsk-automate-selenium-python-sample-$(date +%Y%m%d-%H%M%S)"
sed -i.bak -e "s/^buildName:.*/buildName: ${BUILD_NAME}/" \
           -e "s/^browserstackLocal:.*/browserstackLocal: false/" browserstack.yml && rm -f browserstack.yml.bak
grep -qxF 'log/' .gitignore 2>/dev/null || echo 'log/' >> .gitignore
```

- **`buildName`** gets a unique name, so the API check below finds exactly this run. Keep the
  `bsk-` prefix: it marks builds started by a skill.
- **`browserstackLocal: false`**: the sample tests a public site, and the Local tunnel is only
  needed for private apps (its binary can also fail to start, which drops every session).
- **`log/` in `.gitignore`**: the SDK writes its logs there, sometimes with the access key.
- **Credentials:** leave the `userName`/`accessKey` placeholders alone. The environment variables
  take precedence. Never write real credentials into the file.
- **Real devices** in the file can be retired over time. You checked them before the plan; if one
  was stale, swap it for the closest current device (same OS family) as your plan said:
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
The run prints little. `TestClient: Failed to mark session status: 'sessionId'` and a Test
Observability "not supported" message are harmless: the API check shows the real result.

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
   The plan can show this line with `<version>` until the install reveals it. If `requirements.txt`
   also lists `playwright` or `pytest-playwright`, say in the report that a full `pip install -r requirements.txt`
   brings the clash back, and offer a lasting fix: a separate `requirements-browserstack.txt`
   with only this stack.
3. **Don't run `browserstack-sdk setup`**: it writes `browserstack.yml` with the credentials inline.
   Use the file below instead.
4. **`maximize_window()` on real phones** (only if the plan includes phones): run it on desktop only:
   ```python
   if str(driver.capabilities.get("platformName", "")).lower() not in ("android", "ios"):
       driver.maximize_window()
   ```

Add a `browserstack.yml` next to the build file of the project or module whose tests run (in a
multi-module repo, that module, not the parent). If the project already has BrowserStack wiring
(a `browserstack.yml`, an SDK dependency, an SDK agent), update it in place and show the diff
instead of adding a second copy. By default the file runs on Windows 11 Chrome, macOS Sequoia Safari, a real Samsung Galaxy S23 (Chrome) and a real iPhone 15 (Safari); the user
can change this when approving the plan:

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

Check the real-device rows against the live catalog as in step A3. Add `log/` to the project's
`.gitignore` (create the file if needed) in the same diff, as a plain `log/` line so it also
covers a module's `log/` folder.

**Private apps (BrowserStack Local).** Set `browserstackLocal: true` only when the tests open
`localhost`, a private IP or a staging host, and say so in the plan (the SDK starts the tunnel
itself). Before the run, check both of these and put any problem in the plan instead of running:
- The app answers on this machine, for example `curl -sI http://localhost:3000 | head -1`. If it
  doesn't, ask the user to start it.
- On a Mac with Apple silicon, the Local binary the SDK uses may be an Intel build that needs
  Rosetta. `[ "$(uname -m)" = arm64 ] && ! arch -x86_64 /usr/bin/true 2>/dev/null && echo "no Rosetta"`
  prints `no Rosetta` when it would fail to start (error `-86`). Ask the user to install Rosetta
  (`softwareupdate --install-rosetta`) themselves, then run the prompt again.

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
  `bsk-…-0930  1` (the number varies). Ask for `limit=100`, since a busy account fills the
  default 10 within minutes.
- **No matching build, or 0 sessions** → the tests did not reach BrowserStack. Read the SDK's own
  logs in the `log/` folder next to `browserstack.yml` (mask the key first) before guessing; then
  see Troubleshooting. Report what stopped the run and the fix, without a dashboard link.
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
  Only do this when you can tell which test result belongs to which session (one test per
  platform, or session names that carry the test name). Otherwise report the runner's result and
  explain that the dashboard shows `done`.

## Report

Print one summary block, then one line on what the tests do and where they came from:

```
============================================================
BrowserStack Automate — Run Complete
------------------------------------------------------------
Ran       : [Sample build: browserstack/python-selenium-browserstack] or [Your tests: <path>]
Result    : <N> of <M> sessions passed (from the BrowserStack API)
Platforms : <browser · OS — passed/failed, one per line; with several tests per platform, passed of total>
Build     : <build name>
Dashboard : https://automate.browserstack.com/dashboard/v2/builds/<hashed_id>
============================================================
```

Test runners count tests, not sessions: a test that fails on one platform shows as one failed
test. The API count above is the result. Each session on the dashboard has its video and text
logs, plus network and console logs when `browserstack.yml` turns them on.

## When sessions failed

Report failures as results. Don't change test code to make them pass unless the user asks.

- **Sample build:** never edit BrowserStack's sample.
  - Failed the same way on every platform: the sample itself is out of date (for example a
    locator the demo site now matches more than once, or no wait for the product list). Say so
    plainly, note that the connection and pass/fail reporting worked, and offer to run the user's
    own tests instead.
  - Failed on one platform with an element-not-found error right after the page loaded: a timing
    flake in the sample. Re-run once with a new build name and report both builds.
- **Your own tests:** quote the failing assertion for each platform. If a test fails on only one
  platform (often real iOS Safari), say it is specific to that platform and offer to look at it
  separately. Don't edit the test without the user's OK.

## What I can do next

After the report, offer three or four of these, one line each, then wait for the user's answer
(extra sessions and devices use plan minutes). After a red run, leave out "Run faster".

- **Run faster:** "Your plan allows N parallel sessions and M are free. I can set
  `parallelsPerPlatform: K` so a full suite finishes up to K× faster." N is the smaller of the two
  plan limits. K = max(1, ⌊free ÷ platforms⌋), capped at 5 because other people on the team share
  the same pool; it is how many tests each platform runs at once in a full suite, so don't cap it
  at the number of tests in this run.
- **Wider coverage:** add browsers, OS versions or real devices (for example Firefox, an older
  Safari, a Pixel or an iPad).
- **Your own app:** after the sample build, run their own Selenium Python tests; for localhost or staging,
  turn on BrowserStack Local.
- **On every push:** add a CI job (GitHub Actions, Jenkins, GitLab) that runs this on BrowserStack.

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| Tests pass locally but the API shows no build | The run did not go through the BrowserStack SDK. Check the run command and wiring below, and read `log/sdk-cli.log` (mask the key) |
| Every session fails to start with `[browserstack.local] is set to true but local testing through BrowserStack is not connected` | The Local binary could not start (in `log/sdk-cli.log`: `Local.start … spawn …`; error `-86` = an Intel binary on Apple silicon without Rosetta). Public site → `browserstackLocal: false`. Private app → ask the user to install Rosetta themselves (`softwareupdate --install-rosetta`), then re-run |
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
