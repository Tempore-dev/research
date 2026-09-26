# Compliance Bottlenecks in Financial Services, Fintech, Insurance and Accounting: Software Opportunities for Tempore

> **Read this first: method and limits (September 25, 2026).** These notes come only from web-search result snippets. The research environment's network egress proxy blocked Reddit (www.reddit.com), G2, SoftwareAdvice/Capterra, Hacker News (hn.algolia.com), Kitces, FinCEN, CSBS, KPMG, ABA Banking Journal, Holland & Knight and SecurityMetrics. Every full-page fetch attempted failed. Site-restricted searches (`site:reddit.com`) returned no Reddit threads. The session's web-search budget (200 calls) then ran out.
>
> **So I could not collect any verbatim practitioner posts from Reddit, G2 or Capterra.** Where a "complaint" appears below, it is a search-engine summary of review pages or a vendor-reported anecdote, and it is labelled that way. Many figures come from vendor blogs or law-firm alerts, also labelled. Regulatory status is the most reliable part of these notes. First-hand practitioner sentiment is the weakest part and needs a follow-up pass with Reddit/G2 access, or manual collection.

---

## Q1. Which compliance tasks do practitioners call the biggest time sinks, the most manual or the most stressful, and what time and cost figures do they cite?

### Takeaway
The recurring manual burdens are:
- **AML/BSA:** alert triage (90–95% false positives), SAR investigation and writing, and continuing-activity re-reviews.
- **RIAs:** marketing-rule review of testimonials and ads, capturing and supervising communications, and new written cyber/privacy programs under Reg S-P.
- **Insurance:** tracking licences and CE across many states.
- **Tax/accounting:** writing a real WISP that practitioners have already attested to under penalty of perjury.
- **EU:** assembling a machine-readable DORA Register of Information that passes validation.

Compliance cost falls hardest, in proportion, on the smallest institutions.

### Cited Findings

**AML / BSA (banks, credit unions, fintechs, MSBs)**
- BSA-reporting institutions spend about **$206 million and 5.4 million hours a year** investigating, evaluating and filing SARs. This is FinCEN's own burden methodology. The figure dates from around 2020 and should be treated as old. — [ABA Banking Journal (2020)](https://bankingjournal.aba.com/2020/05/fincen-to-update-methodology-for-calculating-regulatory-burden-of-sars/) (via search snippet)
- **90–95% of alerts** from AML alert engines are false positives, citing a PwC analysis. The source is a vendor blog repeating a consultancy figure. It is widely quoted but is not primary survey data. — [Flagright](https://www.flagright.com/post/understanding-false-positives-in-transaction-monitoring); [LSEG glossary](https://www.lseg.com/en/risk-intelligence/glossary/risk-management/false-positive)
- Continuing-activity reviews became a burden driven by examiners. Guidance to file SARs on ongoing activity "at least every 90 days" had "transformed over time into an expectation among examiners that financial institutions re-review customers and accounts after filing a SAR." FinCEN's October 9, 2025 FAQs (issued jointly with the Fed, FDIC, NCUA and OCC) clarified four points:
  - No separate post-SAR review is required solely to check whether activity continued.
  - A transaction near the $10,000 CTR threshold is not, on its own, enough to require a SAR.
  - There is no BSA requirement to document a decision *not* to file.
  - Continuing-activity reviews may follow risk-based procedures.
  - Sources: [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2025/11/fincen-publishes-faqs-to-reduce-certain-compliance-burdens-associated-with-sar-filings); [FinCEN SAR FAQs PDF](https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf); [WilmerHale](https://www.wilmerhale.com/en/insights/client-alerts/20251028-fincen-clarifies-suspicious-activity-reporting-requirements); [Davis Polk](https://www.davispolk.com/insights/client-update/fincen-and-banking-agencies-release-updated-sar-guidance)
- In CSBS survey data from 2015 to 2024, the **smallest community banks spent roughly 11–15.5% of payroll on compliance**, against 6–10% at the largest. — [ABA Banking Journal, Nov 2025](https://bankingjournal.aba.com/2025/11/csbs-data-show-regulatory-burden-falls-hardest-on-community-banks/) (via snippet)
- The 2025 CSBS Annual Survey added questions on what share of compliance expense comes from each law or regulation, including BSA/AML. I could not retrieve the results. — [CSBS 2025 survey](https://www.csbs.org/2025-csbs-annual-survey); [PDF](https://www.csbs.org/sites/default/files/other-files/2025CBSurvey_web_CSBS.pdf)
- Older baseline (2015, St. Louis Fed/CSBS): compliance accounted for 11% of community banks' personnel expense, 16% of data processing, 20% of legal, 38% of accounting/auditing and **48% of consulting expense**. — [St. Louis Fed (2015)](https://www.stlouisfed.org/on-the-economy/2015/december/compliance-costs-community-banks-billions)
- Hummingbird's site quotes a BSA officer (Director of Financial Crimes & BSA Officer, BHG Financial) as saying automated STR filing "significantly reduced handling times compared to manual processes." This is a vendor testimonial. — [Hummingbird](https://www.hummingbird.co/)

**RIAs and broker-dealers**
- The SEC Marketing Rule is a top 2026 exam priority. The SEC "continues to observe widespread non-compliance with testimonials and endorsements", driven by incomplete disclosures, weak oversight and confusion over what counts as an endorsement. The SEC issued a new risk alert in December 2025. — [ThinkAdvisor, Dec 2025](https://www.thinkadvisor.com/2025/12/17/sec-issues-new-warning-on-marketing-rule-compliance/); [Alston & Bird](https://www.alston.com/en/insights/publications/2025/12/sec-new-compliance-observations-marketing-rule); [Mintz, Feb 2026](https://www.mintz.com/insights-center/viewpoints/2026-02-25-sec-marketing-rule-enforcement-2026-why-buyers-breakaways-and)
- A summary in Kitces-linked material says advisors' satisfaction falls as time on compliance and paperwork rises, and workweeks well beyond about 38 hours correlate with turnover. This is a search-snippet paraphrase. — [Kitces research category](https://www.kitces.com/blog/category/23-research/)
- The 2025 ACA/IAA/Yuter Investment Management Compliance Testing Survey ranked **AI, AML and cybersecurity** as the top three "hot" compliance concerns. Respondents: 23% managed under $1B; 41% had 11–50 employees. — [ACA Group](https://www.acaglobal.com/industry-insights/2025-investment-management-compliance-testing-survey/); [IAA](https://www.investmentadviser.org/resources/investment-management-compliance-testing-surveys/); [BusinessWire](https://www.businesswire.com/news/home/20250722816977/en/Survey-Artificial-Intelligence-Identified-as-Top-Compliance-Concern-Among-Investment-Adviser-Firms)
- Communications recordkeeping has not gone away. FINRA's 2026 Annual Regulatory Oversight Report mentions recordkeeping lapses **more than 50 times**, covering e-comms capture, off-channel use and inadequate supervision. Rules 17a-4 and 204-2 are unchanged, and state regulators can still request records. The source is a vendor article. — [X1 (vendor)](https://x1wealth.com/resources/off-channel-communications-fines-2026); [Corporate Compliance Insights](https://www.corporatecomplianceinsights.com/finra-following-off-channel-enforcement/)

**Insurance agents**
- Multi-state licensing is messy because rules differ by state:
  - California licences expire two years from the month of issue.
  - Kansas renews in odd or even years depending on the licensee's birth year.
  - New York and California do not accept other states' CE for claims adjusters.
  - Tracking gets harder with multiple lines of authority and parent licences.
  - Source: [AgentSync (vendor)](https://agentsync.io/blog/insurance-101/insurance-licensing-101-agent-license-renewals)
- "Most independent agents rely on a mix of spreadsheets, calendar reminders, and state portals… A calendar reminder gets missed, a spreadsheet is not updated, a state portal is not checked in time." — [InsureTrek (vendor)](https://insuretrek.com/blog/Insurance-license-renewals)
- AgentSync's own example: an agency's 10 producers each spend about **one hour a day** on admin for licences, appointments, CE and renewals. Its founder called it "an impossible task to maintain broker compliance with a growing and evolving business using only a spreadsheet." Both are vendor anecdotes. — [AgentSync](https://agentsync.io/blog/compliance/taking-the-cost-out-of-compliance-at-your-insurance-agency); [AgentSync founder story](https://agentsync.io/blog/compliance/agentsyncs-passion-for-compliance-stems-from-hard-experiences-at-zenefits)

**Tax preparers and accounting firms (WISP)**
- Many practitioners attest to a WISP without having one. Form W-12 (PTIN application and renewal) has had a WISP check-box since October 2019. Line 11 asks whether the preparer maintains a WISP, and the answer is given under penalty of perjury. Security trainers report that many firms "were not aware of the requirement, even though they had already attested to it." The sources are vendor and consultancy pages (Bellator, Intuit); the AICPA confirms the requirement. — [Bellator (vendor)](https://bellatorcyber.com/blog/ptin-renewal-security-requirements); [Intuit Tax Pro Center](https://accountants.intuit.com/taxprocenter/practice-management/completing-your-wisp-for-ptin-renewal/); [AICPA & CIMA](https://www.aicpa-cima.com/resources/article/wisp-required-by-federal-law-for-tax-practitioners)
- A WISP must name a security coordinator and include:
  - a written risk assessment
  - employee policies
  - technical controls, including MFA (required as of August 2024)
  - physical safeguards
  - vendor management
  - an incident response plan with IRS breach notification
  - The IRS sample template is Publication 5708, but "your final WISP must reflect your actual environment." — [Bellator (vendor)](https://bellatorcyber.com/blog/wisp-small-tax-firm); [IRS](https://www.irs.gov/newsroom/a-written-information-security-plan-protects-tax-pros-and-their-clients)
- A vendor claims penalties of "FTC fines starting at $46,517 per violation." This is not independently verified. — [Bellator (vendor)](https://bellatorcyber.com/blog/ptin-renewal-security-requirements)

**EU DORA (in force January 17, 2025)**
- In the ESAs' 2024 dry run (almost 1,000 financial entities), **only 6.5% of Registers of Information passed all data-quality checks**. Of the rest, 50% failed fewer than 5 of the 116 checks. — [Finadium](https://finadium.com/esas-report-6-5-data-quality-pass-rate-after-dora-dry-run/); [EBA dry-run report](https://www.eba.europa.eu/sites/default/files/2024-12/c1454b59-15cc-445e-be14-966e3338cedc/ESA%202024%2035%20DORA%20Dry%20Run%20exercise%20summary%20report%20for%20publication.pdf)
- The most common failures were missing or invalid LEIs and misclassification of critical or important functions (CIF). The register must be submitted in xBRL-CSV. — [DORA GRC blog (vendor)](https://doragrc.com/blog/dora-register-of-information-2026-reporting-update); [EBA dry run](https://www.eba.europa.eu/sites/default/files/2024-12/c1454b59-15cc-445e-be14-966e3338cedc/ESA%202024%2035%20DORA%20Dry%20Run%20exercise%20summary%20report%20for%20publication.pdf)
- ICT providers to EU financial entities "will be requested to conduct mapping of their own ICT service supply chain". A law-firm blog notes that "there is currently no guidance or market standard as to how far down the ICT supply chain the reports must cover." — [Sidley Data Matters (Apr 2025)](https://datamatters.sidley.com/2025/04/15/financial-entities-in-the-eu-time-to-register-your-ict-third-party-service-providers-under-dora/)

### Inferences
- Across the verticals the same pattern repeats. The painful work is **evidence assembly and documentation**: narratives, registers, attestations, logs and review trails. It is not the judgement calls. That kind of work suits workflow software.
- The October 2025 SAR FAQs and the April 2026 program NPRM should **shrink the value of "volume" tools**, such as mass continuing-activity reviews. They should **raise the value of tools that document a risk-based rationale**, meaning risk assessments and policy-to-procedure mapping.

### Gaps
- No verbatim Reddit, G2 or Capterra practitioner quotes could be retrieved. Every site was blocked by the proxy; see the note at the top.
- No 2025–2026 survey figures on hours per SAR, hours per marketing review, or hours per WISP for small firms.
- CSBS 2025 results on BSA/AML's share of compliance cost were not retrieved.
- Nothing was found for crypto firms or MSBs specifically: travel rule, state money-transmitter licensing cost. The search budget ran out first.

---

## Q2. What tools do practitioners use, and what do reviews complain about?

### Takeaway
Incumbents in communications archiving (Smarsh, Global Relay) draw complaints about price rises, dated interfaces, slow search and weak support. RIA-specific compliance tools get mediocre attention in advisor surveys. In insurance and small tax practices the de facto tools are spreadsheets, calendar reminders, state portals and free templates. I found no independent negative reviews of Hummingbird, Unit21 or Alloy.

### Cited Findings
- **Smarsh**, as summarised from G2 review pages (search-engine summary, not verbatim):
  - poor support with slow responses
  - slow performance affecting alerts and searches
  - an interface that "feels dated and is not as intuitive"
  - a steep learning curve and insufficient onboarding training
  - A separate pricing complaint: "At three times the original rate per month, it was like charging an incredible amount for an archiving service."
  - Sources: [G2 Smarsh pros and cons](https://www.g2.com/products/smarsh-professional-archive/reviews?qs=pros-and-cons); [G2 Smarsh reviews](https://www.g2.com/products/smarsh-smarsh/reviews); [SoftwareAdvice](https://www.softwareadvice.com/compliance/smarsh-profile/)
- Smarsh and Global Relay are described as the widely used, purpose-built archivers for regulated communications. — [AdvisorHub](https://www.advisorhub.com/resources/how-rias-should-tackle-their-off-channel-communications-responsibilities/)
- **Kitces AdvisorTech 2025:**
  - A vendor blog summarising the report says "compliance barely registers" in the rankings and "remains the weak link".
  - Smartria is said to lead market share among RIA-specific compliance platforms and to rank third in satisfaction.
  - RIA Compliance Technology reports a satisfaction score of 8.7, per its own press release.
  - Sources: [Smartria blog (vendor)](https://smart-ria.com/blog/the-hidden-risk-in-the-kitces-tech-stack-why-compliance-still-lags-behind/); [SuperbCrew press release](https://www.superbcrew.com/ria-compliance-technology-earns-high-marks-in-2025-kitces-report-for-advisor-satisfaction-and-industry-leadership/); [Kitces report page](https://www.kitces.com/kitces-report-independent-financial-advisor-technology-fintech-software-tools-research/)
- **Insurance:**
  - Tools named: NIPR, AgentSync (enterprise-leaning), and smaller entrants CredTally, InsureTrek and RenewOps. — [CredTally](https://www.credtally.com/for/insurance-agents); [InsureTrek](https://insuretrek.com/blog/License-Tracking-for-Insurance-Agents/); [RenewOps](https://renewops.app/guides/insurance-license-renewal-tracking); [NIPR CE help](https://nipr.com/help/continuing-education-requirements)
  - AgentSync claims a 25% reduction in compliance-officer workload in one case study. This is a vendor claim. — [AgentSync](https://agentsync.io/blog/compliance/agentsyncs-passion-for-compliance-stems-from-hard-experiences-at-zenefits)
- **Tax/WISP:** the free IRS Publication 5708 template, plus a crowd of paid templates and cyber-consultancy offerings. — [Western CPE free template](https://www.westerncpe.com/wisp-template/); [ComplianceDocsHQ](https://compliancedocshq.com/toolkits/wisp-taxpro); [Verito](https://verito.com/written-information-security-plan/); [Rightworks](https://www.rightworks.com/blog/wisp-requirements-accountants-guide/)
- **AML platforms (Hummingbird, Unit21, Alloy, Sumsub):** the only search results were vendor marketing and testimonials. I found no independent complaints. — [Hummingbird](https://www.hummingbird.co/industry/banks); [Unit21](https://www.unit21.ai/); [Alloy for credit unions](https://www.alloy.com/credit-unions)

### Inferences
- Complaints about Smarsh (price rises, dated interface, slow search) match a classic "incumbent squeeze" on small RIAs. A small archiving vendor would still need carrier and API integrations (SMS, WhatsApp, LinkedIn). That is a heavy, regulated, 17a-4-grade storage build, **not a good first bet for Tempore**.
- Insurance licence/CE tracking and WISP templates already have many low-cost niche entrants. Differentiation would need to come from UX, a mobile-first design, and integrations such as NIPR data or CE-provider feeds.

### Gaps
- No verbatim G2 or Capterra reviews of Global Relay, ComplySci, RIA in a Box, Hummingbird, Unit21, Alloy or Sumsub. The review sites were blocked and snippets gave nothing.
- No pricing data for incumbents.

---

## Q3. Where do small firms say nothing affordable or simple exists?

### Takeaway
The evidence points to four areas:
- (a) documenting and customising a WISP and Reg S-P incident-response program, beyond fill-in-the-blank templates;
- (b) multi-state insurance licence/CE tracking for independent agents, who still use spreadsheets;
- (c) building and validating a DORA Register of Information for small EU entities and for the non-EU ICT vendors being asked to supply data;
- (d) documenting risk-based AML decisions for small banks, credit unions and MSBs under the new FinCEN framework.

Direct practitioner statements that "nothing affordable exists" could not be verified from forums.

### Cited Findings
- Independent insurance agents: spreadsheets, calendar reminders and state portals, "as license volume increases, small gaps appear." — [InsureTrek (vendor)](https://insuretrek.com/blog/Insurance-license-renewals)
- Small tax practices (1–3 staff) are pointed to the free template, but a copied template does not comply ("must reflect your actual environment, not simply replicate the Publication 5708 template"). — [Bellator (vendor)](https://bellatorcyber.com/blog/wisp-small-tax-firm)
- Reg S-P for small RIAs requires four things that many small firms have not formalised before: a written incident response program, 30-day customer notification, expanded vendor oversight, and new recordkeeping. — [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/05/regulation-s-p-amendments-compliance-deadline-approaching); [Davis Wright Tremaine](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/reg-sp-smaller-entities-june-2026-deadline); [Baker Donelson](https://www.bakerdonelson.com/regulation-s-p-june-3-2026-compliance-deadline-for-smaller-investment-advisers)
- DORA proportionality: microenterprises (fewer than 10 staff, under €2M turnover) get a simplified ICT framework under Article 16, "but still having ICT third-party risk obligations under Article 28". Small payment institutions, investment firms and CASPs are in scope, unlike NIS2's size exemption. — [regulation-dora.eu](https://www.regulation-dora.eu/blog/dora-compliance-small-financial-institutions); [Nemko](https://digital.nemko.com/regulations/digital-operational-resilience-act); [Copla](https://copla.com/blog/compliance-regulations/dora-regulation-proportionality-how-it-works-in-practice/)
- PCI SAQ A merchants must now *confirm their site is not susceptible to script attacks*. Merchants who cannot confirm this "risk… the loss of their SAQ A eligibility, possibly adding over 100 new requirements to their PCI DSS scope." — [DataStealth](https://datastealth.io/blogs/understanding-saq-as-new-eligibility-criteria); [PCI SSC blog](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a)

### Inferences
- The recurring gap is **"template to living program"**: an affordable tool that turns a static policy (WISP, Reg S-P IRP, DORA register, AML risk assessment) into a maintained record with reminders, an evidence log, vendor inventory and annual-review workflow. The inference is that small firms get templates, and large firms get GRC suites or consultants.

### Gaps
- No first-hand forum statements such as "we couldn't find anything under $X/month" were retrievable.
- Pricing floors for small-firm GRC tools were not collected.

---

## Q4. Which regulatory changes in 2025–2027 are creating new pain, and which were rolled back or delayed?

### Takeaway
New or active obligations:
- Reg S-P amendments (smaller-entity deadline June 3, 2026)
- DORA (January 2025, with register updates in 2026)
- PCI DSS 4.0.1 future-dated requirements (March 31, 2025)
- Continued FINRA scrutiny of communications recordkeeping
- Marketing-rule exams

Rolled back, delayed or softened:
- CTA/BOI for US companies (permanently eliminated August 2026)
- The investment-adviser AML rule (delayed to January 1, 2028)
- CFPB 1033 (enjoined and being rewritten)
- CFPB 1071 (narrowed, compliance January 1, 2028)
- SEC off-channel sweeps (ended)
- Disparate-impact liability under Regulation B (removed; litigation pending)

FinCEN's April 2026 AML program NPRM is pending and would reshape BSA programs.

### Cited Findings

**New or active pain**
- **Reg S-P amendments:**
  - Larger entities have had to comply since December 3, 2025. Larger means investment companies over $1B, RIAs over $1.5B RAUM, and most broker-dealers with capital above $500K.
  - Smaller entities (RIAs under $1.5B) had to comply by **June 3, 2026**.
  - The SEC indicated that Reg S-P compliance will be an exam priority later in 2026.
  - Sources: [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/05/regulation-s-p-amendments-compliance-deadline-approaching); [RIA Compliance Consultants](https://www.ria-compliance-consultants.com/2026/05/regulation-s-p-deadline-smaller-investment-advisers/); [Gibson Dunn](https://www.gibsondunn.com/regulatory-compliance-reminders-for-investment-advisers/)
- **DORA:**
  - Applicable from January 17, 2025, with the first Register of Information collected in 2025.
  - In 2026 Belgium's FSMA is running a "limited update": only some firms submit, and firms with no changes can simply confirm.
  - National authorities are running supervisory reviews in 2026. The register, incident classification and third-party oversight are said to produce the most findings (vendor claim).
  - Sources: [FSMA](https://www.fsma.be/en/news/dora-register-information-third-party-ict-service-providers-limited-update-2026); [Nemko](https://digital.nemko.com/regulations/digital-operational-resilience-act)
- **PCI DSS 4.0.1:**
  - Future-dated requirements took effect on March 31, 2025.
  - On January 30, 2025 the PCI SSC removed 6.4.3 (payment-page script inventory), 11.6.1 (tamper detection) and 12.3.1 (TRA) from SAQ A, replacing them with the eligibility criterion above.
  - A 2026 revision of FAQ 1331 reportedly narrows the "N/A" path for 6.4.3/11.6.1. This comes from a vendor headline and was not verified.
  - Sources: [PCI SSC blog](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a); [SecurityMetrics](https://www.securitymetrics.com/blog/big-changes-for-saq-a); [Reflectiz (vendor)](https://www.reflectiz.com/blog/pci-faq-1331-revision-2026/)
- **SEC Marketing Rule:** a top 2026 exam priority, with a December 2025 risk alert. — [ThinkAdvisor](https://www.thinkadvisor.com/2025/12/17/sec-issues-new-warning-on-marketing-rule-compliance/)
  - A snippet claims "new rule updates imposed in January 2026 also require advisors to monitor paid promoters for disqualifying events within 10 years". I could not verify this and it may be a mischaracterisation of the existing rule's disqualification provisions. — [FIG Marketing](https://www.figmarketing.com/blog/a-compliance-checklist-for-financial-advisors-on-social-media-in-2026/)
- **FinCEN AML/CFT Program NPRM** (issued April 7, 2026; Federal Register April 10, 2026; comments due June 9, 2026):
  - A "two-pronged" test separates *establishing* a program from *implementing* it.
  - Enforcement would be limited to a "significant or systemic failure".
  - The stated aim is to move from technical compliance to effectiveness while "decreasing compliance burden".
  - It is not yet final as of these notes; I found no final rule.
  - Sources: [Federal Register](https://www.federalregister.gov/documents/2026/04/10/2026-07033/anti-money-laundering-and-countering-the-financing-of-terrorism-programs); [MoFo](https://www.mofo.com/resources/insights/260417-fincen-proposes-new-rule-aml-cft-programs); [Paul, Weiss](https://www.paulweiss.com/insights/client-memos/fincen-proposes-program-rule-to-fundamentally-reform-bsaaml-compliance); [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/04/out-with-the-old-in-with-the-risk-based-fincen-proposes-fundamental-reform-of-aml-cft-program-requirements); [Sullivan & Cromwell](https://www.sullcrom.com/insights/memo/2026/April/Regulators-Issue-Proposed-Rules-Reforming-AML-CFT-Program-Requirements)
- **Circular 230:**
  - Proposed amendments were published December 26, 2024, with comments due February 24, 2025.
  - They would add a **technological competency** duty and update contingent-fee and electronic-payment provisions.
  - Final rules were "not expected until at least 2026". I did not verify their status as of September 2026.
  - Sources: [Federal Register](https://www.federalregister.gov/documents/2024/12/26/2024-29371/regulations-governing-practice-before-the-internal-revenue-service); [NATP](https://www.natptax.com/news-insights/blog/a-closer-look-at-proposed-changes-to-circular-230/); [NYSSCPA](https://www.nysscpa.org/most-popular-content/what-tax-practitioners-need-to-know-about-the-proposed-amendments-to-circular-230)
- **Off-channel/recordkeeping:**
  - The SEC sweep collected over $2B from 100+ firms between December 2021 and January 2025, then ended.
  - FINRA and the UK FCA continue.
  - Enforcement increasingly targets named individuals.
  - The ICI has urged the SEC to modernise the rules.
  - Sources: [X1 (vendor)](https://x1wealth.com/resources/off-channel-communications-fines-2026); [MirrorWeb (vendor)](https://www.mirrorweb.com/blog/how-finra-took-the-sec-baton-with-off-channel-penalties); [ICI](https://www.ici.org/news-release/sec-should-adapt-offchannel-communications-rules-for-21st-century)

**Rolled back, delayed or superseded (flag as superseded pain)**
- **CTA/BOI:**
  - An interim final rule on March 21, 2025 (Federal Register March 26, 2025) removed reporting for US companies and US persons.
  - FinCEN's **final rule of August 11, 2026 (Federal Register August 14, 2026)** made that permanent: former "domestic reporting companies" have no obligation to file, update or correct.
  - Foreign reporting companies still have obligations.
  - The Eleventh Circuit upheld the CTA's constitutionality, and state rules still apply.
  - **Opportunities built around federal BOI filing for US SMBs are dead.**
  - Sources: [Mayer Brown, Aug 2026](https://www.mayerbrown.com/en/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons); [Federal Register, Aug 14, 2026](https://www.federalregister.gov/documents/2026/08/14/2026-16576/beneficial-ownership-information-reporting-requirement-revision); [FinCEN news](https://www.fincen.gov/news/news-releases/fincen-removes-beneficial-ownership-reporting-requirements-us-companies-and-us); [Procopio](https://www.procopio.com/resource/latest-cta-update)
- **Investment Adviser AML Rule:**
  - The effective date moved from January 1, 2026 to **January 1, 2028**, and FinCEN intends to revisit its scope.
  - This defers an estimated **over $1B in near-term compliance costs**.
  - Sources: [FinCEN](https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028); [Orrick](https://www.orrick.com/en/insights/2025/07/fincen-postpones-investment-adviser-aml-rule-until-2028); [MoFo](https://www.mofo.com/resources/insights/260108-fincen-hits-pause-no-aml-rule-for-investment-advisers-until-2028); [Alessa](https://alessa.com/blog/fincen-investment-adviser-aml-rule-delay/)
- **CFPB 1033 (open banking):**
  - Finalized October 2024.
  - A federal court has enjoined enforcement.
  - The CFPB issued an ANPR on August 22, 2025, reopening four questions: who counts as a consumer "representative", fees, data security and privacy.
  - The first compliance date, April 1, 2026, passed without effect.
  - States are becoming active on data sharing.
  - Sources: [Cozen O'Connor](https://www.cozen.com/news-resources/publications/2026/section-1033-compliance-date-open-banking-rule-enjoined-and-under-reconsideration); [Open Banking Tracker](https://openbankingtracker.com/guides/section-1033-status); [Consumer Finance Monitor, Jun 2026](https://www.consumerfinancemonitor.com/2026/06/26/open-banking-regulation-in-2026-federal-regulation-resurfaces-as-states-bring-data-sharing-into-focus/)
- **CFPB 1071 (small-business lending data):**
  - Final Regulation B amendments narrow the covered institutions, trim data points and set a **single compliance date of January 1, 2028**. This is from a KPMG snippet; the page itself was blocked.
  - Earlier, the CFPB signalled interim final rules amid funding constraints (December 2025).
  - Sources: [KPMG](https://kpmg.com/us/en/articles/2026/cfpb-final-rules-regulation-b-Section-1071-and-disparate-impact-liability-reg-alert.html); [Consumer Financial Services Law Monitor](https://www.consumerfinancialserviceslawmonitor.com/2025/12/cfpb-signals-issuance-of-interim-final-rules-on-section-1071-and-section-1033-amid-funding-constraints/)
- **Fair lending:**
  - A CFPB final rule says ECOA does not authorise disparate-impact liability.
  - Fair-housing groups have sued.
  - Sources: [KPMG](https://kpmg.com/us/en/articles/2026/cfpb-final-rules-regulation-b-Section-1071-and-disparate-impact-liability-reg-alert.html); [Ncontracts](https://www.ncontracts.com/nsight-blog/fair-lending-update); [Ncontracts, Jun 2026](https://www.ncontracts.com/nsight-blog/june-2026-regulatory-update)
- **HMDA:**
  - The 2026 asset-size exemption threshold is $59M.
  - A March 13, 2026 executive order reportedly directs the CFPB to consider raising HMDA exemption thresholds and excluding certain inquiries. This is from snippets and was not verified against the order text.
  - Sources: [Federal Register, Jan 7, 2026](https://www.federalregister.gov/documents/2026/01/07/2026-00087/home-mortgage-disclosure-regulation-c-adjustment-to-asset-size-exemption-threshold); [Credit Technologies](https://www.credittechnologies.com/post/2026-hmda-reporting-changes-lenders)
- **SAR burden relief:** the October 2025 FAQs (see Q1).

### Inferences
- **US deregulation in 2025–2026 cuts demand for tools tied to specific filings** (BOI, 1071, 1033, IA-AML). It raises demand for **"defensible risk-based documentation"**, because examiners will still ask *why*.
- **The SEC and state/FINRA side has not been rolled back.** Reg S-P, the Marketing Rule and recordkeeping remain live, so small RIAs and broker-dealers have steadier, clearer demand than US bank or lending compliance.
- **EU DORA is structural and recurring** (annual registers). It also pulls non-EU ICT vendors, including software firms like Tempore's clients, into supplying data.

### Gaps
- Not verified:
  - whether Circular 230 final rules were issued in 2026;
  - the final text and date of the 1071 amendments;
  - whether the FinCEN program rule was finalised after the June 2026 comment deadline;
  - any EU "digital omnibus" or DORA simplification proposals.
- The FTC Safeguards Rule breach-notification amendment (effective 2024) and any 2025–2026 changes were not researched because the search budget ran out.

---

## Q5. Which gaps could a small web, mobile and desktop software firm like Tempore address? (Assessment)

### Takeaway
The best fits for Tempore are narrow, document-and-workflow products for small regulated firms, where incumbents are enterprise GRC suites or static templates and no licensed data feed or regulated storage is needed:
1. a WISP / Reg S-P "living program" manager for tax, accounting and small-RIA firms;
2. multi-state insurance licence/CE tracking for independent agents;
3. DORA Register of Information building and xBRL-CSV validation for small EU entities and their ICT vendors;
4. a documentation layer for risk-based AML decisions for small banks, credit unions and MSBs.

Poor fits: comms archiving (Smarsh/Global Relay territory), transaction-monitoring or KYC engines (Unit21/Alloy/Sumsub), and anything built on BOI/1071/1033 filings.

### Cited Findings (evidence behind each rating)

**1. WISP and Reg S-P program manager — HIGH fit**
- A legal requirement at every firm size, attested under penalty of perjury, and widely unmet. — [Bellator](https://bellatorcyber.com/blog/ptin-renewal-security-requirements); [AICPA](https://www.aicpa-cima.com/resources/article/wisp-required-by-federal-law-for-tax-practitioners)
- Reg S-P adds an incident-response program, vendor oversight and 30-day notification for RIAs under $1.5B. — [DWT](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/reg-sp-smaller-entities-june-2026-deadline)
- The proposed Circular 230 "technological competency" duty would reinforce this. — [NATP](https://www.natptax.com/news-insights/blog/a-closer-look-at-proposed-changes-to-circular-230/)
- Competition is templates and cyber MSPs. — [Western CPE](https://www.westerncpe.com/wisp-template/); [Verito](https://verito.com/written-information-security-plan/)

**2. Insurance licence/CE tracker — MEDIUM fit**
- Clear spreadsheet pain and messy multi-state rules. — [AgentSync](https://agentsync.io/blog/insurance-101/insurance-licensing-101-agent-license-renewals); [InsureTrek](https://insuretrek.com/blog/Insurance-license-renewals)
- The low end is already crowded (CredTally, InsureTrek, RenewOps), and AgentSync covers the enterprise end. — [CredTally](https://www.credtally.com/for/insurance-agents); [RenewOps](https://renewops.app/guides/insurance-license-renewal-tracking)

**3. DORA Register of Information builder/validator — MEDIUM-HIGH fit (EU)**
- A 6.5% first-pass data-quality rate, a machine-readable xBRL-CSV format, LEI and CIF errors, and an annual cycle. — [Finadium](https://finadium.com/esas-report-6-5-data-quality-pass-rate-after-dora-dry-run/); [EBA](https://www.eba.europa.eu/sites/default/files/2024-12/c1454b59-15cc-445e-be14-966e3338cedc/ESA%202024%2035%20DORA%20Dry%20Run%20exercise%20summary%20report%20for%20publication.pdf)
- ICT vendors face supply-chain mapping requests with no standard. — [Sidley](https://datamatters.sidley.com/2025/04/15/financial-entities-in-the-eu-time-to-register-your-ict-third-party-service-providers-under-dora/)
- A vendor-side "DORA data pack" generator is a possible niche.

**4. AML risk-based documentation for small institutions and MSBs — MEDIUM fit**
- The NPRM's establishment/implementation split and the SAR FAQs shift value toward documenting rationale, meaning risk assessments and decision logs. — [Federal Register](https://www.federalregister.gov/documents/2026/04/10/2026-07033/anti-money-laundering-and-countering-the-financing-of-terrorism-programs); [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2025/11/fincen-publishes-faqs-to-reduce-certain-compliance-burdens-associated-with-sar-filings)
- Risks: bank sales cycles, core-system integrations and a rule that is not yet final.

**5. PCI SAQ A script-monitoring / eligibility-evidence tool — LOW-MEDIUM fit**
- The need is real, since merchants must now confirm their site is not susceptible to script attacks. — [PCI SSC](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a)
- The space is crowded with security vendors (Source Defense, Reflectiz, HUMAN, Akamai). — [Source Defense](https://sourcedefense.com/resources/cheat-sheet-and-action-plan-the-pci-councils-saq-a-eligibility-update/); [HUMAN](https://www.humansecurity.com/learn/blog/pci-dss-4-update-unpacking-the-changes-to-saq-a/)

**6. Marketing-rule review workflow for small RIAs — MEDIUM fit**
- A persistent exam finding (testimonials, disclosures). — [ThinkAdvisor](https://www.thinkadvisor.com/2025/12/17/sec-issues-new-warning-on-marketing-rule-compliance/)
- Existing RIA compliance suites (Smartria, RIA Compliance Technology, RIA in a Box) already bundle this. — [Kitces directory](https://fintech.kitces.com/details/operations-essentials/compliance/ria-compliance-technology)

**7. Avoid:**
- **BOI filing tools:** the rule is eliminated for US companies. — [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons)
- **1071 data collection before 2028.** — [KPMG](https://kpmg.com/us/en/articles/2026/cfpb-final-rules-regulation-b-Section-1071-and-disparate-impact-liability-reg-alert.html)
- **Communications archiving**, where incumbents plus 17a-4 storage requirements make it a heavy build. — [AdvisorHub](https://www.advisorhub.com/resources/how-rias-should-tackle-their-off-channel-communications-responsibilities/)

### Inferences
- For Tempore, a web, mobile and desktop builder without a compliance data licence, the most defensible entry is **option 1, a WISP / Reg S-P program manager**. The reasons: US-wide mandatory demand; buyers who are small and self-serve (tax and CPA firms, small RIAs); no regulated data storage needed; and existing channels such as tax software ecosystems and state CPA societies.
- **Option 3 (DORA RoI) makes sense only with EU go-to-market capacity.**
- Tempore could also offer these as **client-services builds**, meaning custom portals for compliance consultants, rather than as its own SaaS. This is lower risk, given crowded low-end SaaS.

### Gaps
- Market sizing was not collected: the number of PTIN holders, small RIAs, independent agents and DORA microenterprises.
- Pricing benchmarks for competing WISP, CE-tracking and DORA-RoI tools were not collected.
- Practitioner willingness to pay was not validated through forums, because Reddit and review sites were inaccessible from this environment.
