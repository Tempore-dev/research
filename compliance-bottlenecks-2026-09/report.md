# Small operators drown in expiring compliance evidence

Across all six sectors studied, one bottleneck comes up again and again. Practitioners rarely struggle to *interpret* a rule. They struggle to keep per-person, per-asset or per-product **evidence files complete, current and producible on demand**, and to re-type the same facts into government portals, customer questionnaires and auditor formats. Driver-qualification files, subcontractor insurance certificates, provider re-attestations, refrigerant leak logs, product test reports, security questionnaires and app privacy labels all have this shape. So do volunteer background checks and meal counts. For Tempore, a small studio that builds web, mobile and desktop apps, the best bets as of September 2026 fall into two groups. The first is tools that sit *beside* a mandated system of record instead of replacing it. The second is one reusable "people/entities × requirements × expiry × evidence" engine with a thin rules layer per jurisdiction. The top-ranked opportunities are:

1. A mobile privacy-label, age-assurance and COPPA kit, which is squarely in Tempore's existing app work, with Texas enforcement live since June 4, 2026.
2. An offline-first expiring-evidence locker for small fleets and contractors.
3. A per-SKU compliance vault for marketplace sellers, now that CPSC eFiling is mandatory.
4. Honest, developer-centred accessibility tooling.
5. A refrigerant leak-rate logger for HVAC contractors under the 15-lb rule.
6. A "living program" manager for tax preparers' and small advisers' written security plans.

Several popular-sounding ideas are now poor bets because the rules behind them were eliminated, enjoined or pushed to 2027–2029: beneficial-ownership filing, CFPB 1071/1033, CMMC Phase 2, EU AI Act high-risk tooling, FSMA 204 traceability, large-company CSRD reporting and the HIPAA Security Rule overhaul. **The evidence base has one major weakness.** The research environment blocked Reddit, Hacker News, G2, Capterra, Trustpilot and most trade forums. Practitioner "quotes" here are therefore near-verbatim renderings of search-result snippets, not first-hand reads, and many headline figures come from vendors. Treat every ranking below as a hypothesis to test with real practitioners before committing to a build.

## Every practitioner quote here is second-hand, so validate first

**Read this before acting on anything below.** Six research streams covered healthcare and life sciences, financial services, field operations, tech/privacy/security/accessibility, sustainability/trade/product safety, and locally regulated small businesses. Every stream hit the same wall. The environment's egress proxy blocked direct page fetches for reddit.com, news.ycombinator.com item pages and the HN Algolia API, g2.com, capterra.com and softwareadvice.com, trustpilot.com, and forums such as TruckersReport, Mike Holt, allnurses, BiggerPockets, Student Doctor Network and Shopify Community. It also blocked many law-firm and trade-press pages. Site-restricted searches for Reddit returned nothing at all. Several streams also ran out of search budget before finishing.

In practice this means three things. First, **there are no verified first-hand Reddit quotes in this report**. Wherever a forum post or review is quoted, the wording comes from a search engine's summary of the page and may merge several posts or paraphrase them. Only a handful of items were confirmed by opening the primary page, notably Apple's developer notices on Texas age assurance ([Apple Developer](https://developer.apple.com/news/?id=sg176nne)). Second, **many quantified claims come from vendors selling the cure**. Examples:

- 90–95% AML false-positive rates
- $1,524 per manual data-subject request
- "40-plus hours per week" of cannabis compliance labour
- a "30% renewal-reminder failure rate" for electricians
- "$52,847 per clinic" Medicare documentation penalties
- "40% of import entries contain classification errors"

These are flagged as vendor-sourced wherever they appear and should be treated as directional only. Third, several 2026 regulatory claims rest on snippets whose source pages could not be read. These include ICE's reported reclassification of I-9 errors, HUD's reported withdrawal of source-of-income guidance and the claimed tenfold rise in I-9 audits. They are labelled unverified.

The more reliable layer is regulatory status: dates, thresholds and delays checked against the Federal Register, agency pages and multiple law-firm alerts. Also reliable are the handful of independent or association surveys: AMA, Advarra, MedTech Europe, NAFCC, the U.S. Chamber, Seyfarth's lawsuit counts, and DOL's own burden estimates. The ranking therefore leans on "a dated rule creates a recurring documentation job" more than on "practitioners say they would pay for X". **Tempore should not commit engineering time to any opportunity below until direct practitioner validation has been done.** That means reading the actual threads and reviews from an unrestricted network and running structured interviews. The final section sets out the steps.

## Five shapes of pain recur in all six sectors

The sectors differ in vocabulary, but their bottlenecks follow a small number of shapes. That matters for a small firm, because one well-built engine can serve several verticals.

### The expiring evidence file is the dominant bottleneck

The most common complaint is keeping a date-driven evidence file complete and findable when an auditor, inspector, customer or payer asks for it. The underlying calculation is rarely hard. The examples below are all the same data problem: people or entities, times requirements, times expiry dates, times evidence documents.

**Trucking.** Incomplete driver-qualification files are described as "the fastest way to trigger a compliance audit from the FMCSA", and "missing med cards, expired CDLs, and sloppy driver files are audit bait" ([FreightWaves via Yahoo](https://www.yahoo.com/news/articles/improper-driver-files-triggering-surprise-143051026.html)). One compliance aggregator observes that "almost all violations small carriers receive are documentation failures rather than driving failures", and that a one-truck owner-operator carries the same file obligations as a large fleet ([TruckComplianceHQ](https://truckcompliancehq.com/blog/dot-compliance-checklist)).

**Construction.** General contractors collect insurance certificates, W-9s, licences, lien waivers and safety agreements per vendor and per project. Without a structured workflow these end up "scattered across email threads, shared drives, and spreadsheets that nobody trusts by month two" ([Billy, vendor](https://billyforinsurance.com/resources/custom-compliance-forms-construction/)). A lien-waiver spreadsheet "holds up beautifully at two or three active jobs, but somewhere around five, it starts to crack" ([LienDone, vendor](https://www.liendone.com/blog/lien-waiver-tracking-spreadsheet)).

**Healthcare.** CAQH ProView demands re-attestation every 120 days, with fresh uploads of insurance certificates and licences ([ContractingProviders](https://contractingproviders.com/caqh-attestation)). A 90-day credentialing delay is reported to cost a specialty practice **$60,000–$90,000** in deferred revenue ([MGMA](https://www.mgma.com/articles/navigating-the-credentialing-gauntlet-key-actions-for-revenue-cycle-management)). The attribution of that figure to MGMA's own survey could not be confirmed.

**Local services.** The same shape appears in:

- salons cited for missing pedicure logs and expired practitioner licences ([California Board of Barbering and Cosmetology](https://www.barbercosmo.ca.gov/laws_regs/common_violations.shtml))
- youth sports leagues tracking background checks, SafeSport and concussion training on separate renewal cycles for every adult volunteer ([Maryland State Youth Soccer](https://www.msysa.org/mandatory-compliance-safe-soccer/))
- insurance agencies juggling state-by-state licence and CE renewal rules. California renews two years from the month of issue, and Kansas renews by birth-year parity ([AgentSync, vendor](https://agentsync.io/blog/insurance-101/insurance-licensing-101-agent-license-renewals)).

The risk is also shifting, from "you forgot a date" to "your records are indefensible". Examples include electronic I-9 audit trails, medical-director sign-offs at med spas, and Florida HOA records, where board members now face criminal penalties ([Jimerson Firm](https://www.jimersonfirm.com/blog/2024/09/navigating-hb-1203-new-changes-impacting-homeowners-associations-in-florida/)). That favours tools that produce an **audit-ready evidence packet in one click**, not just reminders. A J.J. Keller testimonial from a 14-vehicle fleet says that sorting paper files during a DOT audit took **seven days** ([J.J. Keller, vendor testimonial](https://www.jjkeller.com/shop/j-j-keller-encompass-fleet-management-system)).

### Mandated systems of record cannot be replaced, only prepared for

The second shape is re-entering data into systems that regulators or counterparties mandate: Metrc in cannabis, the FMCSA Drug & Alcohol Clearinghouse, LCPtracker for certified payroll, state EVV aggregators in home care, sponsor portals in clinical trials, CAQH in credentialing, the Circular Action Alliance portal for packaging EPR, and CBP's ACE for CPSC certificates.

Clinical sites illustrate the fragmentation. **Nearly 70% of sites juggle six or more logins per study**, and 55% call sponsor-technology setup extremely or very burdensome ([Advarra](https://www.advarra.com/news/new-clinical-trial-industry-survey-reveals-increased-burdens-on-sites/)). One site coordinator's survey comment calls the portals "a nightmare to try to maintain" ([Sakara Digital](https://sakaradigital.com/blog/investigator-site-portal-consolidation-case-study-analysis/)). In home care, an Arkansas caregiver's paycheck came up **$900 short** after glitches in the state's new EVV system. In an SEIU 775 survey, 49% of respondents reported EVV problems ([OnLabor](https://onlabor.org/electronic-visit-verification-surveils-homecare-workers-and-clients/)). Owner-operators on TruckersReport describe Clearinghouse re-registration loops and a "useless" help line, and say FMCSA staff were "just as frustrated" (near-verbatim, 2021 thread) ([TruckersReport](https://www.thetruckersreport.com/truckingindustryforum/threads/2021-clearinghouse-portal-query-problems.2051909/)).

Nobody can switch away from these systems. So the opening for a small firm is a **companion tool** that prepares, validates, reminds and reconciles *before* data goes in. Such a tool works through CSV imports and exports and respects whatever API or upload terms each system allows. It does not compete with the system itself.

### The same facts get re-rendered for every requester

The third shape is one body of facts reformatted for many audiences. Tech and trade show it most clearly.

**Security questionnaires.** A SaaS company's security posture goes into SIG, CAIQ and custom spreadsheet questionnaires, each with hundreds of rows. Vendors claim growth-stage firms face 5–15 of them a month ([Tribble, vendor](https://tribble.ai/blog/security-questionnaire-automation/)).

**App privacy disclosures.** An app's data practices go into Apple's privacy label, Google's Data Safety form, COPPA notices and state privacy disclosures. A 2022 ACM study found **88% of apps had at least one discrepancy** between privacy policy and label. The main cause was third-party SDK collection that developers did not know about ([ACM CHI EA](https://dl.acm.org/doi/fullHtml/10.1145/3491101.3519739)).

**Supplier ESG requests.** Small suppliers answer overlapping ESG questionnaires from each customer. EcoVadis's own chief customer officer conceded that "most are redundant, asking for similar disclosures" ([BusinessWire](https://www.businesswire.com/news/home/20240312100192/en)). A supplier on Trustpilot complained that EcoVadis asks "the same information from an HR services company as they do from a foundry" (snippet) ([Trustpilot](https://www.trustpilot.com/review/ecovadis.com)).

The software pattern is **capture once, render many**.

### Templates exist, but living programs do not

The fourth shape is the gap between a static template and a maintained program. Tax preparers have attested on Form W-12, under penalty of perjury, that they maintain a written information security plan (WISP). Trainers report that many "were not aware of the requirement, even though they had already attested to it" ([Bellator, vendor](https://bellatorcyber.com/blog/ptin-renewal-security-requirements); [AICPA](https://www.aicpa-cima.com/resources/article/wisp-required-by-federal-law-for-tax-practitioners)). The IRS sample template exists, but "your final WISP must reflect your actual environment" ([IRS](https://www.irs.gov/newsroom/a-written-information-security-plan-protects-tax-pros-and-their-clients)).

The same gap shows up in several other obligations:

- Smaller SEC-registered advisers had until June 3, 2026 to formalise a Reg S-P incident-response program, 30-day customer notification and vendor oversight ([Davis Wright Tremaine](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/reg-sp-smaller-entities-june-2026-deadline)).
- Amended COPPA now requires a written children's information security program and annual risk assessments ([Federal Register](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule)).
- Construction silica rules require a written exposure control plan on site ([OSHA 1926.1153](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1153)).

Small firms get templates and large firms get GRC suites or consultants. Nobody affordably turns the template into a record with reminders, an evidence log, a vendor inventory and an annual review.

### Federal loosening plus state tightening demands a rules layer

The fifth shape is jurisdictional fragmentation, which 2025–26 made worse. Washington withdrew or softened federal requirements while states and cities kept adding their own:

- **Pesticides:** federal recordkeeping for restricted-use pesticides was rescinded, leaving a state patchwork ([Federal Register](https://www.federalregister.gov/documents/2025/05/12/2025-08220/rescission-of-recordkeeping-on-restricted-use-pesticides-by-certified-applications)).
- **Heat safety:** the federal heat rule stalled while California, Washington, Oregon, Maryland and Nevada run their own ([OSHA](https://www.osha.gov/heat-exposure/rulemaking)).
- **Privacy:** 20 state privacy laws are now in force, each with quirks ([MultiState](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026)).
- **Nonprofits:** charitable solicitation registration applies in 41 states plus DC and "can cost hundreds of hours and thousands of dollars in fees per year" ([Foundation Group, service provider](https://www.501c3.org/navigating-multi-state-charitable-solicitations-a-comprehensive-guide-for-nonprofits/)).
- **Tenant screening:** a policy "lawful in Texas can be a violation in Colorado or New York City" ([LeaseRunner, vendor](https://www.leaserunner.com/blog/tenant-screening-laws)).

This favours products with a maintained per-jurisdiction rules layer. That layer is both the moat and the ongoing cost, and a small firm should start with one or two jurisdictions rather than fifty.

The burden is also regressive. Firms with fewer than five employees report **198 compliance hours per employee against 8 hours** at firms with 100+ staff, and $10,208 against $1,374 per employee in 2024 ([U.S. Chamber of Commerce](https://www.uschamber.com/small-business/small-businesses-are-spending-more-time-money-on-regulatory-compliance)). The smallest community banks spend roughly 11–15.5% of payroll on compliance, against 6–10% at the largest ([ABA Banking Journal on CSBS data](https://bankingjournal.aba.com/2025/11/csbs-data-show-regulatory-burden-falls-hardest-on-community-banks/)).

### What each sector complains about most

| Sector | Loudest recurring frustrations | Best-quantified signal |
|---|---|---|
| Healthcare & life sciences | Prior authorization; payer credentialing and CAQH re-attestation; clinical-site portal sprawl; eQMS pricing for tiny medtech; EVV pay and claim losses | **13 hours/week** and ~40 prior auths per physician weekly ([AMA](https://www.ama-assn.org/press-center/ama-press-releases/ama-survey-prior-authorization-reform-pledge-falls-short-physicians)) |
| Financial services | AML alert triage and SAR re-reviews; RIA marketing-rule and communications supervision; multi-state insurance licence/CE; tax-preparer WISPs; DORA registers | Only **6.5%** of DORA Registers of Information passed all data-quality checks in the dry run ([Finadium](https://finadium.com/esas-report-6-5-data-quality-pass-rate-after-dora-dry-run/)) |
| Field operations | DQ files and Clearinghouse; COIs and lien waivers; weekly certified payroll; Metrc reconciliation; temperature/HACCP logs; refrigerant records | WH-347 burden of **56 minutes per response, 1.92M hours/year** ([Praisidio summarising DOL](https://www.praisidio.com/resources/wh347-certified-payroll/)) |
| Tech, privacy, security, accessibility | Security questionnaires; SOC 2 cost and "checkbox" audits; DSARs; accessibility demand letters; app privacy labels and age assurance | **3,117** federal website accessibility suits in 2025, up 27% ([Seyfarth](https://www.adatitleiii.com/2026/03/federal-court-website-accessibility-lawsuit-filings-bounce-back-in-2025/)) |
| Sustainability, trade, product safety | Chasing supplier data (ESG, CBAM, EUDR, UFLPA, EPR); HTS classification after de minimis; GPSR/Amazon/CPSC document packs | **58%** of EU timber operators say suppliers are "unwilling or unable" to support traceability ([Interu](https://www.interu.io/deforestation-regulation-readiness-report)) |
| Local small businesses | CACFP and subsidy paperwork; charitable registration; I-9 fines; Florida HOA records; med-spa supervision; city rental registration | Family child-care homes in CACFP fell **24%** from 2019 to 2024 ([Nutrition Policy Institute](https://ucanr.edu/program/nutrition-policy-institute/article/challenges-experienced-child-and-adult-care-food-program)) |

## Incumbents lose on price floors, offline sync and support

Review complaints about existing tools cluster on the same weaknesses in every sector. Missing regulatory content is rarely the issue. The recurring problems are:

- enterprise pricing and contract structures pushed down onto tiny teams
- per-seat pricing that punishes frontline headcount
- unreliable offline sync
- interfaces deskless workers will not adopt
- support that fails at the critical moment

A small firm can compete on every one of these without matching the incumbents' integration breadth. The table summarises what users dislike. Nearly all review text is from search summaries, and several sources are competitors, which is flagged.

| Tool (sector) | What users dislike | Source | Opening for Tempore |
|---|---|---|---|
| Greenlight Guru (medtech eQMS) | One customer went from ~$20K to $30K to **$58K/year** in three years; 2–3-year minimums; no trial; "not ideal" under 10 staff | [OpenRegulatory (competitor)](https://openregulatory.com/articles/greenlight-guru-price); [Vendr](https://www.vendr.com/marketplace/greenlight-guru); [SoftwareConnect](https://softwareconnect.com/reviews/greenlight-guru/) | Real gap, but validation burden and crowded challengers make it a poor fit |
| MasterControl (pharma QMS) | "Setup is incredibly time-consuming"; licence model "very expensive for small startup businesses" | [G2](https://www.g2.com/products/mastercontrol-quality-management-system/reviews?qs=pros-and-cons) | Same as above |
| Accountable, Compliancy Group (HIPAA) | ~$199/month; "feels pretty rigid", "lacks mobile support"; training content updated yearly | [Software Advice](https://www.softwareadvice.com/lms/accountable-profile/reviews/); [G2](https://www.g2.com/products/compliancy-group-healthcare-compliance/reviews) | Mobile-first, but the market is crowded and the rule is not final |
| Smarsh (communications archiving) | Dated interface, slow search, weak support; "three times the original rate per month" | [G2](https://www.g2.com/products/smarsh-professional-archive/reviews?qs=pros-and-cons) | Avoid: SEC 17a-4-grade storage build |
| Vanta, Drata (SOC 2 automation) | "Expensive" for pre-revenue firms; false-positive alerts "explained away on each sync"; weak exception handling; **20–40% renewal hikes**; add-ons | [AWS Marketplace](https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-5ophamrbfxt44); [G2 Vanta](https://www.g2.com/products/vanta/reviews); [G2 Drata](https://www.g2.com/products/drata/reviews?qs=pros-and-cons) | Sub-20-person questionnaire and trust tooling; verifiable evidence |
| Delve (SOC 2 automation) | Alleged templated reports: 494 leaked SOC 2 reports "99.8% identical"; removed from YC's directory around April 3, 2026 | [IANS Research](https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/19/delve-allegations-expose-weak-points-in-modern-compliance); [HN discussion](https://news.ycombinator.com/item?id=47444319) | Buyers now distrust cheap, fast attestations |
| accessiBe and other overlays | **$1M FTC order** over "automatically comply" claims; suits increasingly hit sites that already run widgets | [FTC](https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-approves-final-order-requiring-accessibe-pay-1-million); [UsableNet](https://blog.usablenet.com/ada-web-lawsuit-trends-2026) | Honest code-level tooling plus services |
| Procore (construction) | "Too expensive and too complex" under 50 staff or $5M; ~$10K–$80K+/year; setup takes weeks to months | [Connecteam](https://connecteam.com/reviews/procore/) | Micro-contractor document and evidence tools |
| SafetyCulture, renamed Mitti in Aug 2026 (inspections) | Per-seat cost "significant" past 20 users; offline photo sync "does not always upload cleanly"; rigid report layouts | [Fluix (competitor)](https://fluix.io/blog/safetyculture-review) | Flat pricing; truly offline-first mobile |
| Jolt, FoodDocs (restaurant logs) | Jolt "really laggy"; staff "wouldn't adopt the software after several months… a design problem rather than a training issue"; FoodDocs annual add-on lock-in | [Capterra Jolt](https://www.capterra.com/p/146384/Jolt/reviews/); [SoftwareConnect FoodDocs](https://softwareconnect.com/reviews/fooddocs/) | Two-tap UX, per-location pricing; crowded |
| Metrc (cannabis, mandated) | $40/month plus $0.45 per plant tag and $0.25 per package tag; one Colorado firm paid >$1,400/month for RFID tags and sued | [MJBizDaily](https://mjbizdaily.com/colorado-marijuana-company-challenging-rfid-tag-requirement/) | Avoid: mandated-API dependency, market in flux |
| EcoVadis (supplier ESG) | "Insanely lengthy and irrelevant" questionnaires; **$8,550** subscriptions; undisclosed auto-renewal; support issues unresolved "over two years" | [Trustpilot](https://www.trustpilot.com/review/ecovadis.com) | Answer-once VSME portal |
| Watershed, Persefoni (carbon) | $50K–$200K+/year; "paying for capability you won't touch" without complex Scope 3 | [Normative (competitor listicle)](https://normative.io/insight/the-5-best-carbon-accounting-software-platforms-2026/) | Gap below ~$10K, but demand is shrinking |
| Brightwheel, Procare (childcare) | Crashes "during critical check-in times"; cannot reach a human; Procare "tends to go offline or 'glitch'" | [Procare blog (competitor)](https://www.procaresoftware.com/blog/why-some-child-care-centers-are-switching-from-brightwheel-in-2026/); [Capterra Procare](https://capterra.com/p/23486/Procare-Child-Care-Management/reviews/?page=6) | Home-provider CACFP tool, not a centre system |
| CE Broker (licence CE, board-mandated) | 4.8 App Store rating but **1.8/5 on Trustpilot**; "pay to speak to a real person"; deficit information paywalled | [RenewRN (competitor)](https://www.renewrn.net/blog/ce-broker-review-2026); [Trustpilot](https://www.trustpilot.com/review/cebroker.com) | Personal multi-licence CE wallet that complements it |
| AppFolio, Buildium (property) | ~50-unit minimum (AppFolio); add-on fees; "most of the stacks are required to pay an extra fee" | [SoftwareConnect](https://softwareconnect.com/comparisons/appfolio-vs-buildium/) | 1–20-unit landlord jurisdiction calendar |

Two lessons stand out. First, **the price floor is the gap, not the feature set**. Vanta's median contract is reported at about $20K a year ([complyjet, competitor](https://www.complyjet.com/blog/vanta-pricing-guide-2025)). A solo founder on Hacker News was told the realistic minimum is roughly $15K a year for a platform plus about $10K per Type 2 audit, and was advised to wait until "a purchase order is made contingent on your SOC2" (snippet) ([HN](https://news.ycombinator.com/item?id=48145524)). Second, **trust in "automatic compliance" collapsed in 2025–26**. The FTC's accessiBe order and the Delve scandal both punished products that promised compliance without real evidence. A small vendor that sells verifiable evidence and makes modest claims now has a positioning advantage. Incumbents' marketing has become a liability.

## Twenty opportunities ranked on five criteria

### How the scores work

Each opportunity is scored from 1 to 5 on five criteria, for a maximum of 25. Ties are broken by evidence strength and build simplicity, then by timing and judgement. The scores are analytical judgements built on the cited evidence, not measured data.

**Pain and evidence** rewards documented, costly pain, weighting independent surveys, regulator data and real forum voices above vendor claims. A score of 2 means the pain is inferred mainly from a new rule.

**Regulatory timing as of September 2026** rewards obligations that are live now or land within about 12 months, and penalises rules that were delayed, enjoined or rescinded.

**Competitor saturation and price gap** scores higher where incumbents are enterprise-priced or absent at the micro end, and lower where cheap niche tools already crowd the space.

**Build complexity and liability** scores higher where a small team can ship with forms, documents, reminders, calculations and exports. It scores lower where the product needs validated GxP software, regulated storage, mandated-system APIs, fast-changing rate tables, or content whose errors create legal exposure.

**Distribution path** scores higher where Tempore has an existing channel (its own mobile and web client work) or a concentrated buyer channel exists, such as associations, sponsors or app marketplaces. It scores lower where buyers are dispersed abroad or budgets are tiny.

The final column marks opportunities that reuse the shared expiring-evidence engine described in the conclusion.

| # | Opportunity (sector) | Pain & evidence | Timing | Gap | Build & liability | Distribution | **Total** | Shared engine |
|---|---|---|---|---|---|---|---|---|
| 1 | Mobile privacy-label, age-assurance and COPPA kit for app developers (tech) | 3 | 5 | 4 | 4 | 5 | **21** | |
| 2 | Offline-first expiring-evidence locker for small fleets and contractors: DQ files, COIs, lien waivers, licences, 608 certs (field) | 4 | 4 | 3 | 5 | 3 | **19** | Yes |
| 3 | Per-SKU marketplace compliance vault with CPSC eFiling data prep (product safety) | 4 | 5 | 3 | 4 | 3 | **19** | Yes |
| 4 | Accessibility CI, remediation tracker, ACR and EAA-statement generator (tech) | 4 | 4 | 3 | 4 | 4 | **19** | |
| 5 | HVAC refrigerant leak-rate logger under EPA ER&R (field) | 2 | 5 | 4 | 5 | 3 | **19** | Yes |
| 6 | WISP and Reg S-P "living program" manager for tax, CPA and small-RIA firms (financial) | 3 | 4 | 3 | 4 | 4 | **18** | Partly |
| 7 | Provider credential, CAQH, licence, DEA and COI expiry tracker for small practices (healthcare) | 4 | 3 | 3 | 4 | 3 | **17** | Yes |
| 8 | Security-questionnaire answer library plus verifiable trust page for sub-20-person SaaS (tech) | 4 | 3 | 3 | 4 | 3 | **17** | |
| 9 | Med-spa supervision evidence log (local) | 3 | 4 | 3 | 4 | 3 | **17** | Yes |
| 10 | EU Cyber Resilience Act 24h/72h reporting workflow plus SBOM diff (tech) | 3 | 5 | 3 | 3 | 3 | **17** | |
| 11 | Family child-care CACFP, attendance and licensing app (local) | 4 | 3 | 3 | 4 | 2 | **16** | Yes |
| 12 | VSME "answer once, share many" supplier portal (sustainability) | 4 | 4 | 2 | 4 | 2 | **16** | |
| 13 | Florida HOA/condo statutory portal and director-education tracker (local) | 4 | 3 | 2 | 4 | 3 | **16** | Yes |
| 14 | EUDR offline plot-polygon capture app (trade) | 4 | 4 | 3 | 4 | 1 | **16** | |
| 15 | Payroll-export to new WH-347 converter and validator (field) | 4 | 5 | 2 | 2 | 3 | **16** | |
| 16 | Micro-importer HTS sanity check and IEEPA-refund ledger (trade) | 4 | 4 | 3 | 2 | 3 | **16** | |
| 17 | Landlord jurisdiction compliance calendar for 1–50 units (local) | 3 | 3 | 4 | 2 | 3 | **15** | Yes |
| 18 | DORA Register of Information builder and validator (EU financial) | 4 | 3 | 3 | 3 | 2 | **15** | |
| 19 | CLIA small-lab personnel, competency and PT file (healthcare) | 2 | 3 | 4 | 4 | 2 | **15** | Yes |
| 20 | EVV exception pre-check for small home-care agencies (healthcare) | 4 | 3 | 3 | 2 | 2 | **14** | |

### Tier 1: six bets that fit a small team now

**1. Mobile privacy-label, age-assurance and COPPA kit.** This ranks first mainly on timing and fit, not on loud practitioner voices, so the pain score is only moderate.

On timing, the Fifth Circuit stayed the injunction against Texas SB2420, and **Apple put age assurance into effect for new Texas accounts on June 4, 2026**. Developers are expected to wire up four Apple components:

- the Declared Age Range API
- the PermissionKit Significant Change API
- StoreKit's ageRatingCode
- App Store Server Notifications for consent revocation

Apple says the same tools support Utah and Louisiana laws taking effect in 2026 (verified on [Apple Developer](https://developer.apple.com/news/?id=sg176nne) and [Apple Developer, Dec 2025](https://developer.apple.com/news/?id=8jzbigf4)). Amended COPPA reached full compliance on **April 22, 2026**. It adds separate parental consent for non-integral third-party disclosures, a written children's security program and annual risk assessments ([Federal Register](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule)). Underneath all of this sits the privacy-label accuracy problem: 88% of apps had a policy/label discrepancy, driven by SDK collection developers did not know about ([ACM](https://dl.acm.org/doi/fullHtml/10.1145/3491101.3519739)). That study dates from 2022.

The product would be a static analyser for Podfile, Gradle and SPM manifests that maps known SDKs to Apple and Google label fields. It would ship with a reusable age-assurance integration library and a COPPA third-party-disclosure checklist. GRC incumbents do not serve this niche. Tempore already ships iPhone and iPad apps, so the first distribution channel is its own client work, with the library as a product spun out of it. On liability, the tool should present SDK mappings as a draft for developer confirmation, never as a guarantee. The main unknown is whether developers will pay for it or expect it free.

**2. Offline-first expiring-evidence locker for small fleets and contractors.** This is the most direct expression of the dominant pain. It is also the first skin on the shared engine.

The evidence is comparatively strong: DQ-file audit triggers, documentation-driven violations, the seven-day paper audit, and COI spreadsheets that crack at about five jobs (sources above). Timing is live:

- **Non-domiciled CDL rule** (effective March 16, 2026): about 194,000 holders could be affected at renewal, and carriers must re-review DQ files and immigration documents ([Jackson Lewis](https://www.jacksonlewis.com/insights/fmcsa-new-rule-cracks-down-non-citizen-commercial-drivers-licenses-creating-carrier-burdens)).
- **English-proficiency out-of-service enforcement**: more than 20,000 drivers had been placed out of service by May 2026, and an August 10, 2026 NPRM would codify it ([TruckingInfo](https://www.truckinginfo.com/news/fmcsa-moves-to-codify-english-language-requirements-for-commercial-drivers)).
- **ELD revocations**: FMCSA has revoked 79 ELD models since January 2025, and the latest replacement deadline is **October 6, 2026** ([FMCSA](https://www.fmcsa.dot.gov/newsroom/fmcsa-removes-fourteen-devices-list-registered-electronic-logging-devices)).

Competition is heavy at the top (J.J. Keller Encompass, TrustLayer, Billy, CertPact) and thin at the micro end, where free Excel templates rank highly in search. The build is forms, OCR of ACORD 25 certificates and medical cards, reminders, offline mobile capture and a one-click PDF audit binder. Distribution is the weak point: owner-operators and small subcontractors are fragmented. Likely channels are insurance agents, factoring companies, trade associations and general contractors who require subs to use the tool. Validation must confirm that micro-operators will pay at all, versus sticking with spreadsheets.

**3. Per-SKU marketplace compliance vault.** Pain here is binary and immediate: a listing gets suspended or a shipment gets held. **CPSC eFiling became mandatory on July 8, 2026**. Importers must file certificate data in ACE before entry, even for shipments claiming de minimis ([CPSC](https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Implements-Mandatory-eFiling-for-Certificates-of-Compliance-Targeting-Dangerous-Foreign-Imports)). Amazon now requires annual testing of children's products, and documents from labs on its suspended-lab list are "treated as no documentation at all" ([ComplianceGate, vendor summary](https://www.compliancegate.com/amazon-product-compliance-document-requests-removals/)). Shopify sellers call EU GPSR a "Total Nightmare" because of the cost of an EU Responsible Person, documentation for multi-component products and grandfathering confusion (snippet) ([Shopify Community](https://community.shopify.com/t/eu-ni-general-product-safety-regulations-gpsd-gpsr-total-nightmare/338849/11)). Handmade goods are not exempt ([Etsy](https://www.etsy.com/seller-handbook/article/1093438529659)).

The product stores, per SKU:

- GPSR Responsible Person details
- test reports, checked against Amazon's suspended-lab list
- CPC/GCC certificate fields formatted for the broker or ACE
- safety images and multilingual warnings

The competition is a cottage industry of Responsible Person services, few of which offer a cross-marketplace SKU vault. Shopify and Etsy app ecosystems and partnerships with those services are plausible channels. The tool must be positioned as data preparation, not legal advice.

**4. Accessibility CI and remediation tooling.** Litigation keeps this market active regardless of federal deadlines. Seyfarth counted **3,117 federal website suits in 2025, up 27%** ([Seyfarth](https://www.adatitleiii.com/2026/03/federal-court-website-accessibility-lawsuit-filings-bounce-back-in-2025/)). UsableNet counts more than 5,000 including state courts, with repeat defendants making up about 46% of federal cases ([UsableNet, vendor](https://blog.usablenet.com/ada-web-lawsuit-trends-2026)). Small businesses report "there are no clear guidelines or specific steps" ([JD Supra](https://www.jdsupra.com/topics/website-accessibility/demand-letter)).

The EAA has been live since June 28, 2025. Its microenterprise exemption covers services only, and "many online retailers relaxed believing they were exempt" ([Taylor Wessing](https://www.taylorwessing.com/en/interface/2025/accessibility/key-eu-accessibility-act-exemptions-and-the-challenges-they-pose)). Vendors to state and local governments face the ADA Title II deadline of April 2027 or April 2028 ([Federal Register](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web)).

With the cheap option discredited by the FTC's accessiBe order, there is room for axe-based CI linting, component-level remediation tracking, an accessibility conformance report (ACR/VPAT) generator and a demand-letter response workflow, sold alongside Tempore's own build services. The one hard rule is **never to claim automatic compliance**.

**5. HVAC refrigerant leak-rate logger.** This is a rule-driven opportunity with thin practitioner evidence, hence a pain score of 2. EPA's ER&R rule took effect **January 1, 2026**. It lowered the leak-repair threshold from 50 lb to **15 lb** for refrigerants with GWP above 53. It requires a leak-rate calculation every time refrigerant is added and repairs within 30 days, and records must be kept for three years ([EPA fact sheet](https://www.epa.gov/system/files/documents/2026-01/er-r-fact-sheet-leak-repair-2026-01-13_1.pdf)). ACHR News ran the headline "New Year, New Refrigerant Rules, No Grace Period" ([ACHR News](https://www.achrnews.com/blogs/17-opinions/post/165785-new-year-new-refrigerant-rules-no-grace-period)). Paper refrigerant logbooks are still sold on Gumroad ([Gumroad](https://nouh3579.gumroad.com/l/uzgahg)). R-454B cylinder prices rose from $345 in 2021 to more than $2,000 in 2025, which makes every pound tracked matter ([Contracting Business](https://www.contractingbusiness.com/refrigeration/article/55288344/cold-truth-the-r-454b-shortage)).

The build is a mobile calculator on every top-off, plus a 30-day repair clock, technician 608-certification capture, a three-year record and a CSV bridge to ServiceTitan or Housecall Pro. Competing tools (Oxmaint and similar CMMS products) target facilities teams, not three- to 20-truck contractors. One caveat: EPA's separate Technology Transitions rule is under reconsideration ([Hunton](https://www.hunton.com/the-nickel-report/status-update-on-the-aim-act-and-epas-hfc-refrigerant-regulations)), but the leak-repair rule is in force. Before building, confirm through contractor interviews that techs actually feel this pain.

**6. WISP and Reg S-P living-program manager.** The obligation covers every paid tax preparer through the Form W-12 attestation ([AICPA](https://www.aicpa-cima.com/resources/article/wisp-required-by-federal-law-for-tax-practitioners)). It extends to advisers under $1.5B through Reg S-P's June 3, 2026 deadline, with the SEC signalling exam focus later in 2026 ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/05/regulation-s-p-amendments-compliance-deadline-approaching)). A WISP must name a security coordinator and include a written risk assessment, MFA and other technical controls, vendor management and an incident-response plan ([Bellator, vendor](https://bellatorcyber.com/blog/wisp-small-tax-firm)).

Competition today is free templates, paid template kits and cyber MSPs ([Western CPE](https://www.westerncpe.com/wisp-template/); [Verito](https://verito.com/written-information-security-plan/)). The product would turn the template into a maintained record: an asset and vendor inventory, an annual-review workflow, a training log and an incident-response runbook. The same core serves COPPA's written security program and FTC Safeguards obligations. Distribution through tax-software ecosystems and state CPA societies is concentrated, which is why this scores well despite vendor-heavy evidence. The liability risk is content accuracy, which argues for partnering with a compliance consultant on the templates.

### Tier 2: strong pain, but a channel, window or moat is missing

**Provider credential tracking (7)** addresses among the best-quantified revenue losses in the research: the $60–90K credentialing delay and CAQH's 120-day cycle. It needs no PHI. But CAQH has no public write API, so the tool can remind and pre-fill but not attest. It also competes with outsourced credentialing services and CVOs that use content marketing for lead generation.

**Security questionnaires and trust pages (8)** have real, deal-blocking pain. Hacker News threads such as "How small startups deal with long security questionnaires" recur ([HN](https://news.ycombinator.com/item?id=36488436)), and the Delve fallout means buyers now scrutinise SOC 2 reports more closely ([Workplace Privacy Report](https://www.workplaceprivacyreport.com/2026/05/articles/governance-risk-and-compliance-2/the-delve-scandal-why-a-soc-2-report-cant-be-a-check-the-box-exercise-for-vendor-management/)). Incumbents bundle questionnaire tooling, though, and every hours figure comes from vendors.

**Med-spa supervision logs (9)** ride what is described as "the tightest enforcement year the med spa industry has ever seen", targeting "paper" medical directors in CA, TX, NY, NJ and FL ([MedSpaStandards, content/vendor](https://medspastandards.com/blog/med-spa-medical-director-complete-guide-2026)). Buyers have budget, but aesthetic EMRs could add the feature.

**CRA reporting (10)** has the hardest clock of any item in the research. Since **September 11, 2026**, EU-selling manufacturers of products with digital elements must send an early warning within 24 hours of an actively exploited vulnerability and a notification within 72 hours through ENISA's Single Reporting Platform ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting); [ENISA](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)). Academic work shows SBOM generators disagree with each other ([arXiv](https://arxiv.org/pdf/2606.13966)). This is a credible tool for small software and IoT houses, but it requires vulnerability-feed plumbing and EU buyers.

**The family child-care CACFP app (11)** has the strongest behavioural signal in the research: providers are *leaving* a subsidy program over paperwork. Yet 35% of family child-care educators earn under $10 an hour ([NAFCC](https://nafcc.org/docs/reports/NAFCC-Annual-Report-2025.pdf)). The product only works if CACFP sponsors or states pay for it.

**The VSME supplier portal (12)** has a legal hook. Companies in CSRD scope may not demand more from partners with ≤1,000 employees than the VSME-based standard, and partners "can refuse requests that exceed" it ([CSSF](https://www.cssf.lu/en/omnibus-package/)). But at least five EU startups already compete (Sunhat, Dcycle, Coolset, CSRDpro, Spectreco).

**The Florida HOA portal (13)** answers a dated mandate that carries criminal exposure for volunteers who "no one wants to serve" ([Mosaic HOA](https://mosaichoa.com/blog/florida-hoa-volunteer-crisis/)), but HOALife, ManageCasa and Condo Control are already there.

**EUDR plot capture (14)** is a natural offline mobile build with dates of December 30, 2026 and June 30, 2027 ([Council of the EU](https://www.consilium.europa.eu/en/press/press-releases/2025/12/18/deforestation-council-signs-off-targeted-revision-to-simplify-and-postpone-the-regulation/)). The buyers are cooperatives and exporters in producer countries, a channel Tempore does not have.

**The WH-347 converter (15)** has the best federal burden data (1.92M hours a year) and a hard trigger: the revised form becomes the only valid version on **October 1, 2026** ([DOL](https://www.dol.gov/newsroom/releases/whd/whd20251216-0)). But LCPtracker is agency-mandated and often free to contractors ([DOE](https://www.energy.gov/infrastructure/weekly-dba-payroll-tracking-lcptracker)), and payroll errors carry legal liability.

**The micro-importer tool (16)** addresses real anxiety. One source describes a small importer as "trying to figure it out with a Google search and a CPA who's never dealt with HTS codes" ([TariffTax](https://www.tarifftax.org/analysis/small-business-impact)). After the Supreme Court struck down IEEPA tariffs, refunds are not automatic ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/02/supreme-court-strikes-down-ieepa-tariffs)). Rate tables that change with each court ruling are a maintenance and liability trap, however. A narrowly scoped ledger of duties paid under each legal basis, for refund tracking, is the safer slice.

### Tier 3 and the do-not-build list

The remaining ranked items are viable only with a specific partner or market. **Landlord calendars (17)** need city-by-city rules curation, so they would start in one or two metros. **DORA (18)** has striking pain, with only 6.5% of registers passing validation, but needs EU go-to-market. **CLIA files (19)** follow new personnel and proficiency-testing rules but have no practitioner voices in the research. **EVV pre-checks (20)** face state-by-state aggregator variation.

Several areas are poor fits for a small studio despite genuine pain, and should be avoided:

- **Communications archiving**: Smarsh and Global Relay territory, requiring SEC 17a-4-grade storage.
- **AML transaction monitoring and KYC engines**: Unit21, Alloy and Sumsub, with bank sales cycles.
- **Metrc reconciliation**: depends on a mandated API, and the market is shifting with the hemp redefinition and partial rescheduling.
- **Assisted-living eMAR**: clinical liability.
- **I-9 and E-Verify**: payroll platforms dominate, and audit-trail failures now carry higher stakes.
- **Prior-authorization automation**: moving to payer FHIR APIs by January 2027 ([CMS](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f)) and AI-PA startups.
- **DSCSA EPCIS tooling**: needs trading-partner connectivity, and wholesalers bundle portals.
- **Lightweight eQMS for medtech and biotech**: Tempore would have to validate its own software, and OpenRegulatory, Qualio, Kivo and Veeva QuickVault already compete.
- **UFLPA deep-tier tracing**: the value lies in proprietary risk data.

## Deadlines that moved, and the ones that did not

Regulatory whiplash is itself a finding. Work done for a date that then moves is wasted, and buyers have learned to wait. Several tempting opportunities are anchored to rules that were eliminated, enjoined or pushed back. Building for them now means building for demand that may never arrive.

### Poor bets: delayed, enjoined or rolled back

| Requirement | Status as of September 2026 | Implication |
|---|---|---|
| CTA beneficial-ownership (BOI) reporting | **Permanently eliminated** for US companies by FinCEN's August 2026 final rule ([Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons)) | BOI filing tools for US SMBs are dead |
| Investment-adviser AML rule | Moved to **January 1, 2028**; scope to be revisited ([FinCEN](https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028)) | Do not build yet |
| CFPB 1033 open banking | Enjoined; reconsideration ANPR August 2025; April 2026 compliance date passed without effect ([Cozen O'Connor](https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration)) | Avoid |
| CFPB 1071 small-business lending data | Narrowed; single compliance date **January 1, 2028** (KPMG snippet) ([KPMG](https://kpmg.com/us/en/articles/2026/cfpb-final-rules-regulation-b-Section-1071-and-disparate-impact-liability-reg-alert.html)) | Avoid before 2027 |
| FinCEN AML/CFT program rule | NPRM April 2026, pending; promises "decreasing compliance burden" ([Federal Register](https://www.federalregister.gov/documents/2026/04/10/2026-07033/anti-money-laundering-and-countering-the-financing-of-terrorism-programs)) | Value shifts from volume tools to documenting risk-based decisions |
| HIPAA Security Rule overhaul | Not final; moved to long-term actions, **~July 2027**; 100+ organisations urged withdrawal ([Clark Hill](https://www.clarkhill.com/news-events/news/hipaa-security-rule-update-delayed-until-2027/)) | Vendor pages calling it "final" are wrong; avoid that credibility trap |
| FSMA 204 food traceability | Moved 30 months to **July 20, 2028** ([Federal Register](https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension)) | Buyers will wait until 2027–28; build light or later |
| TSCA 8(a)(7) PFAS reporting | Start pushed to **by January 31, 2027**; amendments may exempt articles ([Federal Register](https://www.federalregister.gov/documents/2026/04/13/2026-07062/modification-to-the-start-of-the-submission-period-for-perfluoroalkyl-and-polyfluoroalkyl-substances)) | Scope too uncertain |
| OSHA heat rule | Stalled; supplemental NPRM "scaling back burdens" planned December 2026 ([OSHA](https://www.osha.gov/heat-exposure/rulemaking)) | Only state heat rules are live |
| Federal restricted-use pesticide records; 2024 H-2A worker-protection rule | Rescinded in 2025 ([Federal Register](https://www.federalregister.gov/documents/2025/05/12/2025-08220/rescission-of-recordkeeping-on-restricted-use-pesticides-by-certified-applications)) | Burden moved to state patchworks |
| CMMC Phase 2 (mandatory C3PAO Level 2) | **Suspended July 13, 2026**; reform task force reviewing ([Federal News Network](https://federalnewsnetwork.com/cybersecurity/2026/07/pentagon-suspends-cmmc-phase-two-requirements-launches-review-of-program/)) | Demand dampened; Phase 1 self-assessments still apply |
| ADA Title II web rule | Extended to **April 26, 2027 / April 26, 2028** ([Federal Register](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web)) | Private-sector suits and the EAA keep accessibility live anyway |
| EU AI Act high-risk obligations | Deferred to **December 2, 2027** (Annex III) and **August 2, 2028** (Annex I) ([Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)) | AI inventory tools are speculative until 2027 |
| Colorado AI Act | Repealed and replaced by a narrower ADMT framework effective **January 1, 2027** ([McDermott](https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/)) | Wait |
| CSRD and CSDDD | CSRD scope cut to >1,000 employees and >€450M turnover, with first reports in 2028; CSDDD to >5,000 employees and >€1.5B, from July 2029 ([CSSF](https://www.cssf.lu/en/omnibus-package/)) | Large-company ESG software is in a demand trough and consolidating |
| CBAM for small importers | 50-tonne annual threshold exempts about 90% of importers ([Slaughter and May](https://sustainability.slaughterandmay.com/post/102lr0h/eu-cbam-amended-to-exclude-90-of-importers-but-include-99-of-emissions)) | Only a threshold monitor remains for SMEs |
| California SB 261 climate-risk reports | Enjoined by the Ninth Circuit pending appeal ([Jones Day](https://www.jonesday.com/en/insights/2025/11/ninth-circuit-enjoins-sb-261s-climaterelated-risk-reporting-requirements-declines-to-enjoin-sb-253)) | Avoid |
| IEEPA tariffs | Struck down February 20, 2026; refunds not automatic; Section 122 replacement also held unlawful in a narrow CIT ruling now on appeal ([Ward and Smith](https://www.wardandsmith.com/article/court-of-international-trade-rejects-10-section-122-tariff-what-businesses-should-know-while-the-appeal-proceeds)) | Rate-table products are fragile; refund ledgers are timely |
| EU PPWR and ESPR implementing acts | PPWR applies from August 12, 2026, but the producer-register and labelling acts are late ([Food Manufacture](https://www.foodmanufacture.co.uk/Article/2026/08/28/ppwr-is-live-but-label-details-overdue/)); ESPR delegated acts are slipping | Wait for the acts |

### Live windows a small firm can still catch

Most of the obligations that *did* land hit small firms directly and operationally, and none of them has a grace period. They include:

- CBAM's definitive phase (January 2026), with the first annual declarations in 2027
- EPA ER&R leak repair (January 1, 2026)
- FDA QMSR for devices (February 2, 2026)
- the non-domiciled CDL rule (March 16, 2026)
- COPPA full compliance (April 22, 2026)
- Texas app-store age assurance (June 4, 2026)
- Reg S-P for smaller advisers (June 3, 2026)
- CPSC eFiling (July 8, 2026)
- California SB 54 packaging reports (May–June 2026)
- CRA vulnerability reporting (September 11, 2026)
- the new WH-347 (October 1, 2026)
- the latest ELD replacement deadline (October 6, 2026)

Later in the window, EUDR applies to large and medium operators on December 30, 2026, the battery passport arrives on February 18, 2027, and CMS's prior-authorization FHIR APIs are due January 1, 2027. The DSCSA small-dispenser exemption runs to November 27, 2027, and FDA is currently surveying whether tools are "prohibitively expensive" ([NCPA](https://ncpa.org/newsroom/qam/2026/09/01/fda-survey-dscsa-electronic-tracking)).

The pattern is consistent: **large-company disclosure regimes shrank, while transaction-level, operational compliance for small firms grew**. Uncertainty also argues for **cheap, modular, month-to-month or per-filing pricing**, because buyers are wary of annual contracts for rules that may be rescinded. That pricing model suits a small studio better than it suits enterprise incumbents.

## Validation before code: what to test in the next 60 days

Given the evidence limitation, the right next step is not a build. It is a short, structured validation sprint on the top six opportunities, run from a network that can reach the blocked sources. The table sets out the steps in order. Each row names what would move an opportunity up or down the ranking.

| Step | What to do | What would change the ranking |
|---|---|---|
| 1. Re-read the blocked sources first-hand | Pull dated threads and reviews from r/Truckers, r/Construction, r/HVAC, r/FulfillmentByAmazon, r/AmazonSeller, r/iOSProgramming, r/androiddev, r/accessibility, r/taxpros, r/CFP, r/medicalbilling and r/cybersecurity. Also read the HN threads cited here and G2/Capterra pages for SafetyCulture/Mitti, J.J. Keller, TrustLayer, Billy, Vanta and Drata. Record reviewer role, company size and date | Frequent unprompted complaints move an item up. Silence on a rule-driven item (especially HVAC ER&R and COPPA) moves it down |
| 2. Verify vendor-sourced and snippet-only claims | Check against primary sources: the MGMA $60–90K figure, the I-9 reclassification (Holland & Knight, April 2026), the HUD source-of-income withdrawal, the de minimis scope (China-only vs global, 2027 statutory repeal), the VSME delegated-act date, the SB 253 first-filing outcome, and whether Circular 230 and the FinCEN program rule were finalised | Any claim that collapses weakens the opportunity resting on it |
| 3. Run 15–20 problem interviews per top-three segment | Owner-operators and small general contractors (via OOIDA, insurance agents and GCs); app developers and Tempore's own clients; small Amazon/Shopify sellers importing consumer products. Ask how they handled the last audit or suspension, the hours spent, and the tools they tried and abandoned | Look for stated willingness to pay above roughly $30–50/month per location, and a recent painful incident |
| 4. Confirm data access before designing | Check Samsara and Motive API terms for IFTA and HOS data, CPSC/ACE filing paths for small importers (broker-filed vs self-filed), ServiceTitan and Housecall import formats, the Apple and Google age-assurance API surface, and whether CAQH, NIPR or Metrc allow any third-party writes | Blocked access demotes the item to a reminder-only tool |
| 5. Test price and channel with smoke tests | Landing pages and waitlists for items 1–6, each with a concrete price. Conversations with two channel partners per item: CPA societies or tax-software marketplaces (WISP); HVAC distributors or ACCA chapters (ER&R); EU Responsible Person services or Shopify app listings (SKU vault); CACFP sponsors (child care) | Sign-up conversion and partner interest decide which vertical skin to build first |
| 6. Get a liability review | A short legal review of disclaimers for each tier-1 item, especially SDK-to-label mappings, WISP templates and CPSC certificate data. Adopt a firm rule against "automatic compliance" claims, following the FTC/accessiBe precedent | High residual liability pushes an item toward a services model |
| 7. Prototype the shared engine as a client build | Build the entities × requirements × expiry × evidence core with a per-jurisdiction rules table, offline mobile capture and an audit-binder export. Ideally deliver it first as a paid custom build for one compliance consultant or trade association | A paying pilot de-risks the product before any self-serve launch |

A few principles should shape the sprint. Treat regulator-dated deadlines as *triggers* for marketing, not as proof of demand. Prefer segments where a failure has a binary consequence (a suspended listing, a driver placed out of service, a lost PO or a demand letter) over voluntary reporting, because the former produces urgent, paid demand. Keep Tempore's first product next to the mandated system of record, never in place of it.

## Conclusion

The research changes the question Tempore should ask. The useful question is not "which regulation should we build for?" but "which **evidence file** do small operators fail to keep, and who already sends them the deadline?" Seen that way, a truck driver's medical card, a subcontractor's insurance certificate, a therapist's CAQH attestation, a med-spa director's sign-off and a child-care home's meal count are the same product with a different rules table. That means a studio of Tempore's size can build one engine and win several narrow verticals. Incumbents built one vertical at enterprise price points and cannot easily go cheaper. The mobile privacy and age-assurance kit is the exception that proves the rule: it wins because it sits in work Tempore already does, not because it shares the engine.

Two things matter most now. First, 2025–26 made **honesty a feature**. After Delve and the FTC's accessiBe order, buyers are primed to distrust "automatic compliance" and to value verifiable, timestamped evidence and modest claims, and a new entrant can offer that credibly. Second, regulatory whiplash favours **modular, month-to-month tools and services-led entry** over multi-year platforms, because customers now wait out rules that may move. Neither advantage survives contact with an unvalidated market, though. The practitioner voice in this report is second-hand, so the sensible next move is 60 days of direct listening before the first line of product code.
