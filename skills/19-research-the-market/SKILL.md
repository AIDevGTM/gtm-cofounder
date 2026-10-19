---
name: research-the-market
description: "Go outside the founder brief and research the real market before the plan is written: the exact communities, newsletters, and venues where the user's ICP already sits, how comparable products launched and what worked, the problem in strangers' own words, and the rivals and openings the user never mentioned. Saves docs/gtm-cofounder/market-research.md with a link for every finding. Use right after start-here and before strategy-and-roadmap, before picking channels in first-50-users or planning launch-it, or whenever the plan feels like it only repeats what the user already said."
---

# Research the market (what you didn't tell me)

> The brief is what you know. A plan built only from the brief can only rearrange your own answers back to you. This is the step where the agent goes out and finds what you don't know yet: where your users actually are, how products like yours got their first users, and the openings you haven't seen.

**Use this when:** you've just written the brief and want a plan grounded in the real market, not just your own read. Or you're about to pick channels or plan a launch and "post on Reddit and HN" is the best idea on the table. Or the roadmap you got back felt like a tidy summary of what you said.

## The core idea

The interview pulls out what's in your head. Research brings in what isn't: the specific subreddit where your ICP complained about this exact problem last week, the newsletter they all read, the three products in your space that launched in the last two years and what actually brought their first users, the competitor you didn't name.

**Research is planning-grade evidence, not proof.** Public evidence that 40 people asked for this in a GitHub issue is strong enough to plan a channel around. It is not strong enough to call the pain validated or to set a price. So it gets its own tag, `[researched]`, between `[assumption]` and `[validated]`. Only a real conversation with a real user who is not a friend earns `[validated]`.

## Before you start: can your agent see the web?

- **If your agent can browse or search the web,** it runs the research for real, and every finding carries a link.
- **If it can't,** it says so up front and hands you a short list of exact searches to run (8 to 12, each a copy-paste query with what to look for). You paste back what you find, and it does the analysis. Same output, you're the browser.

Never fake it. An agent without web access that writes up "communities" from memory is guessing, and invented member counts and dead links destroy trust fast.

## How to run this (for the agent)

- **Start from the brief.** Read `docs/gtm-cofounder/founder-brief.md`: the product, the ICP, the alternatives, the stage. That sets what to search for. Then go further than the brief, on purpose.
- **Check the ICP is concrete enough to research.** "Developers" can't be researched; "platform engineers at 50 to 500 person companies running Kubernetes" can. If the ICP is vague, run the research anyway, but aim it at *which segment shows the most pain in public*, and hand that finding to `who-is-this-for`.
- **Every finding has a link and a date.** No link, it doesn't go in. Never invent a community, a member count, a URL, a quote, or a launch result. If you can't verify a number, say "size unknown" rather than estimating.
- **Name venues, never categories.** "Reddit" is not a finding. "r/devops, where three threads in the last month asked for exactly this" is.
- **Rank by fit, not size.** A 4,000-member Discord where your ICP talks about the problem weekly beats a 2 million member subreddit where they never do. For each venue, record the evidence that *your* ICP is there talking about *this* problem.
- **Check the rules of the room.** For every community, note whether it allows self-promotion, and how (a weekly thread, a flair, an outright ban). A channel that bans you on your first post is not a channel.
- **Keep it bounded.** This is a sprint, not a thesis: roughly 20 to 40 searches, an hour of agent time at most. Stop when new searches stop changing the picture.
- **Lead with surprises.** The most valuable part is what the founder didn't say. Put "What I found that you didn't tell me" at the top of the file, and flag anywhere the research disagrees with the brief (they said their users hang out on X, the evidence says Y).
- **Don't rewrite the brief yourself.** Where the research contradicts or sharpens a brief answer, propose the change, and let the founder accept it. Accepted changes go into the brief tagged `[researched]` with the date.
- **Then hand off.** If there's no roadmap yet, go to `strategy-and-roadmap`, which now has to use this file. Offer, never impose.

## The five things to find

### 1. Where your ICP already sits (the watering holes)

Find the 5 to 10 specific places your ICP already goes to discover tools and talk shop. Ways in:

- Search the problem in their words, plus "reddit", "discord", "slack", "forum". Note which rooms keep coming up.
- Search Hacker News (`site:news.ycombinator.com`) for the category and the named alternatives. Who comments, and what do they ask for?
- GitHub: topics, awesome-lists, and the issue trackers of the alternatives. An issue with 50 thumbs-up asking for what you built is a venue *and* a lead list.
- Newsletters, podcasts, and YouTube channels covering the category. Who has the ICP's attention every week?
- Where competitors show up: what they sponsor, which conferences they speak at, which communities their founders post in. Sponsorship spend is a public tell for where they believe the buyers are.
- Integration marketplaces and ecosystems the product plugs into (VS Code, a framework's plugin directory, a cloud marketplace, a Slack app directory).

For each venue: name, link, size and activity signal (members, posts per week, last active), self-promo rules, and the evidence your ICP is there talking about this problem.

### 2. How comparable products launched

Find 3 to 5 products in or next to the category that launched in roughly the last three years. For each: where they launched (find the actual HN thread or Product Hunt page), how it went (points, rank, the top comments, what got praised and what got flamed), and what founders say brought their first users (search "how we got our first users", launch retrospectives, founder interviews and podcasts). Then name the pattern: what worked for products like this one, and what didn't.

### 3. The problem in strangers' own words

Collect 10 to 20 public posts where people describe the pain (forum threads, issues, HN comments, posts, reviews of the alternatives). Keep the link and a short fragment of their words. This list does three jobs: it's language for `positioning-and-story`, interview candidates for `talk-to-users`, and the first people to reach out to in `first-50-users`.

### 4. The rivals and alternatives you didn't name

Search for the products, open-source projects, and homegrown workarounds people actually use for this job, especially the ones missing from the brief. For each, one line: how they position and what they charge. Keep it light. Ongoing competitor tracking belongs to `market-scan`; this is the first full pass.

### 5. Openings

The outside-the-box part. From everything above, name the 3 to 5 openings the founder didn't bring: an underserved segment that shows up loud in the research, a venue no competitor is working, a marketplace or partner ecosystem to ride, a timely hook (a platform change, a deprecation, a pricing change by a big alternative, a conference coming up), a launch pattern that fits this product. Each opening cites the findings it rests on.

## Decision tree: what to do first

```
Can the agent browse the web?
├─ NO  → hand the founder 8-12 exact searches, wait for the pastes, then analyze.
└─ YES → is the ICP concrete (role, company shape, technical context)?
         ├─ NO  → research which segment shows the most public pain,
         │         then route that finding to who-is-this-for.
         └─ YES → run all five, watering holes and comparable launches first.
                  Those two change the plan the most.
```

## The research file

Save to `docs/gtm-cofounder/market-research.md` in the founder's project. Keep it scannable, links on everything, no em-dashes:

```markdown
# Market research
Researched: <date> · Mode: web | founder-pasted

## What I found that you didn't tell me
- 3 to 5 bullets, the surprises and openings, each pointing to the evidence below.
- Where the research disagrees with the brief, say so here.

## Where your ICP sits (ranked by fit)
| Venue | Link | Size / activity | Self-promo rules | Evidence your ICP is there |

## How comparable products launched
- Product: where, how it went (link), what brought first users, the lesson.
- The pattern: ...

## The problem in their words
- "short fragment" (link, date)

## Rivals and alternatives
- Name (link): positioning in a line, pricing.

## Openings
1. Opening, why now, the evidence it rests on.

## Proposed brief changes
- Brief line → what the research suggests (for the founder to accept).
```

## Mistakes that look reasonable

- **Categories instead of venues.** "Developer communities and social media" is not research. If a line has no link, it's a guess.
- **Size over fit.** Chasing the biggest subreddit because it's big. Your ICP has to be in the room, talking about your problem.
- **Inventing to fill gaps.** A plausible member count or a remembered launch result that you didn't check is worse than "unknown". Founders act on these numbers.
- **Treating research as validation.** Fifty people complaining in public tells you where to go and what to say. It doesn't tell you they'll switch, or pay. That still takes `talk-to-users`.
- **Copying a competitor's launch wholesale.** Their launch fit their product, their audience, and their year. Take the pattern, not the playbook.
- **Researching instead of talking.** Research is an hour, not a hiding place. If it's been a week of research and zero conversations, stop and go talk to the people on your list.

## Your next 30 minutes

- [ ] Tell your agent which mode you're in: it browses, or you paste.
- [ ] Run the research and read "What I found that you didn't tell me" first.
- [ ] Open the top three watering holes yourself. Do they feel like your people? Note any that don't.
- [ ] Accept or reject the proposed brief changes.
- [ ] Run `strategy-and-roadmap` so the plan is built on the brief *and* the research.

---
Built from real dev-tool GTM experience, with frameworks from Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*). This skill exists because of feedback from **Kevin Collins**, founder of [Echofold](https://echofold.ai), who asked for a co-founder that researches the market instead of reflecting his own answers back.
If the research turns up an opening you're not sure how to play, reach out to me on [LinkedIn](https://www.linkedin.com/in/devtoolgtm/).
