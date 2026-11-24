| Logs show `unpatched method`; a browser opens locally | The SDK patched Playwright instead of Selenium: remove Playwright from `node_modules` for the run (B2, step 2) |
| Tests run locally with bare `npx mocha` or `npm test` | Run through the SDK: `npx browserstack-node-sdk mocha …` |
| Android: `Unable to maximize window` | `maximize()` on a real phone: guard it as in B2, step 3 |
| SDK log upload fails on old Node | Use Node 20 or newer |
