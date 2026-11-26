# Automate skills

Each skill takes a coding agent from one pasted prompt to a build on the BrowserStack Automate dashboard: BrowserStack's official sample build, or your own tests with no changes to your test logic. The agent checks your credentials, shows a plan, waits for your OK, runs the build and returns the dashboard link.

| Framework | Language | Runs on | Sample repo (as in the Quick Integration Guide) | Skill |
| --- | --- | --- | --- | --- |
| Selenium | Java | real desktop browsers and real mobile devices | [`junit-browserstack@master`](https://github.com/browserstack/junit-browserstack/tree/master) ([guide](https://www.browserstack.com/docs/onboarding-cad/junit-5-sdk/getting-started)) | [`selenium-java`](selenium-java/SKILL.md) |
| Selenium | Python | real desktop browsers and real mobile devices | [`python-selenium-browserstack@main`](https://github.com/browserstack/python-selenium-browserstack/tree/main) ([guide](https://www.browserstack.com/docs/onboarding-cad/python-sdk/getting-started)) | [`selenium-python`](selenium-python/SKILL.md) |
| Selenium | JavaScript | real desktop browsers and real mobile devices | [`jest-js-browserstack@main`](https://github.com/browserstack/jest-js-browserstack/tree/main) ([guide](https://www.browserstack.com/docs/onboarding-cad/nodejs-sdk/getting-started)) | [`selenium-javascript`](selenium-javascript/SKILL.md) |
| Selenium | C# | real desktop browsers and real mobile devices | [`xunit-browserstack@main`](https://github.com/browserstack/xunit-browserstack/tree/main) ([guide](https://www.browserstack.com/docs/onboarding-cad/xunit-sdk/getting-started)) | [`selenium-csharp`](selenium-csharp/SKILL.md) |
| Playwright | JavaScript | real desktop browsers, with real Android and iPhone on request | [`node-js-playwright-browserstack@tra`](https://github.com/browserstack/node-js-playwright-browserstack/tree/tra) ([guide](https://www.browserstack.com/docs/onboarding-cad/playwright-qig/nodejs-sdk/getting-started)) | [`playwright-javascript`](playwright-javascript/SKILL.md) |
| Playwright | Python | real desktop browsers, with a real iPhone on request | [`pytest-playwright-browserstack@main`](https://github.com/browserstack/pytest-playwright-browserstack/tree/main) ([guide](https://www.browserstack.com/docs/onboarding-cad/playwright-qig/python-sdk/getting-started)) | [`playwright-python`](playwright-python/SKILL.md) |
| Playwright | Java | real desktop browsers, with a real iPhone on request | [`java-playwright-browserstack@main`](https://github.com/browserstack/java-playwright-browserstack/tree/main) ([guide](https://www.browserstack.com/docs/onboarding-cad/playwright-qig/java-sdk/getting-started)) | [`playwright-java`](playwright-java/SKILL.md) |
| Playwright | C# | real desktop browsers, with a real iPhone on request | [`csharp-playwright-browserstack@main`](https://github.com/browserstack/csharp-playwright-browserstack/tree/main) ([guide](https://www.browserstack.com/docs/onboarding-cad/playwright-qig/c-sharp-sdk/getting-started)) | [`playwright-csharp`](playwright-csharp/SKILL.md) |

## Prompts

Set `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` as environment variables first; never paste the key into a prompt.

**Selenium Java**

Run the sample build:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-java/SKILL.md, then follow that skill to run the Selenium Java sample build on BrowserStack Automate.
```
Run your own tests:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-java/SKILL.md, then follow that skill to run my own Selenium Java tests on BrowserStack Automate.
```

**Selenium Python**

Run the sample build:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-python/SKILL.md, then follow that skill to run the Selenium Python sample build on BrowserStack Automate.
```
Run your own tests:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-python/SKILL.md, then follow that skill to run my own Selenium Python tests on BrowserStack Automate.
```

**Selenium JavaScript**

Run the sample build:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-javascript/SKILL.md, then follow that skill to run the Selenium JavaScript sample build on BrowserStack Automate.
```
Run your own tests:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-javascript/SKILL.md, then follow that skill to run my own Selenium JavaScript tests on BrowserStack Automate.
```

**Selenium C#**

Run the sample build:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-csharp/SKILL.md, then follow that skill to run the Selenium C# sample build on BrowserStack Automate.
```
Run your own tests:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/selenium-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-selenium-csharp/SKILL.md, then follow that skill to run my own Selenium C# tests on BrowserStack Automate.
```

**Playwright JavaScript**

Run the sample build:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-javascript/SKILL.md, then follow that skill to run the Playwright JavaScript sample build on BrowserStack Automate.
```
Run your own tests:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-javascript/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-javascript/SKILL.md, then follow that skill to run my own Playwright JavaScript tests on BrowserStack Automate.
```

**Playwright Python**

Run the sample build:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-python/SKILL.md, then follow that skill to run the Playwright Python sample build on BrowserStack Automate.
```
Run your own tests:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-python/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-python/SKILL.md, then follow that skill to run my own Playwright Python tests on BrowserStack Automate.
```

**Playwright Java**

Run the sample build:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-java/SKILL.md, then follow that skill to run the Playwright Java sample build on BrowserStack Automate.
```
Run your own tests:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-java/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-java/SKILL.md, then follow that skill to run my own Playwright Java tests on BrowserStack Automate.
```

**Playwright C#**

Run the sample build:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-csharp/SKILL.md, then follow that skill to run the Playwright C# sample build on BrowserStack Automate.
```
Run your own tests:
```
Download https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/playwright-csharp/SKILL.md and save it permanently in this project's skills folder as browserstack-automate-playwright-csharp/SKILL.md, then follow that skill to run my own Playwright C# tests on BrowserStack Automate.
```

## Maintaining these skills

The `SKILL.md` files are generated. Edit `_source/` (`template.md` for everything the skills share, `parts/<skill>/` for language-specific sections, `skills.json` for names, sample repos and platforms), then run:

```bash
python3 automate/_source/build.py          # regenerate the skills and this README
python3 automate/_source/build.py --check  # fail if anything is out of date
```

Prompts point at `main`, so a merge is live for new installs: test both prompts from your branch's raw URL before merging.
