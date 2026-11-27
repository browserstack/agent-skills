Build first: the SDK hooks into the test assembly at build time.

```bash
dotnet build <path/to/Tests.csproj>
dotnet test <path/to/Tests.csproj>          # add --filter "FullyQualifiedName~Cart" for a subset
```

If the project targets several frameworks, add `-f <newest installed>`; if its only target's
runtime isn't installed, prefix `DOTNET_ROLL_FORWARD=Major`. Don't run `playwright.ps1 install`:
the browsers run on BrowserStack.
