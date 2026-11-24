1. **A virtual environment with only the Selenium stack** (a new folder, `.venv`): the user's own
   `selenium` and test-runner versions plus the current BrowserStack SDK from BrowserStack's server.
   PyPI's `browserstack-sdk` lags well behind, so don't install it from there:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install "selenium==<their version>" "pytest==<their version>" \
     https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz
   .venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"
   ```
2. **Pin the SDK by URL in `requirements.txt`** (diff), so the next install gets the same version
   (`browserstack-sdk==<version>` doesn't exist on PyPI):
   ```
   browserstack-sdk @ https://sdk-assets.browserstack.com/python/browserstack_sdk-<version>.tar.gz
   ```
   The plan can show this line with `<version>` until the install reveals it. If `requirements.txt`
   also lists `playwright` or `pytest-playwright`, say in the report that a full `pip install -r requirements.txt`
   brings the clash back, and offer a lasting fix: a separate `requirements-browserstack.txt`
   with only this stack.
3. **Don't run `browserstack-sdk setup`**: it writes `browserstack.yml` with the credentials inline.
   Use the file below instead.
4. **`maximize_window()` on real phones** (only if the plan includes phones): run it on desktop only:
   ```python
   if str(driver.capabilities.get("platformName", "")).lower() not in ("android", "ios"):
       driver.maximize_window()
   ```
