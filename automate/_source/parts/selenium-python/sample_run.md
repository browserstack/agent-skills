```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt   # includes the current BrowserStack SDK from BrowserStack's server
.venv/bin/browserstack-sdk ./tests/test.py
```

On Windows use `.venv\Scripts\pip` and `.venv\Scripts\browserstack-sdk`. The SDK runs
`tests/test.py` (adds a product to the cart on bstackdemo.com and checks it is there) on every
platform in `browserstack.yml`, in parallel, and the test reports its own pass/fail to BrowserStack.
