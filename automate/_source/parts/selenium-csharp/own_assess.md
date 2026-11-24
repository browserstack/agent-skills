Note these in a short Assessment block at the top of your plan:

- **Project:** the test `.csproj` (and the solution, if any), its `TargetFramework(s)`, and the test
  framework from its packages: NUnit, xUnit or MSTest.
- **Selenium version:** `Selenium.WebDriver` 4.x is required.
- **How the driver is created:** `new RemoteWebDriver(new Uri(...), options)` (the pattern the
  official sample uses) and `new ChromeDriver()` are expected to be routed by the SDK. After the
  run, confirm sessions appear on the API; if a custom factory keeps them local, propose the
  sample's `RemoteWebDriver` pattern instead.
- **`Maximize()` calls:** real Android phones reject them, so they matter only if the plan
  includes phones.
- **Which tests to run:** the ones the user named (as a `dotnet test --filter`); otherwise all. If
  they named a flow that has no test, pick the test whose name is the nearest step in that flow,
  and if two are equally close, the first by file path. State the pick and why.
