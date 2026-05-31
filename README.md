# Cyber Risk, Control and Evidence Register

A practical cybersecurity GRC project that connects cyber risks, security controls, evidence records, remediation actions and executive-ready reporting.

This project demonstrates how cybersecurity governance work can be translated into a structured, auditable and decision-ready workflow. Instead of treating risk, controls, evidence and remediation as separate spreadsheets, this project links them together to show clear traceability from risk identification through to control assurance and reporting.

## Project Summary

Cybersecurity GRC teams need more than a list of risks. They need to show:

* What the risk is
* Which control addresses it
* Who owns the control
* What evidence proves the control is working
* What remediation is still open
* Which issues require governance attention
* What executives need to know for decision-making

This project turns simulated GRC data into a combined governance register and an executive summary report.

```text
Cyber Risk → Control → Evidence → Remediation → Executive Report
```

## Why This Project Matters

In real cybersecurity and information security environments, audit readiness depends on traceability.

A control is not useful unless it has:

* A clear owner
* A defined objective
* Evidence requirements
* Review frequency
* Implementation status
* Remediation tracking
* Closure evidence

This project demonstrates the ability to structure and automate that workflow using Python and CSV-based governance data.

## Key Features

* Cyber risk register
* Security control register
* Evidence register
* Remediation tracker
* Risk-to-control mapping
* Control-to-evidence mapping
* Evidence quality review
* Open remediation visibility
* Governance attention flagging
* Executive GRC summary report
* Combined GRC register generated with Python

## Repository Structure

```text
cyber-risk-control-evidence-register/
│
├── data/
│   ├── risk_register.csv
│   ├── control_register.csv
│   ├── evidence_register.csv
│   └── remediation_tracker.csv
│
├── src/
│   └── generate_grc_report.py
│
├── reports/
│   ├── combined_grc_register.csv
│   └── grc_executive_summary.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Input Files

### `data/risk_register.csv`

Contains simulated cyber risks, including:

* Risk ID
* Risk title
* Risk category
* Business impact
* Likelihood
* Impact
* Inherent risk rating
* Control status
* Risk owner
* Treatment decision

Example risk areas include:

* Privileged access risk
* Logging and monitoring gaps
* Sensitive data classification gaps
* Third-party security review gaps
* Vulnerability remediation delays
* Cloud storage exposure
* Privacy review gaps

### `data/control_register.csv`

Maps each risk to a practical control.

Control examples include:

* Privileged access review
* Centralised cloud logging
* Data classification register
* Vendor security review
* Vulnerability remediation tracking
* Security change approval
* Cloud storage access control
* Privacy impact review

Each control includes:

* Control owner
* Control objective
* Implementation status
* Review frequency
* Evidence required

### `data/evidence_register.csv`

Tracks evidence availability and quality.

Evidence is assessed using:

* Evidence status
* Evidence quality
* Evidence owner
* Review notes

Example evidence statuses:

* Provided
* Missing

Example evidence quality ratings:

* Good
* Partial
* Weak

### `data/remediation_tracker.csv`

Tracks remediation actions linked to risks and controls.

Each remediation item includes:

* Action required
* Priority
* Owner
* Status
* Target date
* Closure evidence required

## Generated Outputs

Running the Python script generates two portfolio-ready outputs.

### `reports/combined_grc_register.csv`

A combined register that links:

```text
Risk → Control → Evidence → Remediation
```

It includes additional governance fields such as:

* Numeric risk score
* Evidence quality score
* Evidence gap flag
* Governance attention flag

### `reports/grc_executive_summary.md`

An executive-ready report that summarises:

* Total risks
* Total controls
* Evidence status
* Open remediation items
* High-risk areas
* Governance attention items
* Recommended actions

## How the Governance Logic Works

The script identifies governance attention items when a high-risk issue has weak evidence, missing evidence or open remediation.

This helps prioritise risks that may create audit-readiness gaps or unresolved control weaknesses.

Example logic:

```text
High Risk + Missing Evidence = Governance Attention Required
High Risk + Open Remediation = Governance Attention Required
```

## How to Run

Install the required packages:

```bash
py -m pip install -r requirements.txt
```

Run the report generator:

```bash
py src/generate_grc_report.py
```

Check the generated reports:

```bash
dir reports
```

Expected outputs:

```text
combined_grc_register.csv
grc_executive_summary.md
```

## Example Workflow

```text
Risk Register
     ↓
Control Register
     ↓
Evidence Register
     ↓
Remediation Tracker
     ↓
Python Report Generator
     ↓
Combined GRC Register + Executive Summary Report
```

## Skills Demonstrated

This project demonstrates practical skills in:

* Cybersecurity GRC
* Cyber risk management
* Control mapping
* Evidence management
* Security assurance
* Audit readiness
* Remediation tracking
* Governance reporting
* Risk-based prioritisation
* Python-based reporting automation
* Executive communication
* Data-driven security governance

## Career Relevance

This project is aligned with roles such as:

* Cybersecurity GRC Analyst
* Cybersecurity Analyst
* Information Security Analyst
* Security Governance Analyst
* Risk and Compliance Analyst
* Security Assurance Analyst
* Data Privacy Analyst
* Cloud Security Governance Analyst

## Practical Value

This project shows how security governance can be made more structured, traceable and repeatable.

It demonstrates the ability to turn GRC data into useful outputs for:

* Control owners
* Security teams
* Risk and compliance teams
* Privacy teams
* Audit and assurance reviewers
* Senior stakeholders

## Future Improvements

Planned improvements include:

* Add a Streamlit dashboard
* Add risk heatmap visualisation
* Add control effectiveness scoring
* Add ISO 27001 and NIST CSF mapping
* Add Essential Eight alignment
* Add remediation SLA tracking
* Add evidence expiry dates
* Add automated overdue remediation flagging
* Add Power BI-ready output
* Add sample screenshots of generated reports

## Disclaimer

This project uses simulated cybersecurity GRC data for portfolio and learning purposes. It does not contain real client, employer, security, privacy, audit or confidential organisational data.

## Author

**Parisa Shojaei**

Cybersecurity GRC · Cloud Security · Privacy Governance · Risk Analytics · AI Assurance | Turning risks into audit-ready evidence
