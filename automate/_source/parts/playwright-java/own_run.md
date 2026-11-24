- **Maven:** `mvn test` (one class: `mvn test -Dtest=CartTest`; one module: `mvn -pl <module> test`).
- **Gradle:** `./gradlew test` (or `gradle test`).

Don't add `-q`. If the output is long, save it to a file and read the `Tests run:` and `BUILD`
lines. Playwright may download its driver on the first run; that is normal.
