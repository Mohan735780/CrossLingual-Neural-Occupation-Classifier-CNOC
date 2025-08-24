# Security Policy

This document describes how to report and handle security issues for CrossLingual-Neural-Occupation-Classifier (CNOC), and how to use and deploy it securely.

## Supported versions
- Main branch and latest tagged release: supported with security fixes.
- Previous minor release: best-effort for 90 days after a new minor release.
- Pre-release/nightly builds: not supported.

## Reporting a vulnerability
- Do not open a public issue for security reports.
- Preferred: open a private GitHub Security Advisory for this repo (Security > Advisories > New draft).
- Alternative: email security@yourdomain.example.
- Include: affected commit or version, environment, reproduction steps, expected vs. actual behavior, impact assessment, logs/PoC, and proposed mitigation if known.
- Service-level targets: acknowledge within 3 business days, triage within 7 business days, and remediate or publish coordinated guidance within 90 days. Timelines may accelerate for actively exploited issues.

If you need encryption, request or provide a public key in your initial email.

## Scope
#### In scope
- Code, scripts, configs, model weights, and example notebooks in this repository.
- Release artifacts and container images published by this project.
- CI/CD workflows owned by this project.

#### Out of scope
- Third-party services, datasets, or dependencies (report upstream).
- Findings requiring non-default, debug-only, or already-privileged access.
- Social engineering, physical attacks, or volumetric DoS.

## Data and model security
- Do not commit secrets or credentials. Use environment variables or a secret manager.
- Never include PII or regulated data in issues, commits, datasets, or model artifacts.
- Validate that training and evaluation data complies with licenses and data protection laws; document sources and consent status.
- Avoid loading untrusted serialized objects (e.g., pickle). Prefer safe formats and verify checksums.
- Run the model in isolated environments with least privilege and restricted network egress.

## Dependency and supply chain
- Pin dependencies and use lock files (requirements.txt/poetry.lock).
- Enable automated scans (Dependabot, pip-audit, Safety) and update promptly.
- Verify artifact integrity (checksums/signatures) and build from clean CI.
- Consider signing releases (e.g., Sigstore) and verifying provenance.

## Secure development and runtime
- Use linters and SAST (ruff, bandit) and run tests in CI.
- Sanitize and validate all user-controlled inputs for demos/APIs.
- Do not expose management endpoints to the public internet.
- Log security-relevant events and monitor for drift and anomalous inputs.

## Responsible and safe use
- This classifier may reflect biases in training data and is not a drop-in replacement for human judgment.
- Do not use outputs for high-stakes decisions without domain validation and human review.
- Document limitations, known failure modes, and intended use cases in deployments.

## Incident response
- Rotate credentials, revoke tokens, and invalidate compromised artifacts.
- File a private advisory or email the security contact with indicators of compromise.
- We will coordinate fixes, advisories, and CVEs where applicable.

## Security updates
- Security-relevant changes are documented in release notes and [CHANGELOG](/CHANGELOG.md).
- Users should track releases and update promptly.

---

## Contact:
**Ashwin R**
📩 [mail.to.ashwinr.tn@gmail.com](mailto:mail.to.ashwinr.tn@gmail.com) | [LinkedIn](https://www.linkedin.com/in/ashwin-r11/) | [GitHub](https://github.com/Ashwin-r11)

