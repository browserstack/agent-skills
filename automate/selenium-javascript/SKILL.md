---
name: browserstack-automate-selenium-javascript
description: >-
  Runs Selenium tests written in JavaScript on BrowserStack Automate (real desktop browsers and real mobile devices)
  from one pasted prompt: either BrowserStack's official Selenium JavaScript sample build, or the user's own
  Selenium JavaScript tests with no changes to their test logic. Checks credentials without printing them,
  shows a plan and waits for approval, runs the build, confirms it on the BrowserStack API and
  returns the dashboard link. Use when the user asks to run Selenium JavaScript tests on BrowserStack, set up
  BrowserStack Automate for a Selenium JavaScript project, or mentions Selenium with JavaScript or Node.js, selenium-webdriver, Mocha, Jest, browserstack-node-sdk or browserstack.yml. Not for other languages
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

# BrowserStack Automate — Selenium JavaScript skill

You are a senior QA automation engineer with access to the user's shell and files. Do the work
yourself (clone, install, edit, run) instead of handing commands to the user, but only after the
user approves your plan.

## Step 0: Install this skill (do this first, once)

Skip this step if `browserstack-automate-selenium-javascript/SKILL.md` already exists in your skills folder (for example
`.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the
project-level folder your agent uses).

1. Create the folder `browserstack-automate-selenium-javascript` in your skills folder.
2. Download this file into it as `SKILL.md`:
   ```bash
   mkdir -p "<skills-folder>/browserstack-automate-selenium-javascript" && curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-javascript/SKILL.md -o "<skills-folder>/browserstack-automate-selenium-javascript/SKILL.md"
   ```
   Replace `<skills-folder>` with your agent's project-level skills folder. The skill stays
   installed for future sessions.
3. Tell the user in one line that the skill is installed, then continue in this session. Do not
   ask them to restart.

To update the skill later, delete the folder and run the prompt again. If the network or the
skills folder is unavailable, say so in one line and carry on using this file for this session
only. Installing is a convenience; never block the run on it.

## Is this the right skill? (check before anything else)

Look at the folder the user is in (read-only). This skill is for **Selenium JavaScript**: `package.json` that depends on `selenium-webdriver` (Mocha or Jest).

- Empty folder, or the user asked for the sample build → right skill, continue.
- A Selenium JavaScript project → right skill, continue.
- A project in another language or framework → stop. Tell the user in one line what you found and
  that this skill is for Selenium JavaScript, then give them the prompt for the right skill:

  - **Selenium Java** (`pom.xml` or `build.gradle` that depends on `selenium-java`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-java/SKILL.md, then follow that skill to run my own Selenium Java tests on BrowserStack Automate.`
  - **Selenium Python** (`requirements.txt`, `pyproject.toml` or `.py` tests that import `selenium`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-python/SKILL.md, then follow that skill to run my own Selenium Python tests on BrowserStack Automate.`
  - **Selenium C#** (a `.csproj` that references `Selenium.WebDriver` (NUnit, xUnit or MSTest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-csharp/SKILL.md, then follow that skill to run my own Selenium C# tests on BrowserStack Automate.`
  - **Playwright JavaScript** (`package.json` that depends on `@playwright/test` (JavaScript or TypeScript)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-javascript/SKILL.md, then follow that skill to run my own Playwright JavaScript tests on BrowserStack Automate.`

  For anything else (Ruby, PHP, WebdriverIO, Nightwatch, Cypress, Playwright with Python, Java
  or C#) there is no skill yet: point the user to https://www.browserstack.com/docs/automate and stop.
- A mixed project (for example Java and Python tests): work only on the Selenium JavaScript part, and name the
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
   - Toolchain: `node -v` (20+), `npm -v`, `git --version`. If something is missing, say what to install and stop. Never
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

- The prompt says **"sample build"**, or the folder has no Selenium JavaScript tests → **Path A: sample build**.
- The prompt says **"my own Selenium JavaScript tests"**, or the folder has Selenium JavaScript tests → **Path B: your own tests**.
  If the user asked for their own tests but you find none, say so, offer the sample build and stop.

## Path A: sample build

This runs BrowserStack's official Selenium JavaScript sample (`browserstack/mocha-browserstack`, branch
`master`), the same one the BrowserStack docs use, on the platforms it ships with.

### A1. Prerequisites

```bash
node -v    # 20 or newer
npm -v
git --version
```
If any is missing, tell the user what to install and stop.

### A2. Clone the official sample into a new folder

```bash
git clone -b master https://github.com/browserstack/mocha-browserstack.git
cd mocha-browserstack
```

If `mocha-browserstack` already exists, clone into `mocha-browserstack-$(date +%Y%m%d-%H%M%S)` instead.
Never overwrite a folder the user may have changed.

### A3. Point `browserstack.yml` at this run

Change only these, and leave everything else as BrowserStack ships it:

```bash
BUILD_NAME="bsk-automate-selenium-javascript-sample-$(date +%Y%m%d-%H%M%S)"
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
npm install
npm run sample-test
```

`npm run sample-test` runs `browserstack-node-sdk mocha test/sample_test.js`: the SDK runs the
Mocha test (adds a product to the cart on bstackdemo.com and checks it is there) on every
platform in `browserstack.yml`, in parallel, and reports pass/fail to BrowserStack. The
`postinstall` step updates the SDK to the latest version.

Then go to **Confirm the run on BrowserStack** and **Report**.

## Path B: your own tests

Run the user's existing Selenium JavaScript tests on BrowserStack with no changes to their test logic.

### B1. Assess the project (read-only, before your plan)

Note these in a short Assessment block at the top of your plan:

- **Test runner:** Mocha or Jest (from `package.json` scripts and dev dependencies), and the
  `selenium-webdriver` version (4.x is required).
- **Not this skill:** WebdriverIO (`@wdio/*`) and Nightwatch have no skill yet; a project that
  only uses `@playwright/test` needs the Playwright JavaScript skill (see "Is this the right skill?").
- **Framework clash:** if `playwright` or `@playwright/test` is also installed, the SDK may patch
  Playwright instead of Selenium. Remove them from `node_modules` for this run (B2).
- **How the driver is created:** `new Builder().forBrowser('chrome').build()` (with or without
  `usingServer(...)`) is intercepted by the SDK.
- **`maximize()` calls:** real Android phones reject them, so they matter only if the plan
  includes phones.
- **Which tests to run:** the ones the user named; otherwise the suite their `npm test` script
  runs. If they named a flow that has no test, pick the test whose name is the nearest step in
  that flow, and if two are equally close, the first by file path. State the pick and why.

### B2. Changes to put in your plan (each one shown as a diff)

1. **Add the BrowserStack Node SDK, pinned exactly** to the current release (`npm view
   browserstack-node-sdk version`); this changes `package.json`:
   ```bash
   npm i -D -E browserstack-node-sdk@<current>
   ```
   If the repo has no lockfile, this also creates `package-lock.json`: say so in the plan.
2. **Framework clash** (only if Playwright is installed): after `npm install`, remove it from
   `node_modules` for this run only:
   ```bash
   npm uninstall --no-save @playwright/test playwright playwright-core
   ```
   `package.json` and the lockfile still list Playwright, so the next `npm install` or `npm ci`
   brings the clash back. Tell the user, and offer the lasting fix (move Playwright to its own
   package, or remove it if unused; diff-gated).
3. **`maximize()` on real phones** (only if the plan includes phones): run it on desktop only:
   ```js
   const platform = String((await driver.getCapabilities()).get('platformName') || '').toLowerCase();
   if (!['android', 'ios'].includes(platform)) await driver.manage().window().maximize();
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
projectName: My Selenium JavaScript Tests
buildName: bsk-automate-selenium-javascript-<timestamp>   # unique per run; keep the bsk- prefix
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

- **Mocha:** `npx browserstack-node-sdk mocha <spec or glob> --timeout 60000` (keep any flags
  from the user's `npm test` script).
- **Jest:** `npx browserstack-node-sdk jest <path>`.

These also appear on genuine BrowserStack runs and are harmless: `npm error code ELSPROBLEMS …
missing: @playwright/test` after the clash step, `EBADENGINE` warnings (current
`selenium-webdriver` asks for Node 22+, but runs on Node 20), and "loadModules: skipping driver
module for selenium-webdriver".

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
  - Mocha sessions are marked and named by the SDK. If a Jest run's sessions show `done`, mark
    them from the runner's result as shown below.
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
Ran       : [Sample build: browserstack/mocha-browserstack] or [Your tests: <path>]
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
- **Your own app:** after the sample build, run their own Selenium JavaScript tests; for localhost or staging,
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
| Logs show `unpatched method`; a browser opens locally | The SDK patched Playwright instead of Selenium: remove Playwright from `node_modules` for the run (B2, step 2) |
| Tests run locally with bare `npx mocha` or `npm test` | Run through the SDK: `npx browserstack-node-sdk mocha …` |
| Android: `Unable to maximize window` | `maximize()` on a real phone: guard it as in B2, step 3 |
| SDK log upload fails on old Node | Use Node 20 or newer |

## Quick reference

| Task | Command |
| --- | --- |
| Sample build | `git clone https://github.com/browserstack/mocha-browserstack.git && cd mocha-browserstack && npm install && npm run sample-test` |
| Your tests (Mocha) | `npx browserstack-node-sdk mocha test/*.js --timeout 60000` |
| Your tests (Jest) | `npx browserstack-node-sdk jest` |
| Current SDK version | `npm view browserstack-node-sdk version` |
| Docs | https://www.browserstack.com/docs/automate/selenium/getting-started/nodejs |
