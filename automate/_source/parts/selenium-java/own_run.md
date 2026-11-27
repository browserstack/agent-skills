- **Maven:** `mvn test` (one class: `mvn test -Dtest=LoginTest`; one module: `mvn -pl <module> test`).
- **Gradle with TestNG:** `./gradlew test` (or `gradle test`), with the agent on `test` (B2).
  Gradle prints no per-test lines on success: take the counts from
  `build/test-results/test/TEST-*.xml`.
- **Gradle with JUnit 5 or JUnit 4:** `./gradlew browserstackTest` (or `gradle browserstackTest`), the task from B2.
  JUnit 5's console launcher prints one test tree per platform: read its "tests successful" /
  "tests failed" lines and `BUILD`. JUnit 4's `JUnitCore` prints `OK (N tests)`, or `FAILURES!!!`
  with `Tests run: N, Failures: M`, once per platform.
- **Plain `main()`:** `mvn test-compile exec:exec`.

Don't add `-q`. If the output is long, save it to a file and read the `Tests run:`, `BUILD` and
`View build` lines. These lines also appear on genuine BrowserStack runs and are harmless:
`[ERROR] Surefire is going to kill self fork JVM` (adds about 30 s), SeleniumManager "chromedriver
version … detected in PATH", `Unable to find CDP implementation`, `Unable to connect to determine websocket url … localhost:9222`, "Set testReporting: true", and, under Gradle, `*** java.lang.instrument ASSERTION FAILED ***:
"!errorOutstanding"`.
