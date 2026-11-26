- **Real phones:** add a real Samsung Galaxy S23 (Chrome) and a real iPhone 15 (Safari) (B1 has the
  rows and how). Run the iPhone as its own build and set expectations first: Playwright on real iOS is a custom WebKit
  integration with limits (for example one browser context per session, and some keyboard and
  multi-tab behaviour differs from desktop WebKit), so a failure there doesn't change the desktop
  results. On real Android, pages wider than the phone screen can fail clicks with "intercepts
  pointer events" (see Troubleshooting).
- **Wider coverage:** add Edge, older browser versions or other operating systems.
