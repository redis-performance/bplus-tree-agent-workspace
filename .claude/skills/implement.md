# Implementer prompt

Start in an isolated worktree at the frozen baseline. Implement only the chair's selected
hypothesis; retain the frozen referee. Write variants/<id>/implementation.md describing
identity/model, exact base, distinct implementation choices, risks, commands and results.
Save a git-applicable patch. Run correctness before timing; never benchmark known broken
code. Failed variants remain evidence. Do not choose the overall winner yourself.
