| Task | Command |
| --- | --- |
| Sample build | `git clone -b sdk-sample https://github.com/browserstack/vanilla-java-browserstack.git && cd vanilla-java-browserstack && mvn test` |
| Your tests (Maven) | `mvn test` with the agent on surefire's `argLine` |
| One test class | `mvn test -Dtest=LoginTest` |
| Your tests (Gradle) | `./gradlew browserstackTest` (the task from B2) |
| Current SDK version | `curl -s https://repo1.maven.org/maven2/com/browserstack/browserstack-java-sdk/maven-metadata.xml \| grep -o '<release>[^<]*'` |
| Docs | https://www.browserstack.com/docs/automate/selenium/getting-started/java |
