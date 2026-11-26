```bash
mvn compile
mvn test -P sample-test
```

The `sample-test` profile attaches the BrowserStack Java SDK as a `-javaagent` and runs
`SampleTest` (adds a product to the cart on bstackdemo.com and checks the cart) with JUnit 5 on
every platform in `browserstack.yml` (desktop Chrome, Firefox and WebKit), in parallel. Don't add
`-q`; if the output is long, read the `Tests run:` and `BUILD` lines. Warnings about the deprecated
`LATEST` versions in the sample's `pom.xml`, and the SDK's "Both Selenium and Playwright detected"
warning, are harmless. The sample test catches its own exceptions, so an `Exception: …` line in
the output means the sample is out of date even when the sessions show `passed`: report it as in
"When sessions failed".

Before running, check `browserstack.yml` for a `browserName: Safari` on a desktop (`os:`) row
(`grep -niB3 "browserName: *safari" browserstack.yml`). If there is one, change it to
`playwright-webkit` and list that change in the plan; `safari` stays only on real iPhone rows.
