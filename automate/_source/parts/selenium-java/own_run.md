- **Maven:** `mvn test` (one class: `mvn test -Dtest=LoginTest`; one module: `mvn -pl <module> test`).
- **Gradle:** `./gradlew test` (or `gradle test`).
- **Plain `main()`:** `mvn test-compile exec:exec`.

Don't add `-q`. These lines also appear on genuine BrowserStack runs and are harmless:
`[ERROR] Surefire is going to kill self fork JVM` (adds about 30 s), SeleniumManager "chromedriver
version … detected in PATH", `Unable to find CDP implementation`, and "Set testReporting: true".
