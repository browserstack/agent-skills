The sample floats `Microsoft.Playwright.NUnit` to the latest release but pins an older
`Microsoft.NET.Test.Sdk`, so restore stops with `NU1605: Detected package downgrade`; and it targets
`net6.0`. Both are handled with environment variables, without changing any file:

```bash
NoWarn=NU1605 DOTNET_ROLL_FORWARD=Major dotnet test --filter "Category=sample-test"
```

`NoWarn` must be an environment variable, not `-p:NoWarn`, because the SDK runs its own restore.
With a 6.0 runtime installed, drop `DOTNET_ROLL_FORWARD=Major`. PowerShell: set
`$env:NoWarn="NU1605"` and `$env:DOTNET_ROLL_FORWARD="Major"` first. The BrowserStack SDK (the
`BrowserStack.TestAdapter` package already in the project) runs `SampleTest` (adds a product to
the cart on bstackdemo.com and checks the cart) on every platform in `browserstack.yml` (desktop
Chrome, WebKit and Firefox), in parallel. The build also adds the SDK's own `browserstack-sdk` tool
to a `dotnet-tools.json`: list it in the plan. Warnings that `net6.0` is out of support are harmless.
If a first attempt failed, delete `bin/` and `obj/` before running again (see Troubleshooting).

Before running, check `browserstack.yml` for a `browserName: Safari` on a desktop (`os:`) row
(`grep -niB3 "browserName: *safari" browserstack.yml`). If there is one, change it to
`playwright-webkit` with `browserVersion: latest`, and list that change in the plan; `safari` stays only on real iPhone rows.
