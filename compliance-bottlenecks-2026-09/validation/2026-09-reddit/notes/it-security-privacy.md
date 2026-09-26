# IT, security, SaaS and privacy: Reddit sweep notes

> **How this was gathered (2026-09-25).** Reddit's anonymous search feeds returned 303 posts from 2024 onwards, and all were read: r/msp 85, r/Compliance 66, r/SaaS 50, r/sysadmin 31, r/startups 28, r/privacy 22, r/gdpr 21. The feeds return **post bodies only**, so comments and votes were not read.
>
> About 60% of the posts were noise: complaints about security teams, privacy news, comparisons of EDR, MDR and SOC vendors, fundraising, and weekly promotion threads. About 25 were posts by vendors or founders promoting their own product, mostly SOC 2 tools. They are used below as evidence of crowding.

## Watch: MSPs completing each client's cyber-insurance application from reusable evidence

**Workflow.** Managed service providers (MSPs) with 1–25 staff complete, or supply evidence for, each small-business client's cyber-insurance application and renewal questionnaire. Every carrier uses its own form, so the same controls get re-proven again and again.

**Driver.** Market pressure, not a rule.
- Vendors report that applications grew from about 30 questions to 200–400 ([Anchor, vendor-written, 2026-06-26](https://www.getanchor.ai/articles/cyber-insurance-application-questionnaire-automation-2026)).
- Carriers now ask about specific products; one insurer letter asked about SonicWall ([2026-01-23](https://www.reddit.com/r/msp/comments/1ql3bv6/)).
- A wrong answer can void cover after a claim ([Scopable, vendor-written, 2026-05-18](https://scopable.io/blog/cyber-insurance-requirements-msp-2026)).

**Reddit evidence.**
- [2025-09-25](https://www.reddit.com/r/msp/comments/1nqbrkz/): an MSP is "bombarded by forms this year". Each takes several hours, and clients push back when the MSP charges for them.
- [2024-07-08](https://www.reddit.com/r/msp/comments/1dya78u/): the self-audit questionnaires vary a lot between insurers.
- [2024-07-09](https://www.reddit.com/r/msp/comments/1dzaz16/): an MSP completing a client's form can't tell what one question actually asks.
- [2026-09-23](https://www.reddit.com/r/Compliance/comments/1wo84t3/): an 80-person EU company re-proves the same MFA control in five places, the insurer's renewal among them.
- Related: due-diligence questionnaires about the MSP itself grow every year ([2025-07-01](https://www.reddit.com/r/msp/comments/1lp0w1x/)).

**Competition (checked 2026-09-25).**
- Tools that produce evidence but don't fill in the carrier's form:
  - Liongard's cyber-insurance assessment report ([docs](https://docs.liongard.com/docs/liongard-and-cybersecurity-insurance)).
  - Guardz's per-client reports.
  - Compliance Scorecard's evidence store (G2 lists it at $299/month).
  - Scopable's readiness assessments.
- Generic AI questionnaire fillers (Anchor, Skypher, Inventive, Responsive, Loopio, Ombud, Tribble, 1up) handle any questionnaire. None targets MSPs or keeps a store of evidence per client.
- The carriers' own portals (Coalition, At-Bay, Cowbell) run their own applications.

No product found maps one client's evidence onto each carrier's form.

**Barrier and gates.** The barrier is moderate. The product needs a library of carrier forms that keep changing, plus evidence pulled from Microsoft 365 or RMM tools. Liability is the main risk: attestation has to stay with the client.

**Buyer base.** About 40,000–50,000 US MSPs, from a weak blog source ([MSP Launchpad](https://www.msplaunchpad.com/blog-posts/msp-market-statistics)). The number is flat to consolidating: Canalys counted 267 MSP acquisitions in 2025, up from 234.

**Scorecard.** Frustration Partial · Barrier Partial · Gate Partial · Alternatives Partial · Paying base Partial.

**Next test (desk research first).**
1. Collect 8–10 current small-business applications (Coalition, At-Bay, Cowbell, Chubb, Travelers, Beazley).
2. Normalise the questions and measure how many overlap.
3. **Kill** if fewer than 60% are shared, or if 5 of 10 MSPs interviewed would rather bill the client and answer from the Liongard or Guardz report they already have.

## Rejected

| Workflow | Evidence | Why rejected |
|---|---|---|
| Tracking each client's compliance program for an MSP (HIPAA, GLBA, CIS) with reminders and status the client can see | [2026-05-29](https://www.reddit.com/r/msp/comments/1trbid0/), [2025-07-10](https://www.reddit.com/r/msp/comments/1lw9dws/) | Crowded. Compliance Scorecard costs $299/month and Cynomi about $3,000 per seat per year; Apptega and BreachSecureNow also compete. The open-source [CISO Assistant](https://github.com/intuitem/ciso-assistant-community) covers 200+ frameworks for free |
| Small company passing security reviews down to its own suppliers under NIS2 | [2026-07-28](https://www.reddit.com/r/sysadmin/comments/1v8tekg/): about 20 suppliers, "no GRC team or a tool budget". [2026-07-29](https://www.reddit.com/r/Compliance/comments/1v9r7am/): a vendor review still marked current against an expired SOC 2 report | Crowded, with free tiers ([Orbiq](https://www.orbiqhq.com/pricing), CISO Assistant's supplier-risk module), and the strongest poster has no budget |
| SOC 2 readiness kits for tiny SaaS companies | At least 14 founders pitching them. One $499 product had 150 free demo users and no paying customers ([2026-02-23](https://www.reddit.com/r/startups/comments/1rc9q3h/)) | Crowded |
| Access-review evidence; screenshot timestamping; cross-framework control mapping; cookie-consent and script mapping; tracking regulatory changes; AI data-loss prevention; SLA reports for MSPs; external attack-surface scanning | Scattered | Crowded or a small one-off purchase |
| Evidence collection for clients' CMMC Level 1 self-assessments | Most posts predate the suspension of Phase 2 on 2026-07-13 | Demand has cooled, and existing tools already cover it |
| FCC Form 499-A and robocall filings for MSPs that resell phone lines; click-to-cancel rules; GDPR representation | One post each | Legal services or single anecdotes |

## Bears on the study's ranked items

**#8 Security-questionnaire library and trust page: competition moves to Fail.**
- The pain is confirmed. Founders report lost deals of $40k ([2026-03-15](https://www.reddit.com/r/SaaS/comments/1ruf7ns/)) and $95k ([2025-11-30](https://www.reddit.com/r/Compliance/comments/1pavduq/)), and they resent Vanta's price of $12k and $20–30k a year ([2026-02-17](https://www.reddit.com/r/SaaS/comments/1r79c87/)).
- One post cuts against a trust page. A small SaaS company supplied a completed questionnaire, a penetration test and a SOC 2 Type II report and still lost a $14k deal because of its size ([2026-03-26](https://www.reddit.com/r/SaaS/comments/1s49gi3/)).
- Cheap substitutes are plentiful:
  - Orbiq's free trust centre.
  - At least 8 AI questionnaire fillers.
  - Open-source trustreply (2026-05) and TrustSite (2026-08-21).
- The MSP cyber-insurance variant above is less crowded.

**#10 Cyber Resilience Act 24h/72h reporting and SBOM diff: competition moves to Fail; reject.**
- Only one Reddit post turned up, and its author had already found a platform ([2026-02-17](https://www.reddit.com/r/Compliance/comments/1r7jj6a/)).
- [CRA Evidence](https://craevidence.com/platform) already has 24h/72h/14-day countdowns, SBOM drift detection and VEX authoring.
- Free tools also exist: the i46 analyser, sbomify (which notes that ENISA's platform had "no reporting API at launch") and OWASP Dependency-Track.

**Data-subject request (DSAR) handling for small businesses: reject.**
- The posts are questions, not buyers ([2026-03-18](https://www.reddit.com/r/gdpr/comments/1rx1z67/); [2026-09-12](https://www.reddit.com/r/gdpr/comments/1we3jgb/), where a 4-person SaaS company was quoted €490–2,000+).
- Termly, Enzuzo and Osano offer free or cheap plans, and Ethyca Fides is open source.

**#6 WISP manager: a possible channel.** MSPs look for GLBA and HIPAA program trackers and say existing policy generators aren't state-specific ([2025-02-11](https://www.reddit.com/r/msp/comments/1incum3/)). A maintained WISP sold through MSPs is worth one question in the interviews for #6.

**#2 Evidence locker: the pattern recurs.** Examples are an expired SOC 2 report, a COI-tracker entrant at $49/month ([2025-06-16](https://www.reddit.com/r/Compliance/comments/1lcu384/)), and anniversary tracking for workplace-violence training in Minnesota assisted living.
