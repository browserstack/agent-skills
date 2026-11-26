The sample leaves Playwright unpinned, and Playwright Python 1.65 renamed an internal module the
current SDK hooks into (Nov 2026), so install with Playwright pinned to 1.64.1. `--no-cache-dir`
makes pip fetch the current SDK instead of reusing an older cached copy:

```bash
python3 -m venv .venv
.venv/bin/pip install --no-cache-dir -r requirements.txt "playwright==1.64.1"
.venv/bin/python -c "import browserstack_sdk._version as v; print(v.__version__)"
sed -i.bak "s/osVersion: Ventura/osVersion: Sequoia/" browserstack.yml && rm -f browserstack.yml.bak
.venv/bin/browserstack-sdk pytest -s tests/sample-test.py
```

The `sed` line moves the sample's WebKit row from macOS Ventura to Sequoia: on Ventura WebKit the
sample's `to_have_count` check fails every run (Nov 2026). List both the Playwright pin and this
swap in the plan. On Windows use `.venv\Scripts\pip` and `.venv\Scripts\browserstack-sdk`. The SDK
runs `tests/sample-test.py` (adds a product to the cart on bstackdemo.com and checks the cart) on
every platform in `browserstack.yml` (desktop Chrome, WebKit and Firefox), in parallel, and the
test reports its own pass/fail. The browsers run on BrowserStack, so don't run `playwright install`. The SDK's notices "Please
install pytest-selenium package", "Failed to patch pytest selenium" and "playwright.Android not
importable" are harmless; don't install packages to silence them.

Before running, check `browserstack.yml` for a `browserName: Safari` on a desktop (`os:`) row
(`grep -niB3 "browserName: *safari" browserstack.yml`). If there is one, change it to
`playwright-webkit` with `browserVersion: latest`, and list that change in the plan; `safari` stays only on real iPhone rows.
