# Practitioner Pain Points in Technology, Security, Privacy and Accessibility Compliance: Software Opportunities for Tempore (as of 25 Sept 2026)

> **Method and source caveats (read first).** Reddit (all subreddits), Hacker News item pages, the HN Algolia API, G2, Capterra, Indie Hackers, FTC.gov, EC digital-strategy, DefenseScoop, Federal News Network, adatitleiii.com, UsableNet's blog and most law-firm and vendor blogs were **blocked by this environment's egress proxy**, so I could not open them directly. The session's WebSearch budget also ran out partway through. Many findings below therefore come from **search-result snippets and summaries**, not full-page reads. They are attributed to the URL the snippet came from and should be spot-checked before anyone quotes them verbatim in a publication. Items marked **[verified]** were confirmed by fetching the primary page (developer.apple.com). A number of the "review aggregation" sources (complyjet.com, soc2auditors.org, smartsuite.com, sprinto.com, 6clicks.com, TestParty, cyberbase.ai, DataGrail) are **vendors or competitors**, so they have commercial bias. I flag this where it matters. I found no direct Reddit quotes because Reddit is blocked to the search tool's user agent as well.

---

## Q1. Which compliance tasks do practitioners describe as the biggest time sinks, most manual, or most anxiety-inducing? What time and cost figures do they cite?

### Takeaway
The recurring time sinks are:
1. **Security questionnaires and vendor-risk reviews.** These run to hundreds of questions each and 5–15 a month at growth stage.
2. **Getting ready for a SOC 2 / ISO 27001 audit and collecting evidence for it.** Year one costs $20k–$80k+.
3. **Handling DSARs (data subject access requests) by hand.** This costs about $1.5k per request, and volumes are up 43% year over year.
4. **Remediating accessibility under legal threat.** More than 3,100 federal website lawsuits were filed in 2025.
5. **For defense subcontractors, CMMC Level 2 preparation.** Assessments alone are estimated at $75k–$150k+.

What makes these tasks stressful is that they are **deal-blocking** (a purchase order depends on them) or **litigation-driven** (a demand letter has arrived).

### Cited Findings

**SOC 2 / ISO 27001 cost and effort**
- Startups should budget "$20,000 to $80,000+ all-in for their first year of SOC 2", covering auditor fees, tooling and remediation. Audit fees are usually $10k–$50k, and Big Four firms charge low six figures. — [Vanta (vendor)](https://www.vanta.com/collection/soc-2/soc-2-audit-cost); [Workstreet](https://www.workstreet.com/blog/soc-2-audit-cost)
- "Big 4 auditors like Deloitte/PwC will charge $60k+ for an audit, while specialized boutique firms will do it for $25k." — search summary of [soc2auditors.org](https://soc2auditors.org/insights/soc-2-compliance-for-startups/)
- Readiness assessments cost $10k–15k on top of the audit. — [soc2auditors.org](https://soc2auditors.org/insights/vanta-alternatives/) (search summary)
- A solo founder asked HN how to get SOC 2 Type 2 as a one-person company (2026). Commenters said a Type 2 is "another ~$10k outlay", renewed every 6–12 months, and that platforms "like Drata, Vanta and HeyLaika you pay for separately (approx $15k annual)". The advice was to wait until "a purchase order is made contingent on your SOC2 Type I attestation, where the revenue from that purchase order more than pays for the attestation". A cheaper alternative some suggested was a CSA CAIQ self-assessment published to the STAR Registry. — [Ask HN: How to be SOC2 Type 2 compliant as a solo-entrepreneur?](https://news.ycombinator.com/item?id=48145524) (snippet only; the page itself was blocked)
- A related HN comment from the same period: "Not possible in case your clients are not stupid. Any company with SOC2 and <5 p..." (truncated). This suggests buyers are sceptical of SOC 2 at micro-companies. — [HN item 48145762](https://news.ycombinator.com/item?id=48145762)
- A long-running HN theme is that screenshot-based evidence collection is the core pain: "SOC2: The screenshots will continue until security improves". — [HN 32018066](https://news.ycombinator.com/item?id=32018066) (older thread, ~2022, but the theme persists)
- A Vanta cofounder on HN said most customers "come with a deal on the line" and that the process can be started "just in time". This confirms SOC 2 is bought reactively, under sales pressure. — [HN 29099691](https://news.ycombinator.com/item?id=29099691) (2021; older)

**Security questionnaires and vendor risk assessments**
- A typical questionnaire takes 2–4 hours. Complex ones take days or weeks, and "some organizations report spending up to 30 business days on a single questionnaire". Many have 200–300 questions. — [Vendict (vendor)](https://vendict.com/blog/50-essential-security-questionnaire-questions); [ResponseHub (vendor)](https://responsehub.ai/blog/security-questionnaire-cross-functional/) (search summary)
- "SaaS companies selling to enterprise buyers in regulated industries can expect 5 to 15 questionnaires per month once they reach growth stage." Questionnaires plus DDQs "quietly burn 200+ engineering hours per quarter". — [Tribble (vendor)](https://tribble.ai/blog/security-questionnaire-automation/); [cyberbase.ai (vendor)](https://www.cyberbase.ai/blog/why-security-questionnaires-are-getting-longer) (vendor claims; treat as directional)
- A "2025 Forrester study" is cited as saying AI tools cut completion time "from 14 days to under 48 hours". This is a vendor citation and I could not verify the underlying Forrester study. — [compyl.com](https://compyl.com/blog/security-questionnaire-automation/) (search summary)
- Classic HN threads on questionnaires: "Our Dumb Security Questionnaire" ([HN 25793230](https://news.ycombinator.com/item?id=25793230)); "Ask HN: How small startups deal with long security questionnaires from clients?" ([HN 36488436](https://news.ycombinator.com/item?id=36488436), 2023); "Could I email you a Vendor Security Questionnaire…" ([HN 18125993](https://news.ycombinator.com/item?id=18125993), 2018). The questionnaires "arrive at the worst moment: a startup's first enterprise deal, when the team is small and nobody owns compliance, with hundreds of rows of questions where every honest answer feels costly." — [MatrixGard](https://matrixgard.com/blog/security-questionnaire-gauntlet-lean-teams-2026/) (search summary). Common advice: "if a prospect sends a 400-question assessment for a $500/month deal, you should push back". — [buildmvpfast.com](https://www.buildmvpfast.com/blog/vendor-security-questionnaires-startup-guide-2026)
- On the receiving side, the Delve scandal (below) is pushing vendor-management teams to scrutinise SOC 2 reports rather than accept them at face value. This *adds* review work for buyers. — [Workplace Privacy Report (law firm blog), May 2026](https://www.workplaceprivacyreport.com/2026/05/articles/governance-risk-and-compliance-2/the-delve-scandal-why-a-soc-2-report-cant-be-a-check-the-box-exercise-for-vendor-management/); [Whistic (vendor)](https://www.whistic.com/resources/blog/your-vendor-has-a-soc-2-report-now-what)

**DSARs and privacy operations**
- DataGrail's 2025 Data Privacy Trends Report found:
  - DSAR volume rose 43% from 2023 to 2024; a mid-sized company went from about 600 to about 860 requests.
  - Deletion requests are now 56% of DSARs, up 82% YoY.
  - Manual handling costs **$1,524 per request**.
  - The estimated total is **$1.26M a year per 5M unique visitors**, and "upwards of $1.5 million annually" for a mid-sized organisation (using Gartner's estimate of manual cost).
  - DataGrail is a vendor, so the figures are self-interested but quantified. — [DataGrail press release](https://www.datagrail.io/press/datagrail-report-consumer-demand-for-data-privacy-surges-driving-up-business-costs-as-data-deletion-requests-rise/); [DataGrail $1.5M DSR problem](https://www.datagrail.io/blog/data-privacy/the-1-5m-dsr-problem-what-datagrails-research-found/)
- 20 US states have comprehensive privacy laws in effect in 2026. Indiana, Kentucky and Rhode Island took effect on 1 Jan 2026, and each "brings unique requirements":
  - Kentucky has a permanent cure period and no universal opt-out.
  - Rhode Island requires data protection assessments for high-risk processing.
  - Indiana's threshold is 100k residents. — [MultiState](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026); [TrustArc](https://trustarc.com/resource/new-in-2026-state-privacy-laws-in-indiana-kentucky-and-rhode-island/); [IAPP](https://iapp.org/news/a/new-year-new-rules-us-state-privacy-requirements-coming-online-as-2026-begins)

**Accessibility**
- Seyfarth Shaw counts **3,117 federal website accessibility lawsuits in 2025, up 27% from 2,452 in 2024**. — [ADA Title III blog (Seyfarth), Mar 2026](https://www.adatitleiii.com/2026/03/federal-court-website-accessibility-lawsuit-filings-bounce-back-in-2025/) (search summary)
- UsableNet counts "more than 5,000 digital accessibility lawsuits" across federal and key state courts in 2025, covering websites and mobile apps. 1,427 of them targeted companies that had already been sued. Repeat defendants made up about 46% of federal cases. — [UsableNet 2026 trends](https://blog.usablenet.com/ada-web-lawsuit-trends-2026); [UsableNet 2025 midyear](https://blog.usablenet.com/2025-midyear-accessibility-lawsuit-report-key-legal-trends) (search summary; UsableNet is a vendor)
- Small-business owners who try to comply "quickly realize there are no clear guidelines or specific steps, and compliance can be subjective". — [JD Supra demand-letter topic page](https://www.jdsupra.com/topics/website-accessibility/demand-letter) (search summary)

**CMMC**
- Phase 1 started on **10 Nov 2025**. From then, Level 1 and Level 2 self-assessments became a condition of award for new contracts with a CMMC requirement, and a limited number of contracts could require a Level 2 C3PAO assessment. — [Dorsey](https://www.dorsey.com/newsresources/publications/client-alerts/2025/11/cmmc); [DefenseScoop](https://defensescoop.com/2025/11/10/cmmc-compliance-dod-enforcement-defense-industry-readiness-gaps/) (headline: "readiness gaps remain")
- Level 2 assessment fees are projected at **$75,000–$150,000+** by late 2026. This excludes remediation such as GCC High, MSSP fees and documentation. — search summary citing industry analysts (source page not identified; see Gaps)
- The SBA Office of Advocacy warned in 2024 that the rules would "force small businesses out of the defense industrial base". — [CMMC.com (vendor)](https://www.cmmc.com/newsroom/how-does-cmmc-impact-small-businesses); [Coalition for Government Procurement](https://thecgp.org/what-federal-contractors-need-to-know-about-cmmc/) (search summary)

### Inferences
- The most painful jobs share one shape: **the same facts get re-entered in many formats**. Security posture goes into questionnaires in SIG, CAIQ and custom spreadsheets. Data inventories go into DSAR responses, privacy labels, COPPA notices and state-law disclosures. Control evidence goes to SOC 2, ISO and CMMC. Software that captures facts once and renders them many ways is the common opportunity.
- Anxiety peaks when a **deadline comes from outside**: a PO contingent on SOC 2, a demand letter, a DoD solicitation, or a 24-hour CRA report. Tools that shorten time-to-first-artifact (a trust page, a VPAT/ACR, an SSP, a first report) are likely to sell better than "continuous compliance" dashboards.

### Gaps
- I could not retrieve Reddit threads (r/cybersecurity, r/sysadmin, r/SaaS, r/CMMC, r/gdpr, r/accessibility etc.). All reddit.com access was blocked to both search and fetch. **I have no Reddit quotes.**
- I found no independent (non-vendor) survey of hours spent on security questionnaires. All the figures above come from vendors selling questionnaire automation.
- I could not identify the original source of the $75k–$150k CMMC Level 2 figure. DoD's own regulatory impact estimates were not retrieved.

---

## Q2. What do practitioners say about incumbent tools (price, lock-in, auditor quality, false sense of security, integrations)?

### Takeaway
The criticisms of compliance-automation platforms (Vanta, Drata, Secureframe, Sprinto, Thoropass) fall into five groups:
- high price for pre-revenue companies
- renewal price hikes of about 20–40%
- add-on upselling
- noisy false-positive tests and too few ways to record exceptions
- the "checkbox" critique that they prove controls *exist* rather than *work*

The **Delve scandal (March–April 2026)** made the "checkbox" critique concrete: hundreds of near-identical SOC 2 reports, rubber-stamped by affiliated audit mills. Trust in fast, cheap automated compliance has collapsed. Accessibility overlays (accessiBe and others) face a parallel backlash, including the **FTC's $1M order against accessiBe (Jan/Apr 2025)**.

### Cited Findings

**Compliance-automation platforms (Vanta, Drata etc.)**
- Vanta reviews (AWS Marketplace and G2, via search summary):
  - "To some extent it feels like just checking boxes rather than making sure you're actually set up to succeed, and it's easy to get 'stuck'."
  - "For a pre-revenue startup it is a bit expensive."
  - Manual processes remain: "creating policy documents that are not automatically integrated into controls". — [AWS Marketplace Vanta reviews](https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-5ophamrbfxt44)
- Vanta G2 dislikes:
  - Integrations surface "systems, vendors, or issues that are irrelevant—basically false positives—that must be explained away on each sync".
  - "Limited flexibility can create false positives such as users being flagged as improperly offboarded when a valid special case applies."
  - Alerts are "overwhelming at times".
  - Vanta "often lacks simple options for handling exceptions, and newly discovered vendors require constant review".
  - Sources: [G2 Vanta reviews](https://www.g2.com/products/vanta/reviews); [6clicks (competitor)](https://www.6clicks.com/resources/blog/understanding-vantas-limitations-insights-from-real-user-experiences); [Sprinto (competitor)](https://sprinto.com/blog/vanta-review/) (search summaries)
- Vanta pricing: about $10k–12k a year for one framework under 50 employees, with a **median contract of about $20k a year**, according to "verified purchase data". — [complyjet (competitor)](https://www.complyjet.com/blog/vanta-pricing-guide-2025); [soc2auditors.org](https://soc2auditors.org/insights/vanta-review/) (search summary; underlying purchase data not visible)
- Drata G2 and Reddit complaints:
  - "Prices often rise 20–40% at renewal without major feature changes."
  - One case of a 10% uplift that Drata offered to waive for a multi-year commitment.
  - Trust Center Pro, User Access Reviews and Multi-Entity are sold as add-ons.
  - Integration gaps, for example "integration with Linear was supported, but submitting Linear tickets as evidence is not possible".
  - Despite this, Drata is rated 4.8/5 on 1,000+ G2 reviews. — [G2 Drata pros/cons](https://www.g2.com/products/drata/reviews?qs=pros-and-cons); [complyjet Drata pricing (competitor)](https://www.complyjet.com/blog/drata-pricing-plans); [smartsuite (competitor)](https://www.smartsuite.com/blog/drata-pricing?338ea48f_page=8) (search summaries)
- The structural critique, as summarised in search results: platforms like Vanta and Drata "were designed for one job: to prove that you have a control, but were not designed to verify that the control actually stops anything." — surfaced in search summary (vendor-comparison sites; e.g. [strac.io](https://www.strac.io/blog/soc-2-compliance-software))

**HN views on auditors**
- "Auditors themselves pretty much only care that you answered all questions, they don't really care what the answers are and absolutely aren't going to dig any deeper."
- "SOC2 is mainly to check boxes, and forces you to think about a few things." — [HN 46142956](https://news.ycombinator.com/item?id=46142956)
- A counterpoint on the same themes: "80% box checking but that doesn't make it performative… the box checking is here so that the dude who checked the box become legally responsible". — HN threads surfaced in search ([HN 46142956](https://news.ycombinator.com/item?id=46142956), [HN 44362720](https://news.ycombinator.com/item?id=44362720)). The snippet attributions are approximate.

**Delve scandal (March–April 2026)**
- The story broke through an anonymous Substack, "DeepDelver", with "Delve – Fake Compliance as a Service – Part I", around 18–20 March 2026. — [DeepDelver Substack Part II](https://deepdelver.substack.com/p/192144506); [HN discussion "Delve – Fake Compliance as a Service"](https://news.ycombinator.com/item?id=47444319)
- The allegations:
  - pre-generated auditor conclusions
  - templated reports: of 494 leaked SOC 2 reports and 81 ISO 27001 registration forms, the text was "99.8% identical", "down to the same typo"
  - 99%+ of audits routed through two affiliated firms, Accorp and Gradient, described as "Indian certification mills operating through U.S. shell structures"
  - fabricated evidence
- Delve had raised $32M at a $300M valuation. — [Captain Compliance](https://captaincompliance.com/news/the-delve-scandal-fake-soc-2-audits-open-source-code-theft-and-exit-from-y-combinator/); [ComplianceHub.Wiki](https://compliancehub.wiki/delve-compliance-startup-fake-soc2-audit-scandal/); [licens.io](https://licens.io/blog/delve-fake-compliance-soc2-fraud/) (search summaries)
- Around 3 April 2026, **Y Combinator removed Delve from its directory and asked the founders to leave**. Delve denies the claims and says independent auditors issue the opinions. — [Captain Compliance](https://captaincompliance.com/news/the-delve-scandal-fake-soc-2-audits-open-source-code-theft-and-exit-from-y-combinator/); [IANS Research, 19 Apr 2026](https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/19/delve-allegations-expose-weak-points-in-modern-compliance)
- **Scale is disputed across sources.** "Delve sold fake SOC 2 reports to 1,700 companies" (search summary), versus 494 leaked reports, versus "533 fake reports" (HN headline). Treat the 1,700 figure as unverified.
- LiteLLM (an open-source AI gateway, ~95–97M downloads/month) showed SOC 2 and ISO 27001 badges obtained through Delve. It was compromised in a supply-chain attack linked to the Mercor breach (confirmed 31 Mar 2026; about 4TB of data, 40k+ contractors' data exposed). HN thread: "97M downloads, $0 real auditing: LiteLLM's SOC 2 was one of 533 fake reports". — [HN 47506938](https://news.ycombinator.com/item?id=47506938); [Strike Graph (vendor)](https://www.strikegraph.com/blog/the-mercor-breach-exposed-silicon-valleys-fragile-ai-supply-chain?hs_amp=true) (search summaries)
- Commentary headlines: "SOC 2 Is Broken. The Delve Scandal Is Showing Us How." — [Corporate Compliance Insights](https://www.corporatecomplianceinsights.com/soc-2-broken-delve-scandal-shows/). Also "compliance broken, performative GRC". — [agnivault Substack](https://agnivault.substack.com/p/compliance-broken-performative-grc)

**Accessibility overlays**
- The FTC announced on 3 Jan 2025, and finalised in April 2025, a $1M order against accessiBe. It had claimed accessWidget would "[a]utomatically comply" with WCAG 2.1 AA, and it had formatted paid reviews as independent. The order bars claims that automated products make any site WCAG-compliant without evidence. The settlement was non-admission. — [FTC Jan 2025](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-order-requires-online-marketer-pay-1-million-deceptive-claims-its-ai-product-could-make-websites); [FTC final order Apr 2025](https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-approves-final-order-requiring-accessibe-pay-1-million); [Lainey Feingold](https://www.lflegal.com/2025/01/ftc-accessibe-million-dollar-fine/)
- Overlays "fail to address the actual code-level accessibility issues" and give "a false sense of security". A growing share of suits targets sites that already run widgets. — [UsableNet (vendor)](https://blog.usablenet.com/2025-midyear-accessibility-lawsuit-report-key-legal-trends); [JD Supra](https://www.jdsupra.com/topics/website-accessibility/demand-letter) (search summaries)
- An accessibility company sued an accessibility advocate. This is a sign of how hostile the overlay debate has become. — [SBLTN Lab Notes 049](https://sbltn.substack.com/p/049) (headline only)

**App-store privacy labels (tooling gap rather than tool dislike)**
- Research found that 88% of apps had at least one discrepancy between their privacy policy and their label. At least 16% sent data to third parties without disclosing it on the label. Developers were "confused about the terminology" and found Apple's documentation "ambiguous", and **third-party SDK collection they were unaware of** is the main cause. — [ACM CHI EA 2022 study](https://dl.acm.org/doi/fullHtml/10.1145/3491101.3519739) (older; ~2022); [CACM opinion](https://cacm.acm.org/opinion/mobile-app-privacy-nutrition-labels-missing-key-ingredients-for-success)

### Inferences
- **The post-Delve trust gap is a real opening.** Buyers now distrust cheap, fast SOC 2 reports, and vendors need ways to show *real* evidence. Products that deliver verifiable, tamper-evident evidence (signed, timestamped control telemetry that customers can view directly), or that help buyers triage vendor reports (auditor legitimacy, templated-report detection), are timely and small enough for a boutique firm to build.
- Incumbents are strongest at breadth of integrations (Vanta 400+, Drata 300+). A small firm should not try to beat them there. Weaker spots worth targeting: exception handling and false-positive workflow, pricing for companies under 10 employees, and "bring your own auditor" portability.
- The overlay backlash, combined with the FTC order, leaves room for **honest, developer-centred accessibility tooling**: CI linting, component-level fixes, and remediation tracking tied to real code. These must avoid any "automatic compliance" claims, which the FTC order has made legally risky.

### Gaps
- I could not open G2 or Capterra pages directly. The review quotes are search-engine summaries and may merge several reviews. No verified quotes on Secureframe, Sprinto or Thoropass were obtained.
- I found no practitioner commentary on how Vanta, Drata and the others responded commercially after Delve (price cuts, auditor-network changes).

---

## Q3. Where do small companies and solo developers say nothing affordable or simple exists?

### Takeaway
The clearest "nothing fits" signals are:
- SOC 2 for companies of 1–10 people, where a platform plus audit costs ~$25k+ a year against tiny ACVs
- security questionnaires for startups with no dedicated security staff
- accessibility for small businesses facing demand letters, whose only cheap option (overlays) is discredited
- small defense subcontractors facing CMMC
- mobile developers who cannot accurately fill in privacy labels, Data Safety forms, or the new age-assurance API requirements

### Cited Findings
- **SOC 2 for solo founders:** the HN Ask thread (2026) shows that the minimum realistic stack costs ~$15k a year for a platform plus ~$10k per audit. The advice is effectively "don't, until a PO pays for it", or to self-publish a CSA CAIQ. — [HN 48145524](https://news.ycombinator.com/item?id=48145524); [Indie Hackers "SOC2 as a solo founder"](https://www.indiehackers.com/post/soc2-as-a-solo-founder-868b173ed4) (fetch blocked; title only)
- The "pre-revenue startup" price complaint about Vanta. — [AWS Marketplace reviews](https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-5ophamrbfxt44)
- Questionnaire tools (Conveyor, Vendict, Tribble, ResponseHub, cyberbase.ai) are mostly aimed at growth-stage companies handling 5–15 questionnaires a month. Early startups get "hundreds of rows" with "nobody [who] owns compliance". — [MatrixGard](https://matrixgard.com/blog/security-questionnaire-gauntlet-lean-teams-2026/); [Conveyor](https://www.conveyor.com/products/security-questionnaire-automation)
- **CMMC:** the SBA Office of Advocacy said the rules could push small firms out of the defense industrial base, and industry leaders noted that DoD "did not address all comments and concerns from small businesses". — [CMMC.com](https://www.cmmc.com/newsroom/how-does-cmmc-impact-small-businesses) (search summary)
- **EAA microenterprise confusion:** "many online retailers relaxed believing they were exempt, but the exemptions are narrower than most assume". The exemption covers only *service*-providing microenterprises (fewer than 10 staff and ≤€2M turnover), not product manufacturers. B2B-only services are out of scope. Organisations "still struggle to understand how to interpret" the Act "in the absence of guidance from both the EU and its Member States". — [Taylor Wessing](https://www.taylorwessing.com/en/interface/2025/accessibility/key-eu-accessibility-act-exemptions-and-the-challenges-they-pose); [XICTRON](https://www.xictron.com/en/blog/accessibility-act-exemptions-microenterprises-2026/); [Kris Rivenburgh](https://krisrivenburgh.com/microenterprises-exempt-eaa-requirements/) (search summaries)
- **Cookie consent for small sites:** HN threads keep circling back to confusion over when a banner is legally needed (ePrivacy vs GDPR, "strictly necessary" cookies, first-party analytics). A "developer-first cookie banner" Show HN shows demand for lightweight alternatives to enterprise CMPs. — [HN 46521179 "Most websites don't need cookie consent banners"](https://news.ycombinator.com/item?id=46521179); [HN 25458567](https://news.ycombinator.com/item?id=25458567); [HN 44879661 "Consent – The Developer-First Cookie Banner"](https://news.ycombinator.com/item?id=44879661); [HN 45668748 (DataGrail consent lead dev)](https://news.ycombinator.com/item?id=45668748)
- **App privacy labels / Data Safety:** developers under-report SDK data collection because they do not know what their SDKs collect. Common mistakes include confusing "processing" with "sharing" and marking collection "optional" when users cannot opt out. — [ACM study](https://dl.acm.org/doi/fullHtml/10.1145/3491101.3519739); [legalpolicygen.com](https://legalpolicygen.com/blog/app-store-privacy-labels-ios-google-play-2026)
- **CRA and SBOM for small developers:** academic work shows SBOM generators disagree and have gaps in accuracy and coverage. "SBOM producers can plausibly attribute missing components to tool limitations". — [arXiv 2606.13966 "Software Dark Matter"](https://arxiv.org/pdf/2606.13966); [arXiv 2601.05622 "Adherence Gap between Standards and Tools in SBOM"](https://arxiv.org/pdf/2601.05622); [arXiv 2502.03975 SBOM challenges from Stack Overflow](https://arxiv.org/pdf/2502.03975). HN discussions: [Greg Kroah-Hartman explains the CRA for OSS developers](https://news.ycombinator.com/item?id=45447776); [CRA brief guide for OSS developers](https://news.ycombinator.com/item?id=44561400)

### Inferences — Tempore addressability assessment

The table rates each gap on fit for a small web, mobile and desktop app studio. It covers competition and whether the product can be built without regulated status (for example, it does not need to *be* an auditor or C3PAO).

| Gap | Tempore fit | Rationale |
|---|---|---|
| **Security questionnaire answer library for companies under 20 people** (import SIG/CAIQ/Excel, reuse answers, LLM draft grounded in the company's own policies, export) | **High** | A well-scoped web app with a crowded top end but an under-served cheap end. Needs no auditor relationships. Risk: incumbents bundle it. |
| **Public trust page / trust center generator** (policies, sub-processors, evidence snapshots) for micro-SaaS | **High** | Simple web product. After Delve, adding *verifiable* evidence (signed config snapshots) is a differentiator. |
| **"Real evidence" SOC 2 lite**: CLI or desktop agent collecting timestamped, signed evidence (MFA, disk encryption, backups) that the customer can share directly | **Medium** | Buildable, but it competes with Vanta and Drata agents. Its value depends on auditors accepting it. |
| **Vendor-report triage for buyers** (flag templated or suspect SOC 2 reports, track auditor firms, map to questionnaire) | **Medium** | New post-Delve need. Requires data on auditors. Liability considerations. |
| **Accessibility CI and remediation tracker** (axe-based linting, VPAT/ACR generator, demand-letter response workflow, EAA accessibility statement generator) | **High** | Tempore already builds web and mobile apps and can pair a tool with services. Must avoid "auto-compliance" claims (FTC/accessiBe). |
| **DSAR intake and workflow for SMBs** (form, identity verification, data-map checklist, deadline clocks per state/GDPR) | **Medium–High** | Incumbents (DataGrail, OneTrust, Transcend) target the mid-market and enterprise. A simple SMB workflow is buildable. The 20-state patchwork needs rules maintenance. |
| **Mobile privacy-label / Data Safety generator from SDK scan** (static analysis of Podfile/Gradle/SPM mapped to Apple and Google label fields, plus COPPA third-party-disclosure checklist) | **High** | Directly within Tempore's mobile expertise. Evidence of the problem is strong (88% discrepancy). |
| **Age-assurance integration kit** (Apple Declared Age Range, PermissionKit Significant Change, StoreKit ageRatingCode, server notifications for consent revocation; Google equivalents) | **High (services + SDK)** | Texas SB2420 took effect 4 Jun 2026 and Utah and Louisiana are also active. Every app developer must wire this up. A good fit for consulting plus a reusable library. |
| **CRA 24h/72h vulnerability-reporting workflow + SBOM-diff for small manufacturers** | **Medium** | Reporting started 11 Sep 2026. Needs a SBOM → vulnerability → "actively exploited" (e.g. KEV) → ENISA single reporting platform workflow. Incumbents (Anchore, Snyk, Cycode) are enterprise-focused. |
| **CMMC for small subcontractors** (SSP/POA&M authoring, SPRS score calculator, evidence binder) | **Low–Medium** | Real pain, but the market needs FedRAMP/GCC-High awareness and an MSP channel, and program uncertainty (Phase 2 suspended) dampens demand. |
| **EU AI Act / Colorado ADMT notice and inventory tool** | **Low–Medium (for now)** | The deadlines slipped (Dec 2027 / Aug 2028; Colorado reset to Jan 2027). Demand is speculative until 2027. |

### Gaps
- There is no direct evidence (because Reddit and Indie Hackers were blocked) of what solo developers say they would pay for these tools. Willingness to pay remains unvalidated.
- I found no practitioner data on EAA enforcement actions against small firms since June 2025.

---

## Q4. What recent or upcoming regulatory changes (2025–2027) are creating new pain?

### Takeaway
The 2025–2026 period brought a wave of deadlines, and several of them were then **delayed or reset**. That creates "compliance whiplash" costs: work done for a date that then moves.

**Active now (Sept 2026):**
- EAA (since 28 Jun 2025)
- amended COPPA (full compliance 22 Apr 2026)
- Texas SB2420 app-store age assurance (in effect 4 Jun 2026 after the Fifth Circuit stay)
- CRA vulnerability reporting (11 Sep 2026)
- 20 US state privacy laws
- CMMC Phase 1 (10 Nov 2025)

**Delayed or reset:**
- ADA Title II web rule: deadline moved to **Apr 2027 / Apr 2028**
- EU AI Act high-risk obligations: moved to **2 Dec 2027 / 2 Aug 2028**
- Colorado AI Act: **repealed and replaced**, new framework effective 1 Jan 2027
- CMMC **Phase 2 suspended** (13 Jul 2026)

### Cited Findings

**CMMC 2.0**
- Phase 1 took effect on 10 Nov 2025 (Level 1/2 self-assessments as a condition of award; some Level 2 C3PAO assessments). — [Dorsey](https://www.dorsey.com/newsresources/publications/client-alerts/2025/11/cmmc); [Secureframe](https://secureframe.com/blog/cmmc-deadline-announcement)
- **NEW / supersedes the brief:** DoD **suspended Phase 2** on **13 July 2026**. Phase 2 had been scheduled for 10 Nov 2026 and would have made C3PAO certification mandatory for Level 2. DoD also stood up a **CMMC Reform Task Force** to review the program. — [Federal News Network, Jul 2026](https://federalnewsnetwork.com/cybersecurity/2026/07/pentagon-suspends-cmmc-phase-two-requirements-launches-review-of-program/); [FCA Counsel blog](https://www.fcacounsel.com/blog/dod-cmmc-level-2-pause); [Cabrillo Club](https://cabrilloclub.com/insights/cmmc-timeline-2026-key-dates) (search summaries; page fetch blocked)

**ADA Title II (public entities)**
- DOJ published an **Interim Final Rule on 20 April 2026**, four days before the original deadline of 24 April 2026. It extends the deadlines by one year: entities serving 50k+ people now have until **26 April 2027**, and smaller entities until **26 April 2028**. The standard stays WCAG 2.1 AA. DOJ "fully anticipates implementing the regulation at the new deadline". Underlying Title II obligations and private lawsuits continue. — [Federal Register 2026-07663](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web); [Duane Morris](https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html); [SBA Office of Advocacy](https://advocacy.sba.gov/2026/04/27/doj-extends-compliance-dates-for-state-and-local-governments-to-make-their-websites-accessible/)
- A separate **HHS Section 504 digital-accessibility deadline (May 2026)** still applied to HHS-funded entities. — [Jackson Lewis](https://www.jacksonlewis.com/insights/doj-extends-public-entities-compliance-deadline-ada-related-website-accessibility-hhss-may-2026-deadline-still-looms)
- Disability groups (AAPD, ACB) objected to the delay. — [AAPD statement](https://www.aapd.com/aapd-statement-title-ii-doj-web-rule-ifr/); [ACB](https://www.acb.org/notice-title-ii-interim-final-rule-publication-april-20-2026)

**European Accessibility Act**
- Enforceable from 28 June 2025. The microenterprise exemption applies to services only, and B2B-only services are out of scope. Guidance from the EU and member states is thin. — [Travers Smith](https://www.traverssmith.com/knowledge/knowledge-container/a-new-milestone-for-accessibility-the-european-accessibility-act-now-applies/); [Taylor Wessing](https://www.taylorwessing.com/en/interface/2025/accessibility/key-eu-accessibility-act-exemptions-and-the-challenges-they-pose)

**Accessibility litigation (US private sector)**
- 3,117 federal website suits in 2025 (+27%), per Seyfarth. UsableNet counts 5,000+ including state courts. — see Q1 citations

**EU AI Act**
- GPAI obligations applied from 2 Aug 2025 (per the original Act timeline; not re-verified in this session).
- The Commission's **Digital Omnibus on AI** (19 Nov 2025) proposed deferring high-risk obligations. The trilogue failed on 28 Apr 2026, reached **provisional agreement on 6 May 2026**, and was confirmed by the Council on 13 May.
- The final regulation is **Regulation (EU) 2026/1744**, published in the OJ on 24 July 2026 and in force from 27 July 2026:
  - Annex III stand-alone high-risk systems (recruitment, credit, education etc.) now apply from **2 Dec 2027**.
  - Annex I product-embedded AI applies from **2 Aug 2028**. — [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/); [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/); [DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act); [ComplianceHub.Wiki](https://compliancehub.wiki/eu-digital-omnibus-ai-act-deadline-deferral-annex-iii-2027/) (search summaries)

**US state AI laws**
- **Colorado:**
  - SB 25B-004 (signed 28 Aug 2025) delayed SB 24-205 from 1 Feb 2026 to 30 Jun 2026.
  - A federal court then **paused enforcement on 27 Apr 2026**.
  - **SB 26-189 (signed 14 May 2026) repealed SB 24-205** and replaced it with a narrower notice- and rights-based automated decision-making technology (ADMT) framework, **effective 1 Jan 2027**.
  - Sources: [McDermott](https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/); [Carpe Datum Law](https://www.carpedatumlaw.com/2026/05/colorados-ai-reset-two-weeks-a-white-house-callout-and-a-pivot-away-from-the-eu-model/); [Troutman](https://www.troutmanprivacy.com/2026/04/colorado-attorney-general-delays-enforcement-of-colorado-ai-act/); [Akin](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205)
- **NYC Local Law 144 (AEDT):** I could not research this because the search budget was exhausted. See Gaps.

**EU Cyber Resilience Act**
- Article 14 reporting obligations apply from **11 September 2026**, ahead of the main obligations on 11 Dec 2027. The timeline for actively exploited vulnerabilities and severe incidents:
  - an early warning within **24h**
  - a full notification within **72h**
  - a final report within **14 days** of a fix being available (vulnerabilities), or within one month (severe incidents)
- Open-source stewards' reporting duties start on 11 Dec 2027.
- ENISA has launched the CRA Single Reporting Platform.
- Commission guidance includes "67 practical examples" aimed at SMEs. — [EC CRA reporting](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting); [ENISA SRP launch](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched); [EC guidance](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation); [HeroDevs (vendor) on EOL dependencies](https://www.herodevs.com/blog-posts/cra-reporting-obligations-start-september-2026-what-eol-dependencies-mean-for-your-compliance)

**Children's privacy and age assurance**
- **COPPA amendments:** published 22 Apr 2025, effective 23 Jun 2025, **full compliance required by 22 Apr 2026**. New obligations include:
  - separate verifiable parental consent for third-party disclosures that are not integral to the service
  - a **written children's information security program**
  - annual risk assessments
  - written assurances from third parties
- The FTC has signalled COPPA as an enforcement priority. — [Federal Register](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule); [Davis Polk](https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect); [Finnegan](https://www.finnegan.com/en/insights/articles/coppas-amended-rule-is-now-in-full-effect-what-operators-need-to-know.html); [IAPP](https://iapp.org/news/a/top-5-impacts-of-the-new-coppa-rule)
- **Texas SB2420 (App Store Accountability Act):**
  - A district court preliminary injunction was issued on 23 Dec 2025, and Apple paused its implementation. **[verified]** — [Apple Developer news](https://developer.apple.com/news/?id=8jzbigf4)
  - The Fifth Circuit stayed the injunction on 1 Jun 2026. **Apple announced on 3 Jun 2026 that the law is in effect from 4 Jun 2026** for new Texas accounts. It requires age assurance and parental consent for under-18 downloads, IAP and "significant changes", and parents can revoke consent. **[verified]** — [Apple Developer news 3 Jun 2026](https://developer.apple.com/news/?id=sg176nne); [AppleInsider](https://appleinsider.com/articles/26/06/03/age-verification-now-mandatory-for-app-store-users-in-texas); [MoFo](https://www.mofo.com/resources/insights/251111-texas-targets-app-stores-with-new-accountability-law)
  - Developers are expected to implement:
    - the **Declared Age Range API**
    - the **Significant Change API (PermissionKit)**
    - the **StoreKit ageRatingCode**
    - **App Store Server Notifications** for consent revocation **[verified]**
  - Age data may be used only for age enforcement and compliance, and must be deleted after verification. — [Texas Policy Research](https://www.texaspolicyresearch.com/federal-court-blocks-texas-app-store-accountability-act/); [McDermott](https://www.mcdermottlaw.com/insights/app-store-accountability-acts/)
  - Apple's December 2025 note said the same tools support **Utah and Louisiana laws (effective 2026)**. **[verified]** — [Apple Developer](https://developer.apple.com/news/?id=8jzbigf4)

**Platform policy (Android)**
- Google's **Android developer verification** program requires developers to verify their identity with Google (government ID, $25 fee, registered package names), including for **sideloaded apps**:
  - Enforcement starts **September 2026** in Brazil, Indonesia, Singapore and Thailand.
  - There is a limited free tier for students and hobbyists.
  - F-Droid called it an "existential threat": "Android… is to become a locked-down platform, requiring that developers everywhere register centrally with Google".
  - Sources: [Android Developer Console Help](https://support.google.com/android-developer-console/answer/16561738?hl=en); [Median.co](https://median.co/blog/android-developer-verification-2026); [Testers Community](https://www.testerscommunity.com/blog/android-developer-verification-2026); [AdGuard](https://adguard.com/en/blog/android-play-store-verification-sideloading.html)
  - Sources disagree on the start date ("starting March 2026" vs regional enforcement from Sept 2026). The March date likely refers to registration opening.

**US state privacy patchwork**
- 20 states have comprehensive laws in effect. Indiana, Kentucky and Rhode Island were added on 1 Jan 2026, alongside amendments to existing laws. — [MultiState](https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026); [IAPP](https://iapp.org/news/a/new-year-new-rules-us-state-privacy-requirements-coming-online-as-2026-begins)

### Inferences
- **The biggest new, *active* pain for app developers in H2 2026 is age assurance plus COPPA plus privacy labels.** Texas is live, Utah and Louisiana are live in 2026, and the COPPA full-compliance date has passed. This sits squarely in Tempore's mobile expertise and is not well served by GRC incumbents.
- **CRA reporting (live 11 Sep 2026) is the most time-critical new obligation for EU-selling software makers.** 24-hour clocks favour tooling: an SBOM inventory feeding an exploited-vulnerability watch, a pre-filled ENISA report, and an audit trail. This could be sold to small and mid-sized software houses and IoT firms.
- **Delay whiplash** (ADA Title II, EU AI Act, Colorado, CMMC Phase 2) lowers near-term demand for tools tied to those regimes and raises demand for **regulatory-calendar and applicability tools** ("which of these apply to me, and when?"). But the rules-content maintenance burden is high for a small firm.
- For accessibility, the ADA Title II delay does not reduce private-sector litigation (3,117+ federal suits in 2025). The EAA is live. So accessibility remains a strong near-term market, especially for state and local government vendors preparing for April 2027.

### Gaps
- **NYC Local Law 144 (AEDT):** no 2025–2026 data gathered (search budget exhausted). I could not verify reports of weak enforcement or the state comptroller audit.
- **EU Digital Omnibus changes to GDPR, cookies and ePrivacy** (the Nov 2025 proposal to ease cookie consent and use browser signals): status not verified.
- **Utah and Louisiana app-store laws:** exact effective dates and litigation status were not verified beyond Apple's "effective 2026" statement.
- **GPAI Code of Practice uptake and developer complaints:** not researched.
- **Google Play Data Safety changes and Apple App Review policy changes in 2026:** not researched beyond developer verification.
- **CMMC:** actual counts of C3PAO-certified companies and SPRS readiness statistics were not retrieved (DefenseScoop was blocked).
