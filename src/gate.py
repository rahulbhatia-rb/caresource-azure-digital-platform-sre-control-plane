REQUIRED={'azure': ['subscription_owner', 'vnet', 'private_connectivity', 'managed_identity', 'key_vault', 'encryption', 'diagnostics', 'backup_restore', 'policy', 'cost_tags'], 'terraform_enterprise': ['remote_state', 'locking', 'policy_as_code', 'module_versioning', 'secure_defaults', 'reviewed_plan', 'audit_trail', 'ownership_tags'], 'cicd': ['github_actions', 'test_gate', 'security_scan', 'immutable_artifact', 'release_metadata', 'environment_approval', 'blue_green', 'health_gate', 'rollback_trigger'], 'sre': ['sli', 'slo', 'error_budget', 'capacity_threshold', 'dependency_map', 'incident_owner', 'runbook', 'postmortem', 'leadership_metrics'], 'observability': ['dynatrace', 'splunk', 'metrics', 'logs', 'traces', 'deployment_markers', 'alert_owner', 'synthetic_checks'], 'streaming': ['schema_owner', 'consumer_lag', 'replay', 'dlq', 'retention', 'idempotency', 'backpressure', 'failure_isolation'], 'security_controls': ['least_privilege', 'secrets_isolation', 'encryption_in_transit', 'encryption_at_rest', 'audit_logging', 'change_traceability', 'environment_separation', 'vulnerability_management', 'access_review'], 'release_traceability': ['work_item', 'pull_request', 'commit', 'build', 'artifact_digest', 'deployment_target', 'approval', 'rollout_result'], 'kubernetes': ['requests_limits', 'autoscaling', 'pdb', 'topology_spread', 'workload_identity', 'network_policy', 'probes', 'graceful_shutdown']}

def evaluate(spec):
    findings=[]
    for section, fields in REQUIRED.items():
        values=spec.get(section,{})
        for field in fields:
            if not values.get(field): findings.append(f'{section}.{field} is required')
    return {'allowed': not findings, 'findings': findings}
