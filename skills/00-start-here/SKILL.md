---
name: start-here
description: Interview the founder once and write a docs/gtm-cofounder/founder-brief.md that every other skill reads first, so the advice is about their real business, not a textbook. Use this before anything else, or whenever the agent lacks context on the founder's product, ICP, market, or stage, or is giving generic GTM advice.
---

# Start here (your founder brief)

> Every other skill is only as sharp as what the agent knows about *your* business. This is that context. Do it once, and every skill after it gets personal.

**Use this when:** it's your first time here, or the advice you're getting feels generic and textbook because the agent doesn't actually know your product, your users, or your stage.

## The core idea

Answer **five core questions** and the agent writes a **`docs/gtm-cofounder/founder-brief.md`** in your project, enough to give you a real diagnosis and a roadmap in minutes. Everything else is optional and answered as you go: each skill pulls the deeper questions it actually needs, when it needs them, and tells you what answering unlocks. So you start seeing value fast, and the brief gets richer the more you use it, instead of facing a wall of questions on day one.

And the part that matters most: separate what you have **validated** (a real user who is not your friend told you) from what you are **assuming** (your best guess for now). Assumptions are completely fine to start with. They just get sent to `talk-to-users` to become real, so you never build a beautiful go-to-market on a guess.

## How to run this (for the agent)

- **Ask the five core questions one at a time, and nothing else.** One question, wait for the answer, let it shape the next. It should feel like a conversation with a co-founder, not a form to fill in. Never paste multiple questions at once. (If the founder would rather see all five and answer in one go, give them the list, but default to one at a time.)
- Write the brief from those five, then move to `strategy-and-roadmap`. The founder should get a diagnosis and a next move before they answer anything optional.
- **Pull the deeper questions just-in-time.** When a later skill needs more (positioning needs the villain, pricing needs the buyer), ask only the two or three relevant ones right then, and say what answering unlocks. Never front-load them.
- For every substantive answer, ask: "have you heard a real user say this, or is that your read for now?" Tag it `[validated]` or `[assumption]`.
- "Zero users interviewed" is a valid and revealing answer. Note it plainly, no judgment, and flag `talk-to-users` as the highest-priority next step.
- Keep the founder's own words. Don't polish their pain into marketing language.
- Once the core brief is written, do **not** jump into a task or start prescribing work. Hand off to `strategy-and-roadmap`, or ask the founder what they want to tackle. Offer, never impose.

## The core five (answer these first)

This is the whole required intake. Answer these and the agent can already diagnose and plan.

1. In one plain sentence, with no jargon, what does it do?
2. Who exactly is it for? (role, company size and shape, technical context)
3. What do they use today instead, and why you over that?
4. Stage and traction: how many users, and do they come back?
5. Your single **strongest asset**: the most powerful, provable thing you have (a marquee logo, a hard number, a real user quote, a live demand signal).

## Go deeper (optional, answer anytime)

Skip these to start. Each skill asks for the ones it needs, when it needs them. Every question says what answering it unlocks, so you only invest where you want the payoff.

**Positioning and story**
- What painful problem does it kill, in the user's own words? → *becomes your homepage headline and the stakes in your story.*
- What trend is making that pain worse right now? → *this is your villain, what gives your positioning urgency instead of just listing features.*
- What does your homepage or repo description say today? (paste the actual line) → *lets the agent sharpen what you have instead of guessing it.*

**Buyers and pricing**
- Who pays, if that is a different person from who adopts? → *lets the agent design pricing and a sales motion aimed at the real buyer, not just the user.*
- Who is it clearly *not* for? → *a sharp "not for" makes your ICP believable and your messaging land.*
- The job they hire it for: "When [situation], I want to [motivation], so I can [outcome]." → *becomes your value proposition.*

**Distribution and motion**
- Motion: open source, PLG, inbound, sales-led, or unsure? → *picks which channels and tactics actually fit you.*
- Where do your users already hang out and discover tools? → *tells us where to launch and find your first users.*

**Focus**
- What are you deliberately saying no to right now? (the roadmap you're protecting, the requests you turn down) → *keeps the agent from recommending work you've already ruled out.*

**Evidence (be honest, this is the whole point)**
- Which known companies or notable developers already use it, that you can name? → *your strongest proof; even a couple of logos does your credibility work.*
- How many real users have you interviewed who are not friends? → *tells the agent how much of this is validated versus guessed, so nothing gets built on sand.*
- Which answers are still assumptions? → *routes the guesses to `talk-to-users` to make them real.*

## Write the brief

Save the answers to `docs/gtm-cofounder/founder-brief.md` in the founder's project (create the `docs/gtm-cofounder/` folder if it does not exist), using the template in this repo (`founder-brief.template.md`). Keep the `[validated]` / `[assumption]` tags on each answer. This file is the shared memory for every other skill. Write it in plain, human prose, with no em-dashes (use commas, colons, or periods), so it never reads as machine-generated.

Lead the brief with the **strongest asset** (core question 5) at the very top, so the single most powerful thing this founder has anchors every downstream skill. Founders routinely bury it under modesty or detail. As deeper questions get answered over time, add them to the brief under their category.

## Keep it alive

The brief is a living document, not a form you fill once and forget. Every time the founder learns something real from a user (a `talk-to-users` call, a lost deal, a piece of feedback), update the relevant line and flip its tag from `[assumption]` to `[validated]`. A brief that is mostly `[validated]` is a company that knows itself. And run `market-scan` periodically to refresh what has changed *outside* the brief: a rival's rebrand, a new entrant, a shifted category.

## Your next 30 minutes

- [ ] Answer just the **core five**. Rough and honest beats polished and fake.
- [ ] Tag each answer `[validated]` or `[assumption]`.
- [ ] Save it as `docs/gtm-cofounder/founder-brief.md` in your project so your agent reads it.
- [ ] Run `01-strategy-and-roadmap` to get your diagnosis and first move. Don't answer the optional questions yet.
- [ ] Answer deeper questions later, only when a skill asks and tells you what it unlocks.

---
Built from real dev-tool GTM experience, with frameworks from Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).
When a framework can't make the call, that's what a human is for: [The DevTool GTM Company](https://thedevtoolgtmcompany.com).
