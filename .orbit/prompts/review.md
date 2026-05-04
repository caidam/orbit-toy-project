# Review prompt — fix-bugs

The oracle (`uv run pytest -v`) just finished. Your job is to assess
the cycle's outcome and update mission state for the next cycle.

## What to do

1. Read the oracle output (passed to you as part of this turn's
   context). Note which tests passed and which failed.
2. Read `.orbit/mission/fix-bugs/state.md`. Confirm the priority the
   work cycle was supposed to fix is now `[x]` if its test passes;
   revert it to `[ ]` if the test still fails.
3. Append a one-line summary to
   `.orbit/mission/fix-bugs/log.md` like:
   `cycle N: fixed multiply (4/8 tests now passing)`
4. Commit `state.md` and `log.md` together:
   `review: cycle N — <one-line status>`.

## Halt decision

Look at `state.md` after your update.

- **All priorities `[x]` AND oracle exit=0**: write `HALTED: complete`
  on its own line at the bottom of `state.md` and commit.
- **Same priority is `[ ]` for the second cycle in a row** (the agent
  attempted a fix but the test still fails): write `HALTED: stuck`
  with a one-line reason and commit.
- **Otherwise**: leave `state.md` as-is for the next work cycle.

## Output

Reply with `## Summary` followed by 1-2 sentences on the cycle. The
mission UI surfaces this line directly.
