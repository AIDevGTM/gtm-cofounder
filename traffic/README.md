# Traffic log

`traffic-daily.csv` is a permanent, de-duplicated **daily** record of GitHub clones and views
for this repo, appended weekly by `.github/workflows/traffic-snapshot.yml`.

GitHub's own traffic API only retains the last **14 days**, so this file preserves the history
GitHub otherwise throws away.

**Columns:** `date, clones, clones_unique, views, views_unique`

- `clones` ≈ installs (the skills CLI, the Claude Code plugin, and manual `git clone` all clone the repo)
- `clones_unique` ≈ people
- **Cumulative installs to date = the sum of the `clones` column.**

## One-time setup (required)
The traffic API needs a token with push access; the default `GITHUB_TOKEN` **cannot** read traffic.

1. Create a **classic** Personal Access Token with the `repo` scope: <https://github.com/settings/tokens>
2. Add it as an Actions secret named **`TRAFFIC_TOKEN`**:
   repo **Settings > Secrets and variables > Actions > New repository secret**.
3. Run it once to confirm: **Actions tab > Traffic snapshot > Run workflow**.

After that it runs every Monday and the CSV grows on its own.
