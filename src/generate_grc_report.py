from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

RISK_REGISTER_FILE = DATA_DIR / "risk_register.csv"
CONTROL_REGISTER_FILE = DATA_DIR / "control_register.csv"
EVIDENCE_REGISTER_FILE = DATA_DIR / "evidence_register.csv"
REMEDIATION_TRACKER_FILE = DATA_DIR / "remediation_tracker.csv"

OUTPUT_REPORT_FILE = REPORTS_DIR / "grc_executive_summary.md"
OUTPUT_COMBINED_REGISTER_FILE = REPORTS_DIR / "combined_grc_register.csv"


RISK_SCORE = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Critical": 4,
}

EVIDENCE_QUALITY_SCORE = {
    "Good": 3,
    "Partial": 2,
    "Weak": 1,
}


def load_csv(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")

    return pd.read_csv(file_path)


def validate_columns(df: pd.DataFrame, required_columns: list[str], file_name: str) -> None:
    missing = [column for column in required_columns if column not in df.columns]

    if missing:
        raise ValueError(f"{file_name} is missing required columns: {', '.join(missing)}")


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    risks = load_csv(RISK_REGISTER_FILE)
    controls = load_csv(CONTROL_REGISTER_FILE)
    evidence = load_csv(EVIDENCE_REGISTER_FILE)
    remediation = load_csv(REMEDIATION_TRACKER_FILE)

    validate_columns(
        risks,
        [
            "risk_id",
            "risk_title",
            "risk_category",
            "business_impact",
            "likelihood",
            "impact",
            "inherent_risk_rating",
            "control_status",
            "risk_owner",
            "treatment_decision",
        ],
        "risk_register.csv",
    )

    validate_columns(
        controls,
        [
            "control_id",
            "linked_risk_id",
            "control_name",
            "control_domain",
            "control_objective",
            "control_owner",
            "implementation_status",
            "review_frequency",
            "evidence_required",
        ],
        "control_register.csv",
    )

    validate_columns(
        evidence,
        [
            "evidence_id",
            "control_id",
            "evidence_name",
            "evidence_type",
            "evidence_owner",
            "evidence_status",
            "evidence_quality",
            "review_notes",
        ],
        "evidence_register.csv",
    )

    validate_columns(
        remediation,
        [
            "remediation_id",
            "linked_risk_id",
            "control_id",
            "remediation_action",
            "priority",
            "owner",
            "status",
            "target_date",
            "closure_evidence_required",
        ],
        "remediation_tracker.csv",
    )

    return risks, controls, evidence, remediation


def build_combined_register(
    risks: pd.DataFrame,
    controls: pd.DataFrame,
    evidence: pd.DataFrame,
    remediation: pd.DataFrame,
) -> pd.DataFrame:
    combined = risks.merge(
        controls,
        left_on="risk_id",
        right_on="linked_risk_id",
        how="left",
    )

    combined = combined.merge(
        evidence,
        on="control_id",
        how="left",
    )

    combined = combined.merge(
        remediation,
        on=["linked_risk_id", "control_id"],
        how="left",
        suffixes=("", "_remediation"),
    )

    combined["risk_numeric_score"] = (
        combined["inherent_risk_rating"].map(RISK_SCORE).fillna(1).astype(int)
    )

    combined["evidence_quality_score"] = (
        combined["evidence_quality"].map(EVIDENCE_QUALITY_SCORE).fillna(1).astype(int)
    )

    combined["evidence_gap"] = combined["evidence_status"].apply(
        lambda value: "Yes" if value == "Missing" else "No"
    )

    combined["governance_attention_required"] = combined.apply(
        lambda row: "Yes"
        if row["inherent_risk_rating"] == "High"
        and (row["evidence_status"] == "Missing" or row["status"] == "Open")
        else "No",
        axis=1,
    )

    return combined


def markdown_table(df: pd.DataFrame, columns: list[str]) -> str:
    if df.empty:
        return "No records found."

    return df[columns].to_markdown(index=False)


def generate_report(combined: pd.DataFrame) -> str:
    total_risks = combined["risk_id"].nunique()
    total_controls = combined["control_id"].nunique()
    total_evidence_items = combined["evidence_id"].nunique()
    total_remediation_items = combined["remediation_id"].nunique()

    high_risks = combined[combined["inherent_risk_rating"] == "High"]["risk_id"].nunique()
    missing_evidence = combined[combined["evidence_status"] == "Missing"]["evidence_id"].nunique()
    open_remediation = combined[combined["status"] == "Open"]["remediation_id"].nunique()
    governance_attention = combined[
        combined["governance_attention_required"] == "Yes"
    ]["risk_id"].nunique()

    risk_category_summary = (
        combined.groupby("risk_category")["risk_id"]
        .nunique()
        .reset_index(name="risk_count")
        .sort_values(by="risk_count", ascending=False)
    )

    evidence_status_summary = (
        combined.groupby("evidence_status")["evidence_id"]
        .nunique()
        .reset_index(name="evidence_count")
        .sort_values(by="evidence_count", ascending=False)
    )

    remediation_status_summary = (
        combined.groupby("status")["remediation_id"]
        .nunique()
        .reset_index(name="remediation_count")
        .sort_values(by="remediation_count", ascending=False)
    )

    attention_items = combined[
        combined["governance_attention_required"] == "Yes"
    ].sort_values(by="risk_numeric_score", ascending=False)

    report = f"""# Cyber Risk, Control and Evidence Register — Executive Summary

## Overview

This report demonstrates a practical cybersecurity GRC workflow that links cyber risks to controls, control evidence, remediation actions and governance attention items.

The project shows how a security governance team can move beyond static spreadsheets and create traceability across:

Risk -> Control -> Evidence -> Remediation -> Executive Reporting

## Key Metrics

| Metric | Value |
|---|---:|
| Total unique risks | {total_risks} |
| Total controls | {total_controls} |
| Total evidence items | {total_evidence_items} |
| Total remediation items | {total_remediation_items} |
| High risks | {high_risks} |
| Missing evidence items | {missing_evidence} |
| Open remediation items | {open_remediation} |
| Risks requiring governance attention | {governance_attention} |

## Risk Category Summary

{markdown_table(risk_category_summary, ["risk_category", "risk_count"])}

## Evidence Status Summary

{markdown_table(evidence_status_summary, ["evidence_status", "evidence_count"])}

## Remediation Status Summary

{markdown_table(remediation_status_summary, ["status", "remediation_count"])}

## Governance Attention Items

{markdown_table(
        attention_items,
        [
            "risk_id",
            "risk_title",
            "inherent_risk_rating",
            "control_name",
            "evidence_status",
            "status",
            "owner",
            "target_date",
        ],
    )}

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
"""

    return report


def save_outputs(combined: pd.DataFrame, report: str) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    combined.to_csv(OUTPUT_COMBINED_REGISTER_FILE, index=False)
    OUTPUT_REPORT_FILE.write_text(report, encoding="utf-8")

    print("GRC report generated successfully.")
    print(f"- {OUTPUT_COMBINED_REGISTER_FILE}")
    print(f"- {OUTPUT_REPORT_FILE}")


def main() -> None:
    risks, controls, evidence, remediation = load_data()

    combined = build_combined_register(
        risks=risks,
        controls=controls,
        evidence=evidence,
        remediation=remediation,
    )

    report = generate_report(combined)
    save_outputs(combined, report)


if __name__ == "__main__":
    main()
