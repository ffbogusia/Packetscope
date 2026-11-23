# PacketScope — AI Development Guidelines

Project ID: PACKETSCOPE-V01

## Project context
Read docs/PROJECT_CONTEXT.md before making changes.

PacketScope is a Python application for offline
PCAP/PCAPNG analysis and explainable security detections.

## Development rules
- Use Python 3.13.
- Write clear, modular, maintainable code.
- Use type hints for public functions.
- Keep parsing, detection logic and UI separate.
- Follow agreed data contracts.
- Do not redesign architecture without agreement.
- Make small, focused changes.
- Never modify unrelated modules.
- Explain any proposed new dependencies.

## Testing
- Use pytest.
- Test both suspicious and benign traffic.
- Run relevant tests before proposing a commit.
- Report any tests that could not be run.

## Security
- Use only synthetic or authorized PCAP samples.
- No live packet interception in the MVP.
- Never commit confidential captures or secrets.
- Validate inputs and limit resource usage.
- Explain false positives and detection limitations.

## Collaboration
- One feature branch per task.
- Link work to GitHub Issues.
- Use Pull Requests and code review.
- Document shared interface changes.
- Keep commits focused and descriptive.

## AI behavior
- Summarize the task before coding.
- Explain important technical decisions.
- Avoid unrelated changes.
- Report changed files, test results and limitations.
- Never commit or push without explicit permission.
