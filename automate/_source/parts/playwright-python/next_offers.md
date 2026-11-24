- **Real iPhone:** add a real iPhone 15 (Safari) as its own build. Set expectations first:
  Playwright on real iOS is a custom WebKit integration with limits (one browser context per
  session; storage state, `setContent` and tracing are not supported), so a failure there
  doesn't change the desktop results. Real Android phones need BrowserStack's device API rather
  than a normal browser launch, so this skill doesn't set them up: see the Playwright Android docs.
- **Wider coverage:** add Edge, older browser versions or other operating systems.
