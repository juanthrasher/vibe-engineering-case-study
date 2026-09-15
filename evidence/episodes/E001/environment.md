# E001 — Execution Environment

## Canonical execution and verification environment
- Runner: GitHub Actions `ubuntu-latest`
- Python: 3.14.7
- Django: 5.2.17
- Database: SQLite
- Dependency file: `requirements.txt`

## Auxiliary authoring environment
The ChatGPT sandbox available during preparation reports Python 3.13.5 and is not the canonical E001 runtime. It may be used to prepare files, but claims about execution must come from the canonical environment above or another explicitly recorded P2 environment.

## Network and secrets
- No production credentials.
- No external service required by the application.
- No real personal data.
- GitHub Actions may access package indexes only to install declared dependencies.

## Status
Environment frozen before the first functional implementation change.
