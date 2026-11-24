```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt   # includes the current BrowserStack SDK from BrowserStack's server
.venv/bin/browserstack-sdk pytest -s tests/sample-test.py
```

On Windows use `.venv\Scripts\pip` and `.venv\Scripts\browserstack-sdk`. The SDK runs
`tests/sample-test.py` (adds a product to the cart on bstackdemo.com and checks the cart) on every
platform in `browserstack.yml` (desktop Chrome, WebKit and Firefox), in parallel, and the test
reports its own pass/fail. The browsers run on BrowserStack, so don't run `playwright install`.
