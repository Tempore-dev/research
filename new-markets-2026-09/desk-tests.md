# New-markets desk tests (September 2026)

Three decisive desk tests on product leads from the 2026-09-26 new-markets research: the nursing-home Medicaid look-back packet builder (Watch), the long-term-care insurance claim manager (near miss), and building MCP servers / ChatGPT apps / Claude connectors for SaaS vendors (service lead). All research below is desk research only — no sign-ins, no accounts, no forms submitted, no outreach, reddit.com was not used.

**Environment note (applies to all three tests):** this session's network egress was blocked for nearly every external domain except a narrow allowlist (mostly package registries). Direct page/PDF reads (`WebFetch`, `curl`) failed for CMS, state Medicaid agencies, KFF, MACPAC, insurance-carrier sites, the iTunes Search API, and even neutral sites like Wikipedia and `example.com`. All three tests had to rely on a server-side web-search tool's synthesized snippets instead of reading primary sources directly. This is flagged inline throughout and is the largest single driver of the "Unclear" / "Unknown" results below — see the Coverage line at the end of each test and the overall Coverage section.

---

## Test A — Nursing-home Medicaid look-back packet builder (currently Watch)

**Idea:** families (then elder-law paralegals) import 60 months of bank statements, the tool flags transactions above the state disclosure threshold, attaches explanations/receipts, and produces an indexed PDF packet plus a state checklist — organizing only, never advising (Medicaid planning by non-lawyers is unauthorized practice of law in FL, OH, NJ, TN). Main free alternative: facility-paid Senior Planning Services (built on Ocrolus).

### Method

**Task 1 sample:** the CMS Provider Data Catalog (`data.cms.gov`) could not be reached (network-blocked), so the intended true random sample from CMS's sampling frame was not possible. Per the task's own fallback instructions, this was replaced with a **documented, reproducible convenience sample**: candidate FL/PA nursing homes were identified via operator "locations" pages (Life Care Centers of America, Genesis HealthCare, Priority Healthcare Group "Gardens" brand, HCR ManorCare/ProMedica, NSPIRE Healthcare/ex-Consulate) and nonprofit/county/church directories, classified chain vs. independent by operator-name match, sorted alphabetically, then sampled with Python's `random.seed(42)` (script and full candidate pools in `data/nursing-home-sample-script.py`). **This is explicitly a convenience sample, not a true random sample** — treat the chain/independent split (70%/30% overall) as an artifact of search-findability, not a population estimate. Each of the 40 facilities was then checked with one targeted web search for evidence of advertised free Medicaid-application help; because facility pages could not be fetched directly, "Unclear" means no evidence was *surfaced by search*, not confirmed absence.

**Tasks 2–4:** state Medicaid verification-checklist facts were sourced from Texas HHSC's and Ohio's own administrative code/handbook pages (via search snippets, not direct reads); application-volume data was sought from CMS/MACPAC/KFF/state reports; the competitive refresh covered ElderDocx/ElderCounsel, LawPRO, Clio, ezel.ai, bank-statement analyzers, and 2025–26 App Store entrants.

### Results

**Task 1 — free-Medicaid-help evidence, 40 facilities (full data: `data/nursing-home-sample-40.csv`, `data/nursing-home-medicaid-help-evidence.csv`):**

| Cut | Yes | Unclear | No | n |
|---|---|---|---|---|
| Overall | 7 (17.5%) | 33 (82.5%) | 0 | 40 |
| Florida | 0 (0%) | 20 (100%) | 0 | 20 |
| Pennsylvania | 7 (35%) | 13 (65%) | 0 | 20 |
| Chain | 7 (25%) | 21 (75%) | 0 | 28 |
| Independent | 0 (0%) | 12 (100%) | 0 | 12 |

All 7 "Yes" facilities were chain-operated (6 of 7 are Priority Healthcare Group's "Gardens"-brand facilities in PA, sharing near-identical admissions-page marketing about "navigating Medicare and Medicaid insurance coverage"). This reads as generic in-house admissions/financial-counseling marketing — closer to ordinary business-office help than a branded Senior-Planning-Services-style service. No facility was confirmed to explicitly lack help (that fact is essentially never published); the 82.5% Unclear rate reflects the inability to read facility websites directly, not a confirmed absence of help programs.

**Task 2 — state verification checklists:**

| State | Look-back | Per-transaction explanation threshold | Required documents | Source |
|---|---|---|---|---|
| Texas (HHSC) | 60 months | Reportedly $500 per a secondary search summary — **not independently confirmed** against primary text | Form H1239 ("Request for Verification of Bank Accounts") confirmed used; full itemized list Unknown (could not open Appendix XVI) | HHSC MEPD Handbook I-2100, [fhb.hhs.texas.gov](https://fhb.hhs.texas.gov/handbooks/medicaid-elderly-people-disabilities-handbook/i-2100-look-back-policy), accessed 2026-09-28 |
| Ohio (ODM) | 60 months (5 years) | Unknown — rule text shows no stated dollar figure, appears to be caseworker judgment | Combined application is JFS Form 07200; itemized checklist inside it not readable this session | Ohio Admin. Code 5160:1-6-06, [codes.ohio.gov](https://codes.ohio.gov/ohio-administrative-code/rule-5160:1-6-06), accessed 2026-09-28 |

**Task 3 — volume data:** no annual count of long-stay Medicaid *applications or approvals*, and no breakdown of *who files* them, was found from CMS, MACPAC, KFF, or state reports — reported as **Unknown** rather than estimated. Related utilization figures that were found: ~1.3M people used Medicaid nursing-facility care in 2021 (KFF, accessed 2026-09-28); Medicaid was the primary payer for 59% of nursing-facility residents in 2019, 84% of whom were dually eligible (MACPAC, accessed 2026-09-28); Medicaid covered 44% of long-term institutional care costs in 2023 (KFF, accessed 2026-09-28).

**Task 4 — competitive refresh:** ElderCounsel has merged into WealthCounsel; ElderDocx is now WealthCounsel's elder-law document-automation product — a drafting/assembly tool for attorneys (trusts, Medicaid/VA letters), not a bank-statement ingestion tool [vendor, wealthcounsel.com, accessed 2026-09-28]. LawPRO has no Medicaid/elder-law features (it's a general personal-injury practice-management tool). Clio has an "Elder Law Case Management" page and an ElderDocx App Directory listing [vendor, clio.com, accessed 2026-09-28], but no bank-statement/look-back feature. **ezel.ai does not appear to exist** — no such product was found. No dedicated Medicaid look-back bank-statement analyzer was found; the closest is Docsumo, a general document-OCR vendor content-marketing into this use case [vendor, docsumo.com, accessed 2026-09-28]. App Store search (via web search, not the iTunes API directly, which was also blocked) surfaced one new 2025–26 entrant, "GovAid: Health" — a general Medicaid/ACA eligibility estimator, not a look-back/packet tool.

### Kill-test verdict: **Not triggered (Pass), but low-confidence — treat as inconclusive**

The stated criterion ("if more than half offer free help, the consumer buyer is weak") was not met — 17.5% is far below 50%. However, 82.5% of the sample was Unclear specifically because facility websites could not be read directly; the true "Yes" rate could plausibly be materially higher if re-checked with normal web access. This result should not be treated as a clean pass on the consumer-buyer question.

### What it changes: **Stays Watch**

The kill criterion wasn't triggered, so the idea isn't rejected — but data quality is too weak (convenience sample, 82.5% Unclear) to promote it to Go. The one genuinely new signal: Task 4 found no existing tool (ElderDocx, Clio, Docsumo, or otherwise) that ingests 60 months of bank statements and flags disclosure-threshold transactions — that white space is real and supports keeping this on Watch and testing the B2B (elder-law paralegal) angle next, per the brief's own fallback instruction, rather than dropping the idea.

### Single next test

Re-run Task 1 from an environment with working web access (or a working CMS Provider Data Catalog pull for a true random sample): read each of the 40 facilities' actual business-office/admissions pages directly to convert the 82.5% Unclear into confirmed Yes/No, and pull CMS's Ownership dataset to replace name-based chain/independent classification with an ownership-record-based one.

---

## Test B — Long-term-care insurance claim manager for families (currently near miss)

**Idea:** families managing a parent's LTC insurance claim log caregiver hours/receipts, the tool generates monthly invoices per insurer format, and tracks the benefit pool. Known: ~353,000 claimants and $14.1B paid in 2023 (AALTCI); John Hancock's CareGiver app already logs sessions for invoicing; Genworth steers claimants to its CareScout network; Genworth and MetLife need monthly PDF invoices/timesheets.

### Method

Searched the Connecticut Partnership for Long-Term Care's statistical/claims-experience pages and AALTCI/Milliman/ASPE research for a quantified agency-vs-independent-vs-family split of home-care LTC claims. Separately researched claim requirements and caregiver tooling for six carriers/programs (Mutual of Omaha, Northwestern Mutual, New York Life, Lincoln MoneyGuard, OneAmerica, FLTCIP) from each carrier's own claims/policyholder pages where reachable, and secondary sources where not.

### Results

**Task 1 — provider-type split:** the CT Partnership's own claims-experience and cumulative-stats pages (`portal.ct.gov`) were located by URL but could not be opened (network-blocked); no quantified agency/independent/family breakdown was found there, in AALTCI's setting-level data (31% home care / 30.5% assisted living / 38.5% skilled nursing — a *setting* split, not a *provider-type* split), or in Milliman's 2024 NAIC Experience Reporting Forms summary. Milliman does state qualitatively that "most policies in the stand-alone market do not cover informal care provided by family or others" [Milliman, milliman.com, accessed 2026-09-28] — directionally consistent with independent + family being a small minority of claims, but not a number.

**Task 2 — carrier claim requirements:**

| Carrier / program | Indemnity vs. reimbursement | Caregiver time-logging tool | Family caregivers payable? |
|---|---|---|---|
| Mutual of Omaha | Both — reimbursement default, or 30% cash election with no receipts | No app found | **No** — reimbursement explicitly excludes family members [mutualofomaha.com, accessed 2026-09-28] |
| Northwestern Mutual (QuietCare) | Reimbursement only | No app found | Unknown (source blocked) |
| New York Life | Reimbursement (legacy); new **Asset Flex** hybrid added a cash-indemnity option in July 2026, marketed for family caregiving | No app found (paper/PDF invoice + care-log forms) | Reimbursement track: plausible if documented, not confirmed on NYL's own site |
| Lincoln MoneyGuard | Both — reimbursement, or 80%-of-max indemnity election (no receipts) | General "My Lincoln Portal," not caregiver-specific | Indemnity option explicitly positioned for family/informal caregiving |
| OneAmerica (Asset-Care) | Both — reimbursement, or cash indemnity with no elimination period | No app (human "Care Benefit Concierge"/"Caregiver Consultant") | **Yes** — indemnity track explicitly permits independent and family/informal caregivers [oneamerica.com, accessed 2026-09-28] |
| FLTCIP | Reimbursement, with an explicit "Informal Caregiver Invoice" pathway | **Yes** — LTCFEDS.gov "My LTCFEDS" dashboard tracks time and proofs of payment for informal caregivers | Yes, explicitly, via that pathway [ltcfeds.gov, accessed 2026-09-28] |

Full sourcing and quotes are in the subagent's working notes; every row above has a source URL and 2026-09-28 access date.

### Kill-test verdict: **Cannot be formally applied — Unknown, not confirmed**

The 15% threshold requires a hard percentage that this session could not obtain (CT Partnership pages blocked; no other source gave a quantified split). Directional/qualitative evidence — most standalone reimbursement policies structurally route claims through licensed agencies and exclude family caregivers by default — leans toward independent + family being a small minority, plausibly under 15%, but this is not a confirmed result.

### What it changes: **Stays near miss, leaning reject**

Beyond the unresolved Task 1 kill test, Task 2 surfaces an independent reason for caution: half of the six carriers checked (Mutual of Omaha, Lincoln, OneAmerica, and now New York Life's new Asset Flex product) already offer a no-invoice cash/indemnity election specifically because it suits informal/family caregiving — which directly shrinks the addressable use case for an invoice-generation tool, independent of the claim-volume question. FLTCIP already has a government-built caregiver time-tracking dashboard, one of the exact tools this idea would build. Two separate signals now point away from Go.

### Single next test

Directly open the CT Partnership's "Partnership Claims Experience Updated" and "Partnership Consumer Cumulative Stats" pages (or obtain the full AALTCI Sourcebook or Milliman ERF report) from an environment with working web access, to get a hard agency-vs-independent-vs-family percentage and formally apply the 15% threshold.

---

## Test C — Building MCP servers, ChatGPT apps, and Claude connectors for SaaS vendors (service lead)

**Idea:** Tempore builds MCP servers, ChatGPT apps, and Claude connectors as a services business for SaaS vendors that don't have them yet.

### Method

Selected 50 SaaS vendors with public APIs across three verticals chosen because they're populated by small-to-midsize, often bootstrapped vendors serving fragmented, non-technical buyers — exactly the profile likely to lack an in-house AI-platform team: field-service/trades software (17 vendors: ServiceTitan, Jobber, Housecall Pro, FieldEdge, Service Fusion, Workiz, Kickserv, mHelpDesk, ServiceM8, Synchroteam, Zuper, Joblogic, Simpro, BuildOps, Fergus, Tradify, GorillaDesk), practice-management for small clinics/law firms (17: SimplePractice, TherapyNotes, Clio, MyCase, PracticePanther, Tebra, athenahealth, DrChrono, CentralReach, TheraNest, Valant, AdvancedMD, Smokeball, CosmoLex, Rocket Matter, Filevine, WebPT), and e-commerce back-office tools (16: ShipStation, Extensiv, Cin7, Linnworks, A2X, TaxJar, Veeqo, Ordoro, Sellbrite, ShipBob, Brightpearl, Fishbowl Inventory, inFlow Inventory, Zoho Inventory, SkuVault, Webgility). For each, checked for an official vendor-built MCP server, an official ChatGPT app, and an official Claude connector (Anthropic directory), with URLs. The official Claude Connectors and ChatGPT Apps directories are JS-rendered and were not paginated directly; "Yes" classifications rely on vendor press releases/help-center docs or credible tech press rather than a first-party directory screenshot (see Coverage gaps).

### Results

| Metric | Count | % of 50 |
|---|---|---|
| Official MCP server (incl. 1 pilot) | 7 | 14% |
| Official ChatGPT app | 1 | 2% |
| Official Claude connector (confirmed directory listing) | 2 | 4% |
| Community/third-party MCP only, nothing official | 26 | 52% |
| Nothing found at all | 17 | 34% |
| **Both an official MCP server AND a ChatGPT app or Claude connector** | **2 (Jobber, ShipBob)** | **4%** |

Where integrations exist at all, they're disproportionately solo-developer GitHub repos or paid third-party middleware (viaSocket, Zapier MCP, Composio, Supergood, Oktopeak, RosenAdvertising, Makini) rather than anything the vendor itself built — itself a signal of unmet, outsourceable demand. Full 50-vendor table with URLs is in the subagent's working notes.

**Pricing signal:** no source gave a rate specifically for "an agency builds this for a SaaS vendor to ship to its own customers" — all found pricing describes either a business connecting to an *existing* SaaS, or generic MCP/ChatGPT-app development cost, used here as a proxy. MCP server builds: $3K–8K for a bare single-tool server, $8K–25K for a production build with auth, $25K–60K+ for complex/multi-tool; freelance rates $30–150/hr; ongoing maintenance $5K–25K/month [multiple 2026 agency blog posts, accessed 2026-09-28]. ChatGPT app/GPT Action builds: $15K–50K for MVP-to-mid-complexity, agencies quoting $30K–150K for larger engagements [Wildnetedge/Ptolemay, accessed 2026-09-28]. A realistic entry-level engagement for one small/midsize vendor looks like roughly **$8K–60K** one-time.

### Kill-test verdict: **Not triggered (Pass)**

4% of vendors have both an official MCP server and a ChatGPT app or Claude connector — far below the 70% rejection threshold. 86% have no official MCP server at all; 96% have no official ChatGPT app or Claude connector.

### What it changes: **Go — market is open, not already served**

This is the cleanest result of the three tests: the kill criterion was decisively not met, and the pattern (official integrations rare, community/third-party workarounds common) points to real unmet demand a small services shop could sell into.

### Single next test

Directly browse the official Claude Connectors directory and ChatGPT Apps directory (not via search) to close the Unknown gaps on the 5 vendors with a confirmed MCP server but unconfirmed app/connector status (ServiceM8, Zuper, Zoho Inventory, ShipStation, athenahealth), then price a pilot build against 2–3 mid-tier vendors from the "nothing found" list to test willingness to pay.

---

## Coverage

This session's network egress was blocked for almost every external domain — CMS (`data.cms.gov`, `medicare.gov`), state Medicaid agencies (Texas HHSC, Ohio ODM), KFF, MACPAC, the Connecticut Partnership for Long-Term Care (`portal.ct.gov`), insurance-carrier sites, the iTunes Search API, and even neutral references like Wikipedia — confirmed by direct `curl`/`WebFetch` tests returning `EGRESS_BLOCKED`/HTTP 403 across all three test runs. Every fact in this report was gathered through a server-side web-search tool's synthesized snippets rather than by reading primary source pages directly, which is a materially weaker form of verification: it inflated the "Unclear"/"Unknown" rate in Test A (82.5% of the nursing-home sample, the Task 1 kill test, the full Ohio document checklist) and made Test B's Task 1 kill test entirely unresolvable (the CT Partnership pages that likely hold the needed number were identified but never opened). Test A's sample is a labeled convenience sample, not a true random sample, because the CMS Provider Data Catalog itself was unreachable. Test C's directory-status calls for 5 vendors are marked Unknown rather than Yes/No because the official Claude/ChatGPT directories couldn't be crawled directly. Recommend re-running Tests A and B's Task 1 from a session with unrestricted web access before treating either verdict as final.
