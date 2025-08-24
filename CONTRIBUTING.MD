
# Contributing to CrossLingual-Neural-Occupation-Classifier (CNOC)
-----
## **Thank you for considering a contribution.**
**This guide keeps changes consistent, reviewable, and safe.**

---
## Ways to contribute
- Report bugs and request features via GitHub Issues (search for duplicates first).
- Open a “Proposal” issue to discuss significant or breaking changes before coding.
- Improve documentation, tutorials, examples, and dataset preparation scripts.
- Contribute NCO-2015 mappings and evaluation datasets (with licenses/citations).
- Optimize models, retrieval, multilingual coverage, and performance.

## Quick start
1) Fork the repo and create a topic branch:
    - feat/<short-name>, fix/<short-name>, docs/<short-name>, chore/<short-name>
2) Follow code style:
    - Python, PEP 8; prefer type hints; keep functions small and documented.
    - Run linters/formatters and tests locally.
3) Update README/docs with rationale, usage, and examples as needed.
4) Commit using clear messages (Conventional Commits recommended).
5) Open a PR that links related issues and completes the checklist.

## Issues and proposals
- Bugs: include steps to reproduce, expected vs actual behavior, logs, and environment.
- Features: describe problem, proposed solution, alternatives, and impact.
- Proposals: for major changes (API, models, data formats), open a “Proposal” issue first to align on scope.

## Development workflow
- Environment: use a virtualenv; see README for setup. If available, install dev tools (e.g., pip install -e .[dev]).
- Style and quality: run formatter and linters (e.g., black, isort, ruff/flake8) and type checks if configured.
- Tests: add/adjust tests for your change; run the suite (e.g., pytest) before pushing.
- Docs: update docs/ and README to cover new behavior, config, and examples.
- Data:
  - Do not commit secrets, PII, or licensed/restricted datasets.
  - Provide small, synthetic, or publicly licensed samples and cite sources.
  - For NCO-2015 mappings, document provenance and decisions.
- Commits/PRs: keep them focused and reasonably small for easier review.

## Pull request checklist
- Scope is focused and described in the PR.
- Linked related issues (Fixes #… / Closes #…).
- Linting/formatting/tests pass locally and in CI.
- No secrets, PII, or restricted-licensed data committed.
- Backward compatible or includes clear migration notes.
- Docs/README updated and examples provided where useful.

## Review and merge
- A maintainer will review for scope, quality, tests, docs, and security.
- Changes may be requested; please respond or push updates.
- Squash-merge may be used to keep history clean.

## Security
Do not report vulnerabilities via public issues. Email the maintainers or follow [SECURITY.md](/SECURITY.md) if present. Provide a minimal, reproducible description and impact assessment.

## License
By contributing, you agree that your contributions are licensed under the Apache-2.0 license for this project.