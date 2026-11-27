Note these in a short Assessment block at the top of your plan:

- **Test runner:** pytest (`conftest.py`, `pytest.ini`, `test_*.py`), unittest, behave, or plain scripts.
- **Dependencies:** `requirements.txt` or `pyproject.toml`, and the Selenium version (4.x is required).
- **Framework clash:** if `playwright` or `pytest-playwright` is installed or listed, the SDK may
  patch Playwright instead of Selenium and the tests silently run on the local machine. Use a
  separate virtual environment with only the Selenium stack (B2).
- **How the driver is created:** `webdriver.Chrome()` and similar are intercepted by the SDK. If a
  helper builds the driver some other way, check after the run that sessions appear on the API.
- **`maximize_window()` calls:** real Android phones reject them, so they matter only if the plan
  includes phones.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test, pick the test whose name is the nearest step in that flow, and if two are equally close,
  the first by file path. State the pick and why.
