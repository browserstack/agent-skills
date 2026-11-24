- **Real phones:** add a real Samsung Galaxy S23 (Chrome) and a real iPhone 15 (Safari). Run the
  iPhone as its own build and set expectations first: Playwright on real iOS is a custom WebKit
  integration with limits (one browser context per session; `storageState()`, `setContent` and
  `tracing` are not supported), so a failure there doesn't change the desktop results.
- **Wider coverage:** add Edge, older browser versions or other operating systems.
