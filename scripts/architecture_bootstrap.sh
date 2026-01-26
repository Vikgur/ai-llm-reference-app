#!/usr/bin/env bash
set -euo pipefail

# --- directories ---
dirs=(
app/api
app/llm/{tokenizer,embeddings,transformer,decoding,postprocess}
app/config
app/tests

models/v1
models/registry

docker/app

helm/charts/ai-llm-reference-app/templates
helm/values

k8s/{base,security,manifests}

ci/{entrypoints,policies,artifacts}

security/{threat-model,sbom,attestations,runtime}

observability/{metrics,logs,traces,dashboards}

scripts
docs
)

mkdir -p "${dirs[@]}"

# --- files ---
files=(
README.md
LICENSE
SECURITY.md
CODEOWNERS
.gitignore
.editorconfig
.env.example

app/README.md
app/api/{main.py,routes.py,schemas.py,deps.py}
app/llm/tokenizer/{vocab.json,tokenizer.py,README.md}
app/llm/embeddings/{embedding.py,weights.bin}
app/llm/transformer/{attention.py,ffw.py,decoder.py,model.py}
app/llm/decoding/{sampler.py,decoder.py,guards.py}
app/llm/postprocess/{filters.py,redaction.py,policy.py}
app/llm/version.py
app/config/{runtime.yaml,limits.yaml,logging.yaml}

models/v1/{weights.bin,checksum.sha256,model-card.md}

docker/app/{Dockerfile,entrypoint.sh}
docker/README.md

helm/charts/ai-llm-reference-app/Chart.yaml
helm/charts/ai-llm-reference-app/templates/{deployment.yaml,service.yaml,hpa.yaml,networkpolicy.yaml,podsecurity.yaml,_helpers.tpl}
helm/charts/ai-llm-reference-app/values.yaml
helm/values/{dev.yaml,stage.yaml,prod.yaml}

k8s/base/{namespace.yaml,resourcequota.yaml,limitrange.yaml}
k8s/security/{psa.yaml,seccomp.yaml,apparmor.yaml}

ci/README.md
ci/entrypoints/{build.yaml,test.yaml,release.yaml}
ci/policies/{llm-input.rego,llm-output.rego,model-integrity.rego}

security/threat-model/threat-model.md
security/runtime/{seccomp.json,readonly-fs.yaml}
security/README.md

observability/metrics/prometheus.yaml
observability/logs/fluent-bit.yaml
observability/traces/otel.yaml

scripts/{local-run.sh,kind-up.sh,verify.sh}

docs/{architecture.md,llm-internals.md,llm-security.md,supply-chain.md,deployment.md,repository-structure.md}
)

touch "${files[@]}"

# --- gitkeep ---
gitkeep_dirs=(
app/tests
models/registry
ci/artifacts
security/sbom
security/attestations
observability/dashboards
k8s/manifests
)

for d in "${gitkeep_dirs[@]}"; do
  touch "$d/.gitkeep"
done

echo "LLM reference architecture bootstrap completed."
