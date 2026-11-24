| Android: `UnsupportedCommandException … Unable to maximize window` | `maximize()` on a real phone: guard it as in B2, step 5 |
| `int cannot be converted to java.time.Duration` (or `cannot find symbol findElementById`) after upgrading Selenium | Selenium 4 API changes: apply B2, step 3 |
| `agent already loaded` | The agent is attached twice: keep the surefire `argLine` or `browserstack-sdk mvn test`, not both |
| A browser opens on the user's machine; the API shows no build | A driver-manager factory, or an SDK too old for the Selenium version: use `new ChromeDriver()` and the current SDK |
| `pattern matching in instanceof is not supported in -source 8` | Use the Java 8 form of the callback shown in B2, step 4 |
| JaCoCo prints `Unsupported class file major version` | JaCoCo is older than the JDK Maven runs on; harmless when the API shows the sessions passed |
