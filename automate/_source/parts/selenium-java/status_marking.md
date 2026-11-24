  - Plain JUnit 5 and a framework-less `main()` are left `done` by the SDK. That is why B2 adds the
    callback; without it, mark the sessions from the runner's result as shown below.
  - The official sample has no test framework either, so its sessions are left `done`. Mark each
    from `log/browserstack-javaagent.log`: it records each platform's capabilities and any
    exception (the console prints `Sample test passed!` on success, without the platform).
