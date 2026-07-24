---
name: who-is-this-for
description: Define a real ICP and the developer personas in the sale. Use when the founder says the product is "for developers," can't name who would say no, or is marketing to whoever holds the budget instead of who actually adopts.
---

# Who is this for?

> "Developers" is not a market. It's a medium. If your ICP doesn't exclude anyone, it isn't one.

**Use this when:** you describe your user as "developers" or "engineering teams," you can't name a person who is clearly *not* a fit, or you're aiming your messaging at the VP of Engineering because they have the budget.

## The core idea

A usable ICP is specific enough that some people are obviously **out**. "Every developer" gives you nothing to say, because a message that speaks to everyone speaks to no one. Sharpen until exclusion is possible.

And in almost every AI/dev-tool sale there is **more than one person**: the developer who adopts is rarely the person who pays. Market to the adopter; sell to the buyer. Confuse the two and you get great meetings and no decisions.

## Framework 1: The personas in the sale (Frankl)

Map who plays each role. You need all of them for a complex sale; skip one and the deal stalls.

| Persona | Cares about | Role in the sale |
|---|---|---|
| **Alpha Dev** | "What's possible?" Lives in the future. *No budget.* | Finds you, experiments, advocates internally, creates social proof |
| **Empowered CTO** | Kairos, weeks off a release cycle, competitive edge. *Has budget.* | Approves spend and strategic fit |
| **VP Engineering** | Team velocity, DX, quality at scale. Fears downtime/security | Evaluates feasibility, tests in staging |
| **SRE / Platform Eng** | Reliability, less toil. *Reads your code before your copy.* | Gatekeeps operational risk |

> The Alpha Dev is **not your long-term customer**. They chase the next shiny thing. You need them anyway: they carry new tech to the people who pay.

## Framework 2: Jobs to be done, not demographics (Czakon)

A job title is not actionable; a **job** is. Write it as:

> *When [situation], I want to [motivation], so I can [expected outcome].*

Example: *"When I inherit a service with no tests, I want to generate a safety net fast, so I can refactor without fear."* That sentence tells you the trigger, the pain, and the win. A demographic never does.

## Decision tree: single-player or complex sale?

```
Does the developer who adopts also control the budget?
├─ YES  → single-player / PLG motion.
│         ICP centers on the adopter. Optimize time-to-value, self-serve, transparent pricing.
└─ NO   → complex sale.
          ICP centers on the adopter FOR ADOPTION, and the buyer FOR REVENUE.
          You need a "what's in it for me" for every persona above.
```

## Sharpen it: the 5-attribute ICP

Fill every line with something a stranger couldn't guess:
1. **Company shape**: stage, size, team structure (e.g. "50-500-engineer companies with a platform team")
2. **Technical context**: stack / recent change (e.g. "just adopted Kubernetes")
3. **The trigger**: what just happened that makes this urgent now
4. **The pain, in their words**: the exact phrase they'd use (get this from `talk-to-users`)
5. **Who says no**: the segment you are deliberately *not* for

## Mistakes that look reasonable

- **TAM theater**: "there are 30M developers." True and useless. Nobody sells to 30M anyone.
- **Budget-chasing**: writing everything for the CTO/VP because they pay. They don't visit your homepage; the developer does.
- **Persona = job title**: "backend engineers." That's a hat, not a human. Use the job.
- **One persona, complex sale**: nailing the Alpha Dev and forgetting the buyer → adoption with no revenue.

## Example

❌ "For developers who want to ship faster."
✅ "For **platform engineers at 50-500-eng companies who just standardized on Kubernetes** and are drowning in hand-written YAML, the ones who'd say *'I spend a day a week on manifests I shouldn't have to touch.'* Not for solo devs on Heroku."

## Your next 30 minutes

- [ ] Write your ICP with all 5 attributes filled in, including **who says no**.
- [ ] List every persona in your sale and mark: who *finds* it, who *evaluates* it, who *pays*.
- [ ] Rewrite your one-line pitch as a **Job To Be Done** (`When… I want… so I can…`).
- [ ] If you couldn't fill attribute #4 in their real words → you owe yourself `talk-to-users` before anything else.

---
Grounded in Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).
When a framework can't make the call, that's what a human is for: [The DevTool GTM Company](https://thedevtoolgtmcompany.com).
