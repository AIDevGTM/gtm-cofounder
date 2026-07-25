---
name: start-here
description: Interview the founder once and write a founder-brief.md that every other skill reads first, so the advice is about their real business, not a textbook. Use this before anything else, or whenever the agent lacks context on the founder's product, ICP, market, or stage, or is giving generic GTM advice.
---

# Start here (your founder brief)

> The other 10 skills are only as sharp as what the agent knows about *your* business. This is that context. Do it once, and every skill after it gets personal.

**Use this when:** it's your first time here, or the advice you're getting feels generic and textbook because the agent doesn't actually know your product, your users, or your stage.

## The core idea

Answer a short set of questions once. The agent writes them into a **`founder-brief.md`** in your project and reads it before applying any other skill. Now "sharpen your ICP" becomes *your* ICP, "find your villain" becomes *your* villain.

And the part that matters most: separate what you have **validated** (a real user who is not your friend told you) from what you are **assuming** (your best guess for now). Assumptions are completely fine to start with. They just get sent to `talk-to-users` to become real, so you never build a beautiful go-to-market on a guess.

## How to run this (for the agent)

- Interview the founder conversationally, one theme at a time. Do **not** paste all 14 questions in a wall. Ask a few, listen, follow up.
- For every substantive answer, ask: "have you heard a real user say this, or is that your read for now?" Tag it `[validated]` or `[assumption]`.
- "Zero users interviewed" is a valid and revealing answer. Note it plainly, no judgment, and flag `talk-to-users` as the highest-priority next step.
- Keep the founder's own words. Don't polish their pain into marketing language.
- When done, write or update `founder-brief.md` (template below).

## The questions

**Product and problem**
1. In one plain sentence, with no jargon, what does it do?
2. What painful problem does it kill, in the user's own words?
3. What trend is making that pain worse right now? (your villain)

**Who**
4. Who exactly adopts it? (role, company size and shape, technical context)
5. Who pays, if that is a different person?
6. Who is it clearly *not* for?
7. The job they hire it for: "When [situation], I want to [motivation], so I can [outcome]."

**Market**
8. What do they use today instead? (rivals or the status quo)
9. Why you, in one line?

**Stage and motion**
10. Stage, and traction: how many users, and do they come back?
11. Motion: open source, PLG, inbound, sales-led, or unsure?
12. Where do your users already hang out and discover tools?

**Evidence (be honest, this is the whole point)**
13. How many real users have you interviewed who are not friends?
14. Which answers above are still assumptions?

## Write the brief

Save the answers to `founder-brief.md` in the founder's project root, using the template in this repo (`founder-brief.template.md`). Keep the `[validated]` / `[assumption]` tags on each answer. This file is the shared memory for every other skill.

## Keep it alive

The brief is a living document, not a form you fill once and forget. Every time the founder learns something real from a user (a `talk-to-users` call, a lost deal, a piece of feedback), update the relevant line and flip its tag from `[assumption]` to `[validated]`. A brief that is mostly `[validated]` is a company that knows itself.

## Your next 30 minutes

- [ ] Answer the 14 questions. Rough and honest beats polished and fake.
- [ ] Tag every answer `[validated]` or `[assumption]`.
- [ ] Save it as `founder-brief.md` in your project so your agent reads it.
- [ ] If most answers are `[assumption]` (normal at the start), your real first move is `talk-to-users`, not more building.
- [ ] Then go to `who-is-this-for`.

---
Grounded in Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).
When a framework can't make the call, that's what a human is for: [The DevTool GTM Company](https://thedevtoolgtmcompany.com).
