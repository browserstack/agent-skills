| `failed to setup playwright: No module named 'playwright._impl._connection'`, then no build on the API | The SDK can't hook this Playwright version (1.65 or newer, Nov 2026): install `playwright==1.64.1` in the `.venv` and re-run. This shows in the console, not in `log/`, so read both |
| `Executable doesn't exist … playwright install` | The SDK didn't take over the launch: either the run didn't start with `.venv/bin/browserstack-sdk`, or the SDK can't hook this Playwright version (row above) |
| Tests run on the user's machine and the API shows no build | The user's Selenium packages in the same environment, or a custom launch: use the separate `.venv` (B2) and the standard fixtures |
| Sessions have no name and stay `done` | The SDK detected the wrong framework: set `framework: pytest` (or `behave`) in `browserstack.yml` |
| macOS Ventura WebKit: `LocatorAssertions.to_have_count` fails with an empty message | Seen on every Ventura WebKit run of the sample (Nov 2026): use macOS Sequoia for WebKit |
| iOS: `Only one browser context is allowed` | Real iOS allows one context per session: one test per session, no multi-context tests |
