---
name: seo-reviewer
description: Review websites, landing pages, web apps, and source code for SEO. Use this skill whenever the user asks for an SEO audit, technical SEO review, ranking improvement, pre-launch SEO QA, Core Web Vitals review, metadata/schema/canonical/robots/sitemap checks, AI search readiness, or framework SEO for Next.js, React, Vue, Nuxt, Astro, Remix, or static sites, even if they only say "review this page" in an SEO context.
---

# SEO Reviewer

Use this skill to produce evidence-based SEO audits that are specific to the site, page, or codebase in front of you. The goal is not to recite a checklist; it is to identify the highest-impact search visibility problems, explain why they matter, and give implementation-ready fixes.

## Intake

First determine what evidence is available:

- Live URL only: inspect the rendered page, HTTP behavior, metadata, robots/sitemap files, mobile behavior, and performance signals using available browser, HTTP, or diagnostic tools.
- Source code only: inspect framework conventions, route structure, metadata generation, structured data, image usage, internal links, and build/runtime assumptions. Do not claim deployed behavior unless it is visible in code.
- Both URL and source code: compare intended implementation with rendered output. Call out mismatches because they often explain indexing or sharing issues.
- No target: ask for a URL, repo path, page file, or HTML sample before auditing.

When the audit scope is broad or the page is complex, read `references/audit-checklist.md` and use only the sections relevant to the target.

## Evidence Rules

Separate findings by confidence:

- Confirmed: directly observed in source, rendered HTML, HTTP response, robots.txt, sitemap.xml, diagnostic output, or screenshots.
- Inferred: likely from framework behavior or code patterns, but not directly measured.
- Unverified: important but not checkable with the current inputs.

Do not invent search volume, ranking position, traffic impact, Core Web Vitals field data, or crawl behavior. If metrics cannot be measured, state that and review likely causes from implementation evidence.

## Audit Workflow

1. Identify the site type, framework, important templates, and target page purpose.
2. Inspect indexability first: status codes, redirects, canonical tags, robots directives, robots.txt, sitemap.xml, noindex/nofollow, and duplicate URL patterns.
3. Inspect the document head: title, meta description, canonical, Open Graph, Twitter cards, viewport, charset, language, theme color, favicon, and JSON-LD.
4. Inspect page structure: one clear H1, heading order, semantic landmarks, content hierarchy, internal links, image alt text, and accessible controls.
5. Inspect content quality: search intent alignment, thin or duplicated copy, entity clarity, product/service details, trust signals, freshness, and useful internal links.
6. Inspect performance risks: LCP candidates, CLS risks, render-blocking resources, JavaScript payload, image size/format, lazy loading, font loading, caching, and compression.
7. Inspect framework-specific SEO: server rendering/static generation, metadata APIs, dynamic routes, sitemap/robots generation, structured data generation, and client-only content risks.
8. Inspect AI search readiness: structured, entity-rich content; clear organization and author signals; FAQ-style answers where useful; schema; citations or proof points; and readable page sections.
9. Prioritize issues by likely business and search impact, not by checklist order.

## Priority Rubric

Use this rubric for severity:

- Critical: blocks crawling, indexing, canonicalization, rendering of important content, or creates severe duplication on money pages.
- High: materially weakens relevance, snippets, internal discoverability, page experience, or trust for important pages.
- Medium: improves clarity, accessibility, sharing, performance, or structured understanding but is unlikely to be the single main ranking blocker.
- Low: polish, consistency, optional schema, or future-proofing.

Use scores only as directional heuristics. A score without evidence is less useful than a smaller set of well-prioritized findings.

## Report Structure

Return the audit in this order:

```markdown
# SEO Audit Report

## Overall Assessment
[Short verdict, scope analyzed, and any limitations.]

## Priority Findings
### 1. [Issue title] - [Critical/High/Medium/Low]
- Evidence: [What you observed and where.]
- Why it matters: [SEO/user impact.]
- Recommended fix: [Specific action.]
- Implementation notes: [Code/config example when helpful.]

## Positive Findings
[What is already working well.]

## Category Scores
- Technical SEO: [0-100] - [brief reason]
- Metadata and structured data: [0-100] - [brief reason]
- Content and intent match: [0-100] - [brief reason]
- Performance risk: [0-100] - [brief reason]
- Accessibility and semantic HTML: [0-100] - [brief reason]
- Mobile readiness: [0-100] - [brief reason]
- AI search readiness: [0-100] - [brief reason]

## Fix Roadmap
1. [Highest-impact fix]
2. [Next fix]
3. [Next fix]

## Final Verdict
[SEO maturity level, biggest strengths, biggest risks, and expected improvement after fixes.]
```

For small reviews, keep the same order but shorten sections. For implementation-focused requests, include code examples for the user's framework instead of generic HTML.

## Style

- Be concise and concrete.
- Prefer evidence and implementation detail over theory.
- Avoid repeating the same issue in multiple categories.
- Explain technical concepts in plain language when needed.
- Mention assumptions and limitations explicitly.
- If multiple pages or templates are reviewed, group findings by shared template before page-specific issues.
