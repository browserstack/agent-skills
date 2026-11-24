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
   - **Gradle:**
     ```groovy
     dependencies { testImplementation 'com.browserstack:browserstack-java-sdk:CURRENT_RELEASE' }
     test {
       useJUnitPlatform()
       doFirst { jvmArgs "-javaagent:${classpath.find { it.name.contains('browserstack-java-sdk') }.absolutePath}" }
     }
     ```
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
4. **Pass/fail on the dashboard for plain JUnit 5.** The SDK leaves plain JUnit 5 sessions `done`
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
               + jsonSafe(ctx.getDisplayName()) + "\"}}");
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
   Declare it after the `driver` field. For a framework-less `main()`, call the same two executor
   commands in a `finally` block before `driver.quit()`. If the user declines code edits, run
   anyway and mark the sessions from the runner's result instead (see Confirm the run).
5. **`maximize()` on real phones** (only if the plan includes phones): wrap it so it runs on desktop only:
   ```java
   org.openqa.selenium.Platform p = ((org.openqa.selenium.HasCapabilities) driver).getCapabilities().getPlatformName();
   if (p == null || !(p.is(org.openqa.selenium.Platform.ANDROID) || p.is(org.openqa.selenium.Platform.IOS))) driver.manage().window().maximize();
   ```
