---
name: browserstack-automate-playwright-javascript
description: >-
  Runs Playwright tests written in JavaScript on BrowserStack Automate (real desktop browsers, with real Android and iPhone on request)
  from one pasted prompt: either BrowserStack's official Playwright JavaScript sample build, or the user's own
  Playwright JavaScript tests with no changes to their test logic. Checks credentials without printing them,
  shows a plan and waits for approval, runs the build, confirms it on the BrowserStack API and
  returns the dashboard link. Use when the user asks to run Playwright JavaScript tests on BrowserStack, set up
  BrowserStack Automate for a Playwright JavaScript project, or mentions Playwright with JavaScript or TypeScript, @playwright/test, playwright.config, browserstack-node-sdk or browserstack.yml. Not for other languages
  or frameworks: it names the right skill instead.
languages:
  - JavaScript
category: e2e-testing
license: MIT
user-invocable: true
metadata:
  author: BrowserStack
  version: "1.0"
---

<!-- Generated from automate/_source by build.py. Edit the source, not this file. -->

# BrowserStack Automate — Playwright JavaScript skill

You are a senior QA automation engineer with access to the user's shell and files. Do the work
yourself (clone, install, edit, run) instead of handing commands to the user, but only after the
user approves your plan.

## Step 1: Is this the right skill? (before anything else)

Look at the folder the user is in and its subfolders (read-only). This skill is for
**Playwright JavaScript**: `package.json` that depends on `@playwright/test` (JavaScript or TypeScript).

- Empty folder, or the user asked for the sample build → right skill, continue.
- A Playwright JavaScript project → right skill, continue.
- A project in another language or framework → stop without changing anything. If you already
  saved this skill into the project's skills folder, remove that folder again (and the skills
  folder above it if that leaves it empty and you created it). Tell the user in one line what you found and that this skill is for Playwright JavaScript, then give them the prompt for the right
  skill:

  - **Selenium Java** (`pom.xml` or `build.gradle` that depends on `selenium-java`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-java/SKILL.md, then follow that skill to run my own Selenium Java tests on BrowserStack Automate.`
  - **Selenium Python** (`requirements.txt`, `pyproject.toml` or `.py` tests that import `selenium`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-python/SKILL.md, then follow that skill to run my own Selenium Python tests on BrowserStack Automate.`
  - **Selenium JavaScript** (`package.json` that depends on `selenium-webdriver` (Mocha or Jest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-javascript/SKILL.md, then follow that skill to run my own Selenium JavaScript tests on BrowserStack Automate.`
  - **Selenium C#** (a `.csproj` that references `Selenium.WebDriver` (NUnit, xUnit or MSTest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-csharp/SKILL.md, then follow that skill to run my own Selenium C# tests on BrowserStack Automate.`
  - **Playwright Python** (`requirements.txt` or `pyproject.toml` with `playwright` or `pytest-playwright`, or `.py` tests that import `playwright`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-python/SKILL.md, then follow that skill to run my own Playwright Python tests on BrowserStack Automate.`
  - **Playwright Java** (`pom.xml` or `build.gradle` that depends on `com.microsoft.playwright`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-java/SKILL.md, then follow that skill to run my own Playwright Java tests on BrowserStack Automate.`
  - **Playwright C#** (a `.csproj` that references `Microsoft.Playwright` (NUnit, MSTest or xUnit)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-csharp/SKILL.md, then follow that skill to run my own Playwright C# tests on BrowserStack Automate.`

  For anything else (Ruby, PHP, WebdriverIO, Nightwatch or Cypress) there is no skill yet: point
  the user to https://www.browserstack.com/docs/automate and stop.
- A mixed project (for example Java and Python tests): work only on the Playwright JavaScript part, and name the
  skill that covers the rest.

## Step 2: Install this skill (once)

Skip this step if `browserstack-automate-playwright-javascript/SKILL.md` already exists in your skills folder (for example
`.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the
project-level folder your agent uses).

1. Create the folder `browserstack-automate-playwright-javascript` in your skills folder and download this file into it as `SKILL.md`:
   ```bash
   mkdir -p "<skills-folder>/browserstack-automate-playwright-javascript" && curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-javascript/SKILL.md -o "<skills-folder>/browserstack-automate-playwright-javascript/SKILL.md" || rmdir -p "<skills-folder>/browserstack-automate-playwright-javascript" 2>/dev/null
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
  NuGet dependencies) are fine, and so is BrowserStack's own Local binary when the plan names the
  download and the user approves it (see Private apps).
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
   - Toolchain: `node -v` (20+), `npm -v`, `git --version`. If something is missing, say what to install and stop.
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
     curl -fsSL https://raw.githubusercontent.com/browserstack/node-js-playwright-browserstack/main/browserstack.yml
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

- The prompt says **"sample build"**, or the folder has no Playwright JavaScript tests → **Path A: sample build**.
- The prompt says **"my own Playwright JavaScript tests"**, or the folder has Playwright JavaScript tests → **Path B: your own tests**.
  If the user asked for their own tests but you find none, say so, offer the sample build and stop.

## Path A: sample build

This runs BrowserStack's official Playwright JavaScript sample (`browserstack/node-js-playwright-browserstack`, branch
`main`), the same one the BrowserStack docs use, on the platforms it ships with.

### A1. Prerequisites

```bash
node -v    # 20 or newer
npm -v
git --version
```
If any is missing, tell the user what to install and stop.

### A2. Clone the official sample into a new folder

```bash
git clone -b main https://github.com/browserstack/node-js-playwright-browserstack.git
cd node-js-playwright-browserstack
```

If `node-js-playwright-browserstack` already exists, clone into `node-js-playwright-browserstack-$(date +%Y%m%d-%H%M%S)` instead.
Never overwrite a folder the user may have changed.

### A3. Point `browserstack.yml` at this run

Change only these two lines of `browserstack.yml` (A4 names any other change a sample needs), and
leave the rest as BrowserStack ships it:

```bash
BUILD_NAME="bsk-automate-playwright-javascript-sample-$(date +%Y%m%d-%H%M%S)"
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

```bash
npm install
npm run sample-test
```

`npm run sample-test` runs `npx browserstack-node-sdk playwright test --config=./playwright.config.js`:
the SDK runs the sample spec (pages on the-internet.herokuapp.com) on every platform in
`browserstack.yml` (desktop Chrome, WebKit and Firefox), in parallel, and reports pass/fail to
BrowserStack. `npm install` also updates the tracked `package-lock.json`, and its `postinstall`
step updates the SDK to the latest version: list both in the plan. "Uh-oh! We detected some
issues … SDK-GEN-004" about `GLOBAL_AGENT_HTTP_PROXY` is harmless.

Then go to **Confirm the run on BrowserStack** and **Report**.

## Path B: your own tests

Run the user's existing Playwright JavaScript tests on BrowserStack with no changes to their test logic.

### B1. Assess the project (read-only, before your plan)

Note these in a short Assessment block at the top of your plan:

- **Versions:** `@playwright/test` (and `playwright`) from `package.json`; keep the user's version.
- **Config:** `playwright.config.*`: projects, `baseURL`, `workers`, and `webServer` (an app the
  config starts locally needs BrowserStack Local).
- **Not this skill:** Playwright with Python, Java or C# has its own skill, Cypress has none yet,
  and a Selenium project needs a Selenium skill (see Step 1).
- **Browser launch the SDK can't wrap:** a helper that calls `chromium.launch()` with a hard-coded
  `executablePath`, a `globalSetup` that builds its own browser, or `connect()` to a non-BrowserStack
  endpoint runs on the local machine while the result still looks green. Propose routing it through
  Playwright's standard fixtures.
- **Other SDK bindings** (for example Selenium) in the same `node_modules` can make the SDK patch
  the wrong framework.
- **Real phones (on request):**
  - **Galaxy S23:** add this row to `browserstack.yml` next to the desktop rows (check it against
    the live catalog as in step A3):
    ```yaml
      - deviceName: Samsung Galaxy S23
        osVersion: 13.0
        browserName: chrome
    ```
  - **iPhone 15, as its own build:** keep `browserstack.yml` and add a `browserstack-ios.yml` with
    the same settings, a new `buildName` and only this platform:
    ```yaml
    platforms:
      - deviceName: iPhone 15
        osVersion: 17
        browserName: safari
    ```
    Run it with `npx browserstack-node-sdk playwright test --browserstack.config browserstack-ios.yml`
    after the main run. Set expectations in the plan first (see the "Real phones" offer).
  - On real Android, a page wider than the phone screen can make clicks below the fold time out
    (see Troubleshooting); say so in the plan if the app isn't built for small screens.
- **Which tests to run:** the ones the user named; otherwise the whole suite. If they named a flow
  that has no test, pick the spec whose name is the nearest step in that flow, and if two are
  equally close, the first by file path. State the pick and why.

### B2. Changes to put in your plan (each one shown as a diff)

1. **Add the BrowserStack Node SDK, pinned exactly** to the current release (`npm view
   browserstack-node-sdk version`), and keep the user's Playwright version; this changes `package.json`:
   ```bash
   npm i -D -E browserstack-node-sdk@<current>
   ```
2. **Only if the SDK can't run their Playwright version** (it fails before any session with
   `configLoader.js doesn't exist`, or BrowserStack rejects the client version): first update the
   SDK; if that doesn't fix it, propose pinning `@playwright/test` and `playwright` to `1.64.1`
   (verified with the SDK on desktop, Android and iPhone in Nov 2026) with `npm i -D -E`. Never
   downgrade further.
3. **`webServer` or localhost targets:** set `browserstackLocal: true` in `browserstack.yml` and say
   so in the plan; the SDK starts the tunnel.

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
projectName: My Playwright JavaScript Tests
buildName: bsk-automate-playwright-javascript-<timestamp>   # unique per run; keep the bsk- prefix
buildIdentifier: '#${BUILD_NUMBER}'
browserstackLocal: false   # true only for localhost, staging or a private app
debug: true
networkLogs: true
consoleLogs: info
framework: playwright
testObservability: true
```

Check the real-device rows against the live catalog as in step A3. Add `log/` to the project's
`.gitignore` (create the file if needed) in the same diff, as a plain `log/` line so it also
covers a module's `log/` folder.

**Private apps (BrowserStack Local).** Set `browserstackLocal: true` only when the tests open
`localhost`, a private IP or a staging host, and say so in the plan (the SDK starts the tunnel
itself). Before the run, check these and put any problem in the plan:
- The app answers on this machine at the URL the tests open, for example
  `curl -sI http://localhost:3000/dashboard | head -1`. If it doesn't, ask the user to start it, and
  don't ask for OK: end the plan with that and change nothing.
- On a Mac with Apple silicon (`uname -m` prints `arm64`), the SDK starts BrowserStack's Intel Local
  binary, which fails without Rosetta (error `-86`). Use BrowserStack's native Apple-silicon binary
  instead. Don't move or replace the SDK's own copy in `~/.browserstack/`, and don't install Rosetta.
  1. Check for it: `B="$HOME/.browserstack/arm64/BrowserStackLocal"; [ -x "$B" ] && "$B" --version`
     (or ask whether the user already keeps the arm64 binary somewhere else).
  2. If it isn't there, put this download in the plan (the official "macOS (Arm64)" link from
     https://www.browserstack.com/docs/local-testing/releases-and-downloads):
     ```bash
     mkdir -p ~/.browserstack/arm64 && curl -fsSL https://local-downloads.browserstack.com/BrowserStackLocal-darwin-arm64.zip -o ~/.browserstack/arm64/bslocal.zip \
       && unzip -o ~/.browserstack/arm64/bslocal.zip -d ~/.browserstack/arm64 && rm ~/.browserstack/arm64/bslocal.zip
     ```
  3. Point the SDK at it in `browserstack.yml`, with the absolute path (the SDK still starts and stops
     the tunnel and passes the key itself):
     ```yaml
     browserstackLocal: true
     browserStackLocalOptions:
       binarypath: /Users/<user>/.browserstack/arm64/BrowserStackLocal
     ```
     Verified with the Java, Python, Node and .NET SDKs (Nov 2026). After the run, a `[SUCCESS]` line
     in `log/local.log` shows the tunnel came up.

### B3. Run

```bash
npx browserstack-node-sdk playwright test
```

Add the user's usual arguments (a spec file, `--project`, `--config`). Never run bare
`npx playwright test`: it runs locally. These lines are harmless on a genuine BrowserStack run:
"Uh-oh! We detected some issues … SDK-GEN-004" about `GLOBAL_AGENT_HTTP_PROXY`, and Accessibility
"not a valid session" warnings, and `EBADENGINE` warnings on Node older than 20.16.

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
  default 10 within minutes. If more than one build matches (a shared account), use the
  hashed_id from the SDK's `View build on BrowserStack dashboard` line, or the build whose
  sessions match your platforms and start time.
- **No matching build, or 0 sessions** → the tests did not reach BrowserStack. Read the SDK's own
  logs in the `log/` folder next to `browserstack.yml` (mask the key first) before guessing; then
  see Troubleshooting. Report what stopped the run and the fix, without a dashboard link.
- **Each session's `status`:** `passed` or `failed` means the result reached the dashboard. Report
  from the sessions: the build's own `status` can read `failed` while every session passed (for
  example when a test closes Playwright without closing the browser). If the test runner reports
  a failed test for a platform whose session shows `passed`, trust the runner: mark that session
  `failed` with the runner's message (below) and say so in the report. The SDK has been seen
  marking a timed-out test `passed`.
  **`done` means the session ran but nobody reported pass or fail**: never report it as a pass.
  - The SDK marks desktop, Android and real iPhone sessions (iPhone verified with SDK 1.80.4, Nov
    2026); an iPhone build's own status can still read `done`, so report from the sessions. Every
    session is left `done` when the SDK prints `Binary CLI failed to start — running in direct
    flow`: re-run once in that case, then mark from the runner's result as shown below.
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

Print one summary block per build (an iPhone run of its own is a second build), then one line on
what the tests do and where they came from:

```
============================================================
BrowserStack Automate — Run Complete
------------------------------------------------------------
Ran       : [Sample build: browserstack/node-js-playwright-browserstack] or [Your tests: <path>]
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
  - Failed on some platforms with an element-not-found error right after the page loaded: the
    sample has no wait there. Re-run once with a new build name and report both builds. If the
    same platforms fail again, the sample fails there every time: say so, and offer to run the
    user's own tests instead of re-running again.
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
- **Real phones:** add a real Samsung Galaxy S23 (Chrome) and a real iPhone 15 (Safari) (B1 has the
  rows and how). Run the iPhone as its own build and set expectations first: Playwright on real iOS is a custom WebKit
  integration with limits (for example one browser context per session, and some keyboard and
  multi-tab behaviour differs from desktop WebKit), so a failure there doesn't change the desktop
  results. On real Android, pages wider than the phone screen can fail clicks with "intercepts
  pointer events" (see Troubleshooting).
- **Wider coverage:** add Edge, older browser versions or other operating systems.
- **Your own app:** after the sample build, run their own Playwright JavaScript tests; for localhost or staging,
  turn on BrowserStack Local.
- **On every push:** add a CI job (GitHub Actions, Jenkins, GitLab) that runs this on BrowserStack.

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| Tests pass locally but the API shows no build | The run did not go through the BrowserStack SDK. Check the run command and wiring below, and read `log/sdk-cli.log` (mask the key) |
| Every session fails to start with `[browserstack.local] is set to true but local testing through BrowserStack is not connected` | The Local binary could not start (in `log/sdk-cli.log`: `Local.start … spawn …`; error `-86` = an Intel binary on Apple silicon without Rosetta). Public site → `browserstackLocal: false`. Private app → point `browserStackLocalOptions.binarypath` at BrowserStack's native Apple-silicon binary (see Private apps) and re-run |
| `All parallel tests are currently in use` | The plan's parallel limit is reached; lower `parallelsPerPlatform` or wait |
| `Browser/OS combination not supported` | A retired device or OS version: re-check the catalog (step A3), swap to the closest current one and re-run once |
| Session fails to start with a connect timeout while parallels are free | Usually transient: re-run once. If it repeats, the network may block `*.browserstack.com` (allow outbound HTTPS) |
| `configLoader.js doesn't exist` before any session | The SDK is older than the project's Playwright: update `browserstack-node-sdk`; if needed pin Playwright to `1.64.1` (B2, step 2) |
| `Binary CLI failed to start — running in direct flow` | The SDK's helper timed out; tests still run but sessions are left `done`. Re-run once, then mark from the runner's result |
| iOS: `Only one browser context is allowed` | Real iOS allows one context per session: one test per session, no multi-context tests |
| Sample build: every platform fails at `getByRole('link', { name: 'Dropdown' })` with a strict-mode violation | the-internet.herokuapp.com now has three "Dropdown" links, so the sample's locator matches more than one. It is the sample, not your setup: report it as in "When sessions failed" |
| Tests pass but the API shows no build | Run through `npx browserstack-node-sdk playwright test`, and check for a custom `launch()` or `connect()` (B1) |
| Real Android Chrome: `click()` times out with "<element> intercepts pointer events", and the intercepting element changes on every retry | The page is wider than the phone screen, so Chrome scrolls only the visible area and Playwright checks the wrong spot (seen on Galaxy S23 and Pixel 9, Nov 2026; desktop and iPhone unaffected). Report it as Android-specific. With the user's OK, scroll the page to the element before the click (`await el.evaluate(e => window.scrollTo(0, e.getBoundingClientRect().top + scrollY - 120))`) or use `click({ force: true })` for that click on Android only; the lasting fix is removing the page's horizontal overflow |

## Quick reference

The sample-build row leaves out the A3 and A4 edits to `browserstack.yml`; for a real run follow
A2 to A4.

| Task | Command |
| --- | --- |
| Sample build | `git clone https://github.com/browserstack/node-js-playwright-browserstack.git && cd node-js-playwright-browserstack && npm install && npm run sample-test` |
| Your tests | `npx browserstack-node-sdk playwright test` |
| Current SDK version | `npm view browserstack-node-sdk version` |
| Docs | https://www.browserstack.com/docs/automate/playwright/getting-started/nodejs |
