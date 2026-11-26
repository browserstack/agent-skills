The sample project targets several .NET versions (`net6.0` to `net10.0`), so run it on the newest
one installed (from `dotnet --list-runtimes`), for example `net10.0`:

```bash
dotnet test --filter "Category=sample-test" -f net10.0
```

Use `Category=`: the Quick Integration Guide's xUnit page says `--filter TestCategory=sample-test`,
which matches no test in this project, so 0 tests would run. The BrowserStack SDK (the
`BrowserStack.TestAdapter` package already in the project) runs `SampleTest` (adds a product to
the cart on bstackdemo.com and checks the cart, waiting for each element) with xUnit on every
platform in `browserstack.yml`, in parallel, and names and marks each session itself. The build
also adds the SDK's own `browserstack-sdk` tool to a `dotnet-tools.json`: list it in the plan.
