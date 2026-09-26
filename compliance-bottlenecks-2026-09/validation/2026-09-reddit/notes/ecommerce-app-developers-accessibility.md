# E-commerce sellers, app developers and accessibility: Reddit sweep notes

> **How this was gathered (2026-09-25).** Reddit's anonymous search feeds returned 332 posts from 2024 onwards, and all were read:
>
> | Subreddit | Posts |
> |---|---|
> | r/iOSProgramming | 78 |
> | r/FulfillmentByAmazon | 47 |
> | r/ecommerce | 46 |
> | r/androiddev | 42 |
> | r/EtsySellers | 41 |
> | r/AmazonSeller | 26 |
> | r/webdev | 20 |
> | r/accessibility | 20 |
> | r/shopify | 12 |
>
> The feeds return **post bodies only**, with no comments or votes. About 45% of the posts were noise, such as "CPC" matching pay-per-click ads and "data" matching Android architecture questions.
>
> GitHub stars and App Store dates were checked on 2026-09-25. Two gaps remain: Shopify App Store search returned HTTP 429, so its app counts come from web search, and Google Play was not searched.

This cluster tests three of the study's tier-1 items. **All three move down.**

## #1 App privacy-label, age-assurance and COPPA kit: down as a paid product

**Pain exists, but nobody says they pay to solve it.**
- **iOS privacy manifests:** 12 posts, clustered around Apple's enforcement in 2024. Examples: [2024-04-10](https://www.reddit.com/r/iOSProgramming/comments/1c0klcz/) (an SDK vendor late with its manifest), [2024-04-30](https://www.reddit.com/r/iOSProgramming/comments/1cgm0ec/) (an ITMS-91064 rejection), and [2024-06-29](https://www.reddit.com/r/iOSProgramming/comments/1drf1uu/) (a manifest reported invalid with no diagnostics).
- **Label content:** 8 posts from 2024–26. Examples: [2026-02-21](https://www.reddit.com/r/iOSProgramming/comments/1raidrm/) (confusion over how ad SDKs should be declared) and [2026-03-09](https://www.reddit.com/r/iOSProgramming/comments/1rovaz9/).
- **Google Play Data Safety:** 3 posts. Examples: [2026-05-15](https://www.reddit.com/r/androiddev/comments/1te8p9z/) (the form silently drops precise location) and [2026-07-16](https://www.reddit.com/r/androiddev/comments/1uxxnkj/) (AI tools gave conflicting answers).
- **Age-rating questionnaires:** 15 posts around Apple's 2026-01-31 deadline and the social-media questions announced 2026-07-09 ([Apple](https://developer.apple.com/news/?id=tlur8uvi)). Most are process confusion in App Store Connect, not a tool gap.
- **Age assurance itself:** 3 posts, and all want it free or want to avoid it. One plans to rate the app 18+ to skip the Texas API ([2025-12-16](https://www.reddit.com/r/iOSProgramming/comments/1po9147/)). Another won't pay a per-user SDK fee ([2026-02-08](https://www.reddit.com/r/iOSProgramming/comments/1qzix86/)).
- **COPPA:** effectively absent from the cluster.

**Competition, checked 2026-09-25. Most of the proposed kit already exists, and much of it is free:**
- [RevylAI/greenlight](https://github.com/RevylAI/greenlight) (MIT, about 2,400 stars, created February 2026). It is an offline preflight tool that runs in CI and checks:
  - privacy-manifest completeness
  - Required Reason APIs
  - tracking SDKs against App Tracking Transparency
  - Play policy
  - App Store Connect age-rating
- Other open-source privacy-manifest tools: stelabouras/privacy-manifest, crasowas' fixer and analyser, cocoapods-privacy and xcprivacy-lint (2026).
- Google Checks has a free Essentials plan with a Data Safety assistant and CI support ([pricing](https://checks.google.com/pricing)). Privado also has a free Data Safety CLI.
- Free Declared Age Range wrappers exist for React Native, Flutter, Capacitor, Cordova, Unity, .NET and Delphi. k-ID sells a paid option.

**What is left.** No maintained, current mapping from third-party SDKs to Apple label fields and Play Data Safety fields turned up. Greenlight doesn't do it, and Privado's dataset has been stale since 2022. Tracking age-rating deadlines across many apps is also unserved.

**Recommendation.** Build this as Tempore's own internal tool or a free lead magnet for its client work. Don't treat it as a paid product unless 5 developers commit to paying for it.

## #3 Per-SKU marketplace compliance vault: down

**The pain is loud but mostly out of the seller's hands.** The cluster has about 32 first-hand Amazon document-request or rejection posts, about 21 on the EU product-safety rules (GPSR) and 2 on CPSC eFiling. Most of the failures sit in Amazon's queue, its interface and its product classification, or in lab and Responsible Person fees, not in how sellers organise documents. Examples:
- [2024-02-13](https://www.reddit.com/r/AmazonSeller/comments/1aq5235/): a 10-year seller hit by a children's-jewellery document request.
- [2024-07-11](https://www.reddit.com/r/FulfillmentByAmazon/comments/1e0zcf3/): stock already in the warehouse, but no children's product certificate (CPC) from the factory.
- [2025-03-04](https://www.reddit.com/r/FulfillmentByAmazon/comments/1j3mpvs/): hundreds of listings stuck pending for two months.
- [2026-07-04](https://www.reddit.com/r/FulfillmentByAmazon/comments/1un6lwi/): a product misrouted to infant-walker compliance.

**Amazon now validates toys itself.** Since 2025-09-03, children's toys need annual verification by an Amazon-approved testing lab, with no path for sellers to upload their own documents. It covered 11 marketplaces by March 2026 ([Eurofins](https://www.eurofins.com/toys-hardlines/services/regulatory-and-compliance/amazon-direct-validation-for-toys-furniture/)). Two sellers confirm there is no upload path: one with 60+ listings ([2026-02-12](https://www.reddit.com/r/AmazonSeller/comments/1r2ulzc/)), and one whose manufacturer's CPC was rejected ([2025-12-06](https://www.reddit.com/r/FulfillmentByAmazon/comments/1pfi8iu/)). **For Amazon children's products the vault is now blocked by the platform.**

**GPSR is crowded.** At least 8 Shopify apps cover it. One example is [GPSR Kit](https://apps.shopify.com/gpsr-kit), launched 2026-07-08: free for 10 products, $14.99/month for 500 and $29/month unlimited. At least 7 would-be founders posted about the same idea on r/FulfillmentByAmazon during 2025–26.

**What is left: a document vault across marketplaces, plus CPSC eFiling data.** The vault would serve multi-channel sellers with many SKUs; one example is a seller keeping 300+ safety PDFs up to date ([r/shopify, 2025-08-24](https://www.reddit.com/r/shopify/comments/1myrgyh/)).

CPSC eFiling became mandatory on 2026-07-08 for about 600 HTS codes, at any shipment value ([CPSC FAQ](https://www.cpsc.gov/FAQ/eFiling-Frequently-Asked-Questions-FAQ)). Sellers are being caught by it:
- A Canadian vintage seller's adult clothing shares HTS codes with girls' clothing, and they report parcels destroyed at customs ([2026-07-08](https://www.reddit.com/r/EtsySellers/comments/1uqx7xu/)).
- An EU vintage seller reports the eFiling registry demands testing data ([2026-08-10](https://www.reddit.com/r/EtsySellers/comments/1vkmxqg/)).

No tool for micro sellers turned up, but the Shopify check was incomplete. Treat this as a feature of #3, not a product on its own. Test it with 5 non-US sellers whose carrier asks for GCC data, at $10+/month. Kill it if the postage platforms (ChitChats, PirateShip, Easyship) add free GCC capture.

## #4 Accessibility CI, ACR and EAA statements: down for scanning; one narrow angle holds

**Pain.** About 12 first-hand web posts, plus 3 about documents:
- a Florida lawsuit seeking $50k ([2025-09-18](https://www.reddit.com/r/webdev/comments/1nkbwbu/));
- a Shopify store served over its screen-reader checkout ([2026-06-12](https://www.reddit.com/r/webdev/comments/1u3wrye/));
- a seller with a $500 budget ([2026-01-29](https://www.reddit.com/r/webdev/comments/1qqbfyh/));
- a request for a checker that logs fixes "for compliance" ([2024-12-09](https://www.reddit.com/r/webdev/comments/1hagek3/));
- a third-party auditor who still says "not compliant" after Lighthouse scores of 100 ([2026-02-23](https://www.reddit.com/r/webdev/comments/1rcuame/)).

**Competition.** Free tools cover scanning and CI: axe-core (about 7,500 stars), Lighthouse CI (about 7,100), pa11y-ci, IBM equal-access and GSA OpenACR. VPAT Studio sells ACR authoring. New in 2026: a11y-hd, axle-action, ariada and at least 3 VPAT generators. The subreddit itself mocks the "nine hundredth" scanner launch ([2026-01-22](https://www.reddit.com/r/accessibility/comments/1qk9ths/)).

**What holds.** A dated remediation and evidence log, plus a demand-letter response pack for small Shopify merchants, who are the segment being sued.

## New workflows found and rejected

| Workflow | Evidence | Why rejected |
|---|---|---|
| Per-country EU packaging EPR and PPWR data preparation for micro cross-border sellers | [2026-09-17](https://www.reddit.com/r/ecommerce/comments/1wj4qse/): packaging weights across hundreds of SKUs. [2026-08-10](https://www.reddit.com/r/ecommerce/comments/1vketgs/): €200–900 per country per year for an authorised representative. [2025-10-25](https://www.reddit.com/r/FulfillmentByAmazon/comments/1ofz525/). [2026-09-05](https://www.reddit.com/r/EtsySellers/comments/1w88tmi/): about half of polled sellers would stop EU shipping | Crowded: at least 10 tools, several free or about $15/month and most launched 2025–26 ([Repax list](https://www.repax.io/blog/best-epr-software-for-small-businesses), vendor-written). The authorised representative required in each country is a legal service, and micro sellers are leaving the EU rather than paying. PPWR has been binding since 2026-08-12 |
| Amazon document pre-submission checker | See #3 above | Blocked by the platform: Direct Validation |
| Rules router for cross-border shipping | [2026-08-09](https://www.reddit.com/r/EtsySellers/comments/1vjl0wm/), [2026-07-01](https://www.reddit.com/r/EtsySellers/comments/1ul16s4/) | Sellers switch markets off instead of paying, and the tool would carry liability |
| GPSR Responsible Person for micro sellers; US de minimis and DDP; privacy-policy hosting; DSA trader status; accessible PDFs; Prop 65; Play developer verification | Scattered or none | A legal service, crowded, or no paying demand |
