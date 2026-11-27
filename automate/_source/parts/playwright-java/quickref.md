| Task | Command |
| --- | --- |
| Sample build | `git clone https://github.com/browserstack/java-playwright-browserstack.git && cd java-playwright-browserstack && mvn compile && mvn test -P sample-test` |
| Your tests (Maven) | `mvn test` with the agent on surefire's `argLine` |
| Your tests (Gradle, JUnit 5 or 4) | `./gradlew browserstackTest` (the task from B2) |
| Your tests (Gradle, TestNG) | `./gradlew test` with the agent on `test` (B2) |
| Current SDK version | `curl -s https://repo1.maven.org/maven2/com/browserstack/browserstack-java-sdk/maven-metadata.xml \| grep -o '<release>[^<]*'` |
| Docs | https://www.browserstack.com/docs/automate/playwright/getting-started/java |
