# Installation / 安装

The installable folder is `skills/dialectic/`. Copy the whole folder, including its reference and metadata. Do not copy only SKILL.md, and do not install the repository root.

## Codex: local personal skill

Run from the downloaded or cloned repository root on macOS/Linux:

```bash
mkdir -p ~/.agents/skills
# First installation: stop if a skill with this name already exists.
test ! -e ~/.agents/skills/dialectic && cp -R skills/dialectic ~/.agents/skills/dialectic
```

PowerShell, from the repository root:

```powershell
$destination = Join-Path $HOME ".agents/skills/dialectic"
if (Test-Path $destination) { throw "dialectic already exists; review it before replacing." }
New-Item -ItemType Directory -Force (Split-Path $destination) | Out-Null
Copy-Item -Recurse "skills/dialectic" $destination
```

Invoke `$dialectic`. For repository-scoped use, copy the folder under your target project's `.agents/skills/` instead.

## Claude Code: local personal skill

On macOS/Linux, from this repository:

```bash
mkdir -p ~/.claude/skills
test ! -e ~/.claude/skills/dialectic && cp -R skills/dialectic ~/.claude/skills/dialectic
```

On Windows PowerShell, use the Codex snippet with destination `.claude/skills/dialectic`. Invoke `/dialectic`. For project scope, use your target project's `.claude/skills/dialectic/`.

These commands are local installs. Cloud/account-managed skills can use different distribution paths; local copying does not install into a cloud account.

## Any assistant: manual use

Provide both [SKILL.md](../skills/dialectic/SKILL.md) and [protocol.md](../skills/dialectic/references/protocol.md) as context, then submit your idea and constraints. This does not install a skill or provide automatic triggering.

## Check discovery

Ask the host to use Dialectic on a small proposal. Confirm it can read the protocol and produces a next action plus stopping reason. If discovery fails, inspect the host's skill list and official documentation. Check for a conflicting skill named dialectic before changing files.

## Uninstall and update

Remove only the dialectic folder you installed to disable that local copy. For updates, compare your installed files against this release and preserve any custom changes before replacing them.

## Source and compatibility scope

Paths/invocations were checked against official documentation on 2026-09-29:

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI skills documentation](https://developers.openai.com/codex/skills/)
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)

Format validation and assistant smoke tests are included. A full live test of each client/version/OS is not claimed. The project intentionally uses the minimal portable name/description frontmatter. Optional agents/openai.yaml is host-specific metadata.
