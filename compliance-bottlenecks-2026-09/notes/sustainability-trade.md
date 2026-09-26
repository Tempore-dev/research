# Sustainability, Trade and Supply-Chain Compliance Bottlenecks: Practitioner Pain Points and Software Opportunities (EU/UK/US, as of September 2026)

> **Method note for the report writer.** Research ran on 2026-09-25. Most primary practitioner forums could NOT be fetched from this environment. Reddit, Trustpilot, Shopify Community, MDPI, WEF, IntegrityNext, Holland & Knight and Envirotec were all blocked by the egress proxy, and the web-search budget ran out before UK-specific and Prop 65 queries could run. Practitioner quotes below come from search-result snippets of those pages, not full-page reads, so treat them as **near-verbatim**. Where a figure comes from a vendor blog, not an independent source, it is flagged **[vendor]**. Regulatory dates were checked against several law-firm or official sources where possible.

## Q1. Which compliance tasks do practitioners describe as the biggest time sinks, the most manual work (spreadsheets, emailing suppliers) or the biggest source of anxiety? What time and cost figures do they cite?

### Takeaway
The recurring time sink in every regime is the same: **getting data out of upstream suppliers**. That means ESG questionnaires for CSRD customers, installation-level emissions for CBAM, plot geolocation for EUDR, deep-tier trace documents for UFLPA, SKU-level packaging material weights for EPR, and test reports and certificates for GPSR, CPSC and Amazon. For small US importers, the main anxieties in 2025–26 were per-parcel brokerage costs after de minimis ended, HTS/Chapter 99 classification errors and whipsawing tariff legal bases. Reliable time-per-task figures from practitioners are scarce. Cost figures are mostly per-parcel fees, subscription prices and detention costs.

### Cited Findings

**Supplier ESG data requests (CSRD trickle-down, EcoVadis-style questionnaires)**
- A representative survey of **431 Dutch SMEs plus 48 qualitative interviews** found that SMEs embedded in international value chains report "more frequent and complex data demands, particularly concerning environmental indicators like CO2 emissions and material use." — [MDPI Sustainability 17(17):8029](https://www.mdpi.com/2071-1050/17/17/8029) (abstract via search; full text blocked)
- A 2025 survey by the European Federation of Accountants reportedly found **>60% of large companies planned to request sustainability data from SME suppliers** within the first two years of CSRD. — surfaced in search results alongside [CSRDpro](https://www.csrdpro.com/en/sme-sustainability-data-requests/). Original survey not verified.
- EcoVadis's own chief customer officer acknowledged the problem: "Receiving disparate ESG assessments from multiple customers can be daunting for suppliers – most are redundant, asking for similar disclosures." — [BusinessWire (EcoVadis press release, Mar 2024)](https://www.businesswire.com/news/home/20240312100192/en)
- Supplier complaints about EcoVadis on Trustpilot (near-verbatim from snippets):
  - The questionnaire was "insanely lengthy and irrelevant to what they supply", with subscription costs reaching **$8,550**.
  - EcoVadis requests "the same information from an HR services company as they do from a foundry".
  - "The report generated was useless", and it was "a subscription-based service with auto-renewals" that was not clearly disclosed.
  - One supplier had issues unresolved "over two years".
  - "The cost of assessments is very high, which leads to low intake when trying to get suppliers to sign up" (a buyer-side view).
  - Source: [Trustpilot – EcoVadis](https://www.trustpilot.com/review/ecovadis.com), [p.2](https://www.trustpilot.com/review/ecovadis.com?page=2)
- The World Economic Forum's COO/Supply Chain/Procurement community launched an effort (Jan 2026) to **harmonise the environmental data request forms SMEs receive**, framed as "swapping spreadsheets for solutions". — [WEF, Jan 2026](https://www.weforum.org/stories/2026/01/building-smarter-climate-reporting-for-smes/) (title and snippet only)

**EUDR (deforestation) – geolocation and supplier cooperation**
- In an Interu/Censuswide survey of **300 European timber and forest-risk commodity operators** (Jan 2024), **58%** said their suppliers were "unwilling or unable" to support traceability efforts. — [Interu readiness report](https://www.interu.io/deforestation-regulation-readiness-report)
- Due diligence statements (DDS) must contain geolocation coordinates to **six decimal places for every plot**. Goods from plots without geolocation "cannot be placed on the EU market." — [Coolset EUDR geolocation guide](https://www.coolset.com/academy/eudr-geolocation-requirements-how-to-collect-and-validate-gps-polygon-data-for-your-dds) **[vendor]**; [Lawcode](https://www.lawcode.eu/en/blog/eudr-geo-data/)
- EUDR "asks for plot-level traceability across supply chains that were never built to be traceable, in commodities where the first mile is frequently thousands of smallholders with no formal land documentation." — [Regilient](https://www.regilient.ai/blog/eudr-due-diligence-product-traceability-compliance) **[vendor]**
- The IISD surveyed and interviewed **333 farmers across 16 countries**. Barriers they named were land tenure, compliance cost, traceability, geolocation and limited technical capacity. — [IISD](https://www.iisd.org/publications/report/smallholders-european-union-deforestation-regulation); see also [Mongabay interview, Dec 2025](https://news.mongabay.com/2025/12/se-asias-smallholders-struggling-to-meet-eudr-interview-with-recoftcs-martin-greijmans/)
- Fairtrade **extended its internal timeline** for cooperatives to finish geolocation data collection. — [Fairtrade](https://www.fairtrade.net/en/fairtrade-extends-timeline-for-cooperatives-to-complete-geolocation-data-collection.html)
- Cost: EUDR compliance averages **0.10% of revenue**. The burden is about **3x heavier for SMEs (0.17%) than for large firms (0.06%)**, and the maximum observed was 0.32%. — [Farmforce](https://farmforce.com/articles/the-real-cost-of-eudr-compliance-what-agri-commodities-companies-need-to-know/) **[vendor; methodology unknown]**

**CBAM – embedded-emissions data from non-EU suppliers**
- Importers must "collect actual emissions from suppliers, calculate CBAM cost, and report via the CBAM Registry". Non-EU producers must supply data "calculated at the production installation level", and "without this information, EU importers cannot complete their CBAM reports accurately." — [Asuene](https://asuene.com/us/blog/cbam-enters-its-definitive-phase-on-january-1-2026-what-companies-must-be-ready-for), [Carbonchain](https://www.carbonchain.com/cbam) **[vendors]**
- Fallback default values "are designed to be conservative and assume higher emissions than typical production". The Commission replaced two default-value annexes with effect from 1 Jan 2026. — [Carbonchain](https://www.carbonchain.com/cbam), [Integritynext CBAM 2026](https://www.integritynext.com/resources/blog/article/mastering-cbam-compliance-in-2026-latest-updates-and-how-companies-should-prepare)
- From 2026, non-EU exporters need their emissions **verified by a third party**. — [Cortex AIF](https://cortex-aif.com/blog/cbam-embedded-emissions-verification-2026) **[vendor]**
- During the transitional phase, the old low threshold "burdened SMEs with complex compliance and data acquisition challenges". Evidence showed "fewer than 20% of companies are cause of over 95% of CBAM-covered emissions". — [ICAP](https://icapcarbonaction.com/en/news/eu-adopts-simplifications-cbam-rules-ahead-compliance-phase-starting-2026) / [Umweltbundesamt](https://www.umweltbundesamt.de/en/press/pressinformation/cbam-simplified-90-of-companies-exempt-from-co2)

**US customs for small importers (de minimis end, HTS, tariffs)**
- Per-parcel formal entry now costs roughly **$15–25 in brokerage and processing**. An industry expert quoted by NBC said: "On your average de minimis shipment, paying a customs broker and paying the fees will double the cost… That's before you even get to the money that's actually going to the government." — [NBC News](https://www.nbcnews.com/business/consumer/de-minimis-exemption-ends-low-value-packages-shipped-us-need-know-rcna227772); [GingerControl](https://gingercontrol.com/blog/de-minimis-repeal-small-importer-impact)
- For parcels under about $200, the fixed cost of customs processing (brokerage, MPF, ISF, entry filing) "often exceeds the duty itself". — [GingerControl](https://gingercontrol.com/blog/de-minimis-repeal-small-importer-impact), [Importivity](https://importivity.com/blog/de-minimis-exemption-ended/)
- On the resource gap: "a small boutique owner importing $200,000 of products from China is paying the tariff broker and trying to figure it out with a Google search and a CPA who's never dealt with HTS codes", while Walmart has full-time trade lawyers. — [TariffTax](https://www.tarifftax.org/analysis/small-business-impact) / [SCXchange](https://www.thescxchange.com/finance-strategy/procure/tariffs-smbs)
- Importers are "wistful of the days when politics played a smaller role in their spreadsheets." — [Freightos, "Stability Without Relief"](https://www.freightos.com/freight-resources/stability-without-relief-small-importers-still-strained-by-tariffs/)
- Netstock 2026 SMB tariff survey **[vendor survey]**:
  - **72%** of SMBs cite cost-related challenges, led by increased landed costs (**56%**).
  - **96%** expect tariffs to be their primary 2026 concern.
  - **31%** expect a "significant to devastating" impact.
  - Source: [Netstock 2026 Tariff Impact Report](https://www.netstock.com/research/2026-tariff-impact-report/)
- Classification errors **[vendor figures; primary source not located]**:
  - About **40% of import entries contain classification errors**, and misclassification accounts for **42% of CBP assessments**.
  - The most common small-importer mistake is using the supplier's Chinese HS code unconverted.
  - Missing the Chapter 99 add-on is the most common Section 301 error.
  - Source: [Unicargo](https://www.unicargo.com/hs-code-mistakes-importers-2026/)
- The importer of record stays liable even when using a broker: "If the classification is wrong, CBP penalizes you." Negligence penalties run up to **2x lawful duties or 20% of dutiable value**. — [Beancount.io](https://beancount.io/blog/2026/05/10/hts-codes-tariff-classification-small-importers-2026-importer-of-record-liability-customs-broker-guide); [Gaia Dynamics](https://www.gaiadynamics.ai/blog/penalties-for-wrong-hts-codes-cbp-fines-audit-risk-and-how-to-fix-misclassification)
- CBP completed **200 audits in the first four months of 2025**, recovering **$134M**, a 67% increase year on year. — [Gaia Dynamics](https://www.gaiadynamics.ai/blog/cbp-tariff-classification-101-what-importers-must-know-in-2026) **[vendor; not verified against CBP]**
- DOJ reached a **$54.4M settlement with Ceratizit USA (Dec 2025)** over misclassification and false country of origin used to avoid Section 301. — [Unicargo](https://www.unicargo.com/hs-code-mistakes-importers-2026/)

**UFLPA (forced labour)**
- UFLPA flips the burden of proof: importers must show "by clear and convincing evidence" that goods are not linked to forced labour. That requires documents "traced from the imported good back to raw material extraction or harvest", including ground transport logs. — [CBP UFLPA FAQ](https://www.cbp.gov/trade/forced-labor/faqs-uflpa-enforcement); [Kharon](https://www.kharon.com/resources/use-cases/forced-labor/uflpa-enforcement-and-compliance-strategy)
- "Even importers with extensive documentation often fail because their suppliers cannot or will not provide the deep-tier trace." — [Greenwich Mercantile](https://www.greenwich-mercantile.com/forced-labor-uflpa)
- Cost of a single detention case: **over $810,000** (Oritain 2024 report). Average detention exceeds **90 days**, and some shipments were held more than six months. **Over 8,000 shipments were detained in 2025, valued at over $3.8B.** — [Camtom](https://www.camtomx.com/en/blog/uflpa-forced-labor-import-ban-compliance) / [Kisun Shipping](https://kisunshipping.com/uflpa-enforcement-2026-china-importers-compliance-guide/) **[vendor aggregators; CBP dashboard not checked]**
- CBP issued "comprehensive forced labor guidance" in July 2026. — [Holland & Knight, Jul 2026](https://www.hklaw.com/en/insights/publications/2026/07/new-compliance-tools-cbp-issues-comprehensive-forced-labor-guidance); [Stile Intl](https://stileintl.com/cbp-forced-labor-enforcement-guidance-importers-2026/)

**Packaging EPR (US states) – SKU-level data**
- Oregon requires **SKU-level reporting**. The California, Colorado and Oregon annual supply reports need the most granular data. "The core challenge is packaging data accuracy at the material and SKU level, not the act of registering with a PRO." — [EcoEnclose](https://www.ecoenclose.com/resources/epr-packaging-requirements), [Zenpack](https://www.zenpack.us/blog/us-packaging-epr-compliance-guide/)
- A producer chasing all Colorado and Oregon eco-modulation bonuses may need to file **up to seven separate forms or report packages**, each with SKU-level detail. — [Proskauer 2025 EPR guide](https://www.proskauer.com/alert/the-2025-guide-to-epr-packaging-compliance) / [Certivo](https://www.certivo.com/blog-details/navigating-us-state-packaging-epr-laws-2026-compliance-guide)
- Holland & Knight published "2026 EPR Reporting: Lessons Learned from the Initial Consolidated Reporting Round" (Jul 2026) and "Are You Ready to Report Your Packaging Data Next Month?" (Apr 2026). The full text was blocked. — [H&K Jul 2026](https://www.hklaw.com/en/insights/publications/2026/07/2026-epr-reporting-lessons-learned-initial-consolidated-reporting), [H&K Apr 2026](https://www.hklaw.com/en/insights/publications/2026/04/are-you-ready-to-report-your-packaging-data-next-month)

**Product safety for e-commerce sellers (GPSR, Amazon, CPSC)**
- A Shopify Community thread is titled "EU/NI General Product Safety Regulations (GPSD / GPSR), **Total Nightmare**". Complaints in it:
  - Finding an affordable EU Responsible Person (services "typically €139+ annually").
  - Documentation for products "manufactured from multiple sourced components".
  - Confusion over Article 51 "grandfathering".
  - "How customs will verify compliance remains unknown."
  - Source: [Shopify Community](https://community.shopify.com/t/eu-ni-general-product-safety-regulations-gpsd-gpsr-total-nightmare/338849/11); also [Shopify thread for US businesses](https://community.shopify.com/t/forthcoming-gpsr-regulations-in-the-eu-for-us-based-businesses/378825/6)
- Amazon ended its Amazon Responsible Person service on **31 Mar 2024**, which pushed sellers to third parties. "Thousands of sellers… found their listings suspended or accounts restricted." — [EARP](https://earpcorp.com/helpful-articles/what-happened-to-sellers-using-the-amazon-responsible-person-service-after-it-ended-in-2024/), [Minefield Navigator](https://minefieldnavigator.com/en/knowledge-base/who-is-the-eu-responsible-person-and-why-amazon-sellers-need-one) **[vendors]**; also see the [Amazon Seller Forums thread](https://sellercentral.amazon.com/seller-forums/discussions/t/73744873-d8a8-4a84-a8ee-9e694e192827?postId=22aa0da5-5209-4b3f-8b79-e98564e6249f)
- Handmade and vintage items are **not exempt** from GPSR, which "surprises many small Etsy and Shopify sellers". — [Etsy Seller Handbook](https://www.etsy.com/seller-handbook/article/1093438529659); [24hour-ar "should you stop selling to the EU"](https://www.24hour-ar.com/eu-gpsr-etsy-should-you-stop-selling)
- Amazon compliance changes **[vendor summaries]**:
  - A July 2025 "lab compliance overhaul" requires **annual testing** of toys and children's products through a CPSC-accepted testing lab.
  - Amazon publishes a **Suspended Validation Labs list**. Documents from those labs are "treated as no documentation at all".
  - After a suspension, "the only way to start selling products again… is by submitting requested documents".
  - Sources: [ComplianceGate](https://www.compliancegate.com/amazon-product-compliance-document-requests-removals/), [Spacegoats](https://spacegoats.io/space-wiki/amazon-product-compliance/)
- **CPSC eFiling became mandatory on 8 Jul 2026.** Importers must file certificate data (GCC/CPC) in ACE before entry. It applies even to Section 321 de minimis-claimed shipments. Domestic manufacturers are exempt. — [CPSC press release](https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Implements-Mandatory-eFiling-for-Certificates-of-Compliance-Targeting-Dangerous-Foreign-Imports); [Foley](https://www.foley.com/p/102mvja/cpsc-efiling-begins-july-2026importers-of-consumer-products-are-you-ready/); [Akin](https://www.akingump.com/en/insights/alerts/cpsc-rule-mandates-efiling-of-certificates-of-compliance-for-imported-consumer-products)
- A law-firm press release (29 Aug 2026) highlights "new CPSC compliance challenges for Amazon sellers". — [GlobeNewswire / Valley & Summit Law](https://www.globenewswire.com/news-release/2026/08/29/3352923/0/en/valley-summit-law-highlights-new-cpsc-compliance-challenges-for-amazon-sellers.html)

### Inferences
- The largest time sinks share a structure: **one-to-many supplier data collection, with evidence attachments, re-requested annually and reformatted per customer or regulator**. A single "supplier evidence inbox" (request, chase, validate, reuse) appears in CSRD/VSME, CBAM, EUDR, UFLPA, EPR and GPSR/CPSC alike. That makes it the most reusable architecture for a small firm.
- The anxiety-inducing tasks are the ones with **binary, immediate consequences**: Amazon listing removal, CBP detention, and EUDR "cannot be placed on the market". They trigger urgent, paid demand from small sellers. Voluntary ESG reporting generates slower, softer demand.
- There are almost no credible "hours per task" figures from practitioners. Cost signals are per parcel ($15–25), per subscription (EcoVadis about $8.5k), per detention (about $810k) and share of revenue (EUDR 0.17% for SMEs, from a vendor).

### Gaps
- Reddit threads (r/ESG, r/sustainability, r/supplychain, r/FulfillmentByAmazon, r/importexport) could not be fetched, and no Reddit URLs with verbatim quotes were obtained. The report writer should not claim Reddit-sourced quotes from these notes.
- No independent survey gives hours spent per supplier questionnaire, per EUDR DDS or per CBAM declaration.
- The Holland & Knight "lessons learned" EPR piece (Jul 2026) would likely give concrete first-cycle reporting failures but was blocked.
- The primary SMEunited and BusinessEurope SME surveys were not located.

---

## Q2. Which tools do practitioners use (Excel, EcoVadis, Sphera, Persefoni, Watershed, Sweep, IntegrityNext, Avalara, Flexport, customs brokers, etc.), and what do reviews complain about?

### Takeaway
The de facto tools are **Excel/email, plus outsourced intermediaries**: customs brokers, EU Responsible Person services, the Circular Action Alliance PRO and testing labs. Enterprise platforms (Watershed, Persefoni, Sphera) cost $50k–200k+ a year and are aimed at large firms. Supplier-assessment networks (EcoVadis) draw complaints about cost, auto-renewal, irrelevant generic questionnaires and poor support. Specific G2/Capterra cons for Watershed, Persefoni, Sweep, Avalara and Flexport could not be retrieved.

### Cited Findings
- **EcoVadis:**
  - G2 average **4.2/5 from 92 reviews** (setup 8.2, meets requirements 8.3). — [G2 EcoVadis alternatives](https://www.g2.com/products/ecovadis/competitors/alternatives), [G2 reviews](https://g2.com/products/ecovadis/reviews)
  - Trustpilot supplier complaints: cost ($8,550 subscription), undisclosed auto-renewal, "insanely lengthy and irrelevant" questions, a one-size-fits-all questionnaire (HR services firm vs foundry), support issues unresolved for 2 years. — [Trustpilot](https://www.trustpilot.com/review/ecovadis.com)
  - Gartner Peer Insights also carries reviews (not read). — [Gartner](https://www.gartner.com/reviews/product/ecovadis)
- EcoVadis now offers a free "Vitals" questionnaire for low- and medium-risk suppliers, taking under an hour. This is an implicit admission that the full assessment was too heavy for SMEs. — [EcoVadis](https://resources.ecovadis.com/ecovadis-solution-materials/ecovadis-questionnaire-subs)
- **Carbon accounting price bands** **[vendor listicles]**:
  - Watershed and Persefoni: **$50,000–$200,000+/year**, aimed at large multi-entity organisations. Watershed "earns its cost when Scope 3 is genuinely complicated". Without that complexity, "you're paying for capability you won't touch."
  - Mid-market tools (Plan A, Normative, Sweep mid-tier): **$10,000–$50,000/year**, for firms with 500–5,000 employees.
  - Sources: [Normative](https://normative.io/insight/the-5-best-carbon-accounting-software-platforms-2026/), [OneStop ESG](https://onestopesg.com/esg-resources/leading-carbon-accounting-software-companies), [Gaia](https://gaiacompany.io/best-persefoni-alternatives/)
  - Watershed's G2/Capterra rating is about 4.5/5. — [aigreentools](https://aigreentools.com/ai_tool/watershed/)
- **ESG software market consolidation.** Diginex acquired Plan A (350+ corporate clients). This is described as part of a consolidation trend "already emerging throughout 2025". A German CSRD study calls the ESG software market "fragmented". — [Five Glaciers](https://en.fiveglaciers.com/post/esg-solutions-markt-2026-entwicklungen-ausblick), [CSR Tools study](https://csr-tools.com/en/blog-en/csrd-study-fragmented-esg-software-market/)
- **US EPR:** the Circular Action Alliance is the approved PRO in **6 of 7** EPR states (all but Maine). Producers file via CAA, so the "tool" is the PRO portal plus the producer's own SKU spreadsheets. — [EcoEnclose](https://www.ecoenclose.com/resources/epr-packaging-requirements), [CAA producer resource centre](https://circularactionalliance.org/producer-resource-center)
- **Customs:** small importers rely on brokers, but liability stays with the importer of record. — [Beancount.io](https://beancount.io/blog/2026/05/10/hts-codes-tariff-classification-small-importers-2026-importer-of-record-liability-customs-broker-guide)
- **GPSR:** a cottage industry of EU Responsible Person services has emerged (TBA Global, EU Compliance Partner, Eldris, EaseCert, etc.). — [TBA Global](https://tbaglobal.com/amazon_eurp/), [EU Compliance Partner](https://eucompliancepartner.com/amazon-gpsr-eu-responsible-person)
- A Trustpilot page exists for "GPSR Solutions" (3 reviews, content not read). — [Trustpilot GPSR Solutions](https://au.trustpilot.com/review/gpsrsolutions.com)
- **EUDR:** the EU Information System was immature and was one reason for the Oct 2024 postponement. The Dec 2025 amendment requires competent authorities to **report significant IT disruptions** to the Commission. — [Coolset reporting guide](https://www.coolset.com/academy/eudr-reporting-guide-for-operators) **[vendor]**, [EUDR.today](https://www.eudr.today/en/eu-information-system)

### Inferences
- Complaints centre on **price-to-relevance mismatch**: generic, long questionnaires sold on subscription to small suppliers who are paying only because a customer demands it. A tool that lets a supplier **answer once in the VSME format and share it with many customers for free or cheaply** targets the core EcoVadis grievance.
- Enterprise carbon platforms leave a gap below about $10k/year for firms with fewer than 500 employees. Most of those firms are now out of CSRD scope but still receive customer and bank requests.

### Gaps
- Specific G2/Capterra "cons" text for Watershed, Persefoni, Sweep, Sphera, IntegrityNext, Avalara (cross-border and duties) and Flexport was not retrieved (sites blocked or not reached before the search budget ran out).
- No data was found on which tools small US sellers use for CPSC eFiling (broker-filed vs self-filed via ACE), or on reviews of CBAM-specific tools.

---

## Q3. Where do SMEs and small sellers say nothing affordable or simple exists?

### Takeaway
The gaps named most clearly are:
- **Small/micro suppliers answering customer ESG requests** (hoping VSME will standardise them).
- **Small EU importers with occasional CBAM goods** (now mostly exempt below 50t, but they must monitor the threshold).
- **EUDR first-mile geolocation for smallholders and SME traders.**
- **US micro-importers facing per-parcel formal entry, HTS classification, CPSC eFiling and UFLPA tracing.**
- **Small multi-marketplace sellers needing GPSR, Amazon and CPSC document packs per SKU.**
- **Small brands facing multi-state SKU-level EPR reporting.**

### Cited Findings
- **VSME as the de facto SME format.** The VSME exists because SMEs face "growing sustainability data requests from business counterparties (banks, investors or larger companies)". It is expected to "reduc[e] the number of uncoordinated requests SMEs receive." It has a Basic and a Comprehensive module, no mandatory double materiality and no assurance. Banks and procurement teams already use it. — [EFRAG VSME](https://www.efrag.org/en/projects/voluntary-reporting-standard-for-smes-vsme/concluded), [Dcycle](https://dcycle.io/blog/vsme-voluntary-standard-smes-2026/), [Deutscher Nachhaltigkeitskodex](https://www.deutscher-nachhaltigkeitskodex.de/en/reporting-obligations/voluntary-sustainability-standards-for-smes-vsme/)
- **Value-chain cap.** Companies in scope may not demand more from value-chain partners with **≤1,000 employees** than the VSME-based voluntary standard specifies, and those partners "can refuse requests that exceed" it. — [CSSF Omnibus page](https://www.cssf.lu/en/omnibus-package/), [Accountancy Europe](https://accountancyeurope.eu/publications/omnibus-explained-key-changes-to-the-csrd-and-csddd/)
- **EUDR micro/small operators.** Micro and small primary operators in low-risk countries can file a **one-time simplified declaration** instead of repeated DDS. This "does not remove the need to collect plot geolocation and legality data". — [Coolset FAQ](https://www.coolset.com/academy/eudr-frequently-asked-questions), [Council press release 18 Dec 2025](https://www.consilium.europa.eu/en/press/press-releases/2025/12/18/deforestation-council-signs-off-targeted-revision-to-simplify-and-postpone-the-regulation/)
- **CBAM.** The 50-tonne threshold exempts about 90% of importers, "mainly SMEs and individuals". If an importer exceeds 50t **at any point in the year, all imports that year become subject** to CBAM, so small importers near the line must track cumulative mass. — [Umweltbundesamt](https://www.umweltbundesamt.de/en/press/pressinformation/cbam-simplified-90-of-companies-exempt-from-co2), [CBAM Guide de minimis](https://cbamguide.com/compliance/de-minimis/), [Climastry](https://climastry.com/blog/de-minimis-cbam)
- **US small importers.** The "Google search and a CPA who's never dealt with HTS codes" reality is described above. — [TariffTax](https://www.tarifftax.org/analysis/small-business-impact)
- An academic paper on tariff uncertainty and SME supply chains. — [Journal of Small Business Strategy](https://jsbs.scholasticahq.com/article/157795-the-impact-of-tariffs-and-trade-policy-uncertainty-on-sme-supply-chains) (not read)
- **GPSR.** Small sellers "struggle to find affordable EU representation" (€139+/yr), and small handmade sellers are not exempt. — [Shopify Community](https://community.shopify.com/t/eu-ni-general-product-safety-regulations-gpsd-gpsr-total-nightmare/338849/11), [Etsy Handbook FAQ](https://www.etsy.com/seller-handbook/article/1364599291081)
- **California SB 54.** Producers with **< $1M California gross sales** are exempt but **must still register with CalRecycle and apply for the exemption**. — [Trinity Consultants](https://trinityconsultants.com/resources/sb-54-january-2026-updates/), [Repurpose Global](https://www.repurpose.global/blog/californias-sb-54-is-approved-and-in-effect-your-deadline-remains-may-31-2026)
- **ESPR/DPP.** A KPMG DPP Readiness Survey (Feb 2026) is reported to find **81% of affected companies have no implementation plan**. SMEs get no general exemption, typically only an extra 12–18 months. — reported by [PassportCraft](https://passportcraft.com/insights/espr-timeline-what-brands-need-to-know) / [Narravero](https://www.narravero.com/en/blog/digital-product-passport-deadlines) **[vendors; KPMG original not verified]**

### Inferences (Tempore addressability, by gap)

| Gap | Addressable by a small web/mobile/desktop shop? | Notes |
|---|---|---|
| **VSME "answer once, share many" supplier portal + customer-request triage** (flag requests exceeding the value-chain cap) | **High** | Clear standard (VSME), legal hook (value-chain cap lets suppliers refuse excess), web app. Competition: many EU startups (Sunhat, Dcycle, Coolset, CSRDpro, Spectreco). Differentiate on very low price and on answering existing customer questionnaires (EcoVadis/CDP/custom Excel) by mapping them to VSME. |
| **Mobile field app for EUDR plot polygon capture** (offline GPS, 6-decimal precision, GeoJSON export to DDS, cooperative roll-ups) | **High technical fit, harder go-to-market** | Buyers are cooperatives, exporters and importers in producer countries. NGOs and Fairtrade are extending timelines. Competitors: Farmforce, TraceX, Global Traceability. A niche mobile plus desktop sync product is feasible. |
| **CBAM 50t threshold tracker + supplier emissions template collector** for EU SME importers | **Medium** | Small, well-defined tool (cumulative mass by CN code, alerts before 50t, supplier template chasing). The market narrowed by about 90% after the threshold, so the remaining firms are larger and bigger vendors serve them. |
| **US micro-importer landed-cost / HTS sanity-check + CPSC eFiling data prep** | **Medium-High** | Desktop or web tool that stores per-SKU HTS, Chapter 99 overlays, origin and certificate data (GCC/CPC fields) and exports to brokers. Liability and data risk mean it should be positioned as prep and verification, not advice. Tariff legal bases keep changing, so maintaining rate tables is costly. |
| **Per-SKU compliance document vault for marketplace sellers** (GPSR RP details, test reports, lab validity against Amazon's suspended-lab list, CPC/GCC, safety images, multilingual warnings) | **High** | Plain document and workflow software. Demand is urgent because of listing suspensions. Crowded with RP service firms, but few offer SKU-level vaults that span marketplaces. |
| **Multi-state EPR SKU packaging database** (material weights, per-state format exports for CAA, <$1M exemption registration) | **Medium-High** | Data-model problem suited to a small team. Well-funded competitors exist (e.g., Certivo, Zenpack-type guides). The first reporting cycles in 2026 created acute pain. |
| **UFLPA deep-tier trace document collector** | **Low-Medium** | Needs supplier cooperation that importers say they cannot get. Real value lies in risk data (Kharon etc.), which a small firm cannot replicate. |
| **Battery/DPP passport generator for SMEs** | **Medium, timing risk** | Battery passport is due 18 Feb 2027. Wider ESPR delegated acts are slipping, so demand for SME-level DPP beyond batteries is 2028+. |

### Gaps
- No direct SME quotes saying "nothing affordable exists" were retrieved from Reddit or LinkedIn. That framing is inferred from price bands and complaints.
- No EUDR-specific SME tool reviews were found.
- UK equivalents (UK CBAM from Jan 2027, UK packaging EPR fees, UK GPSR equivalents) were **not researched** because the search budget ran out.

---

## Q4. Which requirements were delayed, cut back or rescinded in 2025–2026, and how does that regulatory uncertainty affect demand for software?

### Takeaway
2025–26 brought large EU rollbacks. The CSRD scope was cut about 80%, the CSDDD was narrowed and pushed to 2029, the EUDR was delayed twice (now Dec 2026 / Jun 2027) and CBAM was trimmed by the 50t exemption. PPWR and ESPR implementing acts are late. In the US, SB 261 is enjoined, IEEPA tariffs were struck down (refunds pending) and the replacement Section 122 tariffs face litigation. Meanwhile, new hard obligations did arrive: CBAM definitive phase (Jan 2026), GPSR (Dec 2024), CPSC eFiling (Jul 2026), PPWR application (Aug 2026), SB 54 regulations (May 2026) and the Oregon/Colorado EPR reporting cycles. The pattern is that **large-company ESG reporting demand is shrinking, while operational, transaction-level compliance (customs, product safety, packaging, CBAM declarants) is growing**. Uncertainty also creates demand for tracking, refund and "optionality" tooling.

### Cited Findings

**EU CSRD / ESRS / VSME (Omnibus I)**
- Directive **(EU) 2026/470** was published in the Official Journal on **26 Feb 2026** and is in force from **18 Mar 2026**. Member States have 12 months to transpose it. — [CSSF](https://www.cssf.lu/en/omnibus-package/), [Latham](https://www.lw.com/en/insights/eu-sustainability-omnibus-published-in-the-official-journal)
- The scope is now **>1,000 employees AND >€450M net turnover** (cumulative). The first reports under the revised directive are expected in **2028 for FY2027**. — [CSSF](https://www.cssf.lu/en/omnibus-package/), [KPMG](https://kpmg.com/xx/en/our-insights/ifrg/2025/esrs-eu-omnibus.html), [PwC Viewpoint](https://viewpoint.pwc.com/gx/en/pwc/in-briefs/ib_int202527.html)
- One secondary source summarises the change as a "CSRD scope reduced by 80%", with ESRS datapoints cut from **1,100+ to an estimated 400–500**. — [financialregulations.eu](https://financialregulations.eu/blog/eu-omnibus-csrd-simplification-2026) **[secondary; datapoint estimate unverified]**
- A value-chain cap protects partners with ≤1,000 employees (see Q3).
- The **VSME delegated act** was adopted in July 2026, but **sources conflict on the date (3 July vs 19 July 2026)**. Vendors expect large companies to start formally requesting VSME data during Sep–Dec 2026. — [Spectreco](https://www.spectreco.com/blog/csrd-vsme-standard-2026-sme-suppliers-voluntary-reporting), [Dcycle](https://dcycle.io/blog/vsme-voluntary-standard-smes-2026/), [Sunhat](https://www.getsunhat.com/blog/csrd-vsme) **[vendors; verify on EUR-Lex]**
- Even with a narrower scope, "customer, investor, and value-chain data requests keep measurement essential" (a Watershed buyer's guide, i.e. a vendor view). — [Watershed](https://watershed.com/blog/esg-software-in-2026-the-buyers-guide)
- An analyst forecast puts the ESG reporting software market at **$1.31B (2026) → $2.93B (2031), a 17.4% CAGR**. — [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/esg-reporting-software-market-173110129.html) **[analyst forecast; low reliability]**
- Consolidation is under way (Diginex acquired Plan A). — [Five Glaciers](https://en.fiveglaciers.com/post/esg-solutions-markt-2026-entwicklungen-ausblick)

**CSDDD**
- The scope is now **>5,000 employees AND >€1.5B turnover**. Application is deferred to **July 2029**. The EU-harmonised civil liability regime was removed (left to national law), and the obligation to put a climate transition plan into effect was removed. Formally adopted Dec 2025; in force 18 Mar 2026. — [MoFo](https://www.mofo.com/resources/insights/251222-eu-sustainability-omnibus-i-detailed-omnibus), [DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/corporate-sustainability-due-diligence-directive-amendments-under-omnibus-i-finalised), [Arthur Cox](https://www.arthurcox.com/insights/omnibus-i-directive-published-revised-scope-and-reduced-obligations-under-csrd-and-csddd/), [ClientEarth critique](https://www.clientearth.org/latest/news/csddd-after-omnibus-i-legal-risks-maladministration-and-the-future-of-due-diligence/)

**EUDR**
- The first delay (Oct 2024) was driven partly by IT-system immaturity. — [Coolset timeline](https://www.coolset.com/academy/eudr-delay-2025-explained)
- The second revision was adopted by Parliament on 17 Dec 2025 and signed off by Council on 18 Dec 2025. Application is now **30 Dec 2026 (large/medium operators and traders)** and **30 Jun 2027 (micro/small)**. It simplified obligations for downstream operators and traders and added a one-time declaration for micro/small primary operators in low-risk countries. — [Council](https://www.consilium.europa.eu/en/press/press-releases/2025/12/18/deforestation-council-signs-off-targeted-revision-to-simplify-and-postpone-the-regulation/), [EC Access2Markets](https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation), [Bird & Bird](https://www.twobirds.com/en/insights/2025/out-of-the-woods-the-eudr-postponed-and-simplified), [Stibbe](https://www.stibbe.com/publications-and-insights/the-amended-eudr-what-has-changed-and-what-has-remained)
- The Commission's simplification review was due **by 30 Apr 2026**. It was published and characterised as "**Minor Simplifications, Same Deadline**". A Commission simplification package and new measures followed (May 2026). — [IntegrityNext (title)](https://www.integritynext.com/resources/blog/article/eudr-review-out-now-minor-simplifications-same-deadline), [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-deforestation-regulation-commission-publishes-simplification-package-ahead-of-december-2026), [GlobalELR May 2026](https://www.globalelr.com/2026/05/european-commission-releases-new-eu-deforestation-regulation-measures/)
- **Flag:** the exact contents of the April/May 2026 package were not read in full. Some sources note that timber-sector micro/small operators keep the Dec 2026 date. — [Coolset reporting guide](https://www.coolset.com/academy/eudr-reporting-guide-for-operators)

**CBAM**
- Regulation **(EU) 2025/2083**, in force **20 Oct 2025**:
  - Replaced the €150-per-consignment exemption with a **50-tonne/year per-importer threshold**, which exempts about 90% of importers but keeps about 99% of emissions in scope.
  - Delayed certificate surrender and simplified emissions reporting.
  - Importers who applied for authorised declarant status **before 31 Mar 2026** may continue importing pending a decision.
  - The first annual declaration and certificate surrender fall in **2027 for 2026 imports**.
  - Sources: [Slaughter and May](https://sustainability.slaughterandmay.com/post/102lr0h/eu-cbam-amended-to-exclude-90-of-importers-but-include-99-of-emissions), [Reed Smith](https://www.reedsmith.com/our-insights/blogs/viewpoints/102lr9t/what-you-need-to-know-as-cbam-simplification-comes-into-effect/), [Mayer Brown Oct 2025](https://www.mayerbrown.com/en/insights/publications/2025/10/eu-adopts-cbam-simplification-regulation-10-key-amendments-and-challenges-ahead), [Council 29 Sep 2025](https://www.consilium.europa.eu/en/press/press-releases/2025/09/29/cbam-council-signs-off-simplification-to-the-eu-carbon-leakage-instrument/), [Linklaters](https://sustainablefutures.linklaters.com/post/102lrbo/eu-cbam-simplification-what-has-changed-for-importers)
- In Dec 2025 the Commission proposed a **downstream scope extension** to more manufactured goods. That would pull in new, smaller importers of steel- and aluminium-intensive products if adopted. — [Mayer Brown Dec 2025](https://www.mayerbrown.com/en/insights/publications/2025/12/european-commission-issues-cbam-operational-rules-and-proposes-downstream-extension-of-the-cbam-scope), [Carboneer](https://carboneer.earth/en/2025/12/cbam-definitive-period-scope-extension/)

**PPWR (EU packaging)**
- PPWR **applied from 12 Aug 2026**. However:
  - The implementing act on the **Register of Producers (due 12 Feb 2026) was delayed**.
  - The **harmonised labelling implementing act missed its 12 Aug 2026 deadline** and is now expected in **Q4 2026**.
  - In April 2026, **100+ companies** (including Coca-Cola, Heineken, McDonald's and Mondelez) signed a joint letter raising readiness concerns.
  - Sources: [EUROPEN](https://www.europen-packaging.eu/news/12-august-2026-ready-or-not-here-comes-the-ppwr/), [CDX](https://public.cdxsystem.com/en/web/cdx/w/ppwr-industry-calls-for-clarifications-as-august-2026-deadline-approaches), [Food Manufacture 28 Aug 2026](https://www.foodmanufacture.co.uk/Article/2026/08/28/ppwr-is-live-but-label-details-overdue/), [Envirotec 19 Aug 2026](https://envirotecmagazine.com/2026/08/19/eu-misses-deadline-for-ppwr-labelling-rules/), [Packa postponement fact-check](https://contenthub.packa.com/ppwr-postponement-fact-check-2026)

**ESPR / DPP / Battery passport**
- The battery passport is mandatory from **18 Feb 2027** for LMT batteries, industrial batteries >2 kWh and EV batteries. — [Wikipedia](https://en.wikipedia.org/wiki/Battery_passport), [dpp-tool](https://dpp-tool.com/en/guide/battery-passport/)
- The first ESPR product delegated acts **slipped from late 2025 to mid-2026**. Textile and electronics DPP deadlines may shift later still. — [PassportCraft](https://passportcraft.com/insights/espr-timeline-what-brands-need-to-know) **[vendor]**

**US packaging EPR**
- California SB 54:
  - CalRecycle **withdrew its proposed regulations from OAL on 9 Jan 2026**, citing needed revisions on food and agricultural packaging.
  - OAL **approved the regulations on 1 May 2026**, effective immediately.
  - Producer registration was due **1 Jun 2026**. The 2026 California Producer Report and Source Reduction Report (on 2025 data) were due **31 May 2026**.
  - Sources: [Rev-Log](https://rev-log.com/calrecycle-withdraws-proposed-sb-54-regulations-what-california-packaging-producers-need-to-know/), [Recycling Today](https://www.recyclingtoday.com/news/california-senate-bill-54-regulations-approved-and-in-effect-epr/), [Mayer Brown Jun 2026](https://www.mayerbrown.com/en/insights/publications/2026/06/californias-sb-54-epr-regulations-take-effect-key-deadlines-and-compliance-obligations-for-producers), [Hogan Lovells](https://www.hoganlovells.com/en/publications/permanent-regulations-for-californias-extended-producer-responsibility-law-sb-54-take-effect)
- Other states: "Packaging EPR hits full swing" across California, Maryland and others (Jun 2026). — [Environmental Law & Policy](https://www.environmentallawandpolicy.com/2026/06/packaging-epr-hits-full-swing-key-milestones-across-california-maryland-and-beyond/)

**California climate disclosure (SB 253 / SB 261)**
- On **18 Nov 2025** the Ninth Circuit **enjoined SB 261** (climate-risk reports, originally due 1 Jan 2026) pending appeal. It **declined to enjoin SB 253**. Oral argument was held on 9 Jan 2026. CARB says SB 261 reporting is **voluntary until the ruling**. — [Jones Day](https://www.jonesday.com/en/insights/2025/11/ninth-circuit-enjoins-sb-261s-climaterelated-risk-reporting-requirements-declines-to-enjoin-sb-253), [Sullivan & Cromwell](https://www.sullcrom.com/insights/memo/2025/November/Ninth-Circuit-Temporarily-Enjoins-Enforcement-SB-261), [White & Case](https://www.whitecase.com/insight-alert/california-climate-disclosure-laws-ninth-circuit-hears-oral-argument-no-ruling-yet), [Nixon Peabody Mar 2026](https://www.nixonpeabody.com/insights/alerts/2026/03/02/california-climate-disclosure-laws-update)
- CARB proposed **10 Aug 2026** as the first SB 253 deadline for Scope 1 and 2. — [Cooley Jan 2026](https://www.cooley.com/news/insight/2026/2026-01-26-californias-sb-253-and-sb-261-developments-and-litigation)
- **Flag:** it was not confirmed whether the Ninth Circuit has ruled or whether the 10 Aug 2026 SB 253 deadline went ahead.

**US tariffs and customs**
- De minimis: sources describe **29 Aug 2025** as the end of Section 321 duty-free treatment. **Conflict:** one source (GingerControl) says it applied only to China and that global repeal comes **1 Jul 2027** under the One Big Beautiful Bill Act. Mainstream coverage (PBS/NBC, Aug 2025) described the end of the exemption for low-value packages generally. — [GingerControl](https://gingercontrol.com/blog/de-minimis-repeal-small-importer-impact), [PBS](https://www.pbs.org/newshour/nation/tariff-exemption-for-small-packages-ends-this-week), [NBC](https://www.nbcnews.com/business/consumer/de-minimis-exemption-ends-low-value-packages-shipped-us-need-know-rcna227772), [TariffsTool](https://www.tariffstool.com/guides/de-minimis-exemption-ended-2026) — **the report writer should state "suspended by executive order from 29 Aug 2025; statutory repeal effective 1 Jul 2027" and verify the scope.**
- On **20 Feb 2026** the Supreme Court held that IEEPA does not authorise tariffs, so the 2025 IEEPA tariffs were unlawful. **Refunds are not automatic.** The CIT paused enforcement while CBP builds an ACE refund system (earliest launch around 20 Apr 2026). — [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/02/supreme-court-strikes-down-ieepa-tariffs), [BDO](https://www.bdo.com/insights/tax/ieepa-tariff-refunds-frequently-asked-questions), [Flexport](https://www.flexport.com/blog/the-supreme-courts-ieepa-tariff-ruling-next-steps-potential-refunds-and/), [Buchalter](https://www.buchalter.com/insights/one-small-step-for-importers-federal-circuit-clears-the-way-for-ieepa-tariff-refund-litigation-to-resume/)
- **Section 122** tariffs:
  - A 10% tariff (later 15%) was imposed from **24 Feb 2026**, limited to 150 days.
  - On **7 May 2026** the CIT held the Section 122 tariffs unlawful, but its injunction covers only **two importers and Washington State**, not the whole country.
  - An appeal is pending.
  - Sources: [Ward and Smith](https://www.wardandsmith.com/article/court-of-international-trade-rejects-10-section-122-tariff-what-businesses-should-know-while-the-appeal-proceeds), [Offit Kurman](https://www.offitkurman.com/offit-kurman-blogs/tariff-litigation-ieepa-refunds-section-122), [Wipfli](https://www.wipfli.com/insights/articles/ieepa-tariff-refunds-the-recent-cit-ruling-and-section-122-updates), [Snell & Wilmer](https://www.swlaw.com/publication/tariffs-redux-what-importers-should-know-about-ieepa-refunds-and-section-122/)
- UFLPA Entity List: **43 companies added effective 3 Aug 2026, bringing the total to 187**. **Conflicting figure:** another source cites "116 entities" in early 2026. — [LandedFees](https://www.landedfees.com/en/content/uflpa-entity-list-2026-update), [Camtom](https://www.camtomx.com/en/blog/uflpa-forced-labor-import-ban-compliance)

**New obligations that did land (no delay)**
- GPSR applies from **13 Dec 2024**. — [Lappa](https://lappa.org/blog/gpsr/amazon-gpsr-requirements-for-sellers/)
- CPSC eFiling is mandatory from **8 Jul 2026**. — [CPSC](https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Implements-Mandatory-eFiling-for-Certificates-of-Compliance-Targeting-Dangerous-Foreign-Imports)
- CBAM definitive period from **1 Jan 2026**. — [Coolset CBAM timeline](https://www.coolset.com/academy/cbam-timeline-deadlines-phases-what-to-expect-2026)
- PPWR from **12 Aug 2026** (see above).

### Inferences
- **Demand shift.** EU large-company ESG reporting software is in a demand trough plus consolidation, so it is a poor entry point for a small firm. Regulated **operational** obligations (customs data, CPSC eFiling, GPSR, EPR SKU reporting, CBAM declarant filings, EUDR DDS from Dec 2026) create recurring, deadline-driven, non-optional work that small firms feel directly.
- **Uncertainty itself creates tool demand**:
  - IEEPA refund eligibility tracking (entry-level ledgers of duties paid under each legal basis) is a timely, bounded opportunity for small importers who lack trade counsel.
  - Deadline and regulation-change trackers (EUDR dates split by operator size, PPWR implementing acts, SB 253/261 status, ESPR delegated acts) help small firms avoid over-investing. Regulatory-intelligence incumbents exist, though (e.g., Compliance & Risks).
  - Buyers are wary of annual enterprise contracts for rules that may be rescinded. That favours **cheap, modular, month-to-month or per-filing pricing**, which suits a small studio.
- **Timing windows for Tempore:**
  - EUDR large/medium deadline: 30 Dec 2026, and micro/small: 30 Jun 2027.
  - Battery passport: 18 Feb 2027.
  - First CBAM annual declaration: 2027.
  - VSME requests ramping: late 2026 onward.
  - OBBBA global de minimis repeal: 1 Jul 2027 (if confirmed).
  - PPWR labelling act: expected Q4 2026.

### Gaps
- Whether the Ninth Circuit ruled on SB 253/261 by Sep 2026, and whether SB 253's first filings occurred on 10 Aug 2026, is unconfirmed.
- The status of Section 122 tariffs after the 150-day window and appeal, and whether CBP's ACE IEEPA refund system actually launched, is not confirmed.
- The exact content of the EUDR April/May 2026 simplification package is unconfirmed.
- The exact VSME delegated act adoption date is unconfirmed (sources conflict).
- **Prop 65:** no 2025–26 practitioner data was gathered. Not researched because the search budget ran out.
- **UK:** not researched (UK CBAM from Jan 2027, UK packaging EPR fee invoices and data submissions, UK product safety regime).
- **EU customs reform affecting e-commerce** (removal of the €150 duty exemption, low-value parcel handling fee): not researched.
