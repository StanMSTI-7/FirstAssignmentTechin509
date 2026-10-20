# My assistant — scoping brief

Replace the prompts with your own answers. Keep this in `docs/SCOPING.md`.

## Objectives

Target user: Professional Engineers (Mechanical, Industrial Electrical, Civil, drafters working under a licensed engineer)

Objectives: to assist engineers in utilizing AI assistant to apply appropriate specifications and requirements for a engineering project. 

1. Assistant to help engineers in suggesting the proper codes and standard to ensure that the project is meeting safety requirements. 

2. Assistant to help engineers in identifying root cause of a problem from diagnosing the symptomps before costing the company significant cost for fixing errors 

## The gap / need

In the past, it would take a significant amount of time for Engineers to apply the appropriate codes and regulation for a certain projects. Engineers tend to miss specific requirements as such This technology is needed to help engineer bridge that gap and work efficiently. 

## Problem:

Engineers must apply many overlapping codes and standards—ASME, ASTM, ISO, IEC, NEC, NFPA, IBC, ASCE, ACI, AISC, ASHRAE, IEEE, UL, OSHA, local amendments—across mechanical, civil, and electrical disciplines. Finding the right edition, clause, jurisdiction amendment, and project-specific requirement is slow and error-prone. Misapplied codes cause rework, RFIs, failed inspections, safety risk, and liability.

from time to time, they also face operational problems (equipment failures, inefficiencies, downtime) where finding the true root cause is difficult and costly. Misapplied codes or misdiagnosed root causes cause rework, RFIs, failed inspections, safety risk, liability, and unnecessary operational expense.

## Key deliverables / Intended tasks:

1. Identify applicable codes/standards by discipline, jurisdiction, project type, and occupancy.
2. Retrieve and summarize specific clauses with edition/year and section citations.
3. Compare project specifications against code requirements.
4. Generate compliance checklists and design-review questions.
5. Draft RFIs, code interpretations, and justification notes for engineer review.
6. Flag conflicts between codes, standards, and client specifications.
7. Assist with preliminary calculations using cited formulas, units, and assumptions.
8. Perform structured root cause analysis (RCA) for operational problems using methods like 5 Whys, Fishbone, FMEA, and fault tree analysis.
9. Diagnose equipment failures, process inefficiencies, and recurring maintenance issues.
10. Recommend corrective actions with estimated cost savings and downtime reduction.
11. Track RCA outcomes and cost savings over time.
12. Summarize code updates and local amendments.
13. Maintain project context across sessions without exposing confidential data.

## Data requirements & constraints

Name the synthetic, sanitized, or permitted public sources you will use. State what must never enter the repository or an agent prompt: PII, credentials, employer/client-confidential and export-controlled material. How will you check the boundary?

Public codes and standards: IBC, IECC, NFPA, NEC, ASHRAE, ASME, ASTM, ASCE, ACI, AISC, IEEE, UL, OSHA, ISO, IEC.
Local jurisdiction amendments and AHJ guidance.
Authorized project specifications, drawings metadata, and internal engineering standards.
Manufacturer data and installation manuals.
Company SOPs and QA/QC checklists.
Operational data: sensor logs, maintenance records, failure reports, downtime logs, work orders, and process data—de-identified or aggregated where required.
Not permitted by default: client-identifying drawings, proprietary trade secrets, export-controlled technical data, personal data, or unapproved third-party uploads.

## Privacy Constraints — essential:

- Comply with NDAs, client confidentiality agreements, and internal IP policies.
- Follow export-control rules such as ITAR/EAR where applicable.
- Protect personal data under GDPR, CCPA, and similar laws if present in project documents.
- No training on proprietary project data without explicit written permission.
- Role-based access control: engineer, reviewer, project manager, admin.
- Encryption in transit and at rest; audit logs for all queries and document access.
- Redact client names, project addresses, proprietary dimensions, trade secrets, and personal data before logging.
-Operational data must be de-identified or aggregated before use; no raw sensitive operational data in prompts unless in an authorized secure environment.
- Data residency and tenant isolation options: on-prem, private cloud, or region-specific deployment.
- User can clear history; retention limits enforced.
- No confidential data in prompts unless the environment is authorized and secure.

## Success measure


1. Correctly identify the applicable code/standard and edition/year in ≥95% of expert-reviewed cases.
2. Provide accurate clause citations in ≥95% of responses.
3. Detect jurisdiction-specific amendments in ≥90% of cases where applicable.
4. Reduce code lookup and compliance-check time by ≥40%.
5. Reduce RFIs/rework caused by code misunderstanding by ≥25%.
6. Flag when licensed engineer judgment, AHJ ruling, or legal review is required in 100% of safety-critical or ambiguous cases.
7. Maintain zero unauthorized disclosures of confidential project data in quarterly audits.
8. Achieve user satisfaction ≥4.5/5 across pilot engineering teams.
9. Correctly identify the root cause in ≥85% of validated operational problem cases (confirmed by post-mortem analysis or senior engineer review).
10. Reduce mean time to repair (MTTR) for diagnosed operational problems by ≥30%.
11. Document measurable cost savings from fixes based on assistant recommendations: average ≥$10,000 per incident or ≥15% reduction in operational maintenance costs within 6 months.
12. Engineers report that the assistant helped them solve operational problems faster and with greater confidence in ≥80% of cases.


