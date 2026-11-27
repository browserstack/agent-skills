Before installing, fix the sample's one stale locator. It is the only change this skill makes to
the sample's code: list it in the plan, and show the diff once applied. `tests/bstack_test_demo.js` opens the
Dropdown page with `getByRole('link', { name: 'Dropdown' })`, and the demo site
(the-internet.herokuapp.com) now also lists "Custom Dropdown" and "Multiple Select Dropdown", so
without `exact: true` the test stops with `strict mode violation: … resolved to 3 elements` on
every platform:

```bash
if grep -q "{ name: 'Dropdown' }" tests/bstack_test_demo.js; then
  sed -i.bak "s/{ name: 'Dropdown' }/{ name: 'Dropdown', exact: true }/" tests/bstack_test_demo.js && rm -f tests/bstack_test_demo.js.bak
fi
git diff tests/
```

If the diff is empty, BrowserStack has fixed the sample already: carry on without the change. Then:

```bash
npm install
npm run sample-test
```

`npm run sample-test` runs `npx browserstack-node-sdk playwright test --config=./playwright.config.js`:
one test (open the-internet.herokuapp.com, tick and untick two checkboxes, pick an option from the
dropdown) on every platform in `browserstack.yml` (desktop Chrome, WebKit and Firefox), one session
each. `npm install` also updates the tracked `package-lock.json`, and its `postinstall` step updates
the SDK to the latest version: list both in the plan. These lines are harmless: "Uh-oh! We
detected some issues … SDK-GEN-004" about `GLOBAL_AGENT_HTTP_PROXY` or `GLOBAL_AGENT_NO_PROXY`, and
`[UNDICI-EHPA] Warning: EnvHttpProxyAgent is experimental` (even when printed as an `error:` line).

The Quick Integration Guide clones this repo's `tra` branch instead: a demo of BrowserStack's test
reporting whose tests fail on purpose. This skill runs `main`, whose one test passes once the
locator is fixed.

When you read the sample's `browserstack.yml` for the plan, look for a `browserName: Safari` on a
desktop (`os:`) row. If there is one, list the change to `playwright-webkit` with
`browserVersion: latest` in the plan, and make it after cloning, before running (find it with
`grep -niB3 "browserName: *safari" browserstack.yml`); `safari` stays only on real iPhone rows.
