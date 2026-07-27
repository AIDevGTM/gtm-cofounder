---
name: pricing
description: "Help the founder decide what to charge and how to package it: the value metric, the tiers, the free-to-paid line, and finding the actual number. Use when the founder is guessing at a price, priced too cheap and can't change it, is stuck on free vs paid, or believes \"developers won't pay\" so never charges."
---

# Pricing (what to charge, and how)

> Price is not a number you pick at the end. It is a positioning decision: it tells the market who you are, what you replace, and how much you believe you are worth. Get it from evidence, not fear.

**Use this when:** you are guessing at a price, you priced on a gut feeling and now feel stuck with it, you don't know where the free line goes, developers use it and nobody pays, or you believe "developers won't pay for this" so you have never charged at all.

## The core idea

Three decisions, in order. Most founders skip to the third and wonder why nothing converts.

1. **The value metric** (what you charge *per*). The single most important pricing decision. Get this wrong and no tier structure saves you.
2. **The packaging** (what is free, what is paid, what is enterprise, and what triggers the upgrade).
3. **The number** (the actual price on each tier).

One rule sits under all of it: **price against the value the customer gets, never against your cost or your fear.** Your AWS bill is not a pricing strategy.

## First: are you even ready to price?

Do not gate before you have proof people come back. If week-2 retention is weak, a paywall just turns a leaky funnel into a smaller leaky funnel. Prove retention, then monetize (see `know-if-its-working`). The one exception: if buyers are already emailing "can we pay you for X," that is a green light regardless of stage. Stated willingness to pay is the strongest signal there is.

## Framework: the value metric

Charge for the thing that grows as the customer gets more value. A good metric:

- **Scales with their success**, so the bill grows as they grow (seats, active users, projects, events, API calls, GB, builds, endpoints monitored).
- **Stays predictable enough** that finance can forecast it. Pure usage that spikes 10x overnight creates bill shock and churn.
- **Is legible in one sentence.** If a dev cannot predict roughly what they will pay, they will not adopt.

```
Does the value come mostly from more PEOPLE using it (collaboration, seats)?
├─ YES → per-seat, but watch for seat-sharing and bot accounts deflating it
└─ NO  → value comes from more USAGE (events, calls, compute, data)
         → usage-based, with a floor and caps so the bill stays predictable
```

Hybrid is common and fine: a platform fee plus usage. Avoid per-seat when the value is machine or usage driven (you tax the thing you want more of), and avoid pure usage when the value is human collaboration (you make teams ration access).

## Framework: packaging (the free-to-paid line)

For an OSS or PLG dev tool, the free tier is **acquisition, not charity.** The line is not "how much can I give away," it is "what does a serious team need that a solo hacker does not."

- **Free / open source:** the core value, for one developer or a tiny team. Generous enough to become part of their workflow. This is your distribution.
- **Paid (team):** the things that appear the moment it matters to a company, not a person: collaboration and seats, higher limits and scale, SSO, audit logs, roles, compliance (SOC 2, on-prem, data residency), support and SLAs.
- **Enterprise:** "contact us." Starts wherever security review, procurement, and custom terms enter, usually the moment someone asks for SSO or a DPA.

The upgrade should trigger at a **moment of earned value**, not an arbitrary wall. Good: "you added your third teammate," "you crossed 10k events," "you need SSO." Bad: a countdown timer, or hiding a feature the tool is useless without.

Rule of thumb: **charge for team, scale, and trust. Give away individual value.** Developers forgive a paywall on "my company needs this." They resent one on "the thing you advertised."

## Framework: finding the number

Never pick it in a conference room. In order of strength:

1. **Deflected willingness to pay.** The "can we pay for X" messages you have already received. Reply and ask: what was the cost of not having it, and what would it need to be to get approved internally? Free, and the highest-signal pricing research that exists.
2. **Value anchoring.** Price against what you replace and what you save. Save a team 10 hours a month at a loaded $100/hr and that is $1,000 of value; charging $50 leaves the room. Capture a slice of value delivered, do not undercut a rival.
3. **Competitor anchoring.** Know the number already in the buyer's head. If they compare you to a $30/mo tool, you need a reason to be $99, or a reason to be $9. Both can win. "Roughly the same but a bit cheaper" loses.
4. **The range question** (in `talk-to-users` calls): "At what price would this be so expensive you would not consider it? At what price would it be so cheap you would doubt the quality?" The gap between the two is your range.

Thresholds worth knowing:
- If **nobody ever pushes back** on price, you are too cheap. A healthy amount of "that is a lot" is correct.
- Aim for the customer to get **roughly 10x the price in value.** Below about 3x, they churn; the math does not survive a budget review.
- **Annual is about two months free** (15 to 20 percent off). It buys cash and retention.
- **Anchor high.** Show the expensive tier so the one you want looks reasonable. Three tiers convert better than two, and the middle is usually the target.
- Free-to-paid conversion of **2 to 5 percent** is normal for OSS/PLG. Near zero usually means the free-to-paid *line* is wrong, not the price.

## Mistakes that look reasonable

- **Cost-plus pricing.** "It costs me $8 in compute so I will charge $12." Cost is a floor, not a strategy. Price the value.
- **Never charging.** "Developers won't pay" is almost always "I have not asked, and I am scared to." The deflected-payment emails already disprove it.
- **Too many tiers.** Four or more creates decision paralysis. Three is the ceiling for self-serve.
- **A free tier that is too generous.** If a real company never needs to upgrade, you built a great free tool and no business. Move the line to team, scale, and compliance.
- **Per-seat on a machine-value product** (or usage on a collaboration product). You end up taxing the exact behavior you want more of.
- **Competing on price.** "Best value" and "cheaper than X" are a race to the bottom, and by the puffery rule, unprovable. Win on the value metric and the wedge, not the discount.
- **Fear-driven discounting.** Caving at the first "too expensive" trains every buyer to push and signals you do not believe your own value.
- **Publishing usage pricing with no cap.** Predictability beats a low headline rate. Bill shock is the top churn driver for usage models.

## Your next 30 minutes

- [ ] Name your **value metric** in one sentence: "we charge per ___." Check that it grows with the customer's success and stays predictable.
- [ ] Draw the **free-to-paid line**: what a solo dev gets free vs what a company must pay for (seats, scale, SSO/compliance, support).
- [ ] Find every **"can we pay for X"** message you have deflected. Draft the three-question reply (cost of not having it, shape of an approvable tier, rough budget).
- [ ] Sketch **three tiers** (free/OSS, team, enterprise-contact-us) with one clear upgrade trigger between each.
- [ ] Put a **real number** on the team tier, anchored to value, not cost. If it does not make you slightly nervous, it is too low.

---
Built from real dev-tool GTM experience, with frameworks from Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).
When a framework can't make the call, that's what a human is for: [The DevTool GTM Company](https://thedevtoolgtmcompany.com).
