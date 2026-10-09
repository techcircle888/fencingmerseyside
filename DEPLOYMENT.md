# Launch handoff

## Prepared and checked

- 19 indexable HTML pages; homepage exceeds 1,000 visible words.
- HTML and XML sitemaps, robots.txt, canonical URLs, unique metadata and JSON-LD.
- Locally stored WebP design images, vector logo and SVG/ICO/Apple favicons.
- Local mobile/tablet/desktop browser checks passed, including all content pages, navigation, no horizontal overflow and no JavaScript page errors.
- Local Lighthouse scores after visual fixes: performance 99, accessibility 100, best practices 100, SEO 100. Local hosting is not evidence of live-domain performance or indexing.
- Automated WCAG checks reported no violations on home, contact, Wirral and sitemap pages. This is not a formal accessibility certification.

## Current blocker

GitHub account read works for techcircle888, but creating a new repository was rejected: `Resource not accessible by integration (createRepository)`. The repository was also unavailable through the existing read-only Git proxy. Owner needs to create an empty public `techcircle888/fencingmerseyside` repository and grant the connected Codex GitHub app access. Do not replace or publish over the bathroom repository.

## Continue when access is granted

1. In this checkout, rerun `npm run build` and `npm test` if content changes.
2. Verify access to the new repository using existing platform Git authentication. Do not request or store a raw token merely because one command fails.
3. Add its HTTPS origin, push the existing `main` baseline and `feat/fencing-merseyside-site` feature branch, and open a pull request. The build/deployment workflow is in `.github/workflows/pages.yml`.
4. Enable GitHub Pages with Actions as its build source. Merge the reviewed feature into main within the user's requested publish scope, then verify the successful deployment and served content.
5. Configure `fencingmerseyside.co.uk` as the Pages custom domain. Check the hostname and Pages domain status before changing DNS.
6. Re-read the Namecheap domain's complete host records and DNS/email settings. Initially the domain had an apex URL forwarding record and a www parking CNAME; no other editable hosts were returned. This observation must be refreshed. Preserve any new TXT, MX, verification or other unrelated records.
7. Replace only the parking website records with the current official GitHub Pages apex records and a www CNAME to `techcircle888.github.io`. Obtain authoritative destination guidance again rather than relying on a stale address list. The owner requested domain connection after a working deployment; do not connect a missing repository or unverified site.
8. Verify public DNS, HTTPS certificate, apex and www behaviour, homepage content, several deep links, robots.txt and both sitemaps. Do not claim domain connection or deployment from a successful DNS API write alone.

## Namecheap API

Reuse `NAMECHEAP_API_KEY` from the execution environment only, with the supplied API username TronGroup. Never write the key to this repository, logs, scripts or command URLs in output. Use TLS verification. The Namecheap API saw outgoing addresses 90.96.176.29 and 90.96.176.31 during setup; the owner added both to the whitelist. Egress can change, so check API errors before changing records. Domain ownership and DNS access were verified read-only; no DNS changes were made during the initial build.

## Email deferred by owner

Owner explicitly chose to connect email later and declined forwarding. Do not create forwarding, buy a mailbox or invent a receiving address. `hello@fencingmerseyside.co.uk` is the planned destination. FormSubmit POST endpoints and field layouts are prepared but fieldsets and submit buttons remain disabled with a visible opening-soon notice. A real mailbox, provider activation and a received test enquiry are required before enabling them. Activate the receiving mailbox through an authorised email host, apply its exact DNS requirements while preserving website records, complete form-provider verification, then test actual delivery. Remove deferred notices only after that succeeds.

## Business details

Business name and Merseyside service area were supplied. “Merseyside town centre” was not treated as a street address, local office or map pin. There are no invented reviews, prices, qualifications or guarantees. Images are generated illustrations rather than completed-project claims. Confirm operational and privacy-retention details before expanding claims.
