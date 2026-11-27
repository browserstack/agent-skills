---
name: browserstack-automate-playwright-java
description: >-
  Runs Playwright tests written in Java on BrowserStack Automate (real desktop browsers, with a real iPhone on request)
  from one pasted prompt: either BrowserStack's official Playwright Java sample build, or the user's own
  Playwright Java tests with no changes to their test logic. Checks credentials without printing them,
  shows a plan and waits for approval, runs the build, confirms it on the BrowserStack API and
  returns the dashboard link. Use when the user asks to run Playwright Java tests on BrowserStack, set up
  BrowserStack Automate for a Playwright Java project, or mentions Playwright with Java, com.microsoft.playwright, Maven, Gradle, JUnit 5, TestNG, browserstack-java-sdk or browserstack.yml. Not for other languages
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

# BrowserStack Automate — Playwright Java skill

You are a senior QA automation engineer with access to the user's shell and files. Do the work
yourself (clone, install, edit, run) instead of handing commands to the user, but only after the
user approves your plan.

## Step 1: Is this the right skill? (before anything else)

Look at the folder the user is in and its subfolders (read-only). This skill is for
**Playwright Java**: `pom.xml` or `build.gradle` that depends on `com.microsoft.playwright`.

- Empty folder, or the user asked for the sample build → right skill, continue.
- A Playwright Java project → right skill, continue.
- A project in another language or framework → stop without changing anything. If you already
  saved this skill into the project's skills folder, remove that folder again (and the skills
  folder above it if that leaves it empty and you created it). Tell the user in one line what you found and that this skill is for Playwright Java, then give them the prompt for the right
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
  - **Playwright C#** (a `.csproj` that references `Microsoft.Playwright` (NUnit, MSTest or xUnit)):
    `Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-csharp/SKILL.md, then follow that skill to run my own Playwright C# tests on BrowserStack Automate.`

  For anything else (Ruby, PHP, WebdriverIO, Nightwatch or Cypress) there is no skill yet: point
  the user to https://www.browserstack.com/docs/automate and stop.
- A mixed project (for example Java and Python tests): work only on the Playwright Java part, and name the
  skill that covers the rest.

## Step 2: Install this skill (once)

Skip this step if `browserstack-automate-playwright-java/SKILL.md` already exists in your skills folder (for example
`.claude/skills/`, `.cursor/skills/`, `.github/skills/` or `.agents/skills/`; use the
project-level folder your agent uses) and passes the check in item 3.

1. Create the folder `browserstack-automate-playwright-java` in your skills folder and download this file into it as `SKILL.md`.
   Replace `<skills-folder>` with the absolute path of your agent's project-level skills folder:
   ```bash
   D="<skills-folder>/browserstack-automate-playwright-java"
   if ! mkdir -p "$D"; then
     echo "INSTALL FAILED: cannot create $D"; false
   elif curl -fsSL https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-java/SKILL.md -o "$D/SKILL.md.part"; then
     mv "$D/SKILL.md.part" "$D/SKILL.md" && echo "INSTALLED: $D/SKILL.md"
   else
     rm -f "$D/SKILL.md.part"; echo "DOWNLOAD FAILED"; false
   fi
   ```
   Go by the printed line. In the steps below, write the full path, since `$D` doesn't carry over
   to your next command.
2. **If it printed `DOWNLOAD FAILED`** (no network, or an HTTP error such as 404), install the copy
   you are following instead: write this file's full text, unchanged, to
   `<skills-folder>/browserstack-automate-playwright-java/SKILL.md` (if you have
   it as a file on disk, copy that file). Save it only if you have every line, from the opening `---`
   to the last line, `<!-- end of browserstack-automate-playwright-java -->`; a summary or shortened page (some web tools return
   one) is not the skill.
3. **Check the installed file** (either way):
   ```bash
   sed -n 1,2p "<skills-folder>/browserstack-automate-playwright-java/SKILL.md"; tail -n 1 "<skills-folder>/browserstack-automate-playwright-java/SKILL.md"
   ```
   Expect `---`, `name: browserstack-automate-playwright-java` and `<!-- end of browserstack-automate-playwright-java -->`. If any is missing, delete that
   `SKILL.md` and follow the paragraph below.
4. Tell the user in one line that the skill is installed (from GitHub, or from the copy you were
   given) and stays installed for future sessions, then continue in this session. Do not ask them
   to restart.

If you can't install a complete copy (no writable skills folder, or only partial text), remove the
empty folder (`rmdir "<skills-folder>/browserstack-automate-playwright-java"`), say so in one line and carry on using this file for this session only.
Installing is a convenience; never block the run on it. To update the skill later, delete the
folder and run the prompt again.

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
   - Toolchain: `java -version` (11+), the project's build tool (`mvn -version` for Maven; `./gradlew -v` or `gradle -v` for Gradle), `git --version`. If something is missing, say what to install and stop.
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
     curl -fsSL https://raw.githubusercontent.com/browserstack/java-playwright-browserstack/main/browserstack.yml
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

- The prompt says **"sample build"**, or the folder has no Playwright Java tests → **Path A: sample build**.
- The prompt says **"my own Playwright Java tests"**, or the folder has Playwright Java tests → **Path B: your own tests**.
  If the user asked for their own tests but you find none, say so, offer the sample build and stop.

## Path A: sample build

This runs BrowserStack's official Playwright Java sample from the repo the in-product Quick
Integration Guide uses (https://www.browserstack.com/docs/onboarding-cad/playwright-qig/java-sdk/getting-started): `browserstack/java-playwright-browserstack`, branch `main`,
on the platforms it ships with.

### A1. Prerequisites

```bash
java -version    # 11 or newer
mvn -version     # Maven on PATH
git --version
```
If any is missing, tell the user what to install and stop.

### A2. Clone the official sample into a new folder

```bash
git clone -b main https://github.com/browserstack/java-playwright-browserstack.git
cd java-playwright-browserstack
```

If `java-playwright-browserstack` already exists, clone into `java-playwright-browserstack-$(date +%Y%m%d-%H%M%S)` instead.
Never overwrite a folder the user may have changed.

### A3. Point `browserstack.yml` at this run

Change only these two lines of `browserstack.yml` (A4 names any other change a sample needs), and
leave the rest as BrowserStack ships it:

```bash
BUILD_NAME="bsk-automate-playwright-java-sample-$(date +%Y%m%d-%H%M%S)"
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
mvn compile
mvn test -P sample-test
```

The `sample-test` profile attaches the BrowserStack Java SDK as a `-javaagent` and runs
`SampleTest` (adds a product to the cart on bstackdemo.com and checks the cart) with JUnit 5 on
every platform in `browserstack.yml` (desktop Chrome, Firefox and WebKit), in parallel. Don't add
`-q`; if the output is long, read the `Tests run:` and `BUILD` lines. Warnings about the deprecated
`LATEST` versions in the sample's `pom.xml`, and the SDK's "Both Selenium and Playwright detected"
warning, are harmless. The sample test catches its own exceptions, so an `Exception: …` line in
the output means the sample is out of date even when the sessions show `passed`: report it as in
"When sessions failed".

When you read the sample's `browserstack.yml` for the plan, look for a `browserName: Safari` on a
desktop (`os:`) row. If there is one, list the change to `playwright-webkit` with
`browserVersion: latest` in the plan, and make it after cloning, before running (find it with
`grep -niB3 "browserName: *safari" browserstack.yml`); `safari` stays only on real iPhone rows.

Then go to **Confirm the run on BrowserStack** and **Report**.

## Path B: your own tests

Run the user's existing Playwright Java tests on BrowserStack with no changes to their test logic.

### B1. Assess the project (read-only, before your plan)

Note these in a short Assessment block at the top of your plan:

- **Build tool:** `pom.xml` → Maven; `build.gradle` / `build.gradle.kts` → Gradle (use `./gradlew`
  if the repo has it). A Gradle project needs Gradle (the wrapper or `gradle`) on this machine:
  if neither works, say what to install and stop. Never convert the build to Maven. In a
  multi-module repo, wire only the module with the Playwright tests.
- **Test framework:** JUnit 5, TestNG or JUnit 4.
- **Playwright version:** `com.microsoft.playwright:playwright`; keep the user's version; if the pom says
  `LATEST`, pin it to the version that resolves today and show the diff.
- **How the browser is created:** `Playwright.create()` with `chromium()`, `firefox()` or
  `webkit()` and `.launch()` (or `.connect()` to a BrowserStack endpoint) is routed by the SDK to
  the platforms in `browserstack.yml`; confirm on the API after the run. `executablePath`,
  `launchPersistentContext` or `connect()` to another endpoint runs on the local machine.
- **Existing BrowserStack wiring or surefire `<argLine>`** (for example JaCoCo): update in place,
  and append the agent rather than replacing an existing `argLine`.
- **Real iPhone (on request, as its own build):** for that run, use only this platform in
  `browserstack.yml` with a new `buildName` (check it against the live catalog as in step A3), and
  put the desktop rows back afterwards if the user wants both:
  ```yaml
  platforms:
    - deviceName: iPhone 15
      osVersion: 17
      browserName: safari
  ```
  The SDK routes a standard `launch()` to it and names and marks the session (verified Nov 2026).
- **Real Android:** needs BrowserStack's Playwright Android device API, which is a code change, so
  this skill doesn't set it up. Never add an Android row: a device session still starts and ends
  in `error` (see Troubleshooting). Point the user to https://www.browserstack.com/docs/automate/playwright/playwright-android.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test, pick the test whose name is the nearest step in that flow, and if two are equally close,
  the first by file path. State the pick and why.

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
       <version>3.8.1</version>
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
   - **Gradle (JUnit 5):** don't put the agent on the `test` task: inside Gradle's test worker the
     SDK can run only one platform, and the others stop with `java.io.EOFException … GradleWorkerMain`.
     Add a separate task that runs the same tests through the JUnit console launcher in a plain JVM,
     and leave the `test` task as it is:
     ```groovy
     dependencies {
       testImplementation 'com.browserstack:browserstack-java-sdk:CURRENT_RELEASE'
       testRuntimeOnly 'org.junit.platform:junit-platform-console'   // version comes from the JUnit BOM
     }
     // Runs the JUnit 5 tests on every platform in browserstack.yml: gradle browserstackTest
     tasks.register('browserstackTest', JavaExec) {
       dependsOn 'testClasses'
       classpath = sourceSets.test.runtimeClasspath
       mainClass = 'org.junit.platform.console.ConsoleLauncher'
       args 'execute', '--scan-classpath', '--include-classname', '.*', '--disable-banner', '--details=tree'
       doFirst { jvmArgs "-javaagent:${classpath.find { it.name.contains('browserstack-java-sdk') }.absolutePath}" }
     }
     ```
     `execute` needs JUnit 5.10 or newer; on an older JUnit 5, leave it out. For one class, replace
     `'--scan-classpath', '--include-classname', '.*'` with `'--select-class', 'com.example.LoginTest'`.
     Don't add BrowserStack's `com.browserstack.gradle-sdk` plugin: with the current SDK no session
     starts. Verified with the Groovy DSL on Gradle 9.9.2 (Nov 2026); for `build.gradle.kts`, write
     the same task in Kotlin and say it is unverified.
   - **Gradle (TestNG):** TestNG runs every platform inside the one test JVM, so the agent can go on
     Gradle's own `test` task (verified on Gradle 9.9.2, Nov 2026, Selenium and Playwright; the SDK names and marks each
     session):
     ```groovy
     dependencies { testImplementation 'com.browserstack:browserstack-java-sdk:CURRENT_RELEASE' }
     test {
       useTestNG()
       doFirst { jvmArgs "-javaagent:${classpath.find { it.name.contains('browserstack-java-sdk') }.absolutePath}" }
     }
     ```
     Run it with `gradle test` and set `framework: testng` in `browserstack.yml`.
   - **Gradle (JUnit 4):** don't put the agent on the `test` task: the SDK's per-platform JVMs fail
     there and no build is created at all. Run the tests through `JUnitCore` in a separate task, and
     leave `test` as it is:
     ```groovy
     dependencies { testImplementation 'com.browserstack:browserstack-java-sdk:CURRENT_RELEASE' }
     // Runs the JUnit 4 tests on every platform in browserstack.yml: gradle browserstackTest
     tasks.register('browserstackTest', JavaExec) {
       dependsOn 'testClasses'
       classpath = sourceSets.test.runtimeClasspath
       mainClass = 'org.junit.runner.JUnitCore'
       args 'com.example.LoginTest', 'com.example.CartTest'   // every test class to run, fully qualified
       doFirst { jvmArgs "-javaagent:${classpath.find { it.name.contains('browserstack-java-sdk') }.absolutePath}" }
     }
     ```
     `JUnitCore` doesn't scan for tests, so list each test class (or one `@RunWith(Suite.class)`
     class). Set `framework: junit4` in `browserstack.yml`. Verified on Gradle 9.9.2 with Selenium
     (Nov 2026); for Playwright with JUnit 4, say it is unverified. Neither TestNG nor JUnit 4 needs an extra dependency on Gradle 9.
   - Never also run through `browserstack-sdk mvn test`: attaching the agent twice fails with
     "agent already loaded".
3. **Set `framework`** in `browserstack.yml` to the test framework (`junit5`, `testng` or `junit4`).
4. **Desktop macOS rows use `playwright-webkit`, never `Safari`.** On desktop, Playwright on
   BrowserStack accepts only `chrome`, `edge`, `playwright-chromium`, `playwright-webkit` or
   `playwright-firefox`: a `browserName: Safari` on an `os: OS X` row (the Quick Integration Guide's
   sample config uses one) fails every test on that platform with `Invalid 'browser'`. If the
   project's `browserstack.yml` has one, change it to `playwright-webkit` with `browserVersion: latest`
   (a Safari version such as `15.6` is not a WebKit version) and show the diff. Keep
   `safari` only on real iPhone rows (`deviceName: iPhone …`).

Add a `browserstack.yml` next to the build file of the project or module whose tests run (in a
multi-module repo, that module, not the parent). If the project already has BrowserStack wiring
(a `browserstack.yml`, an SDK dependency, an SDK agent), update it in place and show the diff
instead of adding a second copy: give it a unique `bsk-` `buildName` (the API check depends on it),
and if it has `browserstackLocal: true` while the tests open only public URLs, set it to `false`.
Leave out tests that need BrowserStack Local or a local server the user hasn't started (for
example a sample's `*local*` test), and say so. By default the file runs on Windows 11 Chrome, macOS Sequoia WebKit and Windows 11 Firefox; the user
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
projectName: My Playwright Java Tests
buildName: bsk-automate-playwright-java-<timestamp>   # unique per run; keep the bsk- prefix
buildIdentifier: '#${BUILD_NUMBER}'
browserstackLocal: false   # true only for localhost, staging or a private app
debug: true
networkLogs: true
consoleLogs: info
framework: junit5   # or testng / junit4: the project's test framework
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

- **Maven:** `mvn test` (one class: `mvn test -Dtest=CartTest`; one module: `mvn -pl <module> test`).
- **Gradle with TestNG:** `./gradlew test` (or `gradle test`), with the agent on `test` (B2).
  Gradle prints no per-test lines on success: take the counts from
  `build/test-results/test/TEST-*.xml`.
- **Gradle with JUnit 5 or JUnit 4:** `./gradlew browserstackTest` (or `gradle browserstackTest`), the task from B2.
  JUnit 5's console launcher prints one test tree per platform: read its "tests successful" /
  "tests failed" lines and `BUILD`. JUnit 4's `JUnitCore` prints `OK (N tests)`, or `FAILURES!!!`
  with `Tests run: N, Failures: M`, once per platform.

Don't add `-q`. If the output is long, save it to a file and read the `Tests run:` and `BUILD`
lines. Playwright may download its driver on the first run, and older surefire versions print
`[ERROR] Surefire is going to kill self fork JVM` (about 30 s); so is a `*** java.lang.instrument
ASSERTION FAILED ***: "!errorOutstanding"` line under Gradle. All are harmless when the build
succeeds and the API shows the sessions.

Then go to **Confirm the run on BrowserStack** and **Report**.

## Confirm the run on BrowserStack

The test runner's "passed" and the dashboard link the SDK prints are **not proof**: the SDK can
print a link when no session was created. Check the BrowserStack API yourself:

```bash
BUILD_NAME="<the buildName you set>"
curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" "https://api.browserstack.com/automate/builds.json?limit=100" \
  | python3 -c "import sys,json; n=sys.argv[1]; [print(b['automation_build']['hashed_id'], b['automation_build']['name']) for b in json.load(sys.stdin) if b['automation_build']['name'].startswith(n)]" "$BUILD_NAME"
curl -su "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" "https://api.browserstack.com/automate/builds/<hashed_id>/sessions.json?limit=100" \
  | python3 -c "import sys,json; [print(' '.join(str(a[k]) for k in ('device','os','os_version','browser','browser_version') if a.get(k)), '|', a['status'], '|', a.get('name')) for a in (s['automation_session'] for s in json.load(sys.stdin))]"
```

- The sessions call returns 10 sessions unless you pass `limit` (as above); for builds with more
  than 100 sessions, page on with `&offset=100`.
- Match the build by **prefix**: the SDK appends an identifier, so `bsk-…-0930` shows up as
  `bsk-…-0930  1` (the number varies). Ask for `limit=100`, since a busy account fills the
  default 10 within minutes. If more than one build matches (a shared account), use the
  hashed_id from the SDK's `View build on BrowserStack dashboard` line, or the build whose
  sessions match your platforms and start time. If nothing matches after a long run, take the
  hashed_id from that line too, or page on with `&offset=100`, `&offset=200`.
- **No matching build, or 0 sessions** → the tests did not reach BrowserStack. Read the SDK's own
  logs in the `log/` folder next to `browserstack.yml` (mask the key first) before guessing; then
  see Troubleshooting. Report what stopped the run and the fix, without a dashboard link.
- **Each session's `status`:** `passed` or `failed` means the result reached the dashboard. Report
  from the sessions: the build's own `status` can read `failed` or `done` while every session passed (for
  example when a test closes Playwright without closing the browser). If the test runner reports
  a failed test for a platform whose session shows `passed`, trust the runner: mark that session
  `failed` with the runner's message (below) and say so in the report. The SDK has been seen
  marking a timed-out test `passed`.
  **`done` means the session ran but nobody reported pass or fail**: never report it as a pass.
  A session whose only failure was a `beforeAll` hook is also left `done` and unnamed: report the
  runner's hook error for that platform.
  - If sessions show `done`, the SDK didn't report the result: mark each from the runner's result
    as shown below (session names carry the test name when the SDK set them; otherwise one test per
    platform maps one-to-one).
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
Ran       : [Sample build: browserstack/java-playwright-browserstack] or [Your tests: <path>]
Result    : <N> of <M> sessions passed (from the BrowserStack API)
Platforms : <browser · OS — passed/failed, one per line; with several tests per platform, passed of total;
            a platform that never got a session: "no session" and the runner's error>
Build     : <build name>
Dashboard : https://automate.browserstack.com/dashboard/v2/builds/<hashed_id>
============================================================
```

Test runners count tests, not sessions: a test that fails on one platform shows as one failed
test. When a run has many tests per platform and each failed test ends its session (Playwright
starts a new worker after a failure), lead the Platforms line with the runner's test counts. The API count above is the result. Each session on the dashboard has its video and text
logs, plus network and console logs when `browserstack.yml` turns them on.

## When sessions failed

Report failures as results. Don't change test code to make them pass unless the user asks.

- **Sample build:** never edit BrowserStack's sample beyond the fixes A4 names.
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
- **Real iPhone:** add a real iPhone 15 (Safari) as its own build (B1 has the row and how). After
  an iPhone-only run, offer the desktop build instead. Set expectations first:
  Playwright on real iOS is a custom WebKit integration with limits (for example one browser
  context per session, and some keyboard and multi-tab behaviour differs from desktop WebKit), so
  a failure there doesn't change the desktop results. Real Android phones need BrowserStack's device API rather
  than a normal browser launch, so this skill doesn't set them up: see https://www.browserstack.com/docs/automate/playwright/playwright-android.
- **Wider coverage:** add Edge, older browser versions or other operating systems.
- **Your own app:** after the sample build, run their own Playwright Java tests; for localhost or staging,
  turn on BrowserStack Local.
- **On every push:** add a CI job (GitHub Actions, Jenkins, GitLab) that runs this on BrowserStack.

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| Tests pass locally but the API shows no build | The run did not go through the BrowserStack SDK. Check the run command and wiring below, and read `log/sdk-cli.log`, or `log/browserstack-javaagent.log` if there is none (mask the key) |
| Every session fails to start with `[browserstack.local] is set to true but local testing through BrowserStack is not connected` | The Local binary could not start (in `log/sdk-cli.log`: `Local.start … spawn …`; error `-86` = an Intel binary on Apple silicon without Rosetta). Public site → `browserstackLocal: false`. Private app → point `browserStackLocalOptions.binarypath` at BrowserStack's native Apple-silicon binary (see Private apps) and re-run |
| `All parallel tests are currently in use` | The plan's parallel limit is reached; lower `parallelsPerPlatform` or wait |
| `Browser/OS combination not supported` | A retired device or OS version: re-check the catalog (step A3), swap to the closest current one and re-run once |
| Session fails to start with a connect timeout while parallels are free | Usually transient: re-run once. If it repeats, the network may block `*.browserstack.com` (allow outbound HTTPS) |
| `agent already loaded` | The agent is attached twice: keep the surefire `argLine` or `browserstack-sdk mvn test`, not both |
| A browser opens on the user's machine; the API shows no build | The launch wasn't routed: check the agent is on surefire's `argLine` (Maven) or on the `browserstackTest` task (Gradle), and the test uses a standard `launch()` |
| iOS: `Only one browser context is allowed` | Real iOS allows one context per session: one test per session, no multi-context tests |
| Real Android: `PlaywrightException: Cannot find parent object android@… to create android-device@…` at `launch()` | A standard `launch()` can't drive real Android, though the device session still starts (`error` / `ABRUPT_CLOSE`): remove the Android row (B1) |
| Gradle: only one platform gets a session and the output shows `java.io.EOFException … GradleWorkerMain` | The agent is on Gradle's `test` task, where the SDK can drive one platform. Use the `browserstackTest` task from B2 |
| Gradle 9: `Failed to load JUnit Platform … including the JUnit Platform launcher` | Gradle 9 no longer adds the launcher; it is the project's build, not BrowserStack. `browserstackTest` brings it in through `junit-platform-console`. For `gradle test` the project needs `testRuntimeOnly 'org.junit.platform:junit-platform-launcher'` (show it as a diff and ask) |
| No output for several minutes, and the API shows no session yet for one platform | The browser connection is slow to start (Ventura Chrome took 3 to 5 minutes on 26 Nov 2026) or has hung. Wait up to 10 minutes; then press Ctrl-C once. Maven then exits 130 with no summary, and the build link is in `log/browserstack-javaagent.log` |
| `Tests run: 0` with `BUILD SUCCESS`, or an empty "View build" link | Nothing reached BrowserStack (for example the disk filled up during the run): fix the cause and re-run; never report it as a pass |
| `Invalid 'browser'. Use 'chrome', 'edge', 'playwright-chromium', 'playwright-webkit' or 'playwright-firefox' only` | A desktop row has `browserName: Safari` (the Quick Integration Guide's config uses it): change it to `playwright-webkit` with `browserVersion: latest`. Keep `safari` only on real iPhone rows |
| `browserType.connect: Error: Unsupported browser version` on a `playwright-webkit` row | The row kept a Safari version (for example `15.6` from the Quick Integration Guide's config): set `browserVersion: latest` |
| Gradle with JUnit 4: `BUILD FAILED` with `java.io.EOFException` or `OutOfMemoryError` in `GradleWorkerMain`, and no build on the API | The agent is on Gradle's `test` task, where JUnit 4 can't run under the SDK. Use the `browserstackTest` JavaExec task from B2 |
| A Gradle daemon is still running after the build | The SDK runs `gradle dependencies` to write `log/dependency-tree.log`, which starts one. Harmless; stop it with `gradle --stop` |

## Quick reference

The sample-build row leaves out the A3 and A4 edits to `browserstack.yml`; for a real run follow
A2 to A4.

| Task | Command |
| --- | --- |
| Sample build | `git clone https://github.com/browserstack/java-playwright-browserstack.git && cd java-playwright-browserstack && mvn compile && mvn test -P sample-test` |
| Your tests (Maven) | `mvn test` with the agent on surefire's `argLine` |
| Your tests (Gradle, JUnit 5 or 4) | `./gradlew browserstackTest` (the task from B2) |
| Your tests (Gradle, TestNG) | `./gradlew test` with the agent on `test` (B2) |
| Current SDK version | `curl -s https://repo1.maven.org/maven2/com/browserstack/browserstack-java-sdk/maven-metadata.xml \| grep -o '<release>[^<]*'` |
| Docs | https://www.browserstack.com/docs/automate/playwright/getting-started/java |

<!-- end of browserstack-automate-playwright-java -->
