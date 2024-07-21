"""
Copyright 2024 Jath Palasubramaniam
Licenced under the AGPLv3
"""

from typing import Annotated

from fastapi import FastAPI, Depends

from .config import Settings
from .dependencies import get_settings

app = FastAPI()

@app.get("/")
async def root(settings: Annotated[Settings, Depends(get_settings)]):
    """
    Return basic service information
    """

    return {
        "service": "chiron-server",
        "version": "1.0",
        "name": settings.server_name
    }
