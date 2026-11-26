1. **Add the BrowserStack Node SDK, pinned exactly** to the current release (`npm view
   browserstack-node-sdk version`), and keep the user's Playwright version; this changes `package.json`:
   ```bash
   npm i -D -E browserstack-node-sdk@<current>
   ```
2. **Only if the SDK can't run their Playwright version** (it fails before any session with
   `configLoader.js doesn't exist`, or BrowserStack rejects the client version): first update the
   SDK; if that doesn't fix it, propose pinning `@playwright/test` and `playwright` to `1.64.1`
   (verified with the SDK on desktop, Android and iPhone in Nov 2026) with `npm i -D -E`. Never
   downgrade further.
3. **`webServer` or localhost targets:** set `browserstackLocal: true` in `browserstack.yml` and say
   so in the plan; the SDK starts the tunnel.
4. **Desktop macOS rows use `playwright-webkit`, never `Safari`.** On desktop, Playwright on
   BrowserStack accepts only `chrome`, `edge`, `playwright-chromium`, `playwright-webkit` or
   `playwright-firefox`: a `browserName: Safari` on an `os: OS X` row (the Quick Integration Guide's
   sample config uses one) fails every test on that platform with `Invalid 'browser'`. If the
   project's `browserstack.yml` has one, change it to `playwright-webkit` and show the diff. Keep
   `safari` only on real iPhone rows (`deviceName: iPhone …`).
