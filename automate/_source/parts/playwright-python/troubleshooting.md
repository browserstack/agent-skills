| `Executable doesn't exist … playwright install` | The run didn't go through the SDK: start it with `.venv/bin/browserstack-sdk pytest` |
| Tests run on the user's machine and the API shows no build | Selenium in the same environment, or a custom launch: use a Playwright-only `.venv` (B2) and the standard fixtures |
| Sessions have no name and stay `done` | The SDK detected the wrong framework: set `framework: pytest` (or `behave`) in `browserstack.yml` |
| iOS: `Only one browser context is allowed` | Real iOS allows one context per session: one test per session, no multi-context tests |
