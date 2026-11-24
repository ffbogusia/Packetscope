# Development

Read [AGENTS.md](../AGENTS.md) and [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)
before changing the project. Target Python 3.13; the package requires Python
3.13.x. Packet and alert models, parsing library, and detection contracts remain
open for joint agreement.

## Environment and installation

From the cloned repository root, create an isolated environment.

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```sh
python3.13 -m venv .venv
source .venv/bin/activate
```

With the environment active:

```sh
python --version
python -m pip install -e ".[dev]"
python -m app
python -m pytest
```

Check that the version is 3.13.x. If PowerShell activation is unavailable, invoke
`.venv\Scripts\python.exe` directly in place of `python`; activation is optional.

Setuptools is the build backend needed for installation. pytest is the sole
development dependency and runs the import smoke test. There are no runtime
dependencies. The entry point prints a title only.

## Collaboration

- Start each task from a GitHub Issue and use a dedicated feature branch.
- Keep changes small and link the Pull Request to the Issue.
- Run relevant pytest tests before proposing a commit; report unavailable tests.
- Use Pull Requests and code review before merging.
- Jointly agree on detection scenarios, packet fields, data contracts, parsing
  library, and interface changes before implementing dependent functionality.
- For future detections, test suspicious and benign synthetic or authorized
  traffic and document false positives and resource limits.

Do not add packet-analysis libraries or implement reserved modules as part of
foundation work. See [sample policy](../samples/README.md) before adding captures.
