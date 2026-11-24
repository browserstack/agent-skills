```bash
dotnet build <path/to/Tests.csproj>
dotnet test <path/to/Tests.csproj>          # add --filter "FullyQualifiedName~Login" for a subset
```

If the project targets several frameworks, add `-f <newest installed>` (for example `-f net10.0`);
otherwise `dotnet test` also tries versions whose runtime isn't installed. Don't add `-v q` or
`--nologo`-style quiet flags that hide the SDK's output.
