# Push toy-project as a standalone GitHub repo

Goal: get `toy-project/` onto GitHub as `<you>/orbit-toy-project` so it
can be a `git-clone` source for orbit missions. Keep this directory in
`orbit-workbench/` too — they stay in sync if you choose; nothing
forces them to.

## One-time push

```bash
cd toy-project

# 1. Stand up a fresh git repo (no history from orbit-workbench).
git init -b main
git add .
git commit -m "Initial commit — orbit-toy-project"

# 2. Create the empty repo on GitHub via the gh CLI (or do it in the UI
#    and skip the gh step). Public for the first smoke; you can flip to
#    private later.
gh repo create orbit-toy-project --public --source=. --remote=origin --push
#   ── alternatively, manually:
#   create at https://github.com/new (don't add a README/license)
#   git remote add origin git@github.com:<you>/orbit-toy-project.git
#   git push -u origin main
```

After that, the URL you'll plug into `orbit.yml` is:
- HTTPS: `https://github.com/<you>/orbit-toy-project.git`
- SSH:   `git@github.com:<you>/orbit-toy-project.git`

## After the test, switching to private

```bash
gh repo edit <you>/orbit-toy-project --visibility private --accept-visibility-change-consequences
# Then: orbit secrets set GIT_TOKEN <a fresh PAT scoped to repo:read>
# Subsequent missions exercise the GIT_TOKEN flow.
```

## You don't need this file in the standalone repo

`PUSH_TO_GITHUB.md` only matters for setting up the standalone repo
from the monorepo. After the first push, `git rm PUSH_TO_GITHUB.md`
to keep the toy-project repo focused.
