| `dotnet test` finishes with 0 tests run, or runs locally | An outdated `BrowserStack.TestAdapter`: update it to the current release (B2, step 1) |
| `You must install or update .NET to run this application` | The project targets a .NET version that isn't installed: run with `-f <installed version>` |
| Android: `Unable to maximize window` | `Maximize()` on a real phone: guard it as in B2, step 3 |
| NuGet restore fails | Check access to `api.nuget.org` (corporate proxy or feed settings) |
