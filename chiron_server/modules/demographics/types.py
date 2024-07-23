"""
Copyright (C) 2024 Jath Palasubramaniam
Licenced under the terms of the AGPLv3
"""

import logging

from enum import Enum

logger = logging.getLogger(__name__)

class Sex(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
