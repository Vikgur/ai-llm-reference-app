package llm.model

deny[msg] {
  not input.model.checksum_valid
  msg := "model integrity check failed"
}
