```bash
npm install
npm run sample-test
```

`npm run sample-test` runs `npx browserstack-node-sdk playwright test --config=./playwright.config.js`
on every platform in `browserstack.yml` (desktop Chrome, WebKit and Firefox). This branch is a
demo for BrowserStack's test reporting: its specs in `moduleA`, `moduleB` and `moduleC` (pages on
the-internet.herokuapp.com) include tests named "always failing" and "flaky" that fail on purpose,
next to passing ones and a retry example. Say so in the plan, and in the report count those as
expected failures (see "When sessions failed"). Playwright starts a new worker, and with it a new
session, after every failed test, so expect about 10 to 20 sessions per platform. The deliberate
failures show these errors: `NullPointerError: Cannot read property 'foo' of null`, a wrong
`toHaveTitle`, `Test failed, retrying...` (the retry example) and, for the flaky tests, `Test
timeout of 10000ms exceeded`. On 26 Nov 2026, Firefox also hit `"beforeAll" hook timeout of
10000ms exceeded` in every worker (the sample's 10 s limit is tight for remote Firefox), and two
WebKit connections hung: those are not part of the demo, so report them as real failures. `npm install` also updates the tracked
`package-lock.json`, and its `postinstall` step updates the SDK to the latest version: list both in
the plan. "Uh-oh! We detected some issues … SDK-GEN-004" about `GLOBAL_AGENT_HTTP_PROXY` is
harmless.

Before running, check `browserstack.yml` for a `browserName: Safari` on a desktop (`os:`) row
(`grep -niB3 "browserName: *safari" browserstack.yml`). If there is one, change it to
`playwright-webkit` and list that change in the plan; `safari` stays only on real iPhone rows.
