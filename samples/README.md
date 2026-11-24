# Samples

No captures are included in the foundation. Use only synthetic or authorized
traffic; never commit confidential captures.

PCAP/PCAPNG files, including compressed variants, are ignored by default.
If both developers explicitly approve a synthetic fixture for version control,
add an exception for that exact path to the root `.gitignore` and document its
synthetic origin and purpose here. For example:

```gitignore
!samples/approved-synthetic-example.pcap
```

This is an example only; no fixture is currently approved. Future detection tests
should cover suspicious and benign traffic and explain limitations.
