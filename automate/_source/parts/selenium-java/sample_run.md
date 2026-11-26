```bash
mvn test
```

Always clone with `-b sdk-sample` (A2): the Quick Integration Guide's git command has no `-b`, and
this repo's default branch holds only a README, so `mvn test` would find no project. The guide's
ZIP link uses `sdk-sample`.

The sample's `pom.xml` attaches the BrowserStack Java SDK as a `-javaagent` and runs
`BStackDemoTest` (adds a product to the cart on bstackdemo.com and checks it is there) on every
platform in `browserstack.yml`, in parallel. Don't add `-q`; if the output is long, read the
`BUILD` lines and `log/browserstack-javaagent.log`. Warnings about the deprecated `LATEST` SDK
version, SeleniumManager driver versions or CDP versions are harmless.
