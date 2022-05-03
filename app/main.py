import uvicorn
from fastapi import FastAPI
from routers import health
from routers import predictServer
from starlette_prometheus import metrics, PrometheusMiddleware
app = FastAPI()
app.include_router(health.router)
app.include_router(predictServer.router)
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics)
import sys
@app.get("/")
def index():
    return { "message": "running"}

if __name__ == "__main__":
    sys.path.append(".")
    uvicorn.run("main:app", port=8000, reload=True)