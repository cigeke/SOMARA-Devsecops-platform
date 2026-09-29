from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI(
    title="SOMARA Cloud API",
    description="Secure DevSecOps Platform API",
    version="1.0.0",
)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
        response.headers["Cache-Control"] = "no-store"

        return response


app.add_middleware(SecurityHeadersMiddleware)


@app.get("/")
def root():
    return {
        "name": "SOMARA Cloud",
        "service": "DevSecOps Platform",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }