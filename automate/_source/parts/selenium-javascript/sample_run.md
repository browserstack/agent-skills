```bash
npm install
npm run sample-test
```

`npm run sample-test` runs the Mocha test `test/sample_test.js` through `browserstack-node-sdk`
(adds a product to the cart on bstackdemo.com and checks it is there) on every platform in
`browserstack.yml`, in parallel, and reports pass/fail to BrowserStack. `npm install` also
updates the tracked `package-lock.json`, and its `postinstall` step updates the SDK to the latest
version: list both in the plan. `EBADENGINE` warnings and `[UNDICI-EHPA] Warning:
EnvHttpProxyAgent is experimental` are harmless.
