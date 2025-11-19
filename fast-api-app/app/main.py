from fastapi import FastAPI

from app.routes import router
from app.seed import seed_if_needed

app = FastAPI(title="Glossary REST API")

app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await seed_if_needed()