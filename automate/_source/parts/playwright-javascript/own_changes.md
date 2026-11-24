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
