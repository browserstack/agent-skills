- **Maven:** `mvn test` (one class: `mvn test -Dtest=CartTest`; one module: `mvn -pl <module> test`).
- **Gradle with TestNG:** `./gradlew test` (or `gradle test`), with the agent on `test` (B2).
  Gradle prints no per-test lines on success: take the counts from
  `build/test-results/test/TEST-*.xml`.
- **Gradle with JUnit 5 or JUnit 4:** `./gradlew browserstackTest` (or `gradle browserstackTest`), the task from B2.
  JUnit 5's console launcher prints one test tree per platform: read its "tests successful" /
  "tests failed" lines and `BUILD`. JUnit 4's `JUnitCore` prints `OK (N tests)`, or `FAILURES!!!`
  with `Tests run: N, Failures: M`, once per platform.

Don't add `-q`. If the output is long, save it to a file and read the `Tests run:` and `BUILD`
lines. Playwright may download its driver on the first run, and older surefire versions print
`[ERROR] Surefire is going to kill self fork JVM` (about 30 s); so is a `*** java.lang.instrument
ASSERTION FAILED ***: "!errorOutstanding"` line under Gradle. All are harmless when the build
succeeds and the API shows the sessions.
