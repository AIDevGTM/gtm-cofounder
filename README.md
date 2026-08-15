# The GTM Co-Founder

[![The GTM Co-Founder - Open-source GTM skills for developer tools and AI products | Product Hunt](https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1207906&theme=light&period=daily)](https://www.producthunt.com/products/the-gtm-co-founder?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-the-gtm-co-founder)

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/AIDevGTM/gtm-cofounder?style=flat)](https://github.com/AIDevGTM/gtm-cofounder/stargazers)

### For whoever is carrying the go-to-market, often alone.

If you're a technical founder pouring your own money, your nights, and your weekends into a developer tool or an AI product you believe in, with **no funding, no team, no commercial co-founder, and some days it is just plain hard**, then this is for you. Especially you.

And it is not only for founders. If you're the first GTM hire, or the founding account executive carrying the commercial side of a technical product with no playbook and no team, this is for you too. The title is different; the fight is the same.

Building alone is isolating. The part you're good at, whether that's shipping the product or working the deal, you can do in your sleep. It's the *other* half that keeps you up at 2am, with no one in the room to think it through: **who is this even for? why would anyone pay? why did nobody come when we shipped?**

That's what this is: **the GTM co-founder you don't have (yet)**, a full set of go-to-market skills sitting in your corner, inside the agent you already work in. Not a course. Frameworks with real numbers and concrete next steps, not theory, built from years of selling and advising developer tools and AI products, sharpened by the sharpest thinking in the field (**[Adam Frankl](https://developerfacingstartup.dev/)** and **[Jakub Czakon](https://www.markepear.dev)**), and pressure-tested by founders and GTM operators who used it in the trenches, so the commercial side can feel as rigorous, and as *doable*, as the product.

You don't have to figure this part out alone anymore.

**Answer a set of questions once (about 15 minutes), and your agent builds you a prioritized GTM roadmap, then works it with you one move at a time: positioning, first users, launch, pricing, in the order that matters for your stage.**

Not marketing tactics or SEO skills. This is the strategy half of go-to-market: who it's for, why they'd pay, and how to land your first users. For the person who can build or sell almost anything, but freezes on that.

Works with **Claude Code, Cursor, Codex, Windsurf, Antigravity** and any agent that supports the Agent Skills spec.

---
## See it in action

*A real example: five questions, then a diagnosis they couldn't see themselves.*

https://github.com/user-attachments/assets/54bbb54a-006d-4189-ba63-5f754fdf5268

## Get your GTM diagnosis in 15 minutes

One path. In the AI coding agent you already use (Claude Code, Cursor, Codex, Windsurf), tell it:

> Install the skills from https://github.com/AIDevGTM/gtm-cofounder and run 00-start-here with me.

If your agent cannot fetch the repo from a link, clone it first with `git clone https://github.com/AIDevGTM/gtm-cofounder.git` (or open it in your editor), then give it the same instruction.

`00-start-here` asks you five questions, one at a time, and writes your **founder brief**: the file every other skill reads first, so the advice is about your product, not a textbook's. A few minutes, no long form.

Then tell it:

> Run 01-strategy-and-roadmap.

That is the payoff: an honest diagnosis of the GTM problem to work on **now**, what to **not** work on yet, and your **single next move**.

**Why this beats generic AI marketing advice.** Tell a normal chatbot "I have 800 GitHub stars but almost nobody pays" and you get ten marketing tactics. GTM Co-Founder does the opposite. It tells you that you do not yet know whether people activate, come back, or would ever pay, so reaching for tactics now is the wrong move. Your next step is not "post more," it is the one piece of evidence you need to go and get. The value is not more ideas. It is knowing what to do next.

### Other ways to install

The path above works in any agent that supports the Agent Skills spec (Claude Code, Cursor, Codex, Windsurf, Antigravity). Reach for these only if you want the skills installed so your agent auto-triggers them, or you are not in a coding agent at all.

- **No coding agent (ChatGPT, Claude, plain chat):** open any skill, copy the text, paste it in, and say "apply this to my product: [one line on what you're building]." Start with `00-start-here`, then `01-strategy-and-roadmap`.
- **No terminal:** grab a zip from the [latest release](https://github.com/AIDevGTM/gtm-cofounder/releases/latest). In the Claude apps, go to **Customize → Skills → Create skill** and upload a skill's zip. For Claude Code, unzip and move the folders into `~/.claude/skills/`.
- **Claude Code (direct):**
  ```bash
  git clone https://github.com/AIDevGTM/gtm-cofounder.git
  cp -r gtm-cofounder/skills/* ~/.claude/skills/
  ```
- **Claude Code (plugin marketplace)** _(run in the Claude Code CLI):_
  ```bash
  /plugin marketplace add AIDevGTM/gtm-cofounder
  /plugin install gtm-cofounder@gtm-cofounder
  ```
- **skills.sh CLI (any agent)** _(requires Node.js):_
  ```bash
  npx skills add AIDevGTM/gtm-cofounder
  ```
- **Cursor / Codex / other agents:** copy the `skills/` folder into your agent's skills directory. Each skill is self-contained: one folder, one `SKILL.md`, zero dependencies.

---

## The skills

### 0 · Start here: brief, then plan (do this first)

Two one-time steps set up everything else. First, the **founder brief**: answer just **five core questions** and the agent writes a `docs/gtm-cofounder/founder-brief.md` it reads before every other skill, so "sharpen your ICP" means *your* ICP and "find your villain" means *your* villain, not a textbook's. If you run it inside your project, it reads your repo first (README, recent commits, PR titles, open issues) to pre-fill the brief with what you've actually shipped, so the advice is specific from the first minute instead of generic. The rest of the intake is optional and answered as you go: each skill asks for the deeper questions it needs, when it needs them, and tells you what answering unlocks, so you get value in minutes instead of after a long form. It separates what you've **validated** with real users from what you're still **assuming**, and routes the assumptions to `talk-to-users` so the brief gets truer over time instead of ossifying a guess.

Then the **roadmap**: the agent turns that brief into an honest diagnosis and a prioritized, stage-aware plan in `docs/gtm-cofounder/gtm-roadmap.md`, the one Now move, what's Next, and what to park for Later. This is the hub you come back to every session, so you never stare at a dead chat wondering what to do next. It sequences the skills for you instead of leaving you to guess which one to trigger.

| Skill | Reach for it when… |
|-------|--------------------|
| **start-here** | Setup, or the agent keeps giving generic advice because it doesn't know your business |
| **strategy-and-roadmap** | You don't know what to work on next, or you're being handed one-off tasks that don't add up to a plan |

### Runs throughout (a gate, not a step)

| Skill | Reach for it when… |
|-------|--------------------|
| **review-the-work** | Before you ship anything. The agent stops being the author and stress-tests the piece as a skeptic, so weak or unprovable claims never reach you |

### 1 · Figure out who it's for

| Skill | Reach for it when… |
|-------|--------------------|
| **who-is-this-for** | You built it "for developers", but *"developers"* is not an ICP, and you can't say who says no |
| **talk-to-users** | You've never interviewed a user who isn't already your friend, so your roadmap is a guess |

### 2 · Say it so it lands

| Skill | Reach for it when… |
|-------|--------------------|
| **positioning-and-story** | Your homepage describes *your solution*, not *their problem*, and you sound like every competitor |
| **beyond-the-wrapper** | *(AI products only, skip if not)* People call your AI product "just a wrapper," everyone claims AI, and you can't say why you win when the model is a commodity |
| **value-prop-that-converts** | Your value prop says "powerful," "better," and "seamless", words a developer has learned to ignore |
| **the-homepage** | Your landing page is written for the buyer, who never visits it, instead of the developer, who does |

### 3 · Get your first users

| Skill | Reach for it when… |
|-------|--------------------|
| **time-to-first-value** | People sign up or star it, then never get it working, or come once and never come back |
| **first-50-users** | You shipped, tweeted once, and nobody came, and you don't know which channel to even try |
| **launch-it** | You're sitting on a Show HN / Reddit / Product Hunt launch because you're scared of getting flamed |
| **market-to-devs-sell-to-buyers** | Developers love it, star it, use the free tier, and nobody will pay |
| **pricing** | You're guessing at a number, gave it away too cheap, or "developers won't pay" so you never charge |
| **founder-led-sales** | Developers love it and use the free tier, but you've never sold anything and "let me think about it" kills every deal |

### 4 · Keep it going

| Skill | Reach for it when… |
|-------|--------------------|
| **founder-led-content** | "Marketing" feels gross, so you do none, while your competitor owns the conversation |
| **know-if-its-working** | You have dashboards full of vanity metrics and no idea whether GTM is actually working |
| **market-scan** | A rival just rebranded or a new tool appeared, and your positioning is answering last year's market |

---

## What's inside each skill

Every `SKILL.md` gives you **frameworks with actual thresholds** (not principles), **decision trees** for the calls that stall whoever owns GTM, **the mistakes that look reasonable but quietly kill you**, real examples, and a **checklist you can run in the next 30 minutes**. Written in a founder's language, direct, specific, allergic to fluff.

## Where this comes from

The spine of this pack is my own experience selling and advising developer tools and AI products: years as an enterprise and founding account executive, and advising early-stage dev-tool and AI founders through exactly the fights these skills cover. That lived experience is what most of this is.

It's sharpened by the two people who have shaped developer go-to-market thinking the most, and their work is worth reading in full:

- **Adam Frankl**, *[The Developer-Facing Startup](https://developerfacingstartup.dev/)*. Strategy and philosophy: TAB customer discovery, the Hero/Villain/Wise-Advisor story, the DREAM funnel, differentiation levels, net developer retention.
- **Jakub Czakon**, *[markepear.dev](https://www.markepear.dev)*. Tactical execution: homepage anatomy, developer psychology, channel playbooks (HN, Reddit, X), README/SEO, "market to developers, sell to decision-makers."

And it was pressure-tested by founders who used it as design partners and made it sharper:

- **Lubos**, founder of *[hey/api](https://heyapi.dev)*
- **Thibault and Max**, cofounders of *[OpenStatus](https://openstatus.dev)*

Where a framework is theirs, the credit is theirs. Where it holds up in practice, that's the founders who tested it. Where it misses, that's on me.

---

## When you don't want to do it alone

Skills are great at the *knowable* calls. But some days you don't need another framework, you need a person who's been in the trenches, who's seen this exact fight across dozens of dev-tool and AI companies, and who can tell you it's going to be okay *and* what to do next.

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
