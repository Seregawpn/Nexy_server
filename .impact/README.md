# Change impact process

The Nexy Server principles require an explicit change impact file for any
modification that exceeds the SIMPLE gate (more than 60 LOC, multiple files,
new dependencies, or cross-axis work). Copy
`change_impact_template.yaml` to `.impact/change_impact.yaml` inside your
feature branch and update every field before requesting review.

Failing to provide a populated change impact file blocks the "Impact gate"
checkbox in `Docs/SERVER_DEVELOPMENT_RULES.md`. The fail-fast CI workflow
asserts that the file exists when the diff touches multiple server modules or
Docs canon files.
