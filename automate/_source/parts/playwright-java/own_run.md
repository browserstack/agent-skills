- **Maven:** `mvn test` (one class: `mvn test -Dtest=CartTest`; one module: `mvn -pl <module> test`).
- **Gradle with TestNG:** `./gradlew test` (or `gradle test`), with the agent on `test` (B2).
- **Gradle with JUnit 5 or JUnit 4:** `./gradlew browserstackTest` (or `gradle browserstackTest`), the task from B2. The
  console launcher prints one test tree per platform: read its "tests successful" / "tests
  failed" lines and `BUILD`.

Don't add `-q`. If the output is long, save it to a file and read the `Tests run:` and `BUILD`
lines. Playwright may download its driver on the first run, and older surefire versions print
`[ERROR] Surefire is going to kill self fork JVM` (about 30 s); both are harmless when the build
succeeds and the API shows the sessions.
