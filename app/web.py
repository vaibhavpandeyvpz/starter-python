from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.routers import index_router
from app.container import Container

app = FastAPI()

container = Container()

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
