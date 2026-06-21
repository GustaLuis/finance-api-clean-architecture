from contextlib import asynccontextmanager

from fastapi import FastAPI

from infrastructure.database.models import Base
from infrastructure.database.session import engine
from infrastructure.web.routers import transaction_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Finance API", lifespan=lifespan)
app.include_router(transaction_router.router)


@app.get("/")
async def root():
    return {"message": "Finance API rodando 🚀"}
