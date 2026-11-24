The sample project targets `net6.0`. If `dotnet --list-runtimes` shows no `Microsoft.NETCore.App
6.0.x`, let it run on the newest installed runtime without changing any file:

```bash
DOTNET_ROLL_FORWARD=Major dotnet test --filter "Category=sample-test"
```

With a 6.0 runtime installed, drop `DOTNET_ROLL_FORWARD=Major` (PowerShell:
`$env:DOTNET_ROLL_FORWARD="Major"` first). The BrowserStack SDK (the `BrowserStack.TestAdapter`
package already in the project) runs `SampleTest` (adds a product to the cart on bstackdemo.com
and checks the cart) on every platform in `browserstack.yml` (desktop Chrome, WebKit and Firefox),
in parallel. The build may also add the SDK's own `browserstack-sdk` tool to a
`dotnet-tools.json`: list it in the plan. Warnings that `net6.0` is out of support are harmless.
