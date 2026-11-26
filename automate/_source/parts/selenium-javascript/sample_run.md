```bash
npm install
npm run sample-test
```

`npm run sample-test` runs `browserstack-node-sdk jest src/sample.test.js`: the SDK runs the two
Jest tests (a sign-in with a locked account that expects the "Your account has been locked." error,
and adding a product to the cart on bstackdemo.com) on every platform in `browserstack.yml`, in
parallel, and reports pass/fail to BrowserStack. `npm install` also updates the tracked
`package-lock.json` and `yarn.lock`, and its `postinstall` step updates the SDK to the latest version: list both
in the plan. `EBADENGINE` warnings, `[UNDICI-EHPA] Warning: EnvHttpProxyAgent is experimental` and
`ACCESSIBILITY Build creation failed` are harmless.
