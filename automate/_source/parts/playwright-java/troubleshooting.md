| `agent already loaded` | The agent is attached twice: keep the surefire `argLine` or `browserstack-sdk mvn test`, not both |
| A browser opens on the user's machine; the API shows no build | The launch wasn't routed: check the agent is on surefire's `argLine` (B2) and the test uses a standard `launch()` |
| iOS: `Only one browser context is allowed` | Real iOS allows one context per session: one test per session, no multi-context tests |
