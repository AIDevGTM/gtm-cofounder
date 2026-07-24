# The Commercial Co-Founder

### For the founder building it alone.

If you're a technical founder pouring your own money, your nights, and your weekends into something you believe in, with **no funding, no team, no commercial co-founder, and some days it is just plain hard**, then this is for you. Especially you.

Building alone is isolating. The engineering, you can do in your sleep. It's the *other* half that keeps you up at 2am, with no one in the room to think it through: **who is this even for? why would anyone pay? why did nobody come when I shipped?**

That's what this is: **the commercial co-founder you don't have (yet)**, 10 go-to-market skills sitting in your corner, inside the agent you already code in. Not a course. Not theory. Frameworks with real thresholds and 30-minute checklists, distilled from the two sharpest minds in developer go-to-market, **[Adam Frankl](https://thedeveloperfacingstartup.com)** (*The Developer-Facing Startup*) and **[Jakub Czakon](https://www.markepear.dev)** (*markepear.dev*), so the commercial side can feel as rigorous, and as *doable*, as the code.

You don't have to figure this part out alone anymore.

Works with **Claude Code, Cursor, Codex, Windsurf, Antigravity** and any agent that supports the Agent Skills spec.

---

## Install

### Claude Code (direct)
```bash
git clone https://github.com/AIDevGTM/commercial-cofounder.git
cp -r commercial-cofounder/skills/* ~/.claude/skills/
```

### Claude Code (plugin marketplace)
```bash
/plugin marketplace add AIDevGTM/commercial-cofounder
/plugin install commercial-cofounder@commercial-cofounder
```

### Cursor / Codex / other agents
Copy the `skills/` folder into your agent's skills directory. Each skill is self-contained, one folder, one `SKILL.md`, zero dependencies.

---

## The skills

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

---

## What's inside each skill

Every `SKILL.md` gives you **frameworks with actual thresholds** (not principles), **decision trees** for the calls that stall technical founders, **the mistakes that look reasonable but quietly kill you**, real examples, and a **checklist you can run in the next 30 minutes**. Written in a founder's language, direct, specific, allergic to fluff.

## Credit where it's due

These skills stand on two people's work, go read the originals:

- **Adam Frankl**, *[The Developer-Facing Startup](https://thedeveloperfacingstartup.com)*. The strategy and philosophy: TAB customer discovery, the Hero/Villain/Wise-Advisor story, the DREAM funnel, differentiation levels, net developer retention.
- **Jakub Czakon**, *[markepear.dev](https://www.markepear.dev)*. The tactical execution: homepage anatomy, developer psychology, channel playbooks (HN, Reddit, X), README/SEO, "market to developers, sell to decision-makers."

This repo translates their frameworks into agent-runnable skills for early-stage founders. If it's useful, the credit is theirs; if a framework is misapplied, that's on this distillation.

---

## When you don't want to do it alone

Skills are great at the *knowable* calls. But some days you don't need another framework, you need a person who's been in the trenches, who's seen this exact fight across dozens of dev-tool companies, and who can tell you it's going to be okay *and* what to do next.

That's the day job: **[The DevTool GTM Company](https://thedevtoolgtmcompany.com)**, go-to-market advisory for AI & developer-first founders. Free skills for everyone; a human in your corner when the road gets steep. Either way, you're not doing this alone.

## Contributing

Battle-tested a framework? Found a gap? Open an issue or PR, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT, free to use, fork, and distribute.

---

<sub>Built by <a href="https://github.com/AIDevGTM">Shane O'Connor</a> · <a href="https://thedevtoolgtmcompany.com">The DevTool GTM Company</a> · <a href="https://www.linkedin.com/in/devtoolgtm/">LinkedIn</a></sub>
