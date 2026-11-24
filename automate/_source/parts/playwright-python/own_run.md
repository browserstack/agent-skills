- **pytest:** `.venv/bin/browserstack-sdk pytest <tests>` (never bare `pytest`, which runs locally).
- **behave:** `.venv/bin/browserstack-sdk behave`.
- **Plain script:** `.venv/bin/browserstack-sdk python <script>.py`.

Don't run `playwright install`: the browsers run on BrowserStack. Notices about Selenium or other
frameworks that aren't installed are harmless; don't install packages to silence them.
