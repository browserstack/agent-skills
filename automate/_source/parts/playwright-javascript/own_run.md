```bash
npx browserstack-node-sdk playwright test
```

Add the user's usual arguments (a spec file, `--project`, `--config`). Never run bare
`npx playwright test`: it runs locally. These lines are harmless on a genuine BrowserStack run:
"Uh-oh! We detected some issues … SDK-GEN-004" about `GLOBAL_AGENT_HTTP_PROXY`, and Accessibility
"not a valid session" warnings.
