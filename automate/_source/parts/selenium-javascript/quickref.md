| Task | Command |
| --- | --- |
| Sample build | `git clone -b main https://github.com/browserstack/jest-js-browserstack.git && cd jest-js-browserstack && npm install && npm run sample-test` |
| Your tests (Mocha) | `npx browserstack-node-sdk mocha test/*.js --timeout 60000` |
| Your tests (Jest) | `npx browserstack-node-sdk jest` |
| Current SDK version | `npm view browserstack-node-sdk version` |
| Docs | https://www.browserstack.com/docs/automate/selenium/getting-started/nodejs |
