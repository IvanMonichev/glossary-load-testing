from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Glossary REST API")

app.include_router(router)

