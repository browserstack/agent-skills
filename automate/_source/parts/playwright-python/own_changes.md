1. **A virtual environment with only the Playwright stack** (a new folder, `.venv`): the user's
   own `playwright`, `pytest-playwright` and runner versions plus the current BrowserStack SDK from
   BrowserStack's server. PyPI's `browserstack-sdk` lags well behind, so don't install it from there:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install "playwright==<their version>" "pytest-playwright==<their version>" \
     https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz
   .venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"
   ```
2. **Pin the SDK by URL in `requirements.txt`** (diff), so the next install gets the same version
   (`browserstack-sdk==<version>` doesn't exist on PyPI):
   ```
   browserstack-sdk @ https://sdk-assets.browserstack.com/python/browserstack_sdk-<version>.tar.gz
   ```
3. **Don't run `browserstack-sdk setup`**: it writes `browserstack.yml` with the credentials inline.
   Use the file below instead, with `framework` set to the runner (`pytest` or `behave`).
