# CareSource Azure Digital Platform SRE Control Plane

Independent proof-of-work inspired by CareSource's public Architect III - Cloud, DevOps, and SRE role.

This project models an Azure-first enterprise digital platform operating in a regulated healthcare environment, with Terraform Enterprise, GitHub Actions, blue/green delivery, automated rollback, SRE practices, Dynatrace/Splunk-style observability, Kubernetes, event streaming, and enterprise governance.

> Based only on the public job description. It does not represent CareSource's private architecture.

## Core problem

The role must connect enterprise architecture standards with product delivery through reusable cloud templates, secure-by-default infrastructure, release automation, automated rollback, SRE alignment, actionable observability, capacity planning, regulated controls, and cross-team governance.

## Reference architecture

```text
Digital Product Teams
        |
        v
   GitHub / VCS
        |
        +--> CI / tests
        +--> security scans
        +--> Terraform plan
        +--> release metadata
        |
        v
 Terraform Enterprise
        |
        +--> policy checks
        +--> remote state
        +--> approvals
        |
        v
 Azure Platform
        |
        +--> VNets / Private Endpoints
        +--> AKS / App Services / VMs
        +--> Storage / Databases
        +--> Key Vault / Managed Identity
        +--> Front Door / App Gateway
        |
        v
 Blue / Green Runtime
        |
        +--> health gate
        +--> progressive traffic
        +--> rollback automation
        |
        v
 Reliability & Operations
        |
        +--> Dynatrace
        +--> Splunk
        +--> SLOs
        +--> incidents
        +--> capacity
        +--> leadership metrics
```

## Azure platform contract

A hardened Azure workload should define subscription/resource-group ownership, VNet segmentation, private connectivity, managed identities, Key Vault, encryption, diagnostic settings, backup/restore, policy/governance, and cost ownership.

## Terraform Enterprise

Reusable templates should encode remote state, locking, policy-as-code, module versioning, secure defaults, auditability, ownership tags, cost tags, and review workflow.

## Blue / green delivery

A deployment should include an immutable artifact, environment parity, health validation, traffic-shift plan, automated rollback trigger, database compatibility check, release record, and observation window.

## Automated rollback

Rollback signals may include error-rate breach, latency breach, failed synthetic test, dependency regression, failed business KPI, or crash-loop/saturation events.

## SRE operating model

For each critical Digital product define SLI, SLO, error budget, capacity threshold, dependency map, incident owner, runbook, escalation path, and postmortem process.

## Observability

Dynatrace/APM: service latency, error rate, dependency graph, traces, resource saturation, release markers.

Splunk/logs: application logs, platform logs, security events, audit events, correlation IDs, operational search patterns.

## Event / message streaming

Define schema ownership, consumer lag, replay, DLQ, retention, idempotency, backpressure, and failure isolation.

## Regulated healthcare controls

Require least privilege, secrets isolation, encryption in transit/at rest, audit logging, change traceability, environment separation, vulnerability management, backup/restore evidence, access review, and retention ownership.

## Agile-to-release integration

Generate release evidence from work items, PRs, commits, build metadata, artifact digest, deployment target, approvals, and rollout result.

## Leadership metrics

Report SLO attainment, error-budget burn, deployment frequency, change failure rate, MTTR, rollback frequency, capacity headroom, recurring incident classes, and cloud spend by product.

## 30 / 60 / 90

### 0-30
- map Digital platform dependencies
- baseline Terraform Enterprise and delivery standards
- identify release / rollback gaps
- map SLOs and incident ownership
- review regulated controls

### 31-60
- standardize Azure workload templates
- implement blue/green reference workflow
- add automated rollback gates
- unify deployment markers with Dynatrace / Splunk
- establish leadership reliability metrics

### 61-90
- improve self-service platform patterns
- automate release documentation
- reduce recurring incident classes
- improve capacity planning
- exercise DR / restore paths
- mentor teams through reusable architecture examples

## Run locally

```bash
python -m unittest -v tests.test_gate
python src/cli.py examples/production.json
python src/cli.py examples/unsafe.json
```
