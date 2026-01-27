#!/usr/bin/env sh
set -euo pipefail

kubectl get ns ai-llm
kubectl get pods -n ai-llm
kubectl describe resourcequota -n ai-llm
kubectl auth can-i create pods --as=system:serviceaccount:ai-llm:default
