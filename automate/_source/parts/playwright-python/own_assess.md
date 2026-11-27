Note these in a short Assessment block at the top of your plan:

- **Test runner:** pytest with `pytest-playwright` (the `page` and `browser` fixtures) or behave.
  Plain scripts with `sync_playwright()` can run through `browserstack-sdk python <script>.py`;
  confirm on the API that sessions were created.
- **Versions:** `playwright` and `pytest-playwright` from `requirements.txt` or `pyproject.toml`;
  keep the user's versions, except Playwright 1.65 or newer, which the current SDK can't hook yet
  (Nov 2026): propose `playwright==1.64.1` in the BrowserStack `.venv` and say why.
- **Framework clash:** if the user's own `selenium` packages are installed or listed too, the SDK
  may patch Selenium instead of Playwright. Use a separate virtual environment without them (B2);
  the SDK pulls in its own Selenium, which is fine.
- **Browser launch the SDK can't wrap:** `executable_path`, `launch_persistent_context`, or
  `connect()` to another endpoint runs on the local machine while the result still looks green.
  Propose the standard fixtures or `browser_type.launch()`.
- **Real iPhone (on request, as its own build):** keep `browserstack.yml` as it is (if there is none
  yet, add the B2 one too and say this run uses only the iPhone file) and add a
  `browserstack-ios.yml` with the same settings, a new `buildName` and only this platform (check
  it against the live catalog as in step A3):
  ```yaml
  platforms:
    - deviceName: iPhone 15
      osVersion: 17
      browserName: safari
  ```
  Run it with `BROWSERSTACK_CONFIG_FILE=browserstack-ios.yml .venv/bin/browserstack-sdk pytest`.
  Real iOS allows one browser context per session, and `pytest-playwright` opens a new context
  for every test in one shared browser, so from the second test on it fails with `Only one browser
  context is allowed`. Put this in `conftest.py` (a new file, or a diff to the existing one) so
  each test gets its own browser and session:
  ```python
  import pytest

  @pytest.fixture
  def browser(launch_browser):
      browser = launch_browser()
      yield browser
      browser.close()
  ```
  Session names end in `[chromium]` on every platform (pytest-playwright's default parameter); the
  API's `device` field shows what really ran.
- **Real Android:** not available for Playwright Python through the SDK (it needs a separate
  BrowserStack package and `playwright.android.connect`, so the tests would need rewriting). Never
  add an Android row, and if `browserstack.yml` already has one (the Quick Integration Guide's config
  does), remove it in the plan and say why: the SDK still starts device sessions, which end in `error`. Point the user to
  https://www.browserstack.com/docs/automate/playwright/playwright-android/python.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test, pick the test whose name is the nearest step in that flow, and if two are equally close,
  the first by file path. State the pick and why.
