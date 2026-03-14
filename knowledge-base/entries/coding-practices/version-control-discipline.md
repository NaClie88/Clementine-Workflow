---
id: version-control-discipline
title: "Version Control Discipline"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: [all]
complexity: medium
maturity: established
theorist: Linus Torvalds
year: 2005
related: [trunk-based-development, gitops, code-review]
tags: [git, commit-messages, branching, history, atomic-commits]
---

## Definition

Commit messages explain *why*, not *what*. A session that ends without a push is an incomplete session.

## Example

Conventional commit: `feat(auth): add OAuth 2.0 PKCE flow for mobile clients` — tooling auto-generates changelogs, determines MAJOR/MINOR/PATCH bump, and links to the related issue.

## Strengths

- Auditable history — `git blame` and `git bisect` work
- Conventional commits enable automated release notes
- Atomic commits make revert tractable

## Weaknesses

- Commit discipline requires tooling (commitlint) or culture — it degrades under pressure
- Large uncommitted working trees are common when deadlines are close
- Merge commits vs. rebased histories create ongoing team-level decisions

## Mitigation

Use commitlint in pre-commit hooks. Make commit message quality part of PR review. Enforce "no commit = not done" as a team norm.
