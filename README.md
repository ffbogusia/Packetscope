# PacketScope — Network Threat Investigator

Project ID: **PACKETSCOPE-V01**

PacketScope is a planned Python application for offline PCAP/PCAPNG analysis,
network traffic investigation, and explainable security detections.

## Current status

Planning and foundation only: an installable Python 3.13 package, a placeholder
entry point, and an import smoke test. No parsing, detections, traffic models,
alerts, or dashboard functionality are implemented.

**Detection logic, packet models, alert models, shared interfaces, and the parsing
library are not yet finalized. Both developers will agree on them together.**

## Planned MVP

- Load and validate offline PCAP/PCAPNG files.
- Extract source/destination IPs, ports, and protocol information.
- Display network traffic statistics.
- Detect potential port scanning and unusual connection rates.
- Show explainable alerts with supporting evidence.
- Provide a Streamlit dashboard.

No live capture is planned for the MVP. Use only synthetic or authorized samples;
never commit confidential captures or secrets. Future detections must document
false positives and limitations.

## Proposed technology stack

- Python 3.13.
- pytest for tests and setuptools for packaging (included in this foundation).
- Streamlit for the planned UI; Docker and GitHub Actions are proposed tooling.
- Packet parsing library: to be selected jointly. Scapy, PyShark, and Zeek are
  not selected or installed.

There are no runtime dependencies. The optional `dev` extra installs only pytest.
Streamlit, Docker configuration, and CI workflows are deferred.

## High-level architecture

The project context proposes this flow; concrete interfaces remain open:

```text
PCAP file -> validation -> parser -> normalized traffic records
          -> detection engine -> alerts -> dashboard
```

```text
app/
  __init__.py
  __main__.py          # Placeholder entry point
  parser/__init__.py   # Reserved package; no parsing logic
  detection/__init__.py
  models/__init__.py   # No packet or alert contracts yet
  reporting/__init__.py
tests/                # Import smoke test
samples/              # Sample policy; no captures included
docs/                 # Project context and development instructions
```

Keep parsing, detection logic, and UI separate. These empty packages reserve the
requested structure without defining data contracts or dashboard behavior.

## Quick start

Create a virtual environment with Python 3.13:

```sh
python3.13 -m venv .venv
```

On Windows, use `py -3.13 -m venv .venv`. Activate it with
`.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate`
on macOS/Linux, then run:

```sh
python -m pip install -e ".[dev]"
python -m app
python -m pytest
```

The entry point only prints `PacketScope — Network Threat Investigator`.
See [development instructions](docs/DEVELOPMENT.md) for details.

## Collaboration

Read [AGENTS.md](AGENTS.md) and [project context](docs/PROJECT_CONTEXT.md) first.
Link tasks and Pull Requests to GitHub Issues, use one feature branch per task,
keep changes focused, and request code review through a Pull Request.
Agree on shared models and interfaces together and document changes before
dependent implementation. No developer ownership is assigned by this skeleton.
