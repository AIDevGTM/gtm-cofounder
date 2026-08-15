---
name: launch-it
description: "Plan a developer launch (Show HN, Reddit, Product Hunt) that earns goodwill instead of a flaming. Use when the user is sitting on a launch out of fear, wants to \"go viral,\" or is about to post a press-release-style announcement to a developer community."
---

# Launch it

> Developer communities reward the honest, technical, slightly humble builder and punish the marketer instantly. A Show HN is not an announcement. It's *"I built this thing, here's how it works and what's still rough."*

**Use this when:** you're scared to launch, you're hoping to "go viral," or you're about to drop marketing copy into a room that eats marketing copy for breakfast.

## The core idea

The bar is **usefulness + honesty**, not polish. Developers will test your claims and read your code. Show up as a real engineer sharing real work, be present to answer everything, and never, ever fake it. One genuine launch beats ten hype posts.

## Framework: Show HN anatomy (Czakon / Tailscale lessons)

1. **Title: plain, specific, zero hype.** "Show HN: A faster Postgres migration tool for large tables", not "🚀 The future of database migrations is HERE."
2. **First comment = the story** (post it yourself, immediately):
   - *why* you built it (the itch, ideally your own),
   - *how* it works (technical, concrete),
   - what's genuinely **hard/limited** right now (honesty buys trust),
   - a dead-simple way to try it.
3. **Be present for hours.** Answer every comment, especially the critical ones, technically and without defensiveness. The comment thread *is* the launch.
4. **Never astroturf.** No vote rings, no sock puppets. Communities detect it and the ban is permanent and public.

## Framework: Product Hunt anatomy (fmerian / Kilo lessons)

1. **Name of the product: simply the name of your product in 40 characters or less.**
2. **Tagline: concise and descriptive, in less than 60 characters.** The most important part, the first thing people read on the front page. Avoid hyperbolic words and emojis. Keep it simple and relatable.
3. **Description: a short description of what the product does in less than 500 characters.**
4. **Launch tags: up to three tags.**
5. **Thumbnail: a 240 x 240 pixel thumbnail.**
6. **Image gallery: at least 3 images to show your product.** No stock images, no marketing fluff. Show the product, i.e. product screenshots. You can add social proof and a call-to-action to inspire action. The first image is used as the social preview when you share the link to your launch page.
7. **First comment: essential to get the discussion started.** This comment is posted upon launch. The first 800 characters are displayed. Pro tip: reuse your HN comment.
8. **Be present for the first 4 hours.** Upvote and reply to every comment. Don't just thank. Ask questions, inspire action.
9. **Find a hunter: an established Product Hunt user who can boost your reach.** If you're in dev tools, Flo Merian (@fmerian) is a great one to ask. PH has dialed down hunter influence over time, so a strong launch and a present founder matter most, but a well-connected hunter still helps.

*Framework adapted from Flo Merian's [awesome-product-hunt](https://github.com/fmerian/awesome-product-hunt).*

## Reddit / community launches

- **Give before you take.** Be a real participant for weeks before you post your thing.
- **Read the rules** of the specific subreddit; many ban self-promo outright, so find the ones that don't.
- Frame as *"I made this to solve X, feedback welcome,"* not a pitch.

## The coordinated moment (not spam)

A launch is **one prepared moment** across the channels your ICP actually uses (from `first-50-users`): HN, your own network, and the relevant communities, all on the same day, each tailored to the room. It is not the same copy blasted five places.

## Decision tree: are you ready to launch?

```
Can a stranger get to first value in < 1 hour from docs alone (the weekend test)?
├─ NO  → don't launch yet. A flood of users who bounce burns the channel and the goodwill.
└─ YES → is your Show HN first-comment written (why/how/limits/try)?
         ├─ NO → write it first; it matters more than the product page.
         └─ YES → launch on a Tue-Thu morning US time, then clear your calendar to reply.
```

## Mistakes that look reasonable

- **Hype title**: emojis and superlatives on HN get flagged to death.
- **Absent founder**: posting then leaving; the unanswered thread dies.
- **Defensive replies**: arguing with critics. Thank them, concede the fair points, note what you'll fix.
- **Astroturfing**: instant, permanent reputational damage.
- **Launching too early**: before the weekend test passes, a launch amplifies your weakest moment.

## Your next 30 minutes

- [ ] Draft your Show HN **title**, plain, specific, no hype. Say it out loud; if it sounds like an ad, redo it.
- [ ] Write the **first comment**: why · how · what's hard · how to try. This is the real work.
- [ ] Confirm the weekend test passes (see `know-if-its-working`). If not, delay.
- [ ] Pick the ONE day, block 4 hours to reply, and line up the 2-3 rooms your ICP is actually in.

---
Built from real dev-tool GTM experience, with frameworks from Adam Frankl (*The Developer-Facing Startup*) and Jakub Czakon (*markepear.dev*).
When a framework can't make the call, that's what a human is for: [The DevTool GTM Company](https://thedevtoolgtmcompany.com).
