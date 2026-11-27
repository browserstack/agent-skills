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
