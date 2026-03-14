---
id: gitops
title: "GitOps"
domain: methodology
sub-domain: "operational philosophy"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Use a Git repository as the single source of truth for infrastructure and application state. Automated reconciliation loops ensure the live system matches the declared state.

## Example

ArgoCD watches a Git repo for changes to Kubernetes manifests. When a PR merges, ArgoCD reconciles the cluster to match the repo state automatically — no manual `kubectl apply` in CI scripts.

## Strengths

- Audit trail for every infrastructure change — who changed what and why is in Git
- Rollback is a `git revert` — fast and low-risk
- The declared state is always human-readable

## Weaknesses

- Works best for Kubernetes and cloud-native infrastructure — retrofitting to legacy systems is difficult
- Secret management is awkward in a Git-centric model — secrets cannot live in the repo
- Requires Git discipline — force pushes to main can cause reconciliation chaos

## Mitigation

Use sealed secrets or an external secrets operator to keep secrets out of Git. Never store plaintext secrets in the GitOps repo. Protect the main branch with required reviews.
