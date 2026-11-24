The sample project targets several .NET versions (`net6.0` to `net10.0`), so run it on the newest
one installed (from `dotnet --list-runtimes`), for example `net10.0`:

```bash
dotnet test --filter "Category=sample-test" -f net10.0
```

The BrowserStack SDK (the `BrowserStack.TestAdapter` package already in the project) runs
`SampleTest` (adds a product to the cart on bstackdemo.com and checks it is there) on every
platform in `browserstack.yml`, in parallel. The first build restores NuGet packages, which takes
a minute.
