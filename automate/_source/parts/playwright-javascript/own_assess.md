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
