# Work prompt — fix-bugs

You're working on `calc.py`, which has four seeded bugs. Your job is to
make `uv run pytest -v` pass without modifying `test_calc.py`. Tests
catch the bugs; let them guide you.

## What to do this cycle

1. Read `.orbit/mission/fix-bugs/state.md` for the priority list.
2. Pick the highest priority that's **not yet marked done** in
   `state.md`, fix only that bug in `calc.py`.
3. Confirm `uv run pytest -v` exits 0 for that test (and doesn't
   regress others).
4. `git add calc.py` and commit with a clear message:
   `fix: <what you fixed>`. Don't push — orbit's mission loop manages
   the branch.
5. Update `.orbit/mission/fix-bugs/state.md`: mark the priority you
   just fixed as `[x]` (done).

## Rails

- **Don't modify `test_calc.py`** — it's the oracle. If a test seems
  wrong, leave it; flag the disagreement in your commit message and
  pick a different priority.
- **Don't push to `main`.** Mission branch is created+managed by
  orbit; just commit on the current branch.
- **One bug per cycle.** Smaller commits = clearer review. The mission
  has time for 4+ cycles.

## When done

If `state.md` shows all priorities `[x]` after your fix, write
`HALTED: complete` on its own line at the bottom of `state.md`. The
mission loop will pick this up after the review cycle.
