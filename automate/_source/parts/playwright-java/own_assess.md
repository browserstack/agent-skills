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
