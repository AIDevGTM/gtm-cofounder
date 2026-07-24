---
name: know-if-its-working
description: Measure GTM with the metrics that matter (net developer retention, DREAM funnel) instead of vanity numbers. Use when the founder has dashboards full of stars and pageviews but can't tell if go-to-market is working, or is optimizing acquisition over a leaky bucket.
---

# Know if it's working

> The only early metric that matters is **net developer retention**. Without it, you're not running a funnel, you're running a colander.

**Use this when:** you're tracking GitHub stars and pageviews and still can't answer "is GTM working?", or you're pouring effort into acquisition while new users quietly churn.

## The core idea

Acquisition is worthless if users don't come back. Prove **retention** first; only then does spending on **acquisition** make sense. Most early founders optimize the top of the funnel while the bottom leaks, fix that order.

## Framework, net developer retention (Frankl)

> Of all the developers who first used the product in **Month 1**, how many used it in **Month 2? Month 3?**

- Hold it **above 100%**, meaning existing cohorts *grow* through internal referral/expansion.
- Below solid retention, **do not focus on acquisition**, you're filling a leaky bucket.
- This single cohort question tells you more than every vanity chart combined.

## Framework, the DREAM metrics (Frankl)

Measure one honest number per stage, not pageviews, not stars.

| Stage | The metric that counts |
|---|---|
| **Discovery** | unique human visitors / month |
| **Research** | newsletter subs + community joins + follows |
| **Evaluation** | free-tier signups / downloads / active free users |
| **Activation** | monthly active users · frequency · session depth |
| **Membership** | community members *actively* posting & answering |

**The gate before all of it, the weekend test:** can a new developer get to first value **over a weekend from docs + Stack Overflow, no support call?** Time-to-value target: **< 1 hour ideal, 1 day max.** If Evaluation/Activation fails here, no channel work will save you.

## Growth benchmarks (non-ARR, Frankl)

- **Pre-seed:** ~30% month-over-month user growth
- **Post-Series-A:** ~10% MoM
- **First $1M ARR:** within 12 months is good, 9 is excellent

## Framework, attribution philosophy (Czakon)

Developer marketing is **hard to attribute and that's normal.** A dev sees your HN post, reads a tutorial, lurks for two months, then signs up direct.
- Don't over-trust last-touch; it will tell you "direct/organic" and hide the real work.
- Add a **"how did you hear about us?"** free-text field, self-reported attribution beats a broken model.
- Judge channels on *trend* and *directional* signal, not spurious precision.

## Decision tree, what to fix first

```
Is month-2 cohort retention healthy (users come back)?
├─ NO  → STOP optimizing acquisition. Fix Evaluation/Activation (the weekend test, time-to-value).
└─ YES → is a channel reliably producing retained users?
         ├─ YES → pour more in (and only now consider paid to amplify).
         └─ NO  → go back to first-50-users; find the channel before scaling spend.
```

## Mistakes that look reasonable

- **Vanity metrics**, stars, pageviews, impressions. They feel like progress and predict nothing.
- **Acquisition over a leaky bucket**, buying users who never return.
- **Demanding clean attribution**, chasing a perfect model instead of acting on directional signal.
- **Ignoring the weekend test**, a beautiful funnel that dies at first-value.

## Your next 30 minutes

- [ ] Compute one number: of the devs who first used it 8 weeks ago, what % used it in the last 2 weeks?
- [ ] Pick **one** honest metric per DREAM stage; delete the vanity charts from your dashboard.
- [ ] Time yourself doing your own onboarding cold. Over an hour? That's your #1 GTM problem.
- [ ] Add a "how did you hear about us?" field to signup this week.

---
*Grounded in Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).*
*For the judgment calls a framework can't make → [The DevTool GTM Company](https://thedevtoolgtmcompany.com).*
