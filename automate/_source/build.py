#!/usr/bin/env python3
"""Generate every automate/<skill>/SKILL.md from one shared template.

Edit automate/_source/ (template.md, skills.json, parts/), never the generated SKILL.md files:
a fix made once in the template reaches every language.

    python3 automate/_source/build.py           # regenerate all skills
    python3 automate/_source/build.py --check   # exit 1 if any SKILL.md is out of date
"""
import json
import pathlib
import re
import sys

SRC = pathlib.Path(__file__).resolve().parent
AUTOMATE = SRC.parent
RAW = "https://raw.githubusercontent.com/browserstack/agent-skills/main/automate/{folder}/SKILL.md"


def prompt(skill, kind):
    """The exact prompt a docs page shows: kind is 'sample' or 'own'."""
    what = (f"run the {skill['label']} sample build" if kind == "sample"
            else f"run my own {skill['label']} tests")
    return (f"Download {RAW.format(folder=skill['folder'])} and save it permanently in this "
            f"project's skills folder as {skill['name']}/SKILL.md, then follow that skill to "
            f"{what} on BrowserStack Automate.")


def prompts_table(skills, current):
    """The other skills: how to recognise their projects, and the own-tests prompt to hand over."""
    lines = []
    for s in skills:
        if s["folder"] == current["folder"]:
            continue
        lines.append(f"  - **{s['label']}** ({s['project_signal']}):\n"
                     f"    `{prompt(s, 'own')}`")
    return "\n".join(lines)


def render(text, skill, skills):
    def part(m):
        path = SRC / "parts" / skill["folder"] / f"{m.group(1)}.md"
        return path.read_text().rstrip("\n")

    text = re.sub(r"\{\{part:([a-z_]+)\}\}", part, text)
    values = dict(skill)
    values["raw_url"] = RAW.format(folder=skill["folder"])
    values["sample_yml_raw"] = (f"https://raw.githubusercontent.com/browserstack/{skill['sample_repo']}/"
                                f"{skill['sample_branch']}{skill['sample_subdir']}/browserstack.yml")
    values["prompt_sample"] = prompt(skill, "sample")
    values["prompt_own"] = prompt(skill, "own")
    values["prompts_table"] = prompts_table(skills, skill)
    for key, val in values.items():
        if isinstance(val, str):
            text = text.replace("{{" + key + "}}", val)
    left = re.findall(r"\{\{[^}]+\}\}", text)
    if left:
        sys.exit(f"{skill['folder']}: unresolved placeholders {sorted(set(left))}")
    return text


def readme(skills):
    """automate/README.md: the skill table and the two prompts per skill, from the same source."""
    out = ["# Automate skills", "",
           "Each skill takes a coding agent from one pasted prompt to a build on the BrowserStack "
           "Automate dashboard: BrowserStack's official sample build, or your own tests with no "
           "changes to your test logic. The agent checks your credentials, shows a plan, waits for "
           "your OK, runs the build and returns the dashboard link.", "",
           "| Framework | Language | Runs on | Sample repo | Skill |",
           "| --- | --- | --- | --- | --- |"]
    for s in skills:
        out.append(f"| {s['framework']} | {s['language']} | {s['platform_kind']} | "
                   f"[`{s['sample_repo']}`](https://github.com/browserstack/{s['sample_repo']}/tree/{s['sample_branch']}) | "
                   f"[`{s['folder']}`]({s['folder']}/SKILL.md) |")
    out += ["", "## Prompts", "",
            "Set `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` as environment variables first; "
            "never paste the key into a prompt.", ""]
    for s in skills:
        out += [f"**{s['label']}**", "", "Run the sample build:", "```", prompt(s, "sample"), "```",
                "Run your own tests:", "```", prompt(s, "own"), "```", ""]
    out += ["## Maintaining these skills", "",
            "The `SKILL.md` files are generated. Edit `_source/` (`template.md` for everything the "
            "skills share, `parts/<skill>/` for language-specific sections, `skills.json` for names, "
            "sample repos and platforms), then run:", "",
            "```bash", "python3 automate/_source/build.py          # regenerate the skills and this README",
            "python3 automate/_source/build.py --check  # fail if anything is out of date", "```", "",
            "Prompts point at `main`, so a merge is live for new installs: test both prompts from "
            "your branch's raw URL before merging.", ""]
    return "\n".join(out)


def main():
    check = "--check" in sys.argv
    skills = json.loads((SRC / "skills.json").read_text())
    template = (SRC / "template.md").read_text()
    stale = []
    outputs = [(AUTOMATE / s["folder"] / "SKILL.md", render(template, s, skills)) for s in skills]
    outputs.append((AUTOMATE / "README.md", readme(skills)))
    for out, text in outputs:
        if check:
            if not out.exists() or out.read_text() != text:
                stale.append(str(out.relative_to(AUTOMATE.parent)))
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text)
            print(f"wrote {out.relative_to(AUTOMATE.parent)} ({text.count(chr(10))} lines)")
    if check:
        if stale:
            print("Out of date — run python3 automate/_source/build.py:\n  " + "\n  ".join(stale))
            sys.exit(1)
        print(f"All {len(skills)} skills and the README are up to date.")


if __name__ == "__main__":
    main()
