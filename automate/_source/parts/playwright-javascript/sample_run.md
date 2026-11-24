```bash
npm install
npm run sample-test
```

`npm run sample-test` runs `npx browserstack-node-sdk playwright test --config=./playwright.config.js`:
the SDK runs the sample spec (checkboxes and a dropdown on the-internet.herokuapp.com) on every
platform in `browserstack.yml` (desktop Chrome, WebKit and Firefox), in parallel, and reports
pass/fail to BrowserStack.
