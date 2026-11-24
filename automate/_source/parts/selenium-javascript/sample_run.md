```bash
npm install
npm run sample-test
```

`npm run sample-test` runs `browserstack-node-sdk mocha test/sample_test.js`: the SDK runs the
Mocha test (adds a product to the cart on bstackdemo.com and checks it is there) on every
platform in `browserstack.yml`, in parallel, and reports pass/fail to BrowserStack. The
`postinstall` step updates the SDK to the latest version.
