---
name: time-to-first-value
description: "Turn a curious developer into an activated one: the docs, the quickstart, and the first-run experience that gets them to their first real win fast, and back again. Use when people sign up or star the repo but never get it working, come once and never return, or you're about to pour traffic into a first-run that leaks."
---

# Time to first value (get them to the first win)

> For a dev tool, the product is the pitch. A developer tries it alone and decides in minutes. Acquisition without activation is just a faster way to lose people.

**Use this when:** people sign up or star the repo and then nothing, they get it working once and never come back, your docs assume the reader already understands it, or you are about to spend on a launch or a channel while the first ten minutes still leak.

## The core idea

You can nail your positioning, your homepage, and your launch, and still lose everyone in the first ten minutes. For a dev tool the first run *is* the sale: the developer tries it, alone, without talking to you, and decides. Two gates, straight from Frankl's DREAM funnel:

- **Evaluation:** can they get it working over a weekend, with zero human help? (the weekend test)
- **Activation:** how fast do they reach their first real win, the "I'm awesome" moment (time to first value)?

Fix this before you scale acquisition. Pouring users into a leaky first run just loses them faster, and `know-if-its-working` will show you that retention, not signups, is the number that matters.

## The two thresholds

**The weekend test (Frankl).** A motivated developer should get your product doing something real over a weekend, without a call, a demo, or an email to you. If they cannot, that is your single highest-leverage work, above any channel, launch, or homepage tweak.

**Time to first value (Czakon: "time to Hello World").** Measured in minutes, not hours, and the first meaningful win in the same sitting, not after an onboarding call next Tuesday. The first "Hello World" should be minutes in; the first real "oh, this is useful" should be that same session.

**The win belongs to the developer, not your product (Frankl: the developer is the hero).** The aha is "look what I just did," not "look what our platform can do." Design the first run so the developer feels capable, fast.

## Framework: the friction log (Czakon)

The core tool. Do not try to document every path. Nail the ONE most common path to first value.

1. Pick the single core journey a new developer takes to their first win.
2. Walk it yourself as a stranger: new machine or incognito, no insider shortcuts, no filling in gaps from memory.
3. At every step, log three things: the **question** they have, the **frustration** they hit, the **friction or barrier** that makes them stop.
4. Fix the obvious barriers first. Cut the top three places a motivated dev would quit.
5. Put a **metric on each core moment** so you can see where they drop.

## What removes friction (and what adds it)

Removes it:
- Free tier or trial, **no credit card, no "contact sales"** (Czakon: hard barriers send devs straight to a competitor).
- An idiot-proof install and a **copy-pasteable example** that works on the first try.
- A "get started in 5 minutes" path, and a docs quickstart written for the stranger, not the expert.
- A sandbox or demo populated with data close to **their** real use case, not `foo` and `bar` (Czakon: realistic sandbox data gets you most of the way).

Adds it:
- A signup wall, a sales call, or a credit card in front of the first win.
- Docs written by someone who already understands the product.
- A first run that shows off your architecture instead of getting the developer to their result.

## Decision tree

```
Can a motivated new dev reach a real win alone, in one sitting, without talking to you?
├─ NO  → this is your highest-leverage work, above any channel or launch.
│         Run a friction log on the one core path and cut the top 3 barriers.
└─ YES → do they come back the next week?
         ├─ NO  → the first win isn't valuable or sticky enough. Wrong "aha,"
         │         or no reason to return. Re-pick the activation moment.
         └─ YES → now acquisition is worth scaling. Go to `first-50-users`.
```

## Mistakes that look reasonable

- **Optimizing the homepage or the launch while the first run leaks.** Fix activation before acquisition. A great channel into a broken first run just burns the channel.
- **Celebrating signups.** Signups are vanity if they never activate. Watch time to first value and week-one activation, not the top of the funnel (see `know-if-its-working`).
- **Gating the first win** behind a wall, a demo, or a credit card. Developers bounce and do not come back.
- **Making your product the hero of the first run.** The developer is the hero. The moment is "look what I did," not "look what it does."
- **Writing docs for the expert.** The quickstart is for the stranger who has never seen it. Test it on one.
- **Documenting every path.** Nail the one common path first. Perfect coverage of a journey nobody takes is wasted work.

## Your next 30 minutes

- [ ] Name the ONE core path a new developer takes to their first real win. Just one.
- [ ] Walk it as a stranger (incognito or a clean machine), and time it. Log every question, frustration, and barrier at each step.
- [ ] Circle the first three points where a motivated dev would give up. That is your backlog, ahead of any marketing task.
- [ ] Define the single "I'm awesome" moment, and make it reachable in minutes, in one sitting, with no human help.
- [ ] Put one number on it: time to first value, or the percent of signups that reach the win in week one. Watch it like you watch uptime.

---
Built from real dev-tool GTM experience, with frameworks from Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).
When a framework can't make the call, that's what a human is for: [The DevTool GTM Company](https://thedevtoolgtmcompany.com).
