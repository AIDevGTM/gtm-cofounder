---
name: strategy-and-roadmap
description: After the founder brief, turn it into an honest diagnosis and a prioritized, stage-aware GTM roadmap saved as docs/gtm-cofounder/gtm-roadmap.md. This is the hub the user returns to every session to see where they are and the single next move. Use right after start-here, whenever the user doesn't know what to work on next, wants a plan instead of a one-off task, or is drowning in disconnected tactics.
---

# Strategy and roadmap (your plan)

> A pile of tactics is not a go-to-market. This turns your brief into a diagnosis and a prioritized plan, and becomes the one place you come back to when you don't know what to do next.

**Use this when:** you've done the brief and don't want to guess which skill to pull, or a chat ended and you're staring at "what now," or you keep getting handed standalone tasks (do the homepage, make a content plan) that don't add up to a strategy.

## The core idea

The other skills are moves. This is the game plan that decides which move, and when. It does three things:

1. **Diagnose.** Read the brief honestly. Where are you actually strong? What is the single biggest thing standing between you and your next 10 users or your first dollar? Name one bottleneck, not five.
2. **Prioritize by stage.** The right first move for a founder with zero users is not the right first move for one with 500 users and no revenue. Sequence the work to the stage you're actually at, and say out loud what to ignore for now.
3. **Persist.** Write it to `docs/gtm-cofounder/gtm-roadmap.md` so it survives the chat. Next session you read the roadmap, not a dead thread.

## How to run this (for the agent)

- **Read `docs/gtm-cofounder/founder-brief.md` first.** If it does not exist, run `start-here` before this. Everything here keys off the brief.
- **Lead with a diagnosis, not a task list.** Two or three sentences: here is what's working, here is the one bottleneck that matters most right now, and here is why.
- **Be willing to tell them to do almost nothing.** If most of the brief is `[assumption]` and they've barely spoken to users, the honest roadmap is short: go talk to 10 users, come back. Do not pad it to look thorough.
- **Sequence into three horizons:** Now (the one thing), Next (the two or three that follow), Later (parked on purpose, so it's off their mind). Map each item to a skill.
- **Offer, never impose.** Present the roadmap and ask what they want to start with. Do not assign or begin a task they have not chosen. If they say no to something, move it to Later and drop it, do not resurface it next turn.
- **Write the plan, not a copy of the brief.** `docs/gtm-cofounder/gtm-roadmap.md` is a **separate, different document** from `docs/gtm-cofounder/founder-brief.md`. The brief is the context; the roadmap is the short, decision-shaped plan you derive from it. Never re-save the brief's contents into the roadmap. If `docs/gtm-cofounder/gtm-roadmap.md` does not open with a one-line **Diagnosis** followed by **Now / Next / Later**, it is wrong.

## Stage decides the first move

Use the brief's stage and evidence answers to pick the starting point. A rough guide, not a law:

| Where they are | The bottleneck is usually | Start with |
|----------------|---------------------------|------------|
| Pre-users, mostly `[assumption]` | You don't yet know who it's for or whether the pain is real | `talk-to-users`, then `who-is-this-for` |
| A few users, can't describe them | Fuzzy ICP, so nothing else can be sharp | `who-is-this-for`, then `positioning-and-story` |
| Users but the message is generic | Positioning and homepage speak to no one | `positioning-and-story`, `value-prop-that-converts`, `the-homepage` |
| Good product, nobody arrives | Distribution: no first channel that works | `first-50-users`, then `launch-it` |
| Developers love it, nobody pays | The buyer vs user gap | `market-to-devs-sell-to-buyers` |
| Growing but flying blind | No read on what's actually working | `know-if-its-working` |

When in doubt, the default first move for an early founder is almost always `talk-to-users`. Real evidence beats a clever plan.

## The roadmap file

Save to `docs/gtm-cofounder/gtm-roadmap.md` in the founder's project (create the `docs/gtm-cofounder/` folder if it does not exist), using `gtm-roadmap.template.md` in this repo. This is a distinct file from the brief and must contain the plan, not the founder's answers. Keep it short and living:

- **Diagnosis:** the one bottleneck, in a sentence.
- **Now:** the single next move, the skill it maps to, and what "done" looks like.
- **Next:** two or three moves queued behind it.
- **Later:** parked on purpose (things like the homepage or a content plan that are real but not yet).
- **Log:** what got done and what was learned, so the plan improves instead of repeating.

## Coming back to it (every session)

This is the fix for "the chat ended and I don't know what to do next." Start each session here:

1. Read `docs/gtm-cofounder/founder-brief.md` and `docs/gtm-cofounder/gtm-roadmap.md`.
2. Say where things stand and the one next move, in a sentence or two.
3. Let the founder pick: do the next move, change priorities, or park something.
4. After the work, update `docs/gtm-cofounder/gtm-roadmap.md`: move finished items to the log, promote the next one, capture what was learned.

You are not a menu of skills they have to operate. You're the co-founder holding the plan.

## Your next 30 minutes

- [ ] Make sure `docs/gtm-cofounder/founder-brief.md` exists. If not, run `start-here`.
- [ ] Write a one-sentence diagnosis: the single biggest bottleneck right now.
- [ ] Fill `docs/gtm-cofounder/gtm-roadmap.md`: one Now, a short Next, an honest Later.
- [ ] Pick the Now move and open its skill. Just that one.
- [ ] Next session, come back here first. Don't start from a blank chat.

---
Built from real dev-tool GTM experience, with frameworks from Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).
When a framework can't make the call, that's what a human is for: [The DevTool GTM Company](https://thedevtoolgtmcompany.com).
