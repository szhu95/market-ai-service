import openai

from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import prompts, socials

import config

app = FastAPI()
app.include_router(prompts.router)
app.include_router(socials.router)


origins = [
    "http://localhost:3000",
]

# CORS for front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global HTTP expection handler
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# Dependency injection for settings
@lru_cache()
def get_settings():
    return config.Settings()

# printing app name
@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    print(settings.app_name)
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}