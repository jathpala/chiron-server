"""
Copyright 2024 Jath Palasubramaniam
Licenced under the AGPLv3
"""

from functools import lru_cache

from .config import Settings

@lru_cache
def get_settings():
    return Settings()