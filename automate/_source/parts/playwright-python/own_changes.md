1. **A virtual environment for the BrowserStack run** (a new folder, `.venv`) without the user's
   Selenium packages: their `playwright`, `pytest-playwright` and runner versions plus the current
   BrowserStack SDK from BrowserStack's server. PyPI's `browserstack-sdk` lags well behind, so don't install it from there:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install --no-cache-dir "playwright==<their version>" "pytest-playwright==<their version>" \
     "pytest==<their version>" https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz
   .venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"
   ```
2. **Pin the SDK by URL in `requirements.txt`** (diff), so the next install gets the same version
   (`browserstack-sdk==<version>` doesn't exist on PyPI):
   ```
   browserstack-sdk @ https://sdk-assets.browserstack.com/python/browserstack_sdk-<version>.tar.gz
   ```
   The plan can show this line with `<version>` until the install reveals it. If `requirements.txt`
   also lists `selenium`, say in the report that a full `pip install -r requirements.txt`
   brings the clash back, and offer a lasting fix: a separate `requirements-browserstack.txt`
   with only this stack.
3. **Don't run `browserstack-sdk setup`**: it writes `browserstack.yml` with the credentials inline.
   Use the file below instead, with `framework` set to the runner (`pytest` or `behave`).
