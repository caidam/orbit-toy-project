# orbit toy project

A small Python project with 4 seeded bugs and tests that catch them.
Used as a target for [orbit](https://github.com/anthropics/orbit-workbench)
mission and sandbox testing — small enough to clone fast, real enough
that fixing the bugs exercises the full mission loop (oracle, cycles,
review, watchdog).

## What the bugs are

```python
def multiply(a, b):     # BUG: off by one
    return a * b + 1

def divide(a, b):       # BUG: no zero division handling
    return a / b

def average(numbers):   # BUG: empty list crashes
    return total / len(numbers)

def clamp(value, low, high):
    if value > high:    # BUG: returns high+1 instead of high
        return high + 1
```

`uv run pytest -v` catches all four.

## Use as an orbit mission target

This repo is meant to be cloned from a public/private git host and
used as a `git-clone` source in `orbit.yml`. The `orbit.yml` shipped
here defaults to `method: copy` so it also works as a local target
(useful when you've cloned this repo to your own laptop and want to
run a quick sandbox).

For a remote-clone mission, swap to:

```yaml
sandbox:
  source:
    method: git-clone
    repo: https://github.com/<you>/orbit-toy-project.git
    branch: main
    protected_branches:
      - main
```

Then in any orbit-managed project elsewhere:

```bash
orbit sandbox mission fix-bugs --stop-after 02:00
```

(The mission loop will git-clone this repo into a sandbox, run
`uv run pytest`, and let the agent fix bugs in cycles.)

## Local quick check

```bash
uv sync
uv run pytest -v
```

Expected: 4 failures (`multiply`, `divide_by_zero`, `average_empty`,
`clamp_high`).

## Files

- `calc.py` — buggy calculator
- `test_calc.py` — pytest tests that catch the bugs
- `orbit.yml` — orbit project config (oracle, runtime, source method)
- `pyproject.toml` + `uv.lock` — uv-managed Python deps

The `.claude/` and `.orbit/` directories appear automatically when
orbit configures hooks or registers a project — they're gitignored by
default.
