# agent-skills
Public repo hosting AI agent (onboarding) skills for Automate customers


## App Automate skills

Each skill takes a coding agent (Claude Code, Cursor, GitHub Copilot, Codex and others) from a pasted prompt to a build on the BrowserStack App Automate dashboard. Set `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` as environment variables first; the skills never ask you to paste credentials into the prompt.

| Framework | Language | Platforms | Skill |
| --- | --- | --- | --- |
| Appium | Python | Android, iOS | [`app-automate/appium-python`](app-automate/appium-python/SKILL.md) |
| Appium | Java (TestNG) | Android, iOS | [`app-automate/appium-java`](app-automate/appium-java/SKILL.md) |
| Appium | JavaScript (WebdriverIO) | Android, iOS | [`app-automate/appium-javascript`](app-automate/appium-javascript/SKILL.md) |

### Use a skill

Paste this into your coding agent, replacing `appium-python` / `Appium Python` with your skill:

```
Read https://raw.githubusercontent.com/browserstack/agent-skills/app-automate-v1.0.0/app-automate/appium-python/SKILL.md, install it as a skill in this project, then follow it to run the Appium Python sample build on BrowserStack App Automate.
```

To integrate your own suite instead of the sample, replace "the Appium Python sample build" with "my own Appium Python tests".

### Releases

App Automate skills are released with tags of the form `app-automate-vX.Y.Z`. Prompts and install steps pin to a tag, so changes on `main` do not affect customers until a new tag is cut.
