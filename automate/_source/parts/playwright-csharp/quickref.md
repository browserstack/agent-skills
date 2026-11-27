| Task | Command |
| --- | --- |
| Sample build | `git clone https://github.com/browserstack/csharp-playwright-browserstack.git && cd csharp-playwright-browserstack/CSharp-Playwright-BrowserStack && NoWarn=NU1605 DOTNET_ROLL_FORWARD=Major dotnet test --filter "Category=sample-test"` |
| Your tests | `dotnet build <Tests.csproj> && dotnet test <Tests.csproj>` |
| Current SDK version | `curl -s https://api.nuget.org/v3-flatcontainer/browserstack.testadapter/index.json` (last entry) |
| Installed runtimes | `dotnet --list-runtimes` |
| Docs | https://www.browserstack.com/docs/automate/playwright/getting-started/c-sharp |
