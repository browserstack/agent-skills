---
name: browserstack-automate-playwright-python
description: >-
  Runs Playwright tests written in Python on BrowserStack Automate (real desktop browsers, with a real iPhone on request)
  from one pasted prompt: either BrowserStack's official Playwright Python sample build, or the user's own
  Playwright Python tests with no changes to their test logic. Checks credentials without printing them,
  shows a plan and waits for approval, runs the build, confirms it on the BrowserStack API and
  returns the dashboard link. Use when the user asks to run Playwright Python tests on BrowserStack, set up
  BrowserStack Automate for a Playwright Python project, or mentions Playwright with Python, pytest-playwright, playwright.sync_api, pytest, behave, browserstack-sdk or browserstack.yml. Not for other languages
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

# BrowserStack Automate — Playwright Python skill

You are a senior QA automation engineer with access to the user's shell and files. Do the work
yourself (clone, install, edit, run) instead of handing commands to the user, but only after the
user approves your plan.

## Step 1: Is this the right skill? (before anything else)

Look at the folder the user is in and its subfolders (read-only). This skill is for
**Playwright Python**: `requirements.txt` or `pyproject.toml` with `playwright` or `pytest-playwright`, or `.py` tests that import `playwright`.

- Empty folder, or the user asked for the sample build → right skill, continue.
- A Playwright Python project → right skill, continue.
- A project in another language or framework → stop without changing anything. If you already
  saved this skill into the project's skills folder, remove that folder again (and the skills
  folder above it if that leaves it empty and you created it). Tell the user in one line what you found and that this skill is for Playwright Python, then give them the prompt for the right
  skill:

  - **Selenium Java** (`pom.xml` or `build.gradle` that depends on `selenium-java`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-java/SKILL.md, then follow that skill to run my own Selenium Java tests on BrowserStack Automate.`
  - **Selenium Python** (`requirements.txt`, `pyproject.toml` or `.py` tests that import `selenium`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-python/SKILL.md, then follow that skill to run my own Selenium Python tests on BrowserStack Automate.`
  - **Selenium JavaScript** (`package.json` that depends on `selenium-webdriver` (Mocha or Jest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-javascript/SKILL.md, then follow that skill to run my own Selenium JavaScript tests on BrowserStack Automate.`
  - **Selenium C#** (a `.csproj` that references `Selenium.WebDriver` (NUnit, xUnit or MSTest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-csharp/SKILL.md, then follow that skill to run my own Selenium C# tests on BrowserStack Automate.`
  - **Playwright JavaScript** (`package.json` that depends on `@playwright/test` (JavaScript or TypeScript)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-javascript/SKILL.md, then follow that skill to run my own Playwright JavaScript tests on BrowserStack Automate.`
  - **Playwright Java** (`pom.xml` or `build.gradle` that depends on `com.microsoft.playwright`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-java/SKILL.md, then follow that skill to run my own Playwright Java tests on BrowserStack Automate.`
  - **Playwright C#** (a `.csproj` that references `Microsoft.Playwright` (NUnit, MSTest or xUnit)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-csharp/SKILL.md, then follow that skill to run my own Playwright C# tests on BrowserStack Automate.`

  For anything else (Ruby, PHP, WebdriverIO, Nightwatch or Cypress) there is no skill yet: point
  the user to https://www.browserstack.com/docs/automate and stop.
- A mixed project (for example Java and Python tests): work only on the Playwright Python part, and name the
  skill that covers the rest.

## Step 2: Install this skill (once)

Skip this step if `browserstack-automate-playwright-python/SKILL.md` already exists in your skills folder (for example
`.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the
project-level folder your agent uses).

1. Create the folder `browserstack-automate-playwright-python` in your skills folder and download this file into it as `SKILL.md`:
   ```bash
   mkdir -p "<skills-folder>/browserstack-automate-playwright-python" && curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-python/SKILL.md -o "<skills-folder>/browserstack-automate-playwright-python/SKILL.md" || rmdir -p "<skills-folder>/browserstack-automate-playwright-python" 2>/dev/null
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
   - Toolchain: `python3 --version` (3.9+), `git --version`. If something is missing, say what to install and stop.
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
     curl -fsSL https://raw.githubusercontent.com/browserstack/pytest-playwright-browserstack/main/browserstack.yml
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
   command and the build name it will use, and don't run anything. That build name stays until
   `browserstack.yml` changes, so later runs share it with a different suffix.

## Which path?

- The prompt says **"sample build"**, or the folder has no Playwright Python tests → **Path A: sample build**.
- The prompt says **"my own Playwright Python tests"**, or the folder has Playwright Python tests → **Path B: your own tests**.
  If the user asked for their own tests but you find none, say so, offer the sample build and stop.

## Path A: sample build

This runs BrowserStack's official Playwright Python sample (`browserstack/pytest-playwright-browserstack`, branch
`main`), the same one the BrowserStack docs use, on the platforms it ships with.

### A1. Prerequisites

```bash
python3 --version   # 3.9 or newer
git --version
```
If either is missing, tell the user what to install and stop.

### A2. Clone the official sample into a new folder

```bash
git clone -b main https://github.com/browserstack/pytest-playwright-browserstack.git
cd pytest-playwright-browserstack
```

If `pytest-playwright-browserstack` already exists, clone into `pytest-playwright-browserstack-$(date +%Y%m%d-%H%M%S)` instead.
Never overwrite a folder the user may have changed.

### A3. Point `browserstack.yml` at this run

Change only these two lines of `browserstack.yml`, and leave the rest as BrowserStack ships it:

```bash
BUILD_NAME="bsk-automate-playwright-python-sample-$(date +%Y%m%d-%H%M%S)"
sed -i.bak -e "s/^buildName:.*/buildName: ${BUILD_NAME}/" \
           -e "s/^browserstackLocal:.*/browserstackLocal: false/" browserstack.yml && rm -f browserstack.yml.bak
git check-ignore -q log/sdk-cli.log || echo 'log/' >> .gitignore
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

The sample leaves Playwright unpinned, and Playwright Python 1.65 renamed an internal module the
current SDK hooks into (Nov 2026), so install with Playwright pinned to 1.64.1. `--no-cache-dir`
makes pip fetch the current SDK instead of reusing an older cached copy:

```bash
python3 -m venv .venv
.venv/bin/pip install --no-cache-dir -r requirements.txt "playwright==1.64.1"
.venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"
sed -i.bak "s/osVersion: Ventura/osVersion: Sequoia/" browserstack.yml && rm -f browserstack.yml.bak
.venv/bin/browserstack-sdk pytest -s tests/sample-test.py
```

The `sed` line moves the sample's WebKit row from macOS Ventura to Sequoia: on Ventura WebKit the
sample's `to_have_count` check fails every run (Nov 2026). List both the Playwright pin and this
swap in the plan. On Windows use `.venv\Scripts\pip` and `.venv\Scripts\browserstack-sdk`. The SDK
runs `tests/sample-test.py` (adds a product to the cart on bstackdemo.com and checks the cart) on
every platform in `browserstack.yml` (desktop Chrome, WebKit and Firefox), in parallel, and the
test reports its own pass/fail. The browsers run on BrowserStack, so don't run `playwright install`.

Then go to **Confirm the run on BrowserStack** and **Report**.

## Path B: your own tests

Run the user's existing Playwright Python tests on BrowserStack with no changes to their test logic.

### B1. Assess the project (read-only, before your plan)

Note these in a short Assessment block at the top of your plan:

- **Test runner:** pytest with `pytest-playwright` (the `page` and `browser` fixtures) or behave.
  Plain scripts with `sync_playwright()` can run through `browserstack-sdk python <script>.py`;
  confirm on the API that sessions were created.
- **Versions:** `playwright` and `pytest-playwright` from `requirements.txt` or `pyproject.toml`;
  keep the user's versions, except Playwright 1.65 or newer, which the current SDK can't hook yet
  (Nov 2026): propose `playwright==1.64.1` in the BrowserStack `.venv` and say why.
- **Framework clash:** if the user's own `selenium` packages are installed or listed too, the SDK
  may patch Selenium instead of Playwright. Use a separate virtual environment without them (B2);
  the SDK pulls in its own Selenium, which is fine.
- **Browser launch the SDK can't wrap:** `executable_path`, `launch_persistent_context`, or
  `connect()` to another endpoint runs on the local machine while the result still looks green.
  Propose the standard fixtures or `browser_type.launch()`.
- **Real devices:** a real iPhone is available on request. Real Android phones aren't available
  for Playwright Python through the SDK.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test, pick the test whose name is the nearest step in that flow, and if two are equally close,
  the first by file path. State the pick and why.

### B2. Changes to put in your plan (each one shown as a diff)

1. **A virtual environment for the BrowserStack run** (a new folder, `.venv`) without the user's
   Selenium packages: their `playwright`, `pytest-playwright` and runner versions plus the current
   BrowserStack SDK from BrowserStack's server. PyPI's `browserstack-sdk` lags well behind, so don't install it from there:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install --no-cache-dir "playwright==<their version>" "pytest-playwright==<their version>" \
     "pytest==<their version>" https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz
   .venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"
   ```
2. **Pin the SDK by URL in `requirements.txt`** (diff), so the next install gets the same version
   (`browserstack-sdk==<version>` doesn't exist on PyPI):
   ```
   browserstack-sdk @ https://sdk-assets.browserstack.com/python/browserstack_sdk-<version>.tar.gz
   ```
   The plan can show this line with `<version>` until the install reveals it. If `requirements.txt`
   also lists `selenium`, say in the report that a full `pip install -r requirements.txt`
   brings the clash back, and offer a lasting fix: a separate `requirements-browserstack.txt`
   with only this stack.
3. **Don't run `browserstack-sdk setup`**: it writes `browserstack.yml` with the credentials inline.
   Use the file below instead, with `framework` set to the runner (`pytest` or `behave`).

Add a `browserstack.yml` next to the build file of the project or module whose tests run (in a
multi-module repo, that module, not the parent). If the project already has BrowserStack wiring
(a `browserstack.yml`, an SDK dependency, an SDK agent), update it in place and show the diff
instead of adding a second copy. By default the file runs on Windows 11 Chrome, macOS Sequoia WebKit and Windows 11 Firefox; the user
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
    browserName: playwright-webkit
    browserVersion: latest
  - os: Windows
    osVersion: 11
    browserName: playwright-firefox
    browserVersion: latest
parallelsPerPlatform: 1
projectName: My Playwright Python Tests
buildName: bsk-automate-playwright-python-<timestamp>   # unique per run; keep the bsk- prefix
buildIdentifier: '#${BUILD_NUMBER}'
browserstackLocal: false   # true only for localhost, staging or a private app
debug: true
networkLogs: true
consoleLogs: info
framework: pytest   # or behave
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

If either check fails, don't ask for OK: end the plan with what the user must fix first, and
change nothing.

### B3. Run

- **pytest:** `.venv/bin/browserstack-sdk pytest <tests>` (never bare `pytest`, which runs locally).
- **behave:** `.venv/bin/browserstack-sdk behave`.
- **Plain script:** `.venv/bin/browserstack-sdk python <script>.py`.

Don't run `playwright install`: the browsers run on BrowserStack. Notices about Selenium or other
frameworks that aren't installed are harmless; don't install packages to silence them.

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
  - The SDK marks pytest and behave sessions. If they show `done` and have no name, the SDK
    detected the wrong framework: check `framework:` in `browserstack.yml`, then mark each session
    from the runner's result as shown below.
  - `pytest-playwright` reuses one browser per platform, so several tests share one session, named
    after the last test and marked with its result. Report per-test results from pytest's output;
    if a test failed while its session shows `passed`, mark the session `failed` with that test's
    name and assertion.
- To mark a session yourself from the test runner's own result (use the assertion message as the
  reason for a failure, and say in your report that you marked it):
  ```bash
  curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" -X PUT -H "Content-Type: application/json" \
    -d '{"status":"passed","reason":"Marked from the test runner result"}' \
    "https://api.browserstack.com/automate/sessions/<session_hashed_id>.json"
  ```
  If the session has no name, add `"name":"<test name>"` to the same body. Only do this when you
  can tell which test result belongs to which session (one test per
  platform, or session names that carry the test name). Otherwise report the runner's result and
  explain that the dashboard shows `done`.

## Report

Print one summary block, then one line on what the tests do and where they came from:

```
============================================================
BrowserStack Automate — Run Complete
------------------------------------------------------------
Ran       : [Sample build: browserstack/pytest-playwright-browserstack] or [Your tests: <path>]
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
    plainly, note that the sessions ran on BrowserStack and their results are on the dashboard
    (say if you marked them yourself), and offer to run the user's own tests instead.
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
- **Real iPhone:** add a real iPhone 15 (Safari) as its own build. Set expectations first:
  Playwright on real iOS is a custom WebKit integration with limits (for example one browser
  context per session, and some keyboard and multi-tab behaviour differs from desktop WebKit), so
  a failure there doesn't change the desktop results. Real Android phones need BrowserStack's device API rather
  than a normal browser launch, so this skill doesn't set them up: see the Playwright Android docs.
- **Wider coverage:** add Edge, older browser versions or other operating systems.
- **Your own app:** after the sample build, run their own Playwright Python tests; for localhost or staging,
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
| `failed to setup playwright: No module named 'playwright._impl._connection'`, then no build on the API | The SDK can't hook this Playwright version (1.65 or newer, Nov 2026): install `playwright==1.64.1` in the `.venv` and re-run. This shows in the console, not in `log/`, so read both |
| `Executable doesn't exist … playwright install` | The SDK didn't take over the launch: either the run didn't start with `.venv/bin/browserstack-sdk`, or the SDK can't hook this Playwright version (row above) |
| Tests run on the user's machine and the API shows no build | The user's Selenium packages in the same environment, or a custom launch: use the separate `.venv` (B2) and the standard fixtures |
| Sessions have no name and stay `done` | The SDK detected the wrong framework: set `framework: pytest` (or `behave`) in `browserstack.yml` |
| macOS Ventura WebKit: `LocatorAssertions.to_have_count` fails with an empty message | Seen on every Ventura WebKit run of the sample (Nov 2026): use macOS Sequoia for WebKit |
| iOS: `Only one browser context is allowed` | Real iOS allows one context per session: one test per session, no multi-context tests |

## Quick reference

| Task | Command |
| --- | --- |
| Sample build | `git clone https://github.com/browserstack/pytest-playwright-browserstack.git && cd pytest-playwright-browserstack && python3 -m venv .venv && .venv/bin/pip install --no-cache-dir -r requirements.txt "playwright==1.64.1" && .venv/bin/browserstack-sdk pytest -s tests/sample-test.py` |
| Your tests | `.venv/bin/browserstack-sdk pytest` |
| Current SDK version | `.venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"` |
| Docs | https://www.browserstack.com/docs/automate/playwright/getting-started/python |
