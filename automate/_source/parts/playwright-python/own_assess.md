Note these in a short Assessment block at the top of your plan:

- **Test runner:** pytest with `pytest-playwright` (the `page` and `browser` fixtures) or behave.
  Plain scripts with `sync_playwright()` can run through `browserstack-sdk python <script>.py`;
  confirm on the API that sessions were created.
- **Versions:** `playwright` and `pytest-playwright` from `requirements.txt` or `pyproject.toml`;
  keep the user's versions.
- **Framework clash:** if `selenium` is installed or listed too, the SDK may patch Selenium instead
  of Playwright. Use a separate virtual environment with only the Playwright stack (B2).
- **Browser launch the SDK can't wrap:** `executable_path`, `launch_persistent_context`, or
  `connect()` to another endpoint runs on the local machine while the result still looks green.
  Propose the standard fixtures or `browser_type.launch()`.
- **Real devices:** a real iPhone is available on request. Real Android phones aren't available
  for Playwright Python through the SDK.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test, pick the test whose name is the nearest step in that flow, and if two are equally close,
  the first by file path. State the pick and why.
