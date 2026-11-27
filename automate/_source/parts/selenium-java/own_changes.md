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
     Gradle's own `test` task (verified on Gradle 9.9.2, Nov 2026; the SDK names and marks each
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
     (Nov 2026). Neither TestNG nor JUnit 4 needs an extra dependency on Gradle 9.
   - **No test framework (a plain `main()` run by `exec-maven-plugin`):** put the agent on the forked
     JVM instead of surefire (`<executable>java</executable>`, `<classpathScope>test</classpathScope>`,
     arguments `-javaagent:${com.browserstack:browserstack-java-sdk:jar}`, `-classpath`, `<classpath/>`,
     `${exec.mainClass}`) and run `mvn test-compile exec:exec`.
   - Never also run through `browserstack-sdk mvn test`: attaching the agent twice fails with
     "agent already loaded".
3. **Selenium 3 → 4** (only for 3.x): bump `selenium-java` to the current 4.x (the `<release>` in
   `https://repo1.maven.org/maven2/org/seleniumhq/selenium/selenium-java/maven-metadata.xml`) and
   compile with `mvn test-compile` before the cloud run. Selenium 4 removed some Selenium 3 APIs,
   so include these edits in the diff: `new WebDriverWait(driver, 20)` →
   `new WebDriverWait(driver, Duration.ofSeconds(20))`; `TimeUnit` timeouts → the `Duration`
   versions; `findElementById("x")` → `findElement(By.id("x"))`; `DesiredCapabilities.chrome()` →
   `new ChromeOptions()`.
4. **Pass/fail on the dashboard for plain JUnit 5** (Maven and the Gradle task alike). The SDK
   leaves plain JUnit 5 sessions `done`
   (grey, no name), so add this to each test class that will run, or once in a shared base class
   (Java 8 compatible; imports: `org.junit.jupiter.api.extension.AfterTestExecutionCallback`,
   `org.junit.jupiter.api.extension.RegisterExtension`, `org.openqa.selenium.JavascriptExecutor`):
   ```java
   // Reports each test's name and pass/fail to BrowserStack (the SDK doesn't for plain JUnit 5).
   @RegisterExtension
   AfterTestExecutionCallback markOnBrowserStack = ctx -> {
       if (!(driver instanceof JavascriptExecutor)) return;
       JavascriptExecutor js = (JavascriptExecutor) driver;
       String reason = ctx.getExecutionException().map(Throwable::getMessage).orElse("");
       js.executeScript("browserstack_executor: {\"action\":\"setSessionName\",\"arguments\":{\"name\":\""
               + jsonSafe(ctx.getRequiredTestClass().getSimpleName() + "." + ctx.getRequiredTestMethod().getName()) + "\"}}");
       js.executeScript("browserstack_executor: {\"action\":\"setSessionStatus\",\"arguments\":{\"status\":\""
               + (ctx.getExecutionException().isPresent() ? "failed" : "passed")
               + "\",\"reason\":\"" + jsonSafe(reason) + "\"}}");
   };

   private static String jsonSafe(String s) {
       if (s == null) return "";
       s = s.replace("\\", "\\\\").replace("\"", "\\\"").replaceAll("[\\r\\n\\t]+", " ");
       return s.length() > 250 ? s.substring(0, 250) : s;
   }
   ```
   Declare it after the `driver` field. For a framework-less `main()`, track the outcome and send
   the status before `driver.quit()` (uses the `jsonSafe` helper above):
   ```java
   boolean ok = false; String reason = "";
   try {
       // ... the existing steps ...
       ok = true;
   } catch (Exception | AssertionError e) {
       reason = String.valueOf(e.getMessage());
       throw e;
   } finally {
       try {
           ((JavascriptExecutor) driver).executeScript("browserstack_executor: {\"action\":\"setSessionStatus\",\"arguments\":{\"status\":\""
                   + (ok ? "passed" : "failed") + "\",\"reason\":\"" + jsonSafe(reason) + "\"}}");
       } catch (Exception ignored) { }
       driver.quit();
   }
   ``` If the user declines code edits, run
   anyway and mark the sessions from the runner's result instead (see Confirm the run).
5. **`maximize()` on real phones** (only if the plan includes phones): wrap it so it runs on desktop only:
   ```java
   org.openqa.selenium.Platform p = ((org.openqa.selenium.HasCapabilities) driver).getCapabilities().getPlatformName();
   if (p == null || !(p.is(org.openqa.selenium.Platform.ANDROID) || p.is(org.openqa.selenium.Platform.IOS))) driver.manage().window().maximize();
   ```
