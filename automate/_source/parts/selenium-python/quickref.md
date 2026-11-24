| Task | Command |
| --- | --- |
| Sample build | `git clone -b main https://github.com/browserstack/python-selenium-browserstack.git && cd python-selenium-browserstack && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt && .venv/bin/browserstack-sdk ./tests/test.py` |
| Your tests (pytest) | `.venv/bin/browserstack-sdk pytest tests/` |
| Install the current SDK | `pip install https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz` |
| SDK version installed | `python -c "import browserstack_sdk._version as v; print(v.__version__)"` |
| Docs | https://www.browserstack.com/docs/automate/selenium/getting-started/python |
