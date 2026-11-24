```bash
npm install
npm run sample-test
```

`npm run sample-test` runs `npx browserstack-node-sdk playwright test --config=./playwright.config.js`:
the SDK runs the sample spec (pages on the-internet.herokuapp.com) on every platform in
`browserstack.yml` (desktop Chrome, WebKit and Firefox), in parallel, and reports pass/fail to
BrowserStack. `npm install` also updates the tracked `package-lock.json`, and its `postinstall`
step updates the SDK to the latest version: list both in the plan. "Uh-oh! We detected some
issues … SDK-GEN-004" about `GLOBAL_AGENT_HTTP_PROXY` is harmless.
