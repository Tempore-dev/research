# Compliance Bottlenecks in Physical / Field-Operations Industries: Practitioner Pain Points and Software Opportunities for Tempore

> **Read this first: how the evidence was gathered and how far it goes (researched 2026-09-25).**
> - The network egress policy for this session **blocked direct page fetches** of reddit.com and old.reddit.com, thetruckersreport.com, capterra.com, achrnews.com, forums.mikeholt.com and substack.com. It also blocked hn.algolia.com. Reddit, Hacker News and most forums could not be read directly.
> - All findings below come from **web-search result summaries**, not full-page reads.
> - Anything marked "near-verbatim" is a search-engine rendering of forum or review text. It was **not checked against the original page**, so a writer should treat it as paraphrase-grade.
> - Many results came from vendor blogs, which count as low-independence sources. Each one is marked **[vendor]**. Their statistics (for example "40+ hours per week" or "30% failure rate") are vendor claims, not survey data.
> - Primary regulatory sources (FDA, EPA, FMCSA, OSHA, DOL, the Federal Register and USDA) and trade or legal press were given priority and are the most reliable parts of these notes.
> - Items older than 2025, or superseded, are marked **[OLDER]** or **[SUPERSEDED]**.

## Q1. Which compliance tasks do practitioners call the biggest time sinks, the most manual or paper-based, or the most anxiety-inducing? What time, cost or fine figures do they cite?

### Takeaway
The recurring pattern is **expiring-document tracking and repeating periodic logs**. This covers driver-file items, COIs, lien waivers, licences and CE hours, temperature logs, weekly certified payroll, Metrc reconciliations and refrigerant leak-rate records, and all of it is kept across paper, email and spreadsheets.

Anxiety peaks around surprise audits and inspections, and around penalties that fall on paperwork failures rather than on real safety failures. For example, "almost all violations small carriers receive are documentation failures rather than driving failures." The best quantitative anchors are federal burden estimates and regulator fine totals, such as 56 minutes per WH-347 and 1.92M burden-hours a year, $10.8M in cannabis fines in 2024, and silica fines of up to $16,500 per serious violation.

### Cited Findings

**Construction: certified payroll (Davis-Bacon / prevailing wage)**
- DOL's own burden estimate for the WH-347 weekly certified payroll is **56 minutes per response**. That covers 89,498 respondents filing 2,058,454 responses a year, a total burden of **1,921,224 hours a year**. — [Praisidio summarising the DOL Federal Register notice](https://www.praisidio.com/resources/wh347-certified-payroll/)
- The WH-347 must be filed weekly for every week any contract work happens, and is usually due within 7 days of the payroll period ending. — [Praisidio](https://www.praisidio.com/resources/wh347-certified-payroll/); [DOL WH-347](https://www.dol.gov/agencies/whd/forms/wh347)
- Practitioner voice (a Mike Holt electricians' forum thread, date unknown and probably **[OLDER]**): the certified payroll process is "so onerous that there are a lot of 'back office' costs that just sky-rocket" (near-verbatim). — [Mike Holt Forum "Silly Question"](https://forums.mikeholt.com/threads/silly-question.73773/latest)
- Prevailing-wage defence is described as "a difficult, very nuanced, very gray area of the law." — [JD Supra topic page](https://www.jdsupra.com/topics/prevailing-wages/contractors/reporting-requirements)
- Many agencies force contractors onto a separate portal. For example, DOE requires IIJA award recipients to use LCPtracker, which is free to them and integrates with 20+ payroll systems including ADP and Paychex. — [DOE: Weekly DBA Payroll Tracking with LCPtracker](https://www.energy.gov/infrastructure/weekly-dba-payroll-tracking-lcptracker)

**Construction: subcontractor COIs and lien waivers**
- **[vendor]** GCs collect COIs, W-9s, business licences, MSAs, warranty letters, lien waivers and safety agreements "on a per-vendor, per-project basis." Without a structured workflow these end up "scattered across email threads, shared drives, and spreadsheets that nobody trusts by month two of a project." — [Billy (COI vendor)](https://billyforinsurance.com/resources/custom-compliance-forms-construction/)
- **[vendor]** "A spreadsheet holds up beautifully at two or three active jobs, but somewhere around five, it starts to crack." — [LienDone lien waiver spreadsheet blog](https://www.liendone.com/blog/lien-waiver-tracking-spreadsheet)
- Construction CFOs discuss lien waiver collection from subcontractors on the CFMA forum. **[OLDER]** Snippet only. — [CFMA forum thread](https://chapters.cfma.org/forum_old/thread_sclienwavers.html)

**Construction: OSHA safety documentation, silica and heat**
- In 2025 OSHA issued "over 400 silica-related citations to construction firms." Silica "remains one of the most-cited health standards in construction." **[vendor-blog figure, not verified against OSHA data]** — [HazComFast](https://hazcomfast.com/blog/osha-silica-compliance-construction-2026)
- Every employer must have a **written exposure control plan** for silica, even when it uses the Table 1 shortcut, and OSHA "will expect to see a completed Written Exposure Control Plan" on site. The maximum serious-violation penalty was **$16,500** as of January 2025, and willful or repeat penalties can be 10 times that. — [HazComFast](https://hazcomfast.com/blog/osha-silica-compliance-construction-2026); primary rule: [OSHA 1926.1153](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1153)
- The OSHA 300A electronic submission via ITA for CY2025 data was due **March 2, 2026**. It applies to establishments with 250+ employees in covered industries and to 20–249-employee sites on the Appendix A high-hazard list. Sites with 100+ employees in Appendix B industries must also submit 300/301 case detail. The penalty is up to $16,131 per violation. — [Coggno](https://coggno.com/blog/osha-300a-electronic-submission-2026-who-files-pull-from-lms/); [OSHA ITA](https://www.osha.gov/injuryreporting)
- Recordability is a common source of confusion. A common mistake is to log every reported case, including cases with no lost time, "which leads many companies to believe they have higher OSHA recordable incidence rates than is necessarily the case." Firms with 10 or fewer employees are partly exempt. — search snippets from [Minnesota DLI recordkeeping](https://dli.mn.gov/sites/default/files/pdf/rcdkpg201_7.pdf) and [NV DIR 300 log instructions](https://dir.nv.gov/uploadedFiles/dirnvgov/content/Governance/300%20Logs%20(Instructions).pdf)
- ContractorTalk small contractors (**[OLDER]** threads) say that OSHA "isn't likely going to find" residential contractors but will on commercial or government jobs. Their toolbox-talk practice is to have "everyone signing off after reading the safety bulletin" (near-verbatim). — [ContractorTalk: OSHA for a sole proprietor](http://www.contractortalk.com/f59/osha-sole-proprieter-90934/); [ContractorTalk: OSHA 10/30](http://www.contractortalk.com/f11/osha-10-osha-30-certifications-8496/)

**Trucking and fleets**
- DQ files: "The fastest way to trigger a compliance audit from the FMCSA is to have incomplete or improperly maintained driver qualification files." "Missing med cards, expired CDLs, and sloppy driver files are audit bait." — [FreightWaves via Yahoo: "Improper driver files triggering surprise…"](https://www.yahoo.com/news/articles/improper-driver-files-triggering-surprise-143051026.html)
- "An owner-operator with a single truck carries the same documentation requirements as a much larger fleet". There is no small-carrier exemption for DQ files, drug testing or maintenance records. "Almost all violations small carriers receive are documentation failures rather than driving failures." **[vendor/aggregator]** — [TruckComplianceHQ DOT checklist](https://truckcompliancehq.com/blog/dot-compliance-checklist)
- A J.J. Keller testimonial from a 14-vehicle fleet says that sorting paper files during a DOT audit **took 7 days** **[vendor testimonial]**. — [J.J. Keller Encompass](https://www.jjkeller.com/shop/j-j-keller-encompass-fleet-management-system)
- Clearinghouse: an annual limited query is required on every CDL driver. TruckersReport owner-operators complain of errors and a "useless" help line ("high call volume, call back later"). They say FMCSA staff were "just as frustrated with all the reregistering/inactive problems" and call it "take from the drivers, no give." One owner-operator self-employed since 2020 admitted missing the requirement for years (all near-verbatim; the 2021 thread is **[OLDER]**). — [TruckersReport: 2021 Clearinghouse/Portal/Query problems](https://www.thetruckersreport.com/truckingindustryforum/threads/2021-clearinghouse-portal-query-problems.2051909/); [TruckersReport: Clearinghouse query notification](https://www.thetruckersreport.com/truckingindustryforum/threads/clearinghouse-query-notification-how-does-yours-notify-you.2507456/page-2); [TruckersReport: Clearinghouse](https://www.thetruckersreport.com/truckingindustryforum/threads/clearinghouse.2359685/)
- IFTA: quarterly returns are due April 30, July 31, October 31 and January 31, and must be filed even when no tax is owed. Miles are tracked per jurisdiction. The source attributes to OOIDA the view that IFTA is "one of the top administrative headaches for small carriers" **[secondary attribution; no OOIDA primary source found]**. The fuel and mileage systems are often "separate or missing entirely." — [Small Fleet HQ](https://smallfleethq.com/fuel-cards/ifta-reporting); [OTR Solutions](https://otrsolutions.com/blog/ifta-fuel-tax-reporting)
- ELD unassigned driving: yard moves by a mechanic who has not logged in create Unidentified Driving events. Fleet managers "report spending time each day cleaning up events that resulted from technical glitches rather than actual driving." — [Samsara KB: Manage Unassigned HOS](https://kb.samsara.com/hc/en-us/articles/360043216412-Manage-Unassigned-HOS); forum thread [TruckersReport: Samsara ELD issues](https://www.thetruckersreport.com/truckingindustryforum/threads/samsara-eld-issues.2475226/) (could not be fetched)

**Food and beverage**
- A FoodReady survey (May 2026) of "hundreds" of food manufacturers found a gap between how audit-ready they believe they are and how ready they actually are. "Locating and organizing records quickly remains a persistent challenge, particularly when information is stored across multiple spreadsheets, paper files, shared drives, and standalone software systems." Many can see only one or two tiers of their supply chain. **[vendor-sponsored survey]** — [BusinessWire: FoodReady research](https://www.businesswire.com/news/home/20260513974347/en/New-FoodReady-Research-Shows-Small-to-Mid-Sized-Food-Manufacturers-Are-Not-Audit-Ready)
- About 70% of food supply-chain organisations say they struggle to exchange data between internal and external systems, and only about 1 in 4 have a single centralised traceability system. **[aggregated; the original survey was not identified]** — [The AgriFood Data](https://theagrifooddata.com/food-manufacturing-new-foodready-research/)
- FSMA 204 requires TLCs, KDEs at CTEs, and **records produced to FDA within 24 hours** of a request. — [FDA FSMA 204 final rule page](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods); [ReliaMag](https://reliamag.com/guides/fsma-rule-204-compliance/)
- Restaurant temperature logs: "Staff time spent walking equipment, recording numbers, and filing logs is time not spent on prep, service, training, or line execution." **[vendor]** — [Label King Turbo blog](https://labelkingturbo.com/blog?post=restaurant-temperature-monitoring-that-works)
- I found no reliable practitioner-sourced figure for hours per week spent on restaurant temperature or HACCP logs (see Gaps).

**Cannabis**
- MJBizDaily (as cited): US cannabis regulators issued **nearly 2,500 violations in 2024, totalling $10.8M in fines**. Track-and-trace errors are "the single biggest source of enforcement actions in most states," with nearly half of violations tied to them. First-offence inventory-discrepancy fines usually run **$1,000–$10,000**. **[secondary citation of MJBizDaily; the primary article was not fetched]** — [Northstar Financial Advisory](https://nstarfinance.com/resources/cannabis-inventory-management-tips-to-stay-compliant); [Distru](https://www.distru.com/cannabis-blog/out-of-compliance-meaning-in-cannabis)
- **[vendor]** "Teams managing compliance manually were spending 40-plus hours per week on tasks that software could handle". The same source puts this at about $52K a year at $25 an hour. — [Northstar Financial Advisory](https://nstarfinance.com/resources/metrc-marijuana-enforcement-tracking-compliance)
- Some states require Metrc and physical inventory to reconcile **daily**, with formal discrepancy reports due within set windows. — [Northstar](https://nstarfinance.com/resources/cannabis-inventory-management-tips-to-stay-compliant); [BayArea Compliance METRC audit checklist](https://bayareacompliance.com/resources/metrc-audit-checklist-california-cannabis)
- Labelling: "Missing a single required field on a label can trigger a product recall, a fine, or a stop-sale order." — [Northstar](https://nstarfinance.com/resources/cannabis-inventory-management-tips-to-stay-compliant)
- MJBizDaily headline: "Track-and-trace expenditures offer little return, cannabis operators say." — [MJBizDaily](https://mjbizdaily.com/cannabis-track-and-trace-expenditures-offer-little-return/)

**Manufacturing and environmental**
- Practical Machinist shop owners say ISO/AS9100 means needing "a full-time quality person whether the shop had 10 or 100 employees" (near-verbatim). One owner "toned down approximately 2/3rds of the template documents" they didn't need. — [Practical Machinist: ISO9000 and AS9100](https://www.practicalmachinist.com/forum/threads/iso9000-and-as9100.401341/); [Practical Machinist: QMP template](https://www.practicalmachinist.com/forum/threads/quality-management-plan-template.429078/)
- Where FAI and traceability apply, "a five-person shop and a five-hundred-person supplier may need to maintain the same core record types." — [Carbon: AS9100 for small shops](https://carbon.ms/learn/as9100-for-small-shops)
- TSCA 8(a)(7) PFAS covers anyone who manufactured or imported PFAS **or PFAS-containing articles** from 2011 to 2022. That is a 12-year lookback on supplier data, which small article importers are unlikely to have. — [EPA TSCA 8(a)(7) page](https://www.epa.gov/assessing-and-managing-chemicals-under-tsca/tsca-section-8a7-reporting-and-recordkeeping)

**Trades licensing and HVAC**
- EPA ER&R rule (effective **January 1, 2026**): the leak-repair threshold dropped from 50 lb to **15 lb** for HFC or substitute refrigerant with GWP above 53. A **leak-rate calculation is required every time refrigerant is added**. Repairs are due within 30 days, or a retrofit or retirement plan applies. Records must be kept for 3+ years, covering leak-rate calculations, repairs, verification tests and ALD calibration. — [EPA leak-repair fact sheet, Jan 2026](https://www.epa.gov/system/files/documents/2026-01/er-r-fact-sheet-leak-repair-2026-01-13_1.pdf); [Oxmaint](https://oxmaint.com/industries/hvac/epa-aim-act-compliance-hvac-refrigerant-management-leak-repair)
- ACHR News opinion headline (January 2026): "New Year, New Refrigerant Rules, No Grace Period" (full text was blocked). — [ACHR News](https://www.achrnews.com/blogs/17-opinions/post/165785-new-year-new-refrigerant-rules-no-grace-period)
- R-454B cylinder prices rose from **$345 (2021) to more than $2,000 (2025)**. Honeywell raised prices by over 40% in April 2025 after it could not meet demand, which delayed installs and led to illegal refrigerant mixing. **[secondary; Contracting Business is trade press]** — [Contracting Business: Cold Truth: The R-454B Shortage](https://www.contractingbusiness.com/refrigeration/article/55288344/cold-truth-the-r-454b-shortage); [The Furnace Outlet](https://thefurnaceoutlet.com/blogs/news/r-454b-refrigerant-shortage-2025-rising-desperation-and-emerging-risks-in-the-hvac-industry)
- Electrician licensing: 24–32 CE hours per 2-year cycle is typical, and most jurisdictions require NEC code-update credits. A lapsed licence risks a stop-work order, a denied insurance claim and a **$2,000–$10,000** state fine. **[vendor]** claim: "past 5 techs, the failure rate on renewal reminders exceeds 30% without automated alerts". This is unsourced and should be treated as marketing. — [US Tech Automations](https://ustechautomations.com/resources/blog/automate-best-certification-renewal-software-for-electrical-contractors-2026)

### Inferences
- The most common bottleneck is **not a hard calculation. It is keeping a date-driven, per-person or per-asset evidence file complete and findable on demand**: DQ files, COIs and waivers, CE hours, SDS versions, refrigerant logs, and FSMA 204 24-hour production. This is a CRUD, reminders, document capture and export problem that suits a small web/mobile/desktop shop.
- The second tier is **recurring forms with heavy per-cycle labour**: weekly WH-347s, quarterly IFTA, daily temperature and HACCP logs, and daily Metrc reconciliation. Here the value is pre-filling from data the firm already holds (payroll, ELD GPS, fuel cards, POS or inventory).
- Anxiety comes mostly from **audits and inspections that arrive without warning** and from fines on documentation failures. That points to an "audit-ready binder in one click" value proposition.

### Gaps
- There are **no direct Reddit quotes**, because Reddit was blocked by egress policy. r/Construction, r/Truckers, r/KitchenConfidential, r/cannabisbusiness and r/HVAC sentiment is not represented first-hand.
- No independent time-and-motion data was found for COI or lien waiver tracking, temperature logs, SDS management or toolbox talks. Only vendor claims exist.
- I could not confirm OSHA's own 2025 silica citation count; the ">400" figure comes from a vendor blog.
- No quantitative source was found for H-2A paperwork hours or for time spent on state pesticide records.

---

## Q2. What tools do practitioners use, and what specific complaints appear in reviews?

### Takeaway
Incumbent tools fall into three groups:
- **Enterprise suites**: Procore and J.J. Keller Encompass. They are too costly or complex for small firms.
- **Per-seat inspection and checklist apps**: SafetyCulture (now Mitti) and Jolt. Complaints are about seat-price escalation, offline photo sync, UI lag and poor frontline adoption.
- **Government-mandated systems**: Metrc, the FMCSA Clearinghouse and LCPtracker. Operators cannot switch away from these, and they complain about fees, outages, support and reregistration friction.

Paper and Excel remain the default for the smallest operators across every sector.

### Cited Findings

**Construction**
- **Procore**: "For most small contractors (under 50 employees or under $5M annual volume), Procore is too expensive and too complex". Pricing runs from about **$10K a year** for small contractors to **$80K+** for enterprises, with opaque quotes. Setup "is not a same-day affair" and can take weeks or months. The safety module "was built … later as a module" and "lacks the depth of dedicated safety platforms." — [Connecteam Procore review](https://connecteam.com/reviews/procore/); [Make Safety Easy](https://makesafetyeasy.com/blog/procore-alternative-small-contractors); [Workyard](https://www.workyard.com/compare/procore-review)
- **SafetyCulture / iAuditor, renamed "Mitti" in August 2026**:
  - The most common complaint from 20+ user teams is that per-seat cost becomes "significant," and users mention recent price hikes.
  - G2's AI summary flags advanced workflows, dashboards and integrations as hard to set up.
  - Report layouts can't be customised to regulator or client formats.
  - "Photo sync issues in offline conditions documented in multiple G2 and Capterra reviews" (offline data "does not always upload cleanly").
  - Pricing: Premium is **$24 per seat per month** billed annually or $29 monthly. The free plan covers up to 10 users, and Lite seats cost $5.

  **[review aggregator by a competitor]** — [Fluix SafetyCulture review](https://fluix.io/blog/safetyculture-review); [G2 SafetyCulture pros and cons](https://www.g2.com/products/safetyculture-2025-01-20/reviews?qs=pros-and-cons); [G2 Mitti](https://www.g2.com/products/safetyculture-iauditor/reviews)
- Certified payroll: LCPtracker is mandated by many agencies (DOE, and cities such as Minneapolis) as a separate upload portal on top of payroll software. — [DOE](https://www.energy.gov/infrastructure/weekly-dba-payroll-tracking-lcptracker); [Minneapolis Prime Approver Guide](https://www2.minneapolismn.gov/media/content-assets/documents/government/Prime-Approver-Guide-V2-2.23.2023.pdf)
- COI and lien waivers: the market has specialist SaaS (TrustLayer, Billy, CertPact, COI Software), but small GCs are pushed toward free Excel templates. — [TrustLayer](https://www.trustlayer.io/pages/lien-waiver); [Billy Excel template](https://billyforinsurance.com/certificate-of-insurance-tracking-template-excel/); [CertPact](https://www.certpact.com/)

**Trucking**
- **ELDs (Samsara, Motive and others)**: the pain is cleaning up unassigned driving and malfunction events, and falling back to paper logs during malfunctions. — [Samsara KB: Unidentified Driving malfunctions](https://kb.samsara.com/hc/en-us/articles/20848422816269-Resolve-Unidentified-Driving-D-Malfunctions); Motive review: [TruckingWay "The Best App You Can't Quit?"](https://www.truckingway.com/motive-eld-review/)
- **Revoked ELDs**: FMCSA has removed **79 devices since January 2025**. Carriers get 60 days to replace them, and after the deadline drivers are placed out of service under 395.8(a)(1). Recent deadlines include February 7, 2026 and March 15, 2026, and devices revoked on August 6, 2026 must be replaced by **October 6, 2026**. Cheap "self-certified" ELDs bought by small carriers turned into a compliance liability. — [FMCSA newsroom](https://www.fmcsa.dot.gov/newsroom/fmcsa-removes-fourteen-devices-list-registered-electronic-logging-devices); [FMCSA ELD site](https://eld.fmcsa.dot.gov/)
- **J.J. Keller Encompass** targets fleets of 1–3,000 drivers with regulation-referenced DQ checklists. I found no independent negative reviews, and the search returned only marketing. — [J.J. Keller Encompass DQ](https://eld.kellerencompass.com/solutions/driver-qualification)
- **FMCSA Clearinghouse**: owner-operators report error messages, reregistration and inactive-account loops, complex password rules, no notification of the annual query, and an unhelpful help line. — [TruckersReport threads, as above](https://www.thetruckersreport.com/truckingindustryforum/threads/2021-clearinghouse-portal-query-problems.2051909/)
- **IFTA**: common tools are free spreadsheets or paid filing services, which shows the self-serve gap. — [American Truckers LLC IFTA spreadsheet](https://www.americantruckersllc.com/ifta-filing-guide-spreadsheet.html); [start4truckers filing service](https://start4truckers.com/services/ifta-quarterly-filing-service/)

**Food and beverage**
- **Jolt** (Capterra 4.6/5 from 308 reviews):
  - The UI is a frequent complaint: "slow logins, an outdated design, and a mobile app that underperforms."
  - Employees find Jolt Lite unintuitive, so managers enter availability themselves.
  - It is "really laggy with connection issues, making getting through task lists pretty tough."
  - One reviewer said staff "wouldn't adopt the software after several months," calling it "a design problem rather than a training issue."
  - Reviewers mention billing transparency and auto-charge problems.

  (Near-verbatim from search summaries; partly via a competitor, Delightree.) — [Capterra Jolt reviews](https://www.capterra.com/p/146384/Jolt/reviews/); [Delightree Jolt alternatives [competitor]](https://www.delightree.com/competitor-alternatives/jolt-alternatives)
- **FoodDocs**: 96% of reviewers come from small companies. Cons are that it is "confusing for first-time users" and that users can't skip daily notifications on days with no staff or deliveries. One reviewer was locked into "an annual contract for add-ons with no clear cancellation path," and another had unclear integrations. — [SoftwareConnect FoodDocs review](https://softwareconnect.com/reviews/fooddocs/); [Capterra FoodDocs](https://www.capterra.com/p/214198/FoodDocs/reviews/); [G2 FoodDocs](https://www.g2.com/products/fooddocs/reviews)
- Paper is still common. Health departments distribute printable temperature log PDFs (Minneapolis, NYC). — [Minneapolis food temp log](https://www.minneapolismn.gov/media/-www-content-assets/documents/English--Food-temperature-log.pdf); [NYC fridge temp log](https://www.nyc.gov/assets/doh/downloads/pdf/imm/fridge-temp-log-f.pdf)

**Cannabis**
- **Metrc** (state-mandated in 23 state contracts per MJBizDaily; the count varies by article date):
  - Operators pay **$40 per month** for access, plus **$0.45 per plant tag** and **$0.25 per package tag**.
  - A Colorado company said RFID tags cost it **more than $1,400 a month** and sued over the requirement.
  - Colorado's Metrc contract **expires October 2026**, and the new bid does not require RFID.
  - California extended its Metrc contract at up to $28.4M a year ($113.6M over 4 years).

  — [MJBizDaily: Colorado RFID challenge](https://mjbizdaily.com/colorado-marijuana-company-challenging-rfid-tag-requirement/); [MJBizDaily: CA contract](https://mjbizdaily.com/metrc-secures-cannabis-track-and-trace-contract-extension-in-california/); [Oklahoma OMMA Metrc tag cost handout, July 2025](https://www.oklahoma.gov/content/dam/ok/en/omma/content/eac/2025-7-11/EAC%20Handout%20July%2011%202025%20-%20Metrc%20plant%20tag%20costs.pdf)
- In Michigan, 100+ businesses missed Metrc's new $40 monthly fee, and some said they were never notified or had paid anyway. Metrc threatened to cut off access, which is "basically a death blow," then support lines were "ringing off the hooks" and Metrc issued a 30-day stay. A Metrc functionality change was also said to undermine distributors and small players. **[newsletter, date not confirmed, likely 2023–24, OLDER]** — [Eric Casey Substack, Issue 35](https://ericcasey.substack.com/p/issue-35-metrc-flexes-its-muscles)
- Metrc fought in court to charge Missouri medical operators fees. — [MJBizDaily](https://mjbizdaily.com/metrc-missouri-in-court-battle-over-medical-marijuana-fees/)
- Commercial ERPs such as Flourish, Distru and BLAZE sit on top of Metrc and BioTrack. Flourish markets queueing of outbound messages "when Metrc is down", which is indirect evidence of Metrc outages. No independent dispensary reviews of sync errors were found. — [Flourish Metrc integration](https://www.flourishsoftware.com/integrations/metrc)

**Manufacturing and HVAC**
- ISO and AS9100 small shops use purchased templates and cut them down. Elsmar Cove and Practical Machinist are the practitioner forums. — [Practical Machinist](https://www.practicalmachinist.com/forum/threads/quality-management-plan-template.429078/); [Elsmar Cove](https://elsmar.com/elsmarqualityforum/threads/do-i-need-both-as9100-and-iso9001.66680/)
- HVAC refrigerant tracking is still sold as **paper "Refrigerant Tracking Log Books"** on Gumroad, which shows that paper practice persists. — [Gumroad Refrigerant Tracking Log Book](https://nouh3579.gumroad.com/l/uzgahg)

### Inferences
- Complaints about incumbents cluster on **per-seat pricing that punishes frontline headcount**, **offline and sync reliability**, **UX that deskless workers won't adopt**, and **annual lock-in contracts**. A small firm can compete on flat or per-location pricing, true offline-first mobile, and a minimal "one button per task" UX for workers.
- Government-mandated systems (Metrc, the Clearinghouse, LCPtracker, the OSHA ITA, the FDA 24-hour sortable spreadsheet) can't be replaced. The opportunity is **companion tools** that prepare, validate, remind and reconcile before data goes into the mandated system, while respecting whatever API or upload terms each system allows.

### Gaps
- Capterra and G2 pages could not be fetched, so there are **no verified individual review quotes with dates**. The complaints above are aggregator paraphrases.
- No independent critical reviews of J.J. Keller Encompass, Motive, LCPtracker, BioTrack or Flourish were found.
- There is no data on market share of paper vs. software by sector.

---

## Q3. Where do small operators say nothing affordable, simple, offline-capable or mobile-friendly exists? (Includes the Tempore addressability assessment)

### Takeaway
The clearest "small-operator gap" signals are:
- owner-operators and small fleets doing DQ files, IFTA and Clearinghouse queries on spreadsheets and paper;
- small GCs whose COI and lien waiver spreadsheets break past about 5 jobs;
- small restaurants for whom Jolt and FoodDocs are too heavy or contract-bound;
- HVAC contractors newly facing leak-rate records at 15 lb, still on paper logbooks;
- small machine shops drowning in ISO/AS9100 templates.

Much of this evidence comes from vendor content describing the gap, so direct practitioner confirmation is thin (see the Gaps note).

### Cited Findings
- Procore is "too expensive and too complex" for firms under 50 employees or under $5M. — [Connecteam](https://connecteam.com/reviews/procore/)
- Search results show "free Excel template" COI, lien waiver, IFTA and HVAC log products ranking highly, which suggests demand for cheap or self-serve options. — [Billy COI Excel template](https://billyforinsurance.com/certificate-of-insurance-tracking-template-excel/); [LienDone spreadsheet](https://www.liendone.com/blog/lien-waiver-tracking-spreadsheet); [American Truckers IFTA spreadsheet](https://www.americantruckersllc.com/ifta-filing-guide-spreadsheet.html)
- SafetyCulture: offline photo sync is unreliable, and per-seat cost grows at 20+ users. — [Fluix](https://fluix.io/blog/safetyculture-review)
- Jolt: the UI is laggy, and frontline staff won't adopt it. — [Capterra Jolt](https://www.capterra.com/p/146384/Jolt/reviews/)
- FoodDocs: users get forced daily notifications and are locked into annual add-on contracts. — [SoftwareConnect](https://softwareconnect.com/reviews/fooddocs/)
- Owner-operators have the same DQ, drug-testing and maintenance record obligations as large fleets. — [TruckComplianceHQ](https://truckcompliancehq.com/blog/dot-compliance-checklist)
- Only about 1 in 4 food supply-chain organisations have a centralised traceability system. — [The AgriFood Data](https://theagrifooddata.com/food-manufacturing-new-foodready-research/)
- HVAC refrigerant logbooks are still sold in paper form. — [Gumroad](https://nouh3579.gumroad.com/l/uzgahg)
- ISO/AS9100 needs a quality person "whether 10 or 100 employees". — [Practical Machinist](https://www.practicalmachinist.com/forum/threads/iso9000-and-as9100.401341/)

### Inferences: Tempore addressability assessment
Tempore is a small firm building web, mobile and desktop apps. The table gives a judgement for each gap. H, M and L are my inference, not sourced.

| # | Gap | Evidence strength | Buildability for a small firm | Regulatory and data-access risk | Competition | Tempore fit |
|---|---|---|---|---|---|---|
| 1 | **Expiring-document vault with reminders and audit-binder export** (DQ files, COIs, lien waivers, licences and CE, 608 certs, med cards). Built for fewer than 25 staff or trucks and offline-first. | Strong. DQ audit triggers, the 7-day paper audit, COI spreadsheets breaking at ~5 jobs | High: forms, OCR of ACORD 25 and med cards, reminders, PDF export | Low | Crowded at the top end (J.J. Keller, TrustLayer, Billy), thin at the micro end | **H** |
| 2 | **HVAC ER&R refrigerant leak-rate logger** (mobile calculator on every top-off, 30-day repair clock, 3-year records, 608 tech ID). New from January 1, 2026. | Medium. Primary rule plus paper logbooks; no forum voices captured | High: calculation, forms, reminders; could export into ServiceTitan or Housecall via CSV | Low–medium. The Technology Transitions rule is being reconsidered, but ER&R leak repair took effect in 2026 | CMMS and enterprise tools (Oxmaint, Fexa, iFactory) target facilities, not 3–20-truck contractors | **H** |
| 3 | **Restaurant temperature/HACCP log app**: flat price per location, true offline, 2-tap entry, optional Bluetooth probe, inspector-ready PDF | Medium. Jolt and FoodDocs complaints | High | Low | Crowded (Jolt, FoodDocs, Zip HACCP, Toast add-ons); differentiate on price and UX | **M** |
| 4 | **FSMA 204 "sortable spreadsheet in 24h" kit for small FTL handlers**: KDE and CTE capture at receiving and shipping, TLC labels, one-click FDA export | Medium–strong on need; the deadline was pushed to July 20, 2028 | Medium: needs supplier data exchange and label printing | Medium. The rule could be amended further; demand will be back-loaded to 2027–28 | Growing (ReliaMag, inecta, Trustwell, FoodReady) | **M**, with a later window |
| 5 | **Certified payroll helper**: turn existing payroll exports (QuickBooks, Gusto, ADP) into the **new WH-347** (sole valid form from October 1, 2026) and state PW forms, and validate fringe and classification | Strong on burden (1.92M hours a year) | Medium: wage-determination lookups and many state formats | Medium: legal liability for errors | LCPtracker, eBacon, Praisidio, Miter, Projul | **M** |
| 6 | **IFTA and HOS side tools for owner-operators**: combine ELD GPS or state-mileage CSV with fuel-card CSV into a quarterly return | Medium | High if it works from CSV imports; API access to Samsara or Motive varies | Low | Many filing services and fuel-card add-ons | **M** |
| 7 | **Silica written exposure control plan and toolbox talk generator**: Table 1 task picker producing a plan PDF, plus crew sign-off on phone with no per-seat fee | Medium: silica is heavily cited; toolbox evidence is anecdotal | High | Low | SafetyCulture and many templates; commoditised | **M–L** |
| 8 | **Metrc reconciliation or label-check companion** | Strong on fines | Low–medium: depends on Metrc API access and approvals in each state, plus state-by-state label rules | High: mandated-system dependency, and the market is contracting and shifting (hemp ban, rescheduling) | Flourish, Distru, BLAZE and others are established | **L** |
| 9 | **ISO 9001/AS9100 lightweight QMS for 5–50-person shops**: doc control, NCR/CAPA, calibration, FAI | Medium (forums) | Medium | Low | Many QMS SaaS products | **M–L** |
| 10 | **TSCA PFAS article-importer supplier survey tool** | Uncertain: the rule is being amended and may exempt articles | Medium | High: the scope is still changing | Enterprise product-compliance tools (iPoint, Certivo, Assent) | **L** for now |

- The best fits combine a **date-driven evidence locker** with **mobile capture** and a **regulator-formatted export**, and avoid dependence on a mandated government API. Rows 1, 2 and 3 fit that pattern.

### Gaps
- Because Reddit and the forums were blocked, I could not capture first-hand statements like "I've looked, nothing cheap exists." The gaps are inferred from incumbent complaints and the prevalence of templates.
- I did not verify whether Samsara or Motive offer public APIs usable by third-party IFTA tools, or the current Metrc API licensing terms.
- Pricing of the micro-market alternatives (for example Zip HACCP, COI Software, CertPact) was not collected.

---

## Q4. Which regulatory changes in 2025–2027 are creating new pain, and which were delayed or rolled back?

### Takeaway
New or tightening in 2025–26:
- trucking English-proficiency out-of-service enforcement (over 20K drivers placed OOS) and the NPRM to codify it (August 10, 2026);
- the non-domiciled CDL rule (effective March 16, 2026);
- ELD revocations (79 devices);
- the EPA ER&R 15-lb leak-repair threshold (January 1, 2026);
- the mandatory new WH-347 (October 1, 2026);
- HazCom 2024 SDS deadlines (May 19, 2026 for substances);
- the new H-2A AEWR methodology;
- the federal hemp THC redefinition (November 12 and December 11, 2026).

Delayed or rolled back:
- FSMA 204 moved to **July 20, 2028**;
- TSCA PFAS reporting start pushed to **by January 31, 2027**;
- the OSHA heat rule stalled, with a supplemental NPRM planned for December 2026;
- federal RUP recordkeeping for applicators rescinded (July 11, 2025);
- the 2024 H-2A worker-protection rule rescinded;
- the AIM Act Technology Transitions rule under reconsideration;
- medical cannabis moved to Schedule III, with 280E relief only for state-licensed medical operators.

### Cited Findings

**Construction**
- **OSHA heat rule (stalled)**:
  - The NPRM was published August 30, 2024, the hearing ended July 2, 2025, and post-hearing comments closed October 30, 2025.
  - The DOL 2026 regulatory plan targets a **supplemental NPRM in December 2026** "with the stated goal of scaling back burdens."
  - A revised Heat NEP (April 10, 2026) narrowed the high-risk industries and dropped numeric inspection goals.

  — [OSHA heat rulemaking page](https://www.osha.gov/heat-exposure/rulemaking); [Ogletree](https://ogletree.com/insights-resources/blog-posts/oshas-heat-program-to-expire-while-heat-standard-stalls/); [Beveridge & Diamond](https://www.bdlaw.com/publications/osha-refines-heat-enforcement-strategy-while-federal-heat-rule-remains-pending/)
- State heat rules continue independently (for example CA, WA, OR, MD, NV). — [HeatStress.com: where states stand 2026](https://heatstress.com/blog/heat-stress-policy-update-where-states-stand-in-2026)
- **WH-347**: DOL revised the form effective January 15, 2025 (valid to January 31, 2028). From **October 1, 2026 the new WH-347 is the only valid form**. DOL released an online fillable version and an annotated form (December 16, 2025 release). — [DOL news release, December 16, 2025](https://www.dol.gov/newsroom/releases/whd/whd20251216-0); [DOL WH-347 web form](https://www.dol.gov/agencies/whd/forms/wh347-web); [SkillSmart: "The New WH-347 Requires More Than a New Form"](https://www.skillsmart.us/the-new-wh-347-requires-more-than-a-new-form/)
- **HazCom 2024**: on January 15, 2026 OSHA extended the deadline for substances by 4 months to **May 19, 2026**, and for mixtures to **November 19, 2027**. SDSs and labels must reflect the new classifications. — [CHEMTREC](https://www.chemtrec.com/resources/blog/osha-extends-hcs-compliance-deadlines); [UT CIS](https://www.cis.tennessee.edu/hazcom-2026-what-employers-need-know)
- The OSHA 300A electronic filing was due March 2, 2026. I found no evidence of a rollback of the 2024 electronic-submission rule. — [OSHA ITA](https://www.osha.gov/injuryreporting); [Coggno](https://coggno.com/blog/osha-300a-electronic-submission-2026-who-files-pull-from-lms/)

**Trucking**
- **English Language Proficiency (ELP)**:
  - CVSA added ELP to the OOS criteria effective June 25, 2025, and printed it in the April 1, 2026 edition.
  - DOT said in May 2026 that **more than 20,000 truckers** had been placed OOS since June 2025.
  - An **NPRM published August 10, 2026** would codify it as a formal OOS violation.
  - Congress mandated the change (CDLLife 2026).

  — [CCJ](https://www.ccjdigital.com/regulations/safety-compliance/article/15833851/how-fmcsa-english-proficiency-impacts-trucking-capacity); [TruckingInfo](https://www.truckinginfo.com/news/fmcsa-moves-to-codify-english-language-requirements-for-commercial-drivers); [CDLLife](https://cdllife.com/2026/congress-mandates-fmcsa-regulation-change-so-english-proficiency-failure-triggers-out-of-service-order-for-cdl-drivers/); [Land Line](https://landline.media/fmcsa-expected-to-propose-stricter-language-for-english-proficiency/)
- **Non-domiciled CDL final rule** (effective **March 16, 2026**): only H-2A, H-2B and E-2 visa holders qualify, and EADs alone are no longer enough. About **194,000** current holders could be affected at renewal. Carriers need to review DQ files and immigration documents. — [Jackson Lewis](https://www.jacksonlewis.com/insights/fmcsa-new-rule-cracks-down-non-citizen-commercial-drivers-licenses-creating-carrier-burdens); [Benesch](https://www.beneschlaw.com/insight/non-domiciled-cdls-fmcsa-final-rule-and-its-operational-impacts/); [DotMotus](https://dotmotuscompliance.com/fmcsas-non-domiciled-cdl-rule-took-effect-march-16-2026-heres-what-your-driver-qualification-file-process-needs-to-change/)
- **ELD revocations**: 79 devices removed since January 2025, and the latest replacement deadline is October 6, 2026. — [FMCSA](https://www.fmcsa.dot.gov/newsroom/fmcsa-removes-fourteen-devices-list-registered-electronic-logging-devices)

**Food**
- **FSMA 204**: the compliance date moved 30 months, from January 20, 2026 to **July 20, 2028** (Federal Register, August 7, 2025). — [Federal Register](https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension); [FDA](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods)
- FDA has announced a FSMA 204 stakeholder engagement initiative and released guidance. — [Food Safety Magazine](https://www.food-safety.com/articles/11158-fda-announces-fsma-204-stakeholder-engagement-initiative-releases-guidance)

**Cannabis and hemp**
- **Rescheduling**:
  - A DOJ order of April 23, 2026 moved FDA-approved and **state-licensed medical** marijuana to Schedule III, effective April 28, 2026.
  - Medical licensees are free of **280E** from tax year 2026, and the IRS was told to consider retroactive relief.
  - **Adult-use remains Schedule I and still subject to 280E.**
  - A DEA expedited hearing on broader rescheduling started June 29, 2026.

  — [Foley Hoag](https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/april/doj-immediately-reschedules-state-licensed-medical-cannabis-to-schedule-iii-and-restarts-the-clock/); [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/04/cannabis-rescheduling-doj-fda-announce-rescheduling); [Duane Morris](https://www.duanemorris.com/alerts/relief_finally_dea_issues_order_expediting_cannabis_rescheduling_schedule_iii_0426.html)
- **New pain from rescheduling**: dual-licence (medical and adult-use) operators now need to split cost accounting between 280E and non-280E activity. This is my inference, based on the medical-only scope in the sources above.
- **Hemp**: the federal definition moves to **total THC ≤0.3%**, finished products are capped at **0.4 mg total THC per container**, and synthesised cannabinoids are excluded. H.R. 6500 (signed September 2, 2026) delays most restrictions to **December 11, 2026**, but non-naturally-occurring cannabinoids lose hemp status on **November 12, 2026**. — [Vicente LLP](https://vicentellp.com/insights/2026-federal-hemp-ban-what-it-means-for-the-future-of-consumable-hemp-products/); [CRS IN12620](https://www.congress.gov/crs-product/IN12620); [Hemp Law Group](https://www.hemplawgroup.com/news/federal-hemp-ban-2026-where-things-stand)
- Colorado's Metrc contract expires in October 2026, and the re-bid has no RFID requirement, so a vendor change is possible. — [MJBizDaily](https://mjbizdaily.com/colorado-marijuana-company-challenging-rfid-tag-requirement/)

**Manufacturing and environmental**
- **TSCA 8(a)(7) PFAS**: a final rule on April 13, 2026 delayed the start of submissions from April 2026 to the **earlier of 60 days after a future amendment's effective date or January 31, 2027**. EPA is still reviewing "thousands of public comments" on amendments that may narrow scope (for example exemptions for articles). — [Federal Register, April 13, 2026](https://www.federalregister.gov/documents/2026/04/13/2026-07062/modification-to-the-start-of-the-submission-period-for-perfluoroalkyl-and-polyfluoroalkyl-substances); [EPA update](https://www.epa.gov/chemicals-under-tsca/update-reporting-deadline-tsca-pfas-reporting-rule); [Stoel Rives](https://www.stoelrivesenvironmentallawblog.com/laws-and-regulations/regulations/epa-again-delays-start-of-tsca-pfas-reporting-now-until-january-2027-at-the-latest/)
- **[SUPERSEDED]** The earlier extension (May 2025) had moved the start to April 2026, with an October 2026 end for most filers. — [Faegre Drinker](https://www.faegredrinker.com/en/insights/publications/2025/5/epa-extends-tsca-8a7-pfas-reporting-to-october-2026)

**HVAC**
- **AIM Act**: the ER&R leak-repair rules took effect January 1, 2026, lowering the threshold to 15 lb and GWP above 53. EPA proposed reconsidering the **Technology Transitions** GWP limits on October 3, 2025, with comments closed November 21, 2025. The outcome was not found. — [EPA fact sheet](https://www.epa.gov/system/files/documents/2026-01/er-r-fact-sheet-leak-repair-2026-01-13_1.pdf); [Hunton: status update](https://www.hunton.com/the-nickel-report/status-update-on-the-aim-act-and-epas-hfc-refrigerant-regulations)

**Agriculture**
- **Pesticide records**: USDA AMS **rescinded** the federal RUP recordkeeping regulations (7 CFR 110) for certified applicators, effective **July 11, 2025**. It skipped notice and comment, and state rules are now the primary standard. The rescission "leaves state rules as the primary standard", which means a patchwork of state requirements. — [Federal Register, May 12, 2025](https://www.federalregister.gov/documents/2025/05/12/2025-08220/rescission-of-recordkeeping-on-restricted-use-pesticides-by-certified-applications); [Illinois Extension](https://extension.illinois.edu/blogs/pesticide-news/2025-05-29-usda-rescinds-federal-restricted-use-pesticide-recordkeeping); [Civil Eats](https://civileats.com/2025/06/03/usda-drops-rules-requiring-farmers-to-record-their-use-of-the-most-toxic-pesticides/)
- EPA's endangered-species pesticide label requirements for 2026 add new mitigation steps at application time. — [Iowa State ICM](https://crops.extension.iastate.edu/post/prepare-now-2026-epa-endangered-species-requirements)
- **H-2A**:
  - An Interim Final Rule (October 2, 2025) moved AEWRs from the USDA Farm Labor Survey to BLS OEWS data, with **two skill levels**. For 2026–27 these average $12.31 (Level I) and $16.07 (Level II).
  - Rates now update each July.
  - ETA-790 job orders must match qualifications to a skill level.
  - The 2024 "Farmworker Protection" rule was **rescinded** (July 2, 2025).
  - EPI estimates farmworker wage losses of $4.4–5.4B a year, and growers want Congress to lock in the change.

  — [AFBF](https://www.fb.org/intel/markets/aewr-changes-for-2026-2027); [Western Growers](https://www.wga.com/news/dol-issues-interim-final-rule-restructuring-h-2a-wages/); [Federal Register rescission](https://www.federalregister.gov/documents/2025/07/02/2025-12315/recission-of-final-rule-improving-protections-for-workers-in-temporary-agricultural-employment-in); [EPI](https://www.epi.org/blog/trumps-new-h-2a-wage-rule-will-radically-cut-the-wages-of-all-farmworkers-new-estimates-show-farmworkers-stand-to-lose-4-4-to-5-4-billion-annually-under-dols-updated-adverse-effec/); [Farm Progress](https://www.farmprogress.com/farm-business/farmers-push-congress-to-lock-in-new-h-2a-wage-rules)

### Inferences
- **Near-term (2026) demand spikes** that a small firm could catch quickly:
  - DQ-file re-audits driven by the non-domiciled CDL rule and English proficiency, for example an ELP-readiness and document checklist;
  - HVAC leak-rate records under ER&R;
  - conversion to the new WH-347 by October 1, 2026;
  - SDS re-collection under HazCom 2024;
  - ELD replacement tracking.
- **Deferred demand**: FSMA 204 (2028) and TSCA PFAS (2027+, scope uncertain). Build later or build light, because customers will postpone buying.
- **Deregulation shifts burden to states**: pesticide records, heat rules and hemp. That creates a "50-state rules engine" need, but also volatility that is risky for a small firm.
- **Cannabis is in flux**: the hemp ban, partial rescheduling and possible Metrc vendor changes. It is high-pain but high-risk for a small generalist firm.

### Gaps
- I could not confirm whether the H-2A IFR has since been finalised, challenged or enjoined in 2026.
- The outcome of EPA's Technology Transitions reconsideration (after comments closed November 2025) was not found.
- I did not confirm whether OSHA has proposed changes to the recordkeeping or electronic-submission rules in 2026. No evidence was found either way beyond the March 2, 2026 filing cycle.
- No FDA front-of-pack or allergen labelling changes for 2025–27 were researched; allergen labelling for sesame and FALCPA is not covered.
- Restaurant health-inspection digitisation by local health departments was not covered.
- Trades licensing: no 2025–27 federal changes were found for electricians. Licensing is state-level and was not surveyed state by state.
