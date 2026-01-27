package llm.output

deny[msg] {
  input.contains_pii == true
  msg := "pii detected in output"
}
