| Task | Command |
| --- | --- |
| Sample build | `git clone https://github.com/browserstack/pytest-playwright-browserstack.git && cd pytest-playwright-browserstack && python3 -m venv .venv && .venv/bin/pip install --no-cache-dir -r requirements.txt "playwright==1.64.1" && .venv/bin/browserstack-sdk pytest -s tests/sample-test.py` |
| Your tests | `.venv/bin/browserstack-sdk pytest` |
| Current SDK version | `.venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"` |
| Docs | https://www.browserstack.com/docs/automate/playwright/getting-started/python |
