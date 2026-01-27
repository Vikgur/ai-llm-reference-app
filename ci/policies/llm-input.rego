package llm.input

deny[msg] {
  input.prompt_length > 8192
  msg := "prompt too large"
}
