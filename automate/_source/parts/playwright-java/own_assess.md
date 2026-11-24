Note these in a short Assessment block at the top of your plan:

- **Build tool:** `pom.xml` → Maven; `build.gradle` / `build.gradle.kts` → Gradle (use `./gradlew`
  if the repo has it). A Gradle project needs Gradle (the wrapper or `gradle`) on this machine:
  if neither works, say what to install and stop. Never convert the build to Maven. In a
  multi-module repo, wire only the module with the Playwright tests.
- **Test framework:** JUnit 5, TestNG or JUnit 4.
- **Playwright version:** `com.microsoft.playwright:playwright`; keep the user's version (never
  `LATEST`).
- **How the browser is created:** `Playwright.create()` with `chromium()`, `firefox()` or
  `webkit()` and `.launch()` (or `.connect()` to a BrowserStack endpoint) is routed by the SDK to
  the platforms in `browserstack.yml`; confirm on the API after the run. `executablePath`,
  `launchPersistentContext` or `connect()` to another endpoint runs on the local machine.
- **Existing BrowserStack wiring or surefire `<argLine>`** (for example JaCoCo): update in place,
  and append the agent rather than replacing an existing `argLine`.
- **Real devices:** a real iPhone is available on request. Real Android phones need BrowserStack's
  device API, which is a code change, so this skill doesn't set them up.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test, pick the test whose name is the nearest step in that flow, and if two are equally close,
  the first by file path. State the pick and why.
