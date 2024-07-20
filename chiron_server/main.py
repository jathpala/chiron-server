"""
Copyright 2024 Jath Palasubramaniam
Licenced under the AGPLv3
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    Return basic service information
    """

    return {"service": "chiron-server"}
