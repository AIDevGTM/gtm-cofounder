---
name: the-homepage
description: Structure a dev-tool homepage that converts developers into champions. Use when the landing page is written for the buyer instead of the developer, reads as salesy, buries what the product does, or makes it hard to start. Pairs with the ShipReady homepage audit.
---

# The homepage

> Write your homepage for the person who actually reads it: the **end-user developer**, not the CTO who signs the check. The developer becomes your champion and sells it internally for you.

**Use this when:** your homepage speaks to buyers/ROI, it's clever but vague about what the thing does, or a developer can't tell in 5 seconds whether to care, and can't start in 5 minutes if they do.

## The core rule (Czakon)

**Address end-user developers on the homepage; put enterprise/ROI/buyer messaging on separate pages** (enterprise, pricing, case studies). If you write the homepage for the buyer, you've written it for someone who isn't there.

## Framework: the sections, in order (Czakon)

1. **Hook / core message**: immediately: what *is* it? Use a category ("CI for monorepos"), a known-incumbent comparison ("a Datadog alternative"), or a plain statement. **Headline = what it is · subhead = for whom / what job.**
2. **Hero**: a real product shot; two CTAs: **Get started** (signup) *and* **Docs**. Answer "what's in it for me?" up top. Lead with the **how**, not the why.
3. **Social proof, right after the hero**: recognizable logos are the fastest credibility you have. Impressive dynamic metrics (users, stars) if you've got them.
4. **Value prop & differentiation**: why you over the 10 alternatives (see `value-prop-that-converts`).
5. **Getting started**: a huge conversion lever. Free trial, **no credit card**, quick setup. Any hard barrier sends developers straight to a competitor.

**Design:** clean typography, breathing room, no "salesy BS," minimal heavy interactions. An embedded playground / copy-pasteable snippet creates an instant *aha*.

## Framework: what must be on it (Frankl)

Cross-check the copy has all six:
1. the **problem in the customer's language** (before the solution)
2. the **villain** / undeniable trend
3. **attributed proof** with numbers (name · title · company)
4. the **inciting event** / urgency
5. **social proof** (not anonymous)
6. a **low-friction path to try** (free tier · docs · GitHub)

## The MVP website (Czakon)

Don't build everything. Start with: **homepage · docs · pricing · navbar (login, signup, contact, GitHub) · About** (an About page builds trust for an unknown brand). Add later, deliberately: case studies → comparison pages → blog → templates → sandbox → enterprise page.

> **Transparent pricing.** "Contact sales for pricing" reads as "expensive and slow." Show a number wherever you can.

## Decision tree: hero CTA

```
Can a developer get value self-serve?
├─ YES → primary CTA "Get started" (signup/download) + secondary "Docs".
└─ NO  → primary CTA "Read the docs" / "See how it works"; don't fake a signup that dead-ends.
```

## Mistakes that look reasonable

- **Writing for the buyer**: ROI language up top; the developer bounces.
- **Why before what**: three sentences of vision before you say what it *is*.
- **"Contact sales" pricing**: kills self-serve trust instantly.
- **No getting-started**: a beautiful hero and no obvious first step.
- **Puffery hero**: "The powerful, seamless platform for modern teams." Says nothing (run `value-prop-that-converts`).

## Your next 30 minutes

- [ ] Read your hero as a skeptical developer: in 5 seconds, do you know *what it is* and *if it's for you*?
- [ ] Confirm the five sections exist **in order**; move buyer/ROI copy to its own page.
- [ ] Put a **no-credit-card** getting-started step above the fold or one click away.
- [ ] Run the page through **[ShipReady](https://ship-ready.xyz)** for the full 10-point scorecard.

---
Grounded in Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).
When a framework can't make the call, that's what a human is for: [The DevTool GTM Company](https://thedevtoolgtmcompany.com).
