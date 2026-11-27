- **pytest:** `.venv/bin/browserstack-sdk pytest <tests>` (never bare `pytest`).
- **unittest:** `.venv/bin/browserstack-sdk python -m unittest <module>`.
- **behave:** `.venv/bin/browserstack-sdk behave`.
- **Plain script:** `.venv/bin/browserstack-sdk python <script>.py`.

These lines also appear on genuine BrowserStack runs and are harmless: `[SDKCLI][ERROR] - Failed
to patch pytest selenium … No module named 'pytest_selenium'`, `failed to setup playwright: No
module named 'playwright'`, "Please install pytest-selenium package", and Selenium's
`DeprecationWarning: setting remote_server_addr …`. Don't install packages to silence them.
