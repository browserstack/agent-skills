| `dotnet test` finishes with 0 tests run, or runs locally | An outdated `BrowserStack.TestAdapter`: update it to the current release (B2, step 1) |
| `You must install or update .NET to run this application` | The project targets a .NET version that isn't installed: run with `-f <installed version>` |
| Android: `Unable to maximize window` | `Maximize()` on a real phone: guard it as in B2, step 3 |
| Sample build: some platforms fail with `NoSuchElementException` on `//*[@id="1"]/p` | The sample has no waits: re-run once with a new build name. If the same platforms fail again (Windows 10 Edge and the Galaxy S22 Ultra did on 26 Nov), it is the sample on those platforms: report it and offer the user's own tests (see "When sessions failed") |
| Test host crashed with `JsonReaderException … AtomicFile`, or the output shows another project's tests | Another .NET SDK run is active on this machine (they share `$TMPDIR/.browserstack/`, which also holds a copy of the credentials): run one at a time, and trust the API |
| iOS: `FindElements` returns nothing right after a page load | Real iOS Safari doesn't apply the implicit wait to `FindElements`: the test needs an explicit wait (ask before changing it) |
| NuGet restore fails | Check access to `api.nuget.org` (corporate proxy or feed settings) |
