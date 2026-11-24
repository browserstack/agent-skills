| Logs show `unpatched method: new_page/launch/connect`; a browser opens locally | The SDK patched Playwright instead of Selenium: use a virtual environment without `playwright`/`pytest-playwright` (B2, step 1) |
| Old SDK behaviour, or `pip` installs `browserstack-sdk` 1.51.x | PyPI's copy is stale: install from `https://sdk-assets.browserstack.com/python/browserstack_sdk-latest.tar.gz` |
| Android: `Unable to maximize window` | `maximize_window()` on a real phone: guard it as in B2, step 4 |
| `browserstack-sdk: command not found` | Use the virtual environment's copy: `.venv/bin/browserstack-sdk` |
