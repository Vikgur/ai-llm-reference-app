from fastapi import APIRouter, Depends
from .schemas import InferenceRequest, InferenceResponse
from .deps import rate_limit, auth_guard

router = APIRouter()

@router.post("/infer", response_model=InferenceResponse, dependencies=[Depends(rate_limit), Depends(auth_guard)])
def infer(req: InferenceRequest) -> InferenceResponse:
    return InferenceResponse(
        model=req.model,
        output=f"echo: {req.prompt}",
        tokens_used=len(req.prompt.split()),
    )
