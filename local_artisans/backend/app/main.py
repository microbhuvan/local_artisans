from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import analyze


def create_app() -> FastAPI:
    app = FastAPI(title="Local Artisans API", version="0.1.0")

    # CORS - allow frontend origin via env or default to localhost ports
    from .config import settings

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    app.include_router(analyze.router, prefix="/api")
    return app


app = create_app()


