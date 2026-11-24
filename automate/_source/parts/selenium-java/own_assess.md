Note these in a short Assessment block at the top of your plan:

- **Build tool:** `pom.xml` → Maven; `build.gradle` / `build.gradle.kts` → Gradle (use `./gradlew`
  if the repo has it). In a multi-module repo, pick the module that has the Selenium tests, wire
  only that module, and run it from the root with `mvn -pl <module> test`.
- **Test framework:** JUnit 5 (`org.junit.jupiter`), JUnit 4, TestNG, Cucumber, or none (a plain
  `main()` run by `exec-maven-plugin`).
- **Selenium version:** 4.x is required; 3.x needs the upgrade in B2.
- **How the driver is created:** `new ChromeDriver()`, `new RemoteWebDriver(new URL(...), options)`
  (even with a hard-coded hub) and a constructor called by reflection are all intercepted by the
  SDK, so leave them alone. A driver-manager factory that builds the driver itself
  (`WebDriverManager.chromedriver().create()`) is not intercepted and runs on the local machine:
  propose `new ChromeDriver()` instead (`.setup()` followed by `new ChromeDriver()` is fine).
- **Existing surefire `<argLine>`** (for example JaCoCo): the agent must be appended, not replace it.
- **`maximize()` calls:** real Android phones reject them, so they matter only if the plan includes phones.
- **Which tests to run:** the ones the user named; otherwise all. If they named a flow that has no
  test (for example "checkout"), pick the test whose name is the nearest step in that flow (for
  example `*Cart*`), and if two are equally close, the first by file path. State the pick and why.
