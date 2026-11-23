# PacketScope- Project Context v0.1

Project version: PACKETSCOPE-V01
Status: Planning

## Goal
Build an open-source Python application for offline PCAP/PCAPNG analysis, network traffic investigation and detection of potentially suspicious behavior.

## MVP
- Load and validate PCAP/PCAPNG files.
- Extract source/destination IPs, ports and protocol information.
- Display network traffic statistics.
- Detect potential port scanning and unusual connection rates.
- Show explainable alerts with supporting evidence.
- Provide a Streamlit dashboard.

## Proposed stack
Python 3.13, Streamlit, pytest, Docker and GitHub Actions. Packet parsing library to be selected jointly.

## Architecture
PCAP file -> validation -> parser -> normalized traffic records -> detection engine -> alerts -> dashboard.

## Collaboration
Two contributors. Work through GitHub Issues, feature branches, Pull Requests and code review. Both contributors participate in technical decisions.

## Security
Offline analysis only. No live capture or confidential traffic. Use synthetic or authorized test samples. Document detection limitations and false positives.

## Current status
Repository and GitHub Project created. First planning Issue opened. Architecture, ownership, parsing library and data models are not yet finalized.

## Next step
Jointly define two MVP detection scenarios and their required packet fields.
