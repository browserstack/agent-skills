  - The SDK marks desktop, Android and real iPhone sessions (iPhone verified with SDK 1.80.4, Nov
    2026); an iPhone build's own status can still read `done`, so report from the sessions. Every
    session is left `done` when the SDK prints `Binary CLI failed to start — running in direct
    flow`: re-run once in that case, then mark from the runner's result as shown below.
