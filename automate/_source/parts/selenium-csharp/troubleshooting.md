| `dotnet test` finishes with 0 tests run, or runs locally | An outdated `BrowserStack.TestAdapter`: update it to the current release (B2, step 1) |
| `You must install or update .NET to run this application` | The project targets a .NET version that isn't installed: run with `-f <installed version>` |
| Android: `Unable to maximize window` | `Maximize()` on a real phone: guard it as in B2, step 3 |
| Sample build: some or all platforms fail with `NoSuchElementException` on `//*[@id="1"]/p` | The sample has no waits (on 26 Nov it failed on 2 of 3 platforms in two runs and on all 3 in a third). If only some failed, re-run once with a new build name; if the same platforms fail again, or all failed, it is the sample: report it and offer the user's own tests (see "When sessions failed") |
| `No test matches the given testcase filter` at the end of the output | Harmless: the filter is also applied to the solution's other test assemblies. Judge the run by the API |
| Test host crashed with `JsonReaderException … AtomicFile`, or the output shows another project's tests | Another .NET SDK run is active on this machine (they share `$TMPDIR/.browserstack/`, which also holds a copy of the credentials): run one at a time, and trust the API |
| iOS: `FindElements` returns nothing right after a page load | Real iOS Safari doesn't apply the implicit wait to `FindElements`: the test needs an explicit wait (ask before changing it) |
| NuGet restore fails | Check access to `api.nuget.org` (corporate proxy or feed settings) |
