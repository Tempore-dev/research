# Nonprofits, HOAs, child care, education, pharmacy, nursing, medical devices, food and other: Reddit sweep notes

> **How this was gathered (2026-09-25).** Reddit's anonymous search feeds returned 492 posts from 2024 onwards, and all of them were read. By subreddit:
>
> | Subreddit | Posts | Subreddit | Posts |
> |---|---|---|---|
> | r/specialed | 49 | r/restaurantowners | 38 |
> | r/ECEProfessionals | 48 | r/QualityAssurance | 36 |
> | r/HOA | 44 | r/labrats | 36 |
> | r/nursing | 42 | r/TravelAgents | 28 |
> | r/MedicalDevices | 41 | r/nonprofit | 27 |
> | r/pharmacy | 40 | r/foodsafety | 23 |
> | r/Accounting | 40 | | |
>
> The feeds return **post bodies only**, without comments or votes. Four feeds returned nothing even on simple retries: r/medicalbilling ("not found"), r/Daycare (repeated rate limits), r/Dentistry and r/CannabisIndustry.

## Near miss: do-it-yourself multi-state charitable solicitation registration for small nonprofits

**Workflow.** Small US nonprofits that fundraise nationally must register and renew in about 40 jurisdictions, each with its own forms. Only 37 accept the Uniform Registration Statement ([FPLG](https://www.fplglaw.com/insights/multistate-charitable-solicitation-registration/)). Today they pay a filing service or do it by hand.

**Driver: the vendors have consolidated.** Harbor Compliance bought Labyrinth in October 2021 ([Harbor](https://www.harborcompliance.com/blog/harbor-compliance-announces-acquisition-of-labyrinth/)), and Labyrinth bought Smart Charity on 2024-09-19 ([PRWeb](https://www.prweb.com/releases/harbor-compliance-announces-acquisition-of-smart-charity-by-its-nonprofit-brand-labyrinth-inc-302253420.html)). Harbor says it supports over half of all nonprofits registered nationwide ([Harbor](https://www.harborcompliance.com/fundraising-registration), vendor-written).

**Reddit evidence.**
- [2026-01-23](https://www.reddit.com/r/nonprofit/comments/1ql04t5/): a very small nonprofit registered in all 50 states says Labyrinth's quality and responsiveness have dropped while its prices rise. It is considering doing the work in-house.
- [2025-05-29](https://www.reddit.com/r/nonprofit/comments/1kykadn/): a paying Labyrinth customer, unhappy with the service, asks what others use.
- [2024-01-25](https://www.reddit.com/r/nonprofit/comments/19fc6ba/): a new operations hire at a nonprofit that pays Cogency is confused about which filings go to the Secretary of State and which to the Attorney General.
- Several single-state "do I need to register" questions show confusion, not paid demand.

**Competition (checked 2026-09-25).**
- *Services:* Labyrinth/Harbor, Cogency, Affinity Fundraising Registration, Foundation Group and RegiSTAR-US. They quote on request today. A 2020 comparison listed Labyrinth at about $175 per state per year, or about $4,950 for all jurisdictions ([Pro Bono Partnership of Atlanta](https://pbpatl.org/wp-content/uploads/2020/08/Comparison-of-Charitable-Solicitation-Compliance-Companies-Aug-2020.pdf)).
- *Software:* Harbor sells License Manager for firms doing it themselves. [CharityIQ US](https://www.charityiq.us/blog/compliance/charitable-solicitation-registration/) is a 2026 AI tracker whose premium tier is in early access.
- *App Store:* no apps.

**Barrier and gates.** A deadline tracker is easy to build. The value lies in a rules and forms database for about 40 jurisdictions that changes every year, which means continuous research. There is no licence or data gate.

**Scorecard.** Frustration Partial · Barrier Partial · Gate Pass · Alternatives Partial · Paying base Unknown.

**Next test.**
1. Get current Labyrinth and Affinity quotes. If the fee for all states is still around $5,000 a year or less, doing it yourself does not repay the staff time.
2. **Kill** if CharityIQ US ships a working tracker for under $500 a year.
3. **Kill** if no source shows at least about 5,000 nonprofits registered in 10 or more states.

## Rejected

| Workflow | Evidence | Why rejected |
|---|---|---|
| SQMS No. 1 quality-management documentation for small CPA firms (in force 2025-12-15) | [2026-07-23](https://www.reddit.com/r/Accounting/comments/1v40dd4/): a new audit director found "literally nothing" documented | Crowded. AICPA gives members free practice aids, risk libraries and templates ([Journal of Accountancy](https://www.journalofaccountancy.com/news/2025/aug/aicpa-unveils-new-qm-resources-to-help-firms-meet-dec-15-deadline/)). CPA.com's QMCore and AuditFile QualityLink (launched 2025-12-04) also compete |
| PBM audit response for independent pharmacies | [2025-11-14](https://www.reddit.com/r/pharmacy/comments/1oxc5vd/), [2024-08-26](https://www.reddit.com/r/pharmacy/comments/1f1rrej/), [2025-02-26](https://www.reddit.com/r/pharmacy/comments/1iym8r0/): 130 pages due in 2 days by fax | Crowded, by an incumbent staffed with experts. [PAAS National](https://paasnational.com/buy-now/) charges $559/year for audit help, and appeal expertise is the value |
| Seller-of-travel registrations (CA, FL, WA, HI) | [2024-09-20](https://www.reddit.com/r/TravelAgents/comments/1fkz8vy/) | A one-off setup with a small recurring burden, and host agencies absorb it |
| IEP timelines and service-minute compliance | Washington's IEP Online 3.0 called "flat out unusable" ([2026-09-22](https://www.reddit.com/r/specialed/comments/1wnmw1g/)). [2026-02-13](https://www.reddit.com/r/specialed/comments/1r42j1k/): IEPs written on evenings and weekends | Gated: districts and states choose the system of record, and FERPA applies |
| HACCP, SQF and FSMA plan builder for small food makers | [2026-02-13](https://www.reddit.com/r/foodsafety/comments/1r3lkzu/), [2025-04-23](https://www.reddit.com/r/foodsafety/comments/1k5y8iq/) (a developer's free tool) | Crowded. FoodReady costs about $99–199/month and FoodDocs $199–299/month |
| Licence and CE tracking for nurses and pharmacists across states | [2026-08-19](https://www.reddit.com/r/nursing/comments/1vsoz8d/) (complaints about fees) | Crowded. Nursys e-Notify and NABP CPE Monitor are free. The buyer would have to be the employer |
| USP 797/800 logs; small-lab chemical inventory; restaurant permit renewals; hood-cleaning reports; child-care staffing ratios; ISO 9001:2026; test-traceability exports | One post or none each | No paying demand, or crowded |

## Bears on the study's ranked items

- **#11 Family child-care CACFP app: no support.** None of the 48 r/ECEProfessionals posts mention CACFP, meal claims, brightwheel or Procare, and the r/Daycare feed could not be read. Home providers may not post on Reddit, so this shows only that Reddit is a weak channel for them.
- **#13 Florida HOA/condo portal: the pain is supported, but so is the crowding.**
  - *Pain:* a Florida board took about 6 hours to reassemble vendor bids under HB 1021 ([2025-12-24](https://www.reddit.com/r/HOA/comments/1pup12n/)). A board secretary spends an hour per records request ([2026-08-17](https://www.reddit.com/r/HOA/comments/1vr5i9u/)).
  - *Outside Florida:* a Utah ombudsman opinion (AO 2026-28, 2026-07-14) reportedly widens members' access to records ([2026-07-21](https://www.reddit.com/r/HOA/comments/1v2ii5r/); not verified).
  - *Crowding:* at least three 2026 posts are founders testing an idea ([2026-08-31](https://www.reddit.com/r/HOA/comments/1w38q1b/), [2026-08-10](https://www.reddit.com/r/HOA/comments/1vkdwyy/), [2026-01-07](https://www.reddit.com/r/HOA/comments/1q62i31/)). New apps include HOA Board (August 2026), HOA Start and EasyHOA.
  - This is consistent with the tracker's "self-managed HOAs crowded" rejection.
- **Lightweight eQMS for medtech (do not build): confirmed and more crowded.** One post says Greenlight Guru is too expensive ([2026-03-31](https://www.reddit.com/r/MedicalDevices/comments/1s8cj89/)). New builders include an Excel CAPA system ([2026-04-16](https://www.reddit.com/r/MedicalDevices/comments/1smppon/)) and a free AI gap tool ([2025-12-22](https://www.reddit.com/r/MedicalDevices/comments/1pt75sl/)).
- **DSCSA (do not build): confirmed.** A hospital had half its items quarantined through a third-party vendor ([2025-11-19](https://www.reddit.com/r/pharmacy/comments/1p1dwvy/)). An independent pharmacy is confused about software and cost ([2026-05-28](https://www.reddit.com/r/pharmacy/comments/1tqc23j/)). The pain is locked to wholesalers and vendors.
- **#7 Provider credential tracker: the failures are real, but individuals won't pay.**
  - A telehealth nurse worked in states before her licences were issued, despite her employer's credentialing team ([2026-09-11](https://www.reddit.com/r/nursing/comments/1wd54cq/)).
  - A pharmacist holding 12 state licences missed Tennessee's live-CE rule ([2025-03-04](https://www.reddit.com/r/pharmacy/comments/1j38k8w/)).
  - The buyer has to be the employer or credentialing team, not the clinician.
