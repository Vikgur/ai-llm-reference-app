#!/usr/bin/env sh
set -euo pipefail

kind create cluster --name ai-llm

kubectl create namespace ai-llm || true
kubectl apply -f k8s/base/
kubectl apply -f k8s/security/
