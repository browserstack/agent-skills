---
name: browserstack-automate-playwright-csharp
description: >-
  Runs Playwright tests written in C# on BrowserStack Automate (real desktop browsers, with a real iPhone on request)
  from one pasted prompt: either BrowserStack's official Playwright C# sample build, or the user's own
  Playwright C# tests with no changes to their test logic. Checks credentials without printing them,
  shows a plan and waits for approval, runs the build, confirms it on the BrowserStack API and
  returns the dashboard link. Use when the user asks to run Playwright C# tests on BrowserStack, set up
  BrowserStack Automate for a Playwright C# project, or mentions Playwright with C# or .NET, Microsoft.Playwright, Microsoft.Playwright.NUnit, PageTest, dotnet test, BrowserStack.TestAdapter or browserstack.yml. Not for other languages
  or frameworks: it names the right skill instead.
languages:
  - C#
category: e2e-testing
license: MIT
user-invocable: true
metadata:
  author: BrowserStack
  version: "1.0"
---

<!-- Generated from automate/_source by build.py. Edit the source, not this file. -->

# BrowserStack Automate — Playwright C# skill

You are a senior QA automation engineer with access to the user's shell and files. Do the work
yourself (clone, install, edit, run) instead of handing commands to the user, but only after the
user approves your plan.

## Step 1: Is this the right skill? (before anything else)

Look at the folder the user is in and its subfolders (read-only). This skill is for
**Playwright C#**: a `.csproj` that references `Microsoft.Playwright` (NUnit, MSTest or xUnit).

- Empty folder, or the user asked for the sample build → right skill, continue.
- A Playwright C# project → right skill, continue.
- A project in another language or framework → stop without changing anything. If you already
  saved this skill into the project's skills folder, remove that folder again (and the skills
  folder above it if that leaves it empty and you created it). Tell the user in one line what you found and that this skill is for Playwright C#, then give them the prompt for the right
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
  - **Playwright Python** (`requirements.txt` or `pyproject.toml` with `playwright` or `pytest-playwright`, or `.py` tests that import `playwright`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-python/SKILL.md, then follow that skill to run my own Playwright Python tests on BrowserStack Automate.`
  - **Playwright Java** (`pom.xml` or `build.gradle` that depends on `com.microsoft.playwright`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-java/SKILL.md, then follow that skill to run my own Playwright Java tests on BrowserStack Automate.`

  For anything else (Ruby, PHP, WebdriverIO, Nightwatch or Cypress) there is no skill yet: point
  the user to https://www.browserstack.com/docs/automate and stop.
- A mixed project (for example Java and Python tests): work only on the Playwright C# part, and name the
  skill that covers the rest.

## Step 2: Install this skill (once)

Skip this step if `browserstack-automate-playwright-csharp/SKILL.md` already exists in your skills folder (for example
`.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the
project-level folder your agent uses).

1. Create the folder `browserstack-automate-playwright-csharp` in your skills folder and download this file into it as `SKILL.md`:
   ```bash
   mkdir -p "<skills-folder>/browserstack-automate-playwright-csharp" && curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-csharp/SKILL.md -o "<skills-folder>/browserstack-automate-playwright-csharp/SKILL.md" || rmdir -p "<skills-folder>/browserstack-automate-playwright-csharp" 2>/dev/null
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
   - Toolchain: `dotnet --version` (6+), `dotnet --list-runtimes`, `git --version`. If something is missing, say what to install and stop.
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
     curl -fsSL https://raw.githubusercontent.com/browserstack/csharp-playwright-browserstack/main/CSharp-Playwright-BrowserStack/browserstack.yml
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

- The prompt says **"sample build"**, or the folder has no Playwright C# tests → **Path A: sample build**.
- The prompt says **"my own Playwright C# tests"**, or the folder has Playwright C# tests → **Path B: your own tests**.
  If the user asked for their own tests but you find none, say so, offer the sample build and stop.

## Path A: sample build

This runs BrowserStack's official Playwright C# sample (`browserstack/csharp-playwright-browserstack`, branch
`main`), the same one the BrowserStack docs use, on the platforms it ships with.

### A1. Prerequisites

```bash
dotnet --version        # .NET SDK 6 or newer
dotnet --list-runtimes  # no Microsoft.NETCore.App 6.0.x? fine: A4 runs on a newer one
git --version
```
If `dotnet` or `git` is missing, tell the user what to install and stop.

### A2. Clone the official sample into a new folder

```bash
git clone -b main https://github.com/browserstack/csharp-playwright-browserstack.git
cd csharp-playwright-browserstack/CSharp-Playwright-BrowserStack
```

If `csharp-playwright-browserstack` already exists, clone into `csharp-playwright-browserstack-$(date +%Y%m%d-%H%M%S)` instead.
Never overwrite a folder the user may have changed.

### A3. Point `browserstack.yml` at this run

Change only these two lines of `browserstack.yml` (A4 names any other change a sample needs), and
leave the rest as BrowserStack ships it:

```bash
BUILD_NAME="bsk-automate-playwright-csharp-sample-$(date +%Y%m%d-%H%M%S)"
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

The sample floats `Microsoft.Playwright.NUnit` to the latest release but pins an older
`Microsoft.NET.Test.Sdk`, so restore stops with `NU1605: Detected package downgrade`; and it targets
`net6.0`. Both are handled with environment variables, without changing any file:

```bash
NoWarn=NU1605 DOTNET_ROLL_FORWARD=Major dotnet test --filter "Category=sample-test"
```

`NoWarn` must be an environment variable, not `-p:NoWarn`, because the SDK runs its own restore.
With a 6.0 runtime installed, drop `DOTNET_ROLL_FORWARD=Major`. PowerShell: set
`$env:NoWarn="NU1605"` and `$env:DOTNET_ROLL_FORWARD="Major"` first. The BrowserStack SDK (the
`BrowserStack.TestAdapter` package already in the project) runs `SampleTest` (adds a product to
the cart on bstackdemo.com and checks the cart) on every platform in `browserstack.yml` (desktop
Chrome, WebKit and Firefox), in parallel. The build also adds the SDK's own `browserstack-sdk` tool
to a `dotnet-tools.json`: list it in the plan. Warnings that `net6.0` is out of support are harmless.
If a first attempt failed, delete `bin/` and `obj/` before running again (see Troubleshooting).

Then go to **Confirm the run on BrowserStack** and **Report**.

## Path B: your own tests

Run the user's existing Playwright C# tests on BrowserStack with no changes to their test logic.

### B1. Assess the project (read-only, before your plan)

Note these in a short Assessment block at the top of your plan:

- **Project:** the test `.csproj` (and the solution, if any), its `TargetFramework(s)`, and the test
  framework: NUnit, MSTest or xUnit.
- **Playwright version:** `Microsoft.Playwright` (and `Microsoft.Playwright.NUnit` or `.MSTest`);
  keep the user's version.
- **How the browser is created:** a `PageTest`/`BrowserTest` base class, or
  `Playwright.CreateAsync()` with `Chromium`/`Firefox`/`Webkit.LaunchAsync()`, is routed by the SDK
  to the platforms in `browserstack.yml`; confirm on the API after the run. `ExecutablePath`,
  `LaunchPersistentContextAsync` or `ConnectAsync` to another endpoint runs on the local machine.
- **Target framework runtime:** if the project targets a .NET version whose runtime isn't
  installed, plan to run with `DOTNET_ROLL_FORWARD=Major` (no file change).
- **Real iPhone (on request, as its own build):** for that run, use only this platform in
  `browserstack.yml` with a new `buildName` (check it against the live catalog as in step A3), and
  put the desktop rows back afterwards if the user wants both:
  ```yaml
  platforms:
    - deviceName: iPhone 15
      osVersion: 17
      browserName: safari
  ```
  The SDK opens one session per test, so `PageTest` and `LaunchAsync` tests stay within iOS's
  one-context limit, and it names and marks each session (verified Nov 2026).
- **Real Android:** needs BrowserStack's device API (`Android.ConnectAsync`), which is a code
  change, so this skill doesn't set it up. Never add an Android row: device sessions still start
  and stay `done` (see Troubleshooting). Point the user to https://www.browserstack.com/docs/automate/playwright/playwright-android/c-sharp.
- **Which tests to run:** the ones the user named (as a `dotnet test --filter`); otherwise all. If
  they named a flow that has no test, pick the test whose name is the nearest step in that flow,
  and if two are equally close, the first by file path. State the pick and why.

### B2. Changes to put in your plan (each one shown as a diff)

1. **Add the BrowserStack SDK package, pinned to the current release** (the last entry of
   `https://api.nuget.org/v3-flatcontainer/browserstack.testadapter/index.json`). An outdated
   adapter can silently run 0 tests on newer .NET, so always use the current one; this changes the `.csproj`:
   ```bash
   dotnet add <path/to/Tests.csproj> package BrowserStack.TestAdapter --version <current>
   ```
2. **Put `browserstack.yml` next to the test `.csproj`** (the file below). The first build also
   creates a `dotnet-tools.json` for the SDK's own `browserstack-sdk` tool, and the SDK writes its
   logs to `log/` next to the `.csproj`: list both in the plan.

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
projectName: My Playwright C# Tests
buildName: bsk-automate-playwright-csharp-<timestamp>   # unique per run; keep the bsk- prefix
buildIdentifier: '#${BUILD_NUMBER}'
browserstackLocal: false   # true only for localhost, staging or a private app
debug: true
networkLogs: true
consoleLogs: info
# testObservability: true   # optional: adds a test report link; check the build report the SDK prints
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

Build first: the SDK hooks into the test assembly at build time.

```bash
dotnet build <path/to/Tests.csproj>
dotnet test <path/to/Tests.csproj>          # add --filter "FullyQualifiedName~Cart" for a subset
```

If the project targets several frameworks, add `-f <newest installed>`; if its only target's
runtime isn't installed, prefix `DOTNET_ROLL_FORWARD=Major`. Don't run `playwright.ps1 install`:
the browsers run on BrowserStack.

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
  - If sessions show `done`, mark each from `dotnet test`'s results as shown below (session names
    carry the test's full name when the SDK set them).
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
Ran       : [Sample build: browserstack/csharp-playwright-browserstack] or [Your tests: <path>]
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
- **Real iPhone:** add a real iPhone 15 (Safari) as its own build (B1 has the row and how). After
  an iPhone-only run, offer the desktop build instead. Set expectations first:
  Playwright on real iOS is a custom WebKit integration with limits (for example one browser
  context per session, and some keyboard and multi-tab behaviour differs from desktop WebKit), so
  a failure there doesn't change the desktop results. Real Android phones need BrowserStack's device API rather
  than a normal browser launch, so this skill doesn't set them up: see https://www.browserstack.com/docs/automate/playwright/playwright-android/c-sharp.
- **Wider coverage:** add Edge, older browser versions or other operating systems.
- **Your own app:** after the sample build, run their own Playwright C# tests; for localhost or staging,
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
| `dotnet test` finishes with 0 tests run, or runs locally | An outdated `BrowserStack.TestAdapter`: update it to the current release (B2, step 1) |
| `You must install or update .NET to run this application` | The target framework's runtime isn't installed: prefix `DOTNET_ROLL_FORWARD=Major`, or use `-f <installed version>` |
| `NU1605: Detected package downgrade: Microsoft.NET.Test.Sdk` | A floating `Microsoft.Playwright.NUnit` needs a newer `Microsoft.NET.Test.Sdk` than the project pins. Sample build: run with the environment variable `NoWarn=NU1605` (A4). Your project: propose raising `Microsoft.NET.Test.Sdk` to 17.8 or newer |
| `Executable doesn't exist … playwright.ps1 install` | The launch wasn't routed: check `BrowserStack.TestAdapter` is in the `.csproj` and run `dotnet build` before `dotnet test`. After a failed build, delete `bin/` and `obj/` first: the SDK otherwise reuses the patch from the failed build and the browsers launch locally |
| Test host crashed with `JsonReaderException … AtomicFile`, or the output shows another project's tests | Another .NET SDK run is active on this machine (they share `$TMPDIR/.browserstack/`, which also holds a copy of the credentials): run one at a time, and trust the API |
| iOS: `Only one browser context is allowed` | Real iOS allows one context per session: one test per session, no multi-context tests |
| Real Android: every test fails with `KeyNotFoundException: The given key 'AndroidDevice' was not present in the dictionary`; sessions stay `done` with no name | Desktop-style tests can't drive real Android: remove the Android row (B1) |

## Quick reference

The sample-build row leaves out the A3 and A4 edits to `browserstack.yml`; for a real run follow
A2 to A4.

| Task | Command |
| --- | --- |
| Sample build | `git clone https://github.com/browserstack/csharp-playwright-browserstack.git && cd csharp-playwright-browserstack/CSharp-Playwright-BrowserStack && NoWarn=NU1605 DOTNET_ROLL_FORWARD=Major dotnet test --filter "Category=sample-test"` |
| Your tests | `dotnet build <Tests.csproj> && dotnet test <Tests.csproj>` |
| Current SDK version | `curl -s https://api.nuget.org/v3-flatcontainer/browserstack.testadapter/index.json` (last entry) |
| Installed runtimes | `dotnet --list-runtimes` |
| Docs | https://www.browserstack.com/docs/automate/playwright/getting-started/c-sharp |
