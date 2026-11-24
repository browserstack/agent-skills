| `configLoader.js doesn't exist` before any session | The SDK is older than the project's Playwright: update `browserstack-node-sdk`; if needed pin Playwright to `1.64.1` (B2, step 2) |
| `Binary CLI failed to start — running in direct flow` | The SDK's helper timed out; tests still run but sessions are left `done`. Re-run once, then mark from the runner's result |
| iOS: `Only one browser context is allowed` | Real iOS allows one context per session: one test per session, no multi-context tests |
| Tests pass but the API shows no build | Run through `npx browserstack-node-sdk playwright test`, and check for a custom `launch()` or `connect()` (B1) |
