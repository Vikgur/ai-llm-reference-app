{{- define "ai-llm-reference-app.name" -}}
ai-llm-reference-app
{{- end }}

{{- define "ai-llm-reference-app.fullname" -}}
{{ include "ai-llm-reference-app.name" . }}
{{- end }}
