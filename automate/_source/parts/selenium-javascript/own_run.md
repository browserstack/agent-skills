- **Mocha:** `npx browserstack-node-sdk mocha <spec or glob> --timeout 60000` (keep any flags
  from the user's `npm test` script).
- **Jest:** `npx browserstack-node-sdk jest <path>`.

These also appear on genuine BrowserStack runs and are harmless: `npm error code ELSPROBLEMS …
missing: @playwright/test` after the clash step, `EBADENGINE` warnings (current
`selenium-webdriver` asks for Node 22+, but runs on Node 20), and "loadModules: skipping driver
module for selenium-webdriver".
