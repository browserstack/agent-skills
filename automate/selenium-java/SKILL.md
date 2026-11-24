---
name: browserstack-automate-selenium-java
description: >-
  Runs Selenium tests written in Java on BrowserStack Automate (real desktop browsers and real mobile devices)
  from one pasted prompt: either BrowserStack's official Selenium Java sample build, or the user's own
  Selenium Java tests with no changes to their test logic. Checks credentials without printing them,
  shows a plan and waits for approval, runs the build, confirms it on the BrowserStack API and
  returns the dashboard link. Use when the user asks to run Selenium Java tests on BrowserStack, set up
  BrowserStack Automate for a Selenium Java project, or mentions Selenium with Java, Maven, Gradle, TestNG, JUnit, RemoteWebDriver, browserstack-java-sdk or browserstack.yml. Not for other languages
  or frameworks: it names the right skill instead.
languages:
  - Java
category: e2e-testing
license: MIT
user-invocable: true
metadata:
  author: BrowserStack
  version: "1.0"
---

<!-- Generated from automate/_source by build.py. Edit the source, not this file. -->

# BrowserStack Automate — Selenium Java skill

You are a senior QA automation engineer with access to the user's shell and files. Do the work
yourself (clone, install, edit, run) instead of handing commands to the user, but only after the
user approves your plan.

## Step 0: Install this skill (do this first, once)

Skip this step if `browserstack-automate-selenium-java/SKILL.md` already exists in your skills folder (for example
`.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the
project-level folder your agent uses).

1. Create the folder `browserstack-automate-selenium-java` in your skills folder.
2. Download this file into it as `SKILL.md`:
   ```bash
   mkdir -p "<skills-folder>/browserstack-automate-selenium-java" && curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-java/SKILL.md -o "<skills-folder>/browserstack-automate-selenium-java/SKILL.md"
   ```
   Replace `<skills-folder>` with your agent's project-level skills folder. The skill stays
   installed for future sessions.
3. Tell the user in one line that the skill is installed, then continue in this session. Do not
   ask them to restart.

To update the skill later, delete the folder and run the prompt again. If the network or the
skills folder is unavailable, say so in one line and carry on using this file for this session
only. Installing is a convenience; never block the run on it.

## Is this the right skill? (check before anything else)

Look at the folder the user is in (read-only). This skill is for **Selenium Java**: `pom.xml` or `build.gradle` that depends on `selenium-java`.

- Empty folder, or the user asked for the sample build → right skill, continue.
- A Selenium Java project → right skill, continue.
- A project in another language or framework → stop. Tell the user in one line what you found and
  that this skill is for Selenium Java, then give them the prompt for the right skill:

  - **Selenium Python** (`requirements.txt`, `pyproject.toml` or `.py` tests that import `selenium`):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-python/SKILL.md, then follow that skill to run my own Selenium Python tests on BrowserStack Automate.`
  - **Selenium JavaScript** (`package.json` that depends on `selenium-webdriver` (Mocha or Jest)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-javascript/SKILL.md, then follow that skill to run my own Selenium JavaScript tests on BrowserStack Automate.`
  - **Playwright JavaScript** (`package.json` that depends on `@playwright/test` (JavaScript or TypeScript)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-javascript/SKILL.md, then follow that skill to run my own Playwright JavaScript tests on BrowserStack Automate.`

  For anything else (C#, Ruby, PHP, WebdriverIO, Nightwatch, Cypress, Playwright with Python, Java
  or C#) there is no skill yet: point the user to https://www.browserstack.com/docs/automate and stop.
- A mixed project (for example Java and Python tests): work only on the Selenium Java part, and name the
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
   - Toolchain: `java -version` (11+), `mvn -version` (or `./gradlew -v` / `gradle -v`), `git --version`. If something is missing, say what to install and stop. Never
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

- The prompt says **"sample build"**, or the folder has no Selenium Java tests → **Path A: sample build**.
- The prompt says **"my own Selenium Java tests"**, or the folder has Selenium Java tests → **Path B: your own tests**.
  If the user asked for their own tests but you find none, say so, offer the sample build and stop.

## Path A: sample build

This runs BrowserStack's official Selenium Java sample (`browserstack/vanilla-java-browserstack`, branch
`sdk-sample`), the same one the BrowserStack docs use, on the platforms it ships with.

### A1. Prerequisites

```bash
java -version    # 11 or newer (Selenium 4 needs Java 11)
mvn -version     # Maven on PATH
git --version
```
If any is missing, tell the user what to install and stop.

### A2. Clone the official sample into a new folder

```bash
git clone -b sdk-sample https://github.com/browserstack/vanilla-java-browserstack.git
cd vanilla-java-browserstack
```

If `vanilla-java-browserstack` already exists, clone into `vanilla-java-browserstack-$(date +%Y%m%d-%H%M%S)` instead.
Never overwrite a folder the user may have changed.

### A3. Point `browserstack.yml` at this run

Change only these, and leave everything else as BrowserStack ships it:

```bash
BUILD_NAME="bsk-automate-selenium-java-sample-$(date +%Y%m%d-%H%M%S)"
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
mvn test
```

The sample's `pom.xml` attaches the BrowserStack Java SDK as a `-javaagent` and runs
`BStackDemoTest` (adds a product to the cart on bstackdemo.com and checks it is there) on every
platform in `browserstack.yml`, in parallel. Don't add `-q`: keep the full output. Warnings about
the deprecated `LATEST` SDK version, SeleniumManager driver versions or CDP versions are harmless.

Then go to **Confirm the run on BrowserStack** and **Report**.

## Path B: your own tests

Run the user's existing Selenium Java tests on BrowserStack with no changes to their test logic.

### B1. Assess the project (read-only, before your plan)

Note these in a short Assessment block at the top of your plan:

- **Build tool:** `pom.xml` → Maven; `build.gradle` / `build.gradle.kts` → Gradle (use `./gradlew`
  if the repo has it). In a multi-module repo, pick the module that has the Selenium tests, wire
  only that module, and run it from the root with `mvn -pl <module> test`.
- **Test framework:** JUnit 5 (`org.junit.jupiter`), JUnit 4, TestNG, Cucumber, or none (a plain
  `main()` run by `exec-maven-plugin`).
- **Selenium version:** 4.x is required; 3.x needs the upgrade in B2.
- **How the driver is created:** `new ChromeDriver()`, `new RemoteWebDriver(new URL(...), options)`
  (even with a hard-coded hub) and a constructor called by reflection are all intercepted by the
  SDK, so leave them alone. A driver-manager factory that builds the driver itself
  (`WebDriverManager.chromedriver().create()`) is not intercepted and runs on the local machine:
  propose `new ChromeDriver()` instead (`.setup()` followed by `new ChromeDriver()` is fine).
- **Existing surefire `<argLine>`** (for example JaCoCo): the agent must be appended, not replace it.
- **`maximize()` calls:** real Android phones reject them, so they matter only if the plan includes phones.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test (for example "checkout"), pick the test whose name is the nearest step in that flow (for
  example `*Cart*`), and if two are equally close, the first by file path. State the pick and why.

### B2. Changes to put in your plan (each one shown as a diff)

1. **BrowserStack Java SDK, pinned to the current release** (never `LATEST`). Get the version from
   `https://repo1.maven.org/maven2/com/browserstack/browserstack-java-sdk/maven-metadata.xml`
   (the `<release>` tag; `search.maven.org` lags):
   ```xml
   <dependency>
     <groupId>com.browserstack</groupId>
     <artifactId>browserstack-java-sdk</artifactId>
     <version>CURRENT_RELEASE</version>
     <scope>compile</scope>
   </dependency>
   ```
2. **Attach the SDK as a `-javaagent`**, exactly once:
   - **Maven:** add `maven-dependency-plugin` (goal `properties`, which exposes the jar path) and the
     agent on surefire. If the project already has an `argLine`, keep it and append:
     ```xml
     <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-dependency-plugin</artifactId>
       <executions><execution><id>getClasspathFilenames</id><goals><goal>properties</goal></goals></execution></executions>
     </plugin>
     <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-surefire-plugin</artifactId>
       <configuration>
         <argLine>-javaagent:${com.browserstack:browserstack-java-sdk:jar}</argLine>
         <!-- existing argLine: <argLine>@{argLine} -javaagent:${com.browserstack:browserstack-java-sdk:jar}</argLine> -->
       </configuration>
     </plugin>
     ```
   - **Gradle:**
     ```groovy
     dependencies { testImplementation 'com.browserstack:browserstack-java-sdk:CURRENT_RELEASE' }
     test {
       useJUnitPlatform()
       doFirst { jvmArgs "-javaagent:${classpath.find { it.name.contains('browserstack-java-sdk') }.absolutePath}" }
     }
     ```
   - **No test framework (a plain `main()` run by `exec-maven-plugin`):** put the agent on the forked
     JVM instead of surefire (`<executable>java</executable>`, `<classpathScope>test</classpathScope>`,
     arguments `-javaagent:${com.browserstack:browserstack-java-sdk:jar}`, `-classpath`, `<classpath/>`,
     `${exec.mainClass}`) and run `mvn test-compile exec:exec`.
   - Never also run through `browserstack-sdk mvn test`: attaching the agent twice fails with
     "agent already loaded".
3. **Selenium 3 → 4** (only for 3.x): bump `selenium-java` to the current 4.x (the `<release>` in
   `https://repo1.maven.org/maven2/org/seleniumhq/selenium/selenium-java/maven-metadata.xml`) and
   compile with `mvn test-compile` before the cloud run. Selenium 4 removed some Selenium 3 APIs,
   so include these edits in the diff: `new WebDriverWait(driver, 20)` →
   `new WebDriverWait(driver, Duration.ofSeconds(20))`; `TimeUnit` timeouts → the `Duration`
   versions; `findElementById("x")` → `findElement(By.id("x"))`; `DesiredCapabilities.chrome()` →
   `new ChromeOptions()`.
4. **Pass/fail on the dashboard for plain JUnit 5.** The SDK leaves plain JUnit 5 sessions `done`
   (grey, no name), so add this to each test class that will run, or once in a shared base class
   (Java 8 compatible; imports: `org.junit.jupiter.api.extension.AfterTestExecutionCallback`,
   `org.junit.jupiter.api.extension.RegisterExtension`, `org.openqa.selenium.JavascriptExecutor`):
   ```java
   // Reports each test's name and pass/fail to BrowserStack (the SDK doesn't for plain JUnit 5).
   @RegisterExtension
   AfterTestExecutionCallback markOnBrowserStack = ctx -> {
       if (!(driver instanceof JavascriptExecutor)) return;
       JavascriptExecutor js = (JavascriptExecutor) driver;
       String reason = ctx.getExecutionException().map(Throwable::getMessage).orElse("");
       js.executeScript("browserstack_executor: {\"action\":\"setSessionName\",\"arguments\":{\"name\":\""
               + jsonSafe(ctx.getDisplayName()) + "\"}}");
       js.executeScript("browserstack_executor: {\"action\":\"setSessionStatus\",\"arguments\":{\"status\":\""
               + (ctx.getExecutionException().isPresent() ? "failed" : "passed")
               + "\",\"reason\":\"" + jsonSafe(reason) + "\"}}");
   };

   private static String jsonSafe(String s) {
       if (s == null) return "";
       s = s.replace("\\", "\\\\").replace("\"", "\\\"").replaceAll("[\\r\\n\\t]+", " ");
       return s.length() > 250 ? s.substring(0, 250) : s;
   }
   ```
   Declare it after the `driver` field. For a framework-less `main()`, call the same two executor
   commands in a `finally` block before `driver.quit()`. If the user declines code edits, run
   anyway and mark the sessions from the runner's result instead (see Confirm the run).
5. **`maximize()` on real phones** (only if the plan includes phones): wrap it so it runs on desktop only:
   ```java
   org.openqa.selenium.Platform p = ((org.openqa.selenium.HasCapabilities) driver).getCapabilities().getPlatformName();
   if (p == null || !(p.is(org.openqa.selenium.Platform.ANDROID) || p.is(org.openqa.selenium.Platform.IOS))) driver.manage().window().maximize();
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
projectName: My Selenium Java Tests
buildName: bsk-automate-selenium-java-<timestamp>   # unique per run; keep the bsk- prefix
buildIdentifier: '#${BUILD_NUMBER}'
browserstackLocal: false   # true only for localhost, staging or a private app
debug: true
networkLogs: true
consoleLogs: info
# testObservability: true   # only for TestNG, Cucumber-TestNG or Serenity; it does nothing for plain JUnit 5
```

Check the real-device rows against the live catalog as in step A3, and set `browserstackLocal: true`
only when the tests open `localhost`, a private IP or a staging host (say so in the plan; the SDK
starts the tunnel itself).

Add `log/` to the project's `.gitignore` (create the file if needed) in the same diff.

### B3. Run

- **Maven:** `mvn test` (one class: `mvn test -Dtest=LoginTest`; one module: `mvn -pl <module> test`).
- **Gradle:** `./gradlew test` (or `gradle test`).
- **Plain `main()`:** `mvn test-compile exec:exec`.

Don't add `-q`. These lines also appear on genuine BrowserStack runs and are harmless:
`[ERROR] Surefire is going to kill self fork JVM` (adds about 30 s), SeleniumManager "chromedriver
version … detected in PATH", `Unable to find CDP implementation`, and "Set testReporting: true".

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
  - Plain JUnit 5 and a framework-less `main()` are left `done` by the SDK. That is why B2 adds the
    callback; without it, mark the sessions from the runner's result as shown below.
  - The official sample has no test framework either: if its sessions show `done`, mark each one
    from the run output (each platform prints `Sample test passed!` when its flow succeeds).
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
Ran       : [Sample build: browserstack/vanilla-java-browserstack] or [Your tests: <path>]
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
- **Your own app:** after the sample build, run their own Selenium Java tests; for localhost or staging,
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
| Android: `UnsupportedCommandException … Unable to maximize window` | `maximize()` on a real phone: guard it as in B2, step 5 |
| `int cannot be converted to java.time.Duration` (or `cannot find symbol findElementById`) after upgrading Selenium | Selenium 4 API changes: apply B2, step 3 |
| `agent already loaded` | The agent is attached twice: keep the surefire `argLine` or `browserstack-sdk mvn test`, not both |
| A browser opens on the user's machine; the API shows no build | A driver-manager factory, or an SDK too old for the Selenium version: use `new ChromeDriver()` and the current SDK |
| `pattern matching in instanceof is not supported in -source 8` | Use the Java 8 form of the callback shown in B2, step 4 |
| JaCoCo prints `Unsupported class file major version` | JaCoCo is older than the JDK Maven runs on; harmless when the API shows the sessions passed |

## Quick reference

| Task | Command |
| --- | --- |
| Sample build | `git clone -b sdk-sample https://github.com/browserstack/vanilla-java-browserstack.git && cd vanilla-java-browserstack && mvn test` |
| Your tests (Maven) | `mvn test` with the agent on surefire's `argLine` |
| One test class | `mvn test -Dtest=LoginTest` |
| Your tests (Gradle) | `./gradlew test` |
| Current SDK version | `curl -s https://repo1.maven.org/maven2/com/browserstack/browserstack-java-sdk/maven-metadata.xml \| grep -o '<release>[^<]*'` |
| Docs | https://www.browserstack.com/docs/automate/selenium/getting-started/java |
