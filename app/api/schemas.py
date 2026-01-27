from pydantic import BaseModel, Field

class InferenceRequest(BaseModel):
    model: str = Field(..., example="v1")
    prompt: str = Field(..., min_length=1, max_length=4096)
    max_tokens: int = Field(default=256, ge=1, le=2048)

class InferenceResponse(BaseModel):
    model: str
    output: str
    tokens_used: int
