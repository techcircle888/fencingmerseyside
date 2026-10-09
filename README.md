# Fencing Merseyside

Separate static website for https://fencingmerseyside.co.uk. No runtime package dependencies, client framework or database.

## Develop and verify

From this checkout, run `npm run build`, `npm test`, then `npm start`. Python 3.12 and Node 24 were used. Source content is in `tools/content.py`; page generation is in `tools/build.py`; styles, browser behaviour and imagery are in `assets/`. The build emits ordinary HTML into ignored `dist/`, plus XML/HTML sitemaps, robots.txt and the custom-domain CNAME file.

## Deployment

The GitHub Actions workflow builds and checks pull requests, then deploys main through GitHub Pages. Enable Pages with GitHub Actions as the source and configure the custom domain after verifying ownership. Do not change domain DNS until the hosting destination and existing records have been checked. Domain connection must be verified on the actual public HTTPS site.

`vercel.json` is an alternative deployment configuration; GitHub Pages does not apply those HTTP headers. Form submissions use FormSubmit's POST endpoint, not a site backend. Email and the provider's one-time recipient activation are deferred at the owner's request. The real hello@fencingmerseyside.co.uk mailbox and activation are prerequisites for delivered enquiries. Forms must remain visibly unavailable until then. Never report a browser submission or provider redirect as proof that email arrived.

## Content and privacy

The homepage exceeds 1,000 words; supporting content includes materials, installation, repair and gate guides, cost and boundary advice, five Merseyside borough pages, contact, privacy, accessibility and an HTML sitemap. No fabricated prices, reviews, qualifications, street addresses or completed-project claims. Images are AI-generated design illustrations, visibly labelled, and encoded as local WebP assets. No API keys or account credentials belong in this repository. Namecheap authentication remains in the environment only.

Email hosting, operational business information, privacy retention arrangements and form delivery must be confirmed before treating the site as a fully operational enquiry channel. SEO structure does not guarantee rankings.
