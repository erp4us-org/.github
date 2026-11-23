# erp4us organization resources

`profile/README.md` is the organization landing page. The root policies and `.github/` templates are defaults for repositories without local equivalents; repository-specific guidance takes precedence. Edit Markdown in a branch, preview it on GitHub, and submit a signed-off PR. No build tools required.

Run `python3 scripts/check.py` from a clone to check issue-template metadata and local policy links. GitHub runs the same check on pushes and pull requests.

[Monthly dependency review and critical security fixes](docs/dependency-maintenance.md) describes the organization-wide process and repository gates. A monthly workflow opens the tracking issue without changing dependencies or merging code.
