from fastapi import FastAPI, Request, status
from api.v1.api import router as router_v1

app = FastAPI(title="Spotify_YouTube_API")

# v1 라우터 포함
app.include_router(router_v1, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)