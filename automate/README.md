# Automate skills

Each skill takes a coding agent from one pasted prompt to a build on the BrowserStack Automate dashboard: BrowserStack's official sample build, or your own tests with no changes to your test logic. The agent checks your credentials, shows a plan, waits for your OK, runs the build and returns the dashboard link.

| Framework | Language | Runs on | Sample repo | Skill |
| --- | --- | --- | --- | --- |
| Selenium | Java | real desktop browsers and real mobile devices | [`vanilla-java-browserstack`](https://github.com/browserstack/vanilla-java-browserstack/tree/sdk-sample) | [`selenium-java`](selenium-java/SKILL.md) |
| Selenium | Python | real desktop browsers and real mobile devices | [`python-selenium-browserstack`](https://github.com/browserstack/python-selenium-browserstack/tree/main) | [`selenium-python`](selenium-python/SKILL.md) |
| Selenium | JavaScript | real desktop browsers and real mobile devices | [`mocha-browserstack`](https://github.com/browserstack/mocha-browserstack/tree/master) | [`selenium-javascript`](selenium-javascript/SKILL.md) |
| Selenium | C# | real desktop browsers and real mobile devices | [`nunit-browserstack`](https://github.com/browserstack/nunit-browserstack/tree/master) | [`selenium-csharp`](selenium-csharp/SKILL.md) |
| Playwright | JavaScript | real desktop browsers, with real Android and iPhone on request | [`node-js-playwright-browserstack`](https://github.com/browserstack/node-js-playwright-browserstack/tree/main) | [`playwright-javascript`](playwright-javascript/SKILL.md) |

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

## Maintaining these skills

The `SKILL.md` files are generated. Edit `_source/` (`template.md` for everything the skills share, `parts/<skill>/` for language-specific sections, `skills.json` for names, sample repos and platforms), then run:

```bash
python3 automate/_source/build.py          # regenerate the skills and this README
python3 automate/_source/build.py --check  # fail if anything is out of date
```

Prompts point at `main`, so a merge is live for new installs: test both prompts from your branch's raw URL before merging.
