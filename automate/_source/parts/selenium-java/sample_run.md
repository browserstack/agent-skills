```bash
mvn test -P sample-test
```

This is the command the Quick Integration Guide's JUnit 5 guide gives. The pom has no
`sample-test` profile, so Maven warns that it "could not be activated" and runs its default
configuration, which is the sample test: harmless. The pom attaches the BrowserStack Java SDK as a
`-javaagent` and runs `BStackSampleTest` (adds a product to the cart on bstackdemo.com and checks
the cart, waiting for each element) with JUnit 5 on every platform in `browserstack.yml`, in
parallel; the SDK names and marks each session itself. Don't add `-q`; if the output is long, read
the `Tests run:` and `BUILD` lines. Warnings about the deprecated `LATEST` SDK version are harmless, and so is
`[ERROR] System Exit has timed out in the forked process` next to `BUILD SUCCESS`.
