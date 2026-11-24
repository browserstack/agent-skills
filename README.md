# agent-skills

AI agent skills for BrowserStack products. Each skill teaches a coding agent (Claude Code, Cursor, GitHub Copilot, Codex and others) to set up and run tests on BrowserStack from a single pasted prompt.

## Products

| Product | Folder |
| --- | --- |
| App Automate | [`app-automate/`](app-automate/) |

Each product folder has its own README listing its skills and the exact prompts to use.

## Use a skill

1. Set your credentials as environment variables. Skills never ask you to paste them into the prompt.
   ```bash
   export BROWSERSTACK_USERNAME=<username>
   export BROWSERSTACK_ACCESS_KEY=<access_key>
   ```
2. Paste the prompt for your skill (from the product folder's README) into your coding agent. The prompt follows this pattern:
   ```
   Download https://raw.githubusercontent.com/browserstack/agent-skills/main/<product>/<skill>/SKILL.md and save it permanently in this project's skills folder as <skill-name>/SKILL.md, then follow that skill to run the <framework> sample build on BrowserStack.
   ```
3. Answer the agent's questions and approve its plan. The agent saves the skill into its own skills folder (it stays installed for future sessions), runs the build and returns the dashboard link.

If your agent cannot run shell commands, open the `SKILL.md` on GitHub and follow it manually.

## Repository layout

```
<product>/
  README.md          # product skills, prompts and notes
  <skill>/
    SKILL.md         # one folder per skill
```

A skill folder is installed under the `name` in its `SKILL.md` frontmatter (for example `browserstack-app-automate-appium-python`).

## Updates

Prompts point at the `main` branch, so changes merged to `main` reach new installs right away. Treat every merge as a release: test the prompt end to end from your branch before merging.

An installed skill stays at the version it was downloaded at. To update, delete its folder from your skills folder and run the prompt again.

## Contributing

- Add or change skills only inside your product's folder, and update that folder's README.
- Each product folder has an owner in [`CODEOWNERS`](CODEOWNERS) who approves changes to it.
- To add a new product, create `<product>/README.md`, add a row to the Products table above and a `CODEOWNERS` entry.
