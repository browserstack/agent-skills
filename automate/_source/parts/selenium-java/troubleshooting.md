| Android: `UnsupportedCommandException … Unable to maximize window` | `maximize()` on a real phone: guard it as in B2, step 5 |
| `int cannot be converted to java.time.Duration` (or `cannot find symbol findElementById`) after upgrading Selenium | Selenium 4 API changes: apply B2, step 3 |
| `agent already loaded` | The agent is attached twice: keep the surefire `argLine` or `browserstack-sdk mvn test`, not both |
| A browser opens on the user's machine; the API shows no build | A driver-manager factory, or an SDK too old for the Selenium version: use `new ChromeDriver()` and the current SDK |
| `pattern matching in instanceof is not supported in -source 8` | Use the Java 8 form of the callback shown in B2, step 4 |
| JaCoCo prints `Unsupported class file major version` | JaCoCo is older than the JDK Maven runs on; harmless when the API shows the sessions passed |
| Gradle: only one platform gets a session and the output shows `java.io.EOFException … GradleWorkerMain` | The agent is on Gradle's `test` task, where the SDK can drive one platform. Use the `browserstackTest` task from B2 |
| Gradle 9: `Failed to load JUnit Platform … including the JUnit Platform launcher` | Gradle 9 no longer adds the launcher; it is the project's build, not BrowserStack. `browserstackTest` brings it in through `junit-platform-console`. For `gradle test` the project needs `testRuntimeOnly 'org.junit.platform:junit-platform-launcher'` (show it as a diff and ask) |
