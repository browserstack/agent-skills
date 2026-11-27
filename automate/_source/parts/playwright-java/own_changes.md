1. **BrowserStack Java SDK, pinned to the current release** (never `LATEST`). Get the version from
   `https://repo1.maven.org/maven2/com/browserstack/browserstack-java-sdk/maven-metadata.xml`
   (the `<release>` tag; `search.maven.org` lags):
   ```xml
   <dependency>
     <groupId>com.browserstack</groupId>
     <artifactId>browserstack-java-sdk</artifactId>
     <version>CURRENT_RELEASE</version>
     <scope>compile</scope>
   </dependency>
   ```
2. **Attach the SDK as a `-javaagent`**, exactly once:
   - **Maven:** add `maven-dependency-plugin` (goal `properties`, which exposes the jar path) and the
     agent on surefire. If the project already has an `argLine`, keep it and append:
     ```xml
     <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-dependency-plugin</artifactId>
       <version>3.8.1</version>
       <executions><execution><id>getClasspathFilenames</id><goals><goal>properties</goal></goals></execution></executions>
     </plugin>
     <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-surefire-plugin</artifactId>
       <configuration>
         <argLine>-javaagent:${com.browserstack:browserstack-java-sdk:jar}</argLine>
         <!-- existing argLine: <argLine>@{argLine} -javaagent:${com.browserstack:browserstack-java-sdk:jar}</argLine> -->
       </configuration>
     </plugin>
     ```
   - **Gradle (JUnit 5):** don't put the agent on the `test` task: inside Gradle's test worker the
     SDK can run only one platform, and the others stop with `java.io.EOFException … GradleWorkerMain`.
     Add a separate task that runs the same tests through the JUnit console launcher in a plain JVM,
     and leave the `test` task as it is:
     ```groovy
     dependencies {
       testImplementation 'com.browserstack:browserstack-java-sdk:CURRENT_RELEASE'
       testRuntimeOnly 'org.junit.platform:junit-platform-console'   // version comes from the JUnit BOM
     }
     // Runs the JUnit 5 tests on every platform in browserstack.yml: gradle browserstackTest
     tasks.register('browserstackTest', JavaExec) {
       dependsOn 'testClasses'
       classpath = sourceSets.test.runtimeClasspath
       mainClass = 'org.junit.platform.console.ConsoleLauncher'
       args 'execute', '--scan-classpath', '--include-classname', '.*', '--disable-banner', '--details=tree'
       doFirst { jvmArgs "-javaagent:${classpath.find { it.name.contains('browserstack-java-sdk') }.absolutePath}" }
     }
     ```
     `execute` needs JUnit 5.10 or newer; on an older JUnit 5, leave it out. For one class, replace
     `'--scan-classpath', '--include-classname', '.*'` with `'--select-class', 'com.example.LoginTest'`.
     Don't add BrowserStack's `com.browserstack.gradle-sdk` plugin: with the current SDK no session
     starts. Verified with the Groovy DSL on Gradle 9.9.2 (Nov 2026); for `build.gradle.kts`, write
     the same task in Kotlin and say it is unverified.
   - **Gradle (TestNG):** TestNG runs every platform inside the one test JVM, so the agent can go on
     Gradle's own `test` task (verified on Gradle 9.9.2, Nov 2026, Selenium and Playwright; the SDK names and marks each
     session):
     ```groovy
     dependencies { testImplementation 'com.browserstack:browserstack-java-sdk:CURRENT_RELEASE' }
     test {
       useTestNG()
       doFirst { jvmArgs "-javaagent:${classpath.find { it.name.contains('browserstack-java-sdk') }.absolutePath}" }
     }
     ```
     Run it with `gradle test` and set `framework: testng` in `browserstack.yml`.
   - **Gradle (JUnit 4):** don't put the agent on the `test` task: the SDK's per-platform JVMs fail
     there and no build is created at all. Run the tests through `JUnitCore` in a separate task, and
     leave `test` as it is:
     ```groovy
     dependencies { testImplementation 'com.browserstack:browserstack-java-sdk:CURRENT_RELEASE' }
     // Runs the JUnit 4 tests on every platform in browserstack.yml: gradle browserstackTest
     tasks.register('browserstackTest', JavaExec) {
       dependsOn 'testClasses'
       classpath = sourceSets.test.runtimeClasspath
       mainClass = 'org.junit.runner.JUnitCore'
       args 'com.example.LoginTest', 'com.example.CartTest'   // every test class to run, fully qualified
       doFirst { jvmArgs "-javaagent:${classpath.find { it.name.contains('browserstack-java-sdk') }.absolutePath}" }
     }
     ```
     `JUnitCore` doesn't scan for tests, so list each test class (or one `@RunWith(Suite.class)`
     class). Set `framework: junit4` in `browserstack.yml`. Verified on Gradle 9.9.2 with Selenium
     (Nov 2026); for Playwright with JUnit 4, say it is unverified. Neither TestNG nor JUnit 4 needs an extra dependency on Gradle 9.
   - Never also run through `browserstack-sdk mvn test`: attaching the agent twice fails with
     "agent already loaded".
3. **Set `framework`** in `browserstack.yml` to the test framework (`junit5`, `testng` or `junit4`).
4. **Desktop macOS rows use `playwright-webkit`, never `Safari`.** On desktop, Playwright on
   BrowserStack accepts only `chrome`, `edge`, `playwright-chromium`, `playwright-webkit` or
   `playwright-firefox`: a `browserName: Safari` on an `os: OS X` row (the Quick Integration Guide's
   sample config uses one) fails every test on that platform with `Invalid 'browser'`. If the
   project's `browserstack.yml` has one, change it to `playwright-webkit` with `browserVersion: latest`
   (a Safari version such as `15.6` is not a WebKit version) and show the diff. Keep
   `safari` only on real iPhone rows (`deviceName: iPhone …`).
