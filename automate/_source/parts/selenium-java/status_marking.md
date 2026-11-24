  - Plain JUnit 5 and a framework-less `main()` are left `done` by the SDK. That is why B2 adds the
    callback; without it, mark the sessions from the runner's result as shown below.
  - The official sample has no test framework either: if its sessions show `done`, mark each one
    from the run output (each platform prints `Sample test passed!` when its flow succeeds).
