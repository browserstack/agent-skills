- **Real iPhone:** add a real iPhone 15 (Safari) as its own build (B1 has the row and how). After
  an iPhone-only run, offer the desktop build instead. Set expectations first:
  Playwright on real iOS is a custom WebKit integration with limits (for example one browser
  context per session, and some keyboard and multi-tab behaviour differs from desktop WebKit), so
  a failure there doesn't change the desktop results. Real Android phones need BrowserStack's device API rather
  than a normal browser launch, so this skill doesn't set them up: see https://www.browserstack.com/docs/automate/playwright/playwright-android/c-sharp.
- **Wider coverage:** add Edge, older browser versions or other operating systems.
