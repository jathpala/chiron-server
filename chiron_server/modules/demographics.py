"""
Copyright 2024 Jath Palasubramaniam
Licenced under the AGPLv3
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/mrn/{mrn}")
def read_by_mrn(mrn: str):
    pass
