1. **Add the BrowserStack SDK package, pinned to the current release** (the last entry of
   `https://api.nuget.org/v3-flatcontainer/browserstack.testadapter/index.json`). An outdated
   adapter can silently run 0 tests on newer .NET, so always use the current one; this changes the `.csproj`:
   ```bash
   dotnet add <path/to/Tests.csproj> package BrowserStack.TestAdapter --version <current>
   ```
2. **Put `browserstack.yml` next to the test `.csproj`** (the file below). The first build also
   creates a `dotnet-tools.json` for the SDK's own `browserstack-sdk` tool, and the SDK writes its
   logs to `log/` next to the `.csproj`: list both in the plan.
3. **Desktop macOS rows use `playwright-webkit`, never `Safari`.** On desktop, Playwright on
   BrowserStack accepts only `chrome`, `edge`, `playwright-chromium`, `playwright-webkit` or
   `playwright-firefox`: a `browserName: Safari` on an `os: OS X` row (the Quick Integration Guide's
   sample config uses one) fails every test on that platform with `Invalid 'browser'`. If the
   project's `browserstack.yml` has one, change it to `playwright-webkit` with `browserVersion: latest`
   (a Safari version such as `15.6` is not a WebKit version) and show the diff. Keep
   `safari` only on real iPhone rows (`deviceName: iPhone …`).
4. **`Microsoft.NET.Test.Sdk` new enough for the Playwright test package.** If the project floats
   `Microsoft.Playwright.NUnit` (or `.MSTest`) and pins `Microsoft.NET.Test.Sdk` below 17.8, restore fails
   with `NU1605: Detected package downgrade`: raise `Microsoft.NET.Test.Sdk` to 17.8 or newer in the plan
   (show the diff).
