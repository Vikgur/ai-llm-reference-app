from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="AI LLM Reference API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None,
)

app.include_router(router, prefix="/v1")
