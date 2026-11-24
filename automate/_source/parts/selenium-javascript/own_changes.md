1. **Add the BrowserStack Node SDK, pinned exactly** to the current release (`npm view
   browserstack-node-sdk version`); this changes `package.json`:
   ```bash
   npm i -D -E browserstack-node-sdk@<current>
   ```
   If the repo has no lockfile, this also creates `package-lock.json`: say so in the plan.
2. **Framework clash** (only if Playwright is installed): after `npm install`, remove it from
   `node_modules` for this run only:
   ```bash
   npm uninstall --no-save @playwright/test playwright playwright-core
   ```
   `package.json` and the lockfile still list Playwright, so the next `npm install` or `npm ci`
   brings the clash back. Tell the user, and offer the lasting fix (move Playwright to its own
   package, or remove it if unused; diff-gated).
3. **`maximize()` on real phones** (only if the plan includes phones): run it on desktop only:
   ```js
   const platform = String((await driver.getCapabilities()).get('platformName') || '').toLowerCase();
   if (!['android', 'ios'].includes(platform)) await driver.manage().window().maximize();
   ```
