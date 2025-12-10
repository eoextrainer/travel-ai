# Git Workflow and Version Control Guide

Repository: `git@github.com:eoextrainer/travel-ai.git`

## Setup

- Ensure Git is installed.
- Initialize repo in the project folder.
- Add GitHub remote.

## Branching Strategy

- Main branch: `main` (protected; PRs required)
- Feature branches: `feature/<short-name>`
- Docs branches: `docs/<short-name>`
- Fix branches: `fix/<short-name>`

## Commit Conventions

- Use concise messages:
  - `docs: add workshop curriculum`
  - `feat: add prompt for travel agent`
  - `chore: update gitignore`
- Prefer small, focused commits.

## Pull Requests

- Open PRs from feature/docs branches into `main`.
- Include a summary of changes and checklist.
- Request review before merging.

## Release Tags (Optional)

- Tag versions like `v1.0.0`, `v1.1.0`.
- Keep a CHANGELOG if needed.

## Initial Commands

Run these from the project root:

```bash
git init
git remote add origin git@github.com:eoextrainer/travel-ai.git

git checkout -b docs/workshop
git add .
git commit -m "docs: scaffold workshop and prompt"
git push -u origin docs/workshop
```

## Updating Workflow

- Create a new branch for each change.
- Push branch; open PR; merge after review.

## Notes

- Ensure SSH keys are set up for GitHub.
- Protect `main` to require PR review.
