1. **Add the BrowserStack SDK package, pinned to the current release** (the last entry of
   `https://api.nuget.org/v3-flatcontainer/browserstack.testadapter/index.json`). An outdated
   adapter can silently run 0 tests on newer .NET, so always use the current one; this changes the `.csproj`:
   ```bash
   dotnet add <path/to/Tests.csproj> package BrowserStack.TestAdapter --version <current>
   ```
2. **Put `browserstack.yml` next to the test `.csproj`** (the file below). The first build also
   creates a `dotnet-tools.json` for the SDK's own `browserstack-sdk` tool, and the SDK writes its
   logs to `log/` next to the `.csproj`: list both in the plan.
3. **`Maximize()` on real phones** (only if the plan includes phones): run it on desktop only:
   ```csharp
   var platformName = (((IHasCapabilities)driver).Capabilities.GetCapability("platformName")?.ToString() ?? "").ToLowerInvariant();
   if (platformName != "android" && platformName != "ios") driver.Manage().Window.Maximize();
   ```
