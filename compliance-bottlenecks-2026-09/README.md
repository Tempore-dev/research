# Compliance bottlenecks (September 2026)

**Question.** Which recurring bottleneck frustrations do practitioners voice on online platforms (Reddit, Hacker News, industry forums, G2/Capterra reviews, trade publications) about industry-specific compliance requirements, and which of them are software opportunities Tempore could realistically pursue?

**Read first:** [report.md](report.md), about 7,400 words with around 86 inline sources.

## Main finding

In every sector studied, the dominant bottleneck is keeping per-person, per-asset or per-product evidence files complete, current and producible on demand, followed by re-typing the same facts into mandated portals and customer questionnaires. The best fit for a small firm is one reusable "people/entities × requirements × expiry × evidence" engine with a thin per-jurisdiction rules layer, sold as companion tools that sit beside mandated systems of record (Metrc, the FMCSA Clearinghouse, CAQH, state EVV aggregators, CBP ACE) rather than replacing them.

## Top of the ranking

Scored 1–5 on pain and evidence, timing, competitor gap, build complexity and liability, and distribution (maximum 25). The full table of 20 is in the report.

| # | Opportunity | Score |
|---|---|---|
| 1 | Mobile privacy-label, age-assurance and COPPA kit for app developers | 21 |
| 2 | Offline-first expiring-evidence locker for small fleets and contractors | 19 |
| 3 | Per-SKU marketplace compliance vault with CPSC eFiling data prep | 19 |
| 4 | Accessibility CI, remediation tracker and ACR/EAA-statement generator | 19 |
| 5 | HVAC refrigerant leak-rate logger under the EPA 15-lb rule | 19 |
| 6 | WISP and Reg S-P "living program" manager for tax, CPA and small-RIA firms | 18 |

## Evidence limitation

The research environment blocked Reddit, Hacker News, G2, Capterra, Trustpilot and most trade forums. Practitioner quotes are near-verbatim renderings of search-result snippets, not first-hand reads, and several headline figures are vendor-sourced. Regulatory dates and the independent surveys (AMA, Advarra, MedTech Europe, NAFCC, U.S. Chamber, Seyfarth, DOL burden estimates) are the more reliable layer. Validate with practitioners before building; the report's last section has a 60-day plan.

## Files

| File | Covers |
|---|---|
| [report.md](report.md) | Synthesis: pain patterns, incumbent complaints, 20 ranked opportunities, delayed and live deadlines, validation plan |
| [notes/healthcare-life-sciences.md](notes/healthcare-life-sciences.md) | HIPAA for small practices, prior auth, credentialing/CAQH, EVV, GxP/CSA, clinical-trial sites, QMSR, CLIA, DSCSA |
| [notes/financial-services.md](notes/financial-services.md) | KYC/AML, small RIAs and broker-dealers, Reg S-P, insurance licensing/CE, WISP, CTA/BOI, PCI DSS 4.0, DORA, CFPB 1033/1071 |
| [notes/field-operations.md](notes/field-operations.md) | Construction/OSHA, certified payroll, COIs and lien waivers, trucking/FMCSA, food safety/FSMA 204, cannabis/Metrc, HVAC refrigerants, PFAS, H-2A |
| [notes/tech-privacy-security.md](notes/tech-privacy-security.md) | SOC 2/ISO 27001 and compliance automation, CMMC, privacy and DSARs, COPPA and age assurance, accessibility, EU AI Act, CRA, app-store policy |
| [notes/sustainability-trade.md](notes/sustainability-trade.md) | CSRD/VSME, CSDDD, EUDR, CBAM, DPP/ESPR, PPWR and US EPR, tariffs and de minimis, UFLPA, GPSR and CPSC eFiling |
| [notes/local-small-business.md](notes/local-small-business.md) | Childcare and CACFP, youth programs, real estate post-NAR settlement, landlords, HOAs, med spas, nonprofits, employer HR, CE tracking |

## Provenance

Produced on September 25–26, 2026 by six parallel research passes (one per notes file) and a synthesis pass, first committed to `Tempore-dev/tempore-site` on branch `claude/compliance-bottleneck-research-354f3t` and moved here. Note file names were changed from snake_case to kebab-case; content is unchanged.
