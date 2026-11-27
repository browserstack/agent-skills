  - The SDK marks pytest and behave sessions. If they show `done` and have no name, the SDK
    detected the wrong framework: check `framework:` in `browserstack.yml`, then mark each session
    from the runner's result as shown below.
  - Without the B1 `conftest.py` fixture, `pytest-playwright` reuses one browser per platform, so
    several tests share one session, named after the last test and marked with its result. Report per-test results from pytest's output;
    if a test failed while its session shows `passed`, mark the session `failed` with that test's
    name and assertion.
