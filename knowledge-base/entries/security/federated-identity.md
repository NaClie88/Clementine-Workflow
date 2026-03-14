---
id: federated-identity
title: "Federated Identity (OAuth 2.0 / OIDC / SAML)"
domain: security
sub-domain: "architecture patterns"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Identity is managed by a dedicated identity provider (IdP). Applications delegate authentication to the IdP and receive signed assertions about the user's identity.

## Example

"Login with Google" using OIDC: a user authenticates with Google; Google issues a signed JWT ID token containing `sub`, `email`, and claims; the application verifies the token signature against Google's JWKS endpoint. The app never sees the user's Google password.

```
# OIDC Authorization Code + PKCE flow:

# 1. App generates:   code_verifier (random), code_challenge = SHA256(code_verifier)
# 2. Redirect to IdP: accounts.google.com/authorize
#                     ?response_type=code&client_id=...&code_challenge=...
# 3. User authenticates with Google (MFA, passkey, etc.)
# 4. IdP redirects:   app.example.com/callback?code=AUTH_CODE
# 5. App exchanges:   POST /token { code, code_verifier } → { id_token, access_token }
# 6. App verifies:    JWT signature against Google's JWKS; checks iss, aud, exp, nonce
# 7. Identity:        id_token.sub is the stable, persistent user identifier
```

## Strengths

- Centralises credential management — passwords and MFA are the IdP's problem
- Enables SSO — one login, many applications
- Eliminates per-app password storage — and the breaches that come with it

## Weaknesses

- The IdP is a single point of failure and a high-value attack target — IdP compromise = all applications compromised
- Token scope creep — applications often request more claims than they need
- OAuth 2.0 is an authorisation framework, not an authentication protocol — misuse leads to vulnerabilities

## Mitigation

Use PKCE for all OAuth flows (prevents auth code interception even without client secrets). Validate all JWT claims on every request (iss, aud, exp, nonce). Minimise token scopes. Implement token revocation and short expiry for sensitive resources.
