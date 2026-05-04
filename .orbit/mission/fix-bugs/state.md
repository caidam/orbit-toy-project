## Summary

Fix the four bugs seeded in `calc.py`. The tests in `test_calc.py` catch
them when the implementation is correct. Don't change `test_calc.py` —
that's the oracle.

## Priorities

- [x] **P1** — Fix `multiply` (off-by-one: returns `a * b + 1`)
- [x] **P2** — Fix `divide` (no zero-division handling — should raise
  `ValueError` on `b == 0`)
- [ ] **P3** — Fix `average` (empty list crashes — should raise
  `ValueError` on empty input)
- [ ] **P4** — Fix `clamp` (returns `high + 1` instead of `high` when
  `value > high`)

## Drift rails

- Do NOT modify `test_calc.py` — it's the oracle
- Do NOT modify `pyproject.toml` or `uv.lock`
- Do NOT push to `main`

## How "done" looks

`uv run pytest -v` exits 0; all 8 tests pass.
