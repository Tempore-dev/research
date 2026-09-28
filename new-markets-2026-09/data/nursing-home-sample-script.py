#!/usr/bin/env python3
"""
Reproducible sample construction for Task 1 (Tempore desk test).

IMPORTANT CONTEXT: The CMS Provider Data Catalog (data.cms.gov) and
Medicare.gov Care Compare were UNREACHABLE from this research environment
(outbound HTTPS to data.cms.gov, www.medicare.gov, and virtually all other
external domains returned "EGRESS_BLOCKED" / HTTP 403 from the sandbox's
network egress proxy -- confirmed via direct curl and via the WebFetch tool;
only a short allowlist of software-package domains, e.g. raw.githubusercontent.com,
was reachable). Because the CMS dataset itself could not be fetched (no CSV/API
pull was possible), this is a CONVENIENCE SAMPLE, not a true random sample
drawn from the CMS sampling frame, per the task's documented fallback
instructions. Candidate facility names/cities were identified via the
WebSearch tool (which performs server-side web search/summarization and was
not subject to the same egress block) from chain operators' own location
pages, ProPublica Nursing Home Inspect summaries surfaced in search results,
and directory/nonprofit sources. All facilities below were found via named,
citable search-result sources (see testA-findings.md for each one's specific
source URL used for the free-help evidence check).

Method:
1. Built two candidate pools per state: "chain" (facility name matches a
   known multi-state/multi-facility nursing home operator: Life Care Centers
   of America, Genesis HealthCare, NSPIRE Healthcare/Consulate/Independence
   Living Centers, Priority Healthcare Group, HCR ManorCare) and
   "independent" (single-facility or single-market nonprofit/county/church
   -sponsored operators identified by name, e.g. "County", "Manor" (church or
   county sponsored), "Presbyterian Homes", "Jewish Health", Archdiocese-run).
2. Candidate pools were sorted alphabetically by facility name (deterministic
   ordering) to remove any incidental ordering bias from search result order.
3. python random.seed(42) was used with random.sample() to draw the final
   selections without replacement whenever a pool was larger than the number
   needed. Where a pool was smaller than or equal to the number needed, all
   candidates in that pool were kept (documented explicitly below).
"""
import random, csv, json

FL_CHAIN = sorted([
    ("Life Care Center of Orlando", "Orlando, FL", "Life Care Centers of America"),
    ("Life Care Center of Palm Bay", "Palm Bay, FL", "Life Care Centers of America"),
    ("Life Care Center of Altamonte Springs", "Altamonte Springs, FL", "Life Care Centers of America"),
    ("Life Care Center of West Palm Beach", "West Palm Beach, FL", "Life Care Centers of America"),
    ("Life Care Center of Estero", "Estero, FL", "Life Care Centers of America"),
    ("Life Care Center of Palm Beach Gardens", "Palm Beach Gardens, FL", "Life Care Centers of America"),
    ("Life Care Center of Hilliard", "Hilliard, FL", "Life Care Centers of America"),
    ("Life Care Center of Lauderhill", "Lauderhill, FL", "Life Care Centers of America"),
    ("Genesis HealthCare - Oakhurst", "Ocala, FL", "Genesis HealthCare"),
    ("NSPIRE Healthcare Lauderhill", "Lauderhill, FL", "NSPIRE Healthcare (ex-Consulate)"),
    ("NSPIRE Healthcare Plantation", "Plantation, FL", "NSPIRE Healthcare (ex-Consulate)"),
    ("Consulate Health Care of North Ft. Myers", "North Fort Myers, FL", "Consulate/Independence Living Centers"),
    ("Consulate Health Care of St. Pete", "St. Petersburg, FL", "Consulate/Independence Living Centers"),
])

FL_INDEP = sorted([
    ("Susanna Wesley Health Center", "Hialeah, FL", "Independent nonprofit"),
    ("Seminole Nursing Pavilion", "Seminole/Temple Terrace, FL", "Independent (ownership unverified)"),
    ("Glades Health Care Center", "Belle Glade area, FL", "Independent (ownership unverified)"),
    ("Florida Presbyterian Homes (Westminster Lakeland / Porter-McGrath Health Center)", "Lakeland, FL", "Independent nonprofit CCRC"),
    ("Presbyterian Homes of Port Charlotte", "Port Charlotte, FL", "Independent nonprofit"),
    ("Miami Jewish Health", "Miami, FL", "Independent nonprofit"),
    ("St Anne's Nursing Center and Residence", "Miami, FL", "Independent nonprofit (Archdiocese of Miami)"),
])

PA_CHAIN = sorted([
    ("Genesis HealthCare - Hopkins Center", "Wyncote, PA", "Genesis HealthCare"),
    ("Genesis HealthCare - Uniontown", "Uniontown, PA", "Genesis HealthCare"),
    ("Genesis HealthCare - King of Prussia Skilled Nursing and Rehabilitation", "King of Prussia, PA", "Genesis HealthCare"),
    ("Genesis HealthCare - Pennsburg Manor", "Pennsburg, PA", "Genesis HealthCare"),
    ("Genesis HealthCare - Gettysburg Center", "Gettysburg, PA", "Genesis HealthCare"),
    ("Genesis HealthCare - Quakertown", "Quakertown, PA", "Genesis HealthCare"),
    ("Priority Healthcare Group - Gardens at Camp Hill", "Camp Hill, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Gardens at West Shore", "Camp Hill, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Gardens at Easton", "Easton, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Gardens for Memory Care at Easton", "Easton, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Gardens at Gettysburg", "Gettysburg, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Gardens at Millville", "Millville, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Gardens at Orangeville", "Orangeville, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Gardens at York Terrace", "Pottsville, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Gardens at Stevens", "Stevens, PA", "Priority Healthcare Group"),
    ("Priority Healthcare Group - Nursing and Rehabilitation at the Mansion", "Sunbury, PA", "Priority Healthcare Group"),
    ("HCR ManorCare - Bethel Park", "Bethel Park, PA", "HCR ManorCare"),
    ("HCR ManorCare - Williamsport North", "Williamsport, PA", "HCR ManorCare"),
    ("HCR ManorCare - Whitehall Borough", "Whitehall, PA", "HCR ManorCare"),
    ("HCR ManorCare - Peters Township", "McMurray, PA", "HCR ManorCare"),
    ("HCR ManorCare - Chambersburg", "Chambersburg, PA", "HCR ManorCare"),
    ("HCR ManorCare - Yeadon", "Yeadon, PA", "HCR ManorCare"),
])

PA_INDEP = sorted([
    ("Neshaminy Manor", "Warrington, PA", "County-owned (Bucks County)"),
    ("Pickering Manor", "Newtown, PA", "Independent nonprofit"),
    ("Moravian Manor", "Lititz, PA", "Independent nonprofit"),
    ("Christ The King Manor", "DuBois, PA", "Independent nonprofit"),
    ("Holy Family Manor", "Bethlehem, PA", "Independent nonprofit"),
])

random.seed(42)

# FL: pool sizes (13 chain + 7 independent = 20) exactly match target of 20, so all are kept.
fl_chain_sample = FL_CHAIN[:]  # all 13 kept (pool == need not larger)
fl_indep_sample = FL_INDEP[:]  # all 7 kept
random.shuffle(fl_chain_sample)  # order randomized for presentation only, seed=42
random.shuffle(fl_indep_sample)

# PA: chain pool (22) > need (15), so random.sample without replacement.
pa_chain_sample = random.sample(PA_CHAIN, 15)
pa_indep_sample = PA_INDEP[:]  # all 5 kept (pool == need not larger; need 5 to reach 20 total)

rows = []
for name, loc, own in fl_chain_sample:
    rows.append(dict(name=name, state="FL", location=loc, chain_or_independent="Chain", chain_name=own))
for name, loc, own in fl_indep_sample:
    rows.append(dict(name=name, state="FL", location=loc, chain_or_independent="Independent", chain_name=own))
for name, loc, own in pa_chain_sample:
    rows.append(dict(name=name, state="PA", location=loc, chain_or_independent="Chain", chain_name=own))
for name, loc, own in pa_indep_sample:
    rows.append(dict(name=name, state="PA", location=loc, chain_or_independent="Independent", chain_name=own))

print(f"FL total: {len(fl_chain_sample)+len(fl_indep_sample)} (chain={len(fl_chain_sample)}, indep={len(fl_indep_sample)})")
print(f"PA total: {len(pa_chain_sample)+len(pa_indep_sample)} (chain={len(pa_chain_sample)}, indep={len(pa_indep_sample)})")
print(f"GRAND TOTAL: {len(rows)}")

with open("/tmp/claude-0/-home-user/5c05aaba-3aeb-5104-be6f-7a7e097b2ad8/scratchpad/testA-data/sample_40.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name","state","location","chain_or_independent","chain_name"])
    w.writeheader()
    for r in rows:
        w.writerow(r)

for r in rows:
    print(r)
