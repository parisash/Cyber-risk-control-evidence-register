# Cyber Risk, Control and Evidence Register — Executive Summary

## Overview

This report demonstrates a practical cybersecurity GRC workflow that links cyber risks to controls, control evidence, remediation actions and governance attention items.

The project shows how a security governance team can move beyond static spreadsheets and create traceability across:

Risk -> Control -> Evidence -> Remediation -> Executive Reporting

## Key Metrics

| Metric | Value |
|---|---:|
| Total unique risks | 10 |
| Total controls | 10 |
| Total evidence items | 10 |
| Total remediation items | 10 |
| High risks | 6 |
| Missing evidence items | 2 |
| Open remediation items | 5 |
| Risks requiring governance attention | 3 |

## Risk Category Summary

| risk_category                  |   risk_count |
|:-------------------------------|-------------:|
| Change and Release Governance  |            1 |
| Cloud Security                 |            1 |
| Data Protection and Privacy    |            1 |
| Identity and Access Management |            1 |
| Incident Response              |            1 |
| Logging and Monitoring         |            1 |
| Privacy Governance             |            1 |
| Security Governance            |            1 |
| Third-Party Risk               |            1 |
| Vulnerability Management       |            1 |

## Evidence Status Summary

| evidence_status   |   evidence_count |
|:------------------|-----------------:|
| Provided          |                8 |
| Missing           |                2 |

## Remediation Status Summary

| status      |   remediation_count |
|:------------|--------------------:|
| Open        |                   5 |
| In Progress |                   4 |
| Closed      |                   1 |

## Governance Attention Items

| risk_id   | risk_title                                             | inherent_risk_rating   | control_name                 | evidence_status   | status   | owner                    | target_date   |
|:----------|:-------------------------------------------------------|:-----------------------|:-----------------------------|:------------------|:---------|:-------------------------|:--------------|
| R-002     | Incomplete logging for critical cloud activities       | High                   | Centralised Cloud Logging    | Provided          | Open     | Security Operations Team | 2026-06-20    |
| R-003     | Sensitive data stored without clear classification     | High                   | Data Classification Register | Missing           | Open     | Data Governance Team     | 2026-06-25    |
| R-010     | Privacy review gaps for new data processing activities | High                   | Privacy Impact Review        | Provided          | Open     | Privacy and Legal Team   | 2026-06-28    |

## GRC Interpretation

The highest-priority issues are risks with a High inherent risk rating, missing or weak evidence, and open remediation actions.

These items require governance attention because they may create audit-readiness gaps, unclear ownership, delayed remediation, or weak evidence traceability.

## Recommended Actions

1. Prioritise High risks with missing evidence.
2. Confirm accountable owners for open remediation items.
3. Improve evidence quality for Partial and Weak evidence records.
4. Review controls that remain Partially Implemented.
5. Track closure evidence before marking remediation items as complete.
6. Maintain a repeatable evidence register for audit and assurance activities.

## Disclaimer

This project uses simulated GRC data for portfolio and learning purposes. It does not contain real client, employer, security, privacy or audit data.
