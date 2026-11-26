| Task | Command |
| --- | --- |
| Sample build | `git clone -b main https://github.com/browserstack/xunit-browserstack.git && cd xunit-browserstack/XUnit-BrowserStack && dotnet test --filter "Category=sample-test" -f net10.0` |
| Your tests | `dotnet test <Tests.csproj>` |
| Current SDK version | `curl -s https://api.nuget.org/v3-flatcontainer/browserstack.testadapter/index.json` (last entry) |
| Installed runtimes | `dotnet --list-runtimes` |
| Docs | https://www.browserstack.com/docs/automate/selenium/getting-started/c-sharp |
