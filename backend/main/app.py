from fastapi import FastAPI

app = FastAPI(
    title="AI Mock Interview API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Mock Interview API is running"
    }


@app.get("/api/health")
def health():
    return {
        "status": "ok"
    }