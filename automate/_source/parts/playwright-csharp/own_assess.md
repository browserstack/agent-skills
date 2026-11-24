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
