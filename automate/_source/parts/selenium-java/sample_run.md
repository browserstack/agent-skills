```bash
mvn test
```

The sample's `pom.xml` attaches the BrowserStack Java SDK as a `-javaagent` and runs
`BStackDemoTest` (adds a product to the cart on bstackdemo.com and checks it is there) on every
platform in `browserstack.yml`, in parallel. Don't add `-q`; if the output is long, read the
`BUILD` lines and `log/browserstack-javaagent.log`. Warnings about the deprecated `LATEST` SDK
version, SeleniumManager driver versions or CDP versions are harmless.
