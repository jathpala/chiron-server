"""
Copyright (C) 2024 Jath Palasubramaniam
Licenced under the terms of the AGPLv3
"""

import logging
import datetime

from pydantic import BaseModel, Field

from chiron_server.modules.demographics.types import Sex

logger = logging.getLogger(__name__)

class PatientDemographics(BaseModel):
    """
    Patient demographic details
    """

    mrn: str = Field(min_length=1)
    firstname: str
    middlenames: str | None
    lastname: str | None
    onlyname: bool
    dob: datetime.date
    sex: Sex
