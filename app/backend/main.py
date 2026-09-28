from fastapi import FastAPI

app = FastAPI(
    title="SOMARA Cloud API",
    description="Secure DevSecOps Platform API",
    version="1.0.0",
)


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