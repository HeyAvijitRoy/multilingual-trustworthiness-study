# RIU Pilot v0.1 Manifest

## Purpose

This pilot tests whether the Required Information Unit (RIU) annotation scheme is sufficiently atomic, scoreable, and language-neutral before scaling annotation to all 500 tasks.

No model outputs were used to create the pilot annotations.

## Coverage

| Domain | Selected tasks |
|---|---|
| Technical troubleshooting | TECH001, TECH004, TECH006, TECH009, TECH010 |
| Cybersecurity and digital safety | CYBER001, CYBER004, CYBER006, CYBER009, CYBER010 |
| Procedural and instructional | PROC001, PROC004, PROC006, PROC009, PROC010 |
| Decision support | DEC001, DEC004, DEC006, DEC009, DEC010 |
| Information synthesis | SYN004, SYN008, SYN009, SYN091, SYN100 |

Total: **25 tasks**

The pilot includes easy, medium, and hard tasks in every domain. `SYN091` and `SYN100` represent the extended-context subset.

## Current QA result

- Tasks: 25
- Domain allocation: 5 per domain
- RIUs: 130
- Critical RIUs: 100
- Extended-context pilot items: SYN091, SYN100
- Structural/schema validation: PASS
- Prompt corpus modified: NO
- Model generations performed: NO

## Review status

All records currently use `pilot-internal-reviewed`.

This means they have been checked for:
- alignment with frozen prompt semantics;
- RIU atomicity;
- explicit scoring rules;
- critical/supporting distinction;
- difficulty/domain coverage;
- basic structural validity.

It does **not** mean the pilot is a frozen gold annotation set. The next gate is annotation-method review/adjudication before scaling to 500 tasks.
