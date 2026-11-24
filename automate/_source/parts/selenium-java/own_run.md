- **Maven:** `mvn test` (one class: `mvn test -Dtest=LoginTest`; one module: `mvn -pl <module> test`).
- **Gradle:** `./gradlew browserstackTest` (or `gradle browserstackTest`), the task from B2. The
  console launcher prints one test tree per platform: read its "tests successful" / "tests
  failed" lines and `BUILD`.
- **Plain `main()`:** `mvn test-compile exec:exec`.

Don't add `-q`. If the output is long, save it to a file and read the `Tests run:`, `BUILD` and
`View build` lines. These lines also appear on genuine BrowserStack runs and are harmless:
`[ERROR] Surefire is going to kill self fork JVM` (adds about 30 s), SeleniumManager "chromedriver
version … detected in PATH", `Unable to find CDP implementation`, `Unable to connect to determine websocket url … localhost:9222`, and "Set testReporting: true".
