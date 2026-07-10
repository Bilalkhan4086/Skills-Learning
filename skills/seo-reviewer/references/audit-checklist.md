# SEO Audit Checklist

Use this reference only when the requested audit needs a deeper category checklist. Do not paste the checklist into the final answer. Convert relevant checks into prioritized findings with evidence.

## Technical SEO

- HTTP status codes, redirects, redirect chains, HTTPS, mixed content
- Canonical tags, duplicate URLs, trailing slash or casing variants
- robots meta tags, X-Robots-Tag headers, noindex/nofollow, blocked assets
- robots.txt availability, sitemap.xml availability, sitemap freshness
- URL structure, pagination, faceted navigation, parameter duplication
- hreflang when the site targets multiple languages or regions
- Crawl depth and internal link discoverability for important pages

## Metadata

- Unique title tags with primary topic and brand where appropriate
- Useful meta descriptions aligned with search intent
- Open Graph and Twitter card tags for share previews
- HTML `lang`, charset, viewport, favicon, theme color
- JSON-LD syntax and schema type fit for the page
- Organization, WebSite, BreadcrumbList, Product, Article, FAQPage, LocalBusiness, Person, or Review schema when relevant
- Schema content matching visible page content

## HTML Structure and Accessibility

- One clear H1 that describes the page topic
- Logical heading hierarchy without skipped levels used only for styling
- Semantic landmarks: header, nav, main, section, article, aside, footer
- Descriptive internal and external link text
- Non-empty links and buttons with accessible names
- Useful image alt text; decorative images handled appropriately
- Form labels, focus states, keyboard navigation, color contrast

## Content SEO

- Clear search intent match for the page type
- Specific product, service, pricing, location, author, or organization details where relevant
- Thin, duplicated, boilerplate, or keyword-stuffed content
- Internal links to and from related pages
- Trust signals: reviews, credentials, policies, contact details, citations, support pages
- Freshness signals for time-sensitive topics
- Entity clarity: consistent names, categories, attributes, and relationships

## Performance and Page Experience

- Likely LCP element and whether it is optimized
- Image dimensions, responsive sizes, modern formats, lazy loading strategy
- CLS risks from missing dimensions, injected banners, late-loading fonts, or dynamic content
- INP risks from heavy JavaScript, long tasks, hydration cost, or third-party scripts
- Render-blocking CSS/JS, unused bundles, code splitting
- Font loading strategy, preconnect/preload usage, font-display
- Compression, caching headers, CDN usage when visible

## Mobile SEO

- Mobile viewport configuration
- Responsive layout and content parity
- Tap target size and spacing
- Readable font sizes
- Mobile navigation crawlability
- Mobile CLS risks

## Framework-Specific Checks

### Next.js

- App Router metadata API or Pages Router `Head` usage
- Dynamic metadata for route params
- `robots.ts`, `sitemap.ts`, static sitemap generation, and canonical consistency
- Server-rendered important content rather than client-only rendering
- `next/image` sizing, priority for LCP image, and alt text
- Open Graph image generation and social metadata

### React/Vite/SPAs

- Whether important content and metadata are server-rendered or prerendered
- Route-level titles, descriptions, canonicals, and structured data
- Client-side routing fallbacks and status code behavior
- Static generation, SSR, or prerendering for indexable pages

### Astro/Remix/Nuxt/Vue

- Route-level metadata conventions
- Static or server rendering for critical pages
- Generated sitemap/robots files
- Canonical handling for dynamic routes
- Structured data generation and hydration risks

## AI Search Readiness

- Clear entity descriptions for brand, products, people, and locations
- Well-structured sections that answer natural-language questions
- FAQ or comparison content when it genuinely helps users
- Author, reviewer, organization, and contact information where relevant
- Structured data matching visible content
- Evidence, citations, specifications, policies, and support details that make claims verifiable

## Security Signals That Affect Trust

- HTTPS and mixed-content problems
- HSTS where appropriate
- Obvious security header gaps that affect trust or embedding
- Cookie security issues visible in responses
- Broken forms or suspicious third-party scripts
