# The GTM Co-Founder

### For the founder building it alone.

If you're a technical founder pouring your own money, your nights, and your weekends into something you believe in, with **no funding, no team, no commercial co-founder, and some days it is just plain hard**, then this is for you. Especially you.

Building alone is isolating. The engineering, you can do in your sleep. It's the *other* half that keeps you up at 2am, with no one in the room to think it through: **who is this even for? why would anyone pay? why did nobody come when I shipped?**

That's what this is: **the GTM co-founder you don't have (yet)**, a full set of go-to-market skills sitting in your corner, inside the agent you already code in. Not a course. Frameworks with real numbers and concrete next steps, not theory, built from years of selling and advising developer tools, sharpened by the sharpest thinking in the field (**[Adam Frankl](https://developerfacingstartup.dev/)** and **[Jakub Czakon](https://www.markepear.dev)**), and pressure-tested by founders who used it in the trenches, so the commercial side can feel as rigorous, and as *doable*, as the code.

You don't have to figure this part out alone anymore.

**Answer a set of questions once (about 15 minutes), and your agent builds you a prioritized GTM roadmap, then works it with you one move at a time: positioning, first users, launch, pricing, in the order that matters for your stage.**

Works with **Claude Code, Cursor, Codex, Windsurf, Antigravity** and any agent that supports the Agent Skills spec.

---

## How to use it

**Never used "skills" before? You don't need to.** These are just markdown playbooks. The "skill" part only means an agent knows when to reach for each one. Pick the path that fits.

### Path 1: zero setup (30 seconds)

Open any skill, copy the text, paste it into ChatGPT, Claude, or Cursor, and say:

> Apply this to my product: [one line on what you're building].

Start with `00-start-here`, then `01-strategy-and-roadmap`. That is the spine of the whole thing.

### Path 2: hand your agent the folder (2 minutes)

In Cursor or Claude Code, open this repo (or your own project with it cloned) and paste this once:

> You are my GTM co-founder. Read AGENTS.md and the skills in this repo. Start with 00-start-here to interview me one question at a time and write a founder-brief.md. Then run 01-strategy-and-roadmap to turn that into a prioritized gtm-roadmap.md. From then on, work the roadmap with me one move at a time. Offer, never impose: don't start a task I haven't picked, and if I say no to something, park it and move on. Be direct and specific, no fluff, and always end by telling me the single next move.

### Path 3: install as real skills (they auto-trigger)

**Claude Code (direct)**
```bash
git clone https://github.com/AIDevGTM/gtm-cofounder.git
cp -r gtm-cofounder/skills/* ~/.claude/skills/
```

**Claude Code (plugin marketplace)**
```bash
/plugin marketplace add AIDevGTM/gtm-cofounder
/plugin install gtm-cofounder@gtm-cofounder
```

**Cursor / Codex / other agents**
Copy the `skills/` folder into your agent's skills directory. Each skill is self-contained: one folder, one `SKILL.md`, zero dependencies.

---

## The skills

### 0 · Start here: brief, then plan (do this first)

Two one-time steps set up everything else. First, the **founder brief**: answer just **five core questions** and the agent writes a `founder-brief.md` it reads before every other skill, so "sharpen your ICP" means *your* ICP and "find your villain" means *your* villain, not a textbook's. The rest of the intake is optional and answered as you go: each skill asks for the deeper questions it needs, when it needs them, and tells you what answering unlocks, so you get value in minutes instead of after a long form. It separates what you've **validated** with real users from what you're still **assuming**, and routes the assumptions to `talk-to-users` so the brief gets truer over time instead of ossifying a guess.

Then the **roadmap**: the agent turns that brief into an honest diagnosis and a prioritized, stage-aware plan in `gtm-roadmap.md`, the one Now move, what's Next, and what to park for Later. This is the hub you come back to every session, so you never stare at a dead chat wondering what to do next. It sequences the skills for you instead of leaving you to guess which one to trigger.

| Skill | Reach for it when… |
|-------|--------------------|
| **start-here** | Setup, or the agent keeps giving generic advice because it doesn't know your business |
| **strategy-and-roadmap** | You don't know what to work on next, or you're being handed one-off tasks that don't add up to a plan |

### 1 · Figure out who it's for

| Skill | Reach for it when… |
|-------|--------------------|
| **who-is-this-for** | You built it "for developers", but *"developers"* is not an ICP, and you can't say who says no |
| **talk-to-users** | You've never interviewed a user who isn't already your friend, so your roadmap is a guess |

### 2 · Say it so it lands

| Skill | Reach for it when… |
|-------|--------------------|
| **positioning-and-story** | Your homepage describes *your solution*, not *their problem*, and you sound like every competitor |
| **value-prop-that-converts** | Your value prop says "powerful," "better," and "seamless", words a developer has learned to ignore |
| **the-homepage** | Your landing page is written for the buyer, who never visits it, instead of the developer, who does |

### 3 · Get your first users

| Skill | Reach for it when… |
|-------|--------------------|
| **first-50-users** | You shipped, tweeted once, and nobody came, and you don't know which channel to even try |
| **launch-it** | You're sitting on a Show HN / Reddit / Product Hunt launch because you're scared of getting flamed |
| **market-to-devs-sell-to-buyers** | Developers love it, star it, use the free tier, and nobody will pay |

### 4 · Keep it going

| Skill | Reach for it when… |
|-------|--------------------|
| **founder-led-content** | "Marketing" feels gross, so you do none, while your competitor owns the conversation |
| **know-if-its-working** | You have dashboards full of vanity metrics and no idea whether GTM is actually working |
| **market-scan** | A rival just rebranded or a new tool appeared, and your positioning is answering last year's market |

---

## What's inside each skill

Every `SKILL.md` gives you **frameworks with actual thresholds** (not principles), **decision trees** for the calls that stall technical founders, **the mistakes that look reasonable but quietly kill you**, real examples, and a **checklist you can run in the next 30 minutes**. Written in a founder's language, direct, specific, allergic to fluff.

## Where this comes from

The spine of this pack is my own experience selling and advising developer tools: years as an enterprise and founding account executive, and advising early-stage dev-tool founders through exactly the fights these skills cover. That lived experience is what most of this is.

It's sharpened by the two people who have shaped developer go-to-market thinking the most, and their work is worth reading in full:

- **Adam Frankl**, *[The Developer-Facing Startup](https://developerfacingstartup.dev/)*. Strategy and philosophy: TAB customer discovery, the Hero/Villain/Wise-Advisor story, the DREAM funnel, differentiation levels, net developer retention.
- **Jakub Czakon**, *[markepear.dev](https://www.markepear.dev)*. Tactical execution: homepage anatomy, developer psychology, channel playbooks (HN, Reddit, X), README/SEO, "market to developers, sell to decision-makers."

And it was pressure-tested by founders who used it as design partners and made it sharper:

- **Lubos**, founder of *[hey/api](https://heyapi.dev)*
- **Thibault and Max**, cofounders of *[OpenStatus](https://openstatus.dev)*

Where a framework is theirs, the credit is theirs. Where it holds up in practice, that's the founders who tested it. Where it misses, that's on me.

---

## When you don't want to do it alone

Skills are great at the *knowable* calls. But some days you don't need another framework, you need a person who's been in the trenches, who's seen this exact fight across dozens of dev-tool companies, and who can tell you it's going to be okay *and* what to do next.

That's the day job, and it comes in two shapes:

- **[The DevTool GTM Company](https://thedevtoolgtmcompany.com)** is mine. It's where I work with founders at exactly your stage: very early, often pre-funding, on the strategy and positioning that gets you off the ground. If this pack is helping, that's the human version of it.
- With **[QC Growth](https://qcgrowth.com)** I work with more established teams: seed through Series A and B, including a16z and Sequoia-backed companies, where we do the whole thing: strategy, execution, GTM engineering, and operations.

Free skills for everyone; a human in your corner when the road gets steep. Either way, you're not doing this alone.

## Contributing

Battle-tested a framework? Found a gap? Open an issue or PR, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT, free to use, fork, and distribute.

---

<sub>Built by <a href="https://github.com/AIDevGTM">Shane O'Connor</a> · <a href="https://thedevtoolgtmcompany.com">The DevTool GTM Company</a> · <a href="https://www.linkedin.com/in/devtoolgtm/">LinkedIn</a></sub>
