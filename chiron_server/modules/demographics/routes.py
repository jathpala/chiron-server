"""
Copyright 2024 Jath Palasubramaniam
Licenced under the AGPLv3
"""

from fastapi import APIRouter

from chiron_server.modules.demographics.schemas import PatientDemographics

router = APIRouter()

@router.get("/{mrn}")
def read_by_mrn(mrn: str):
    pass

@router.post("/{mrn}")
def create(patient: PatientDemographics):
    pass
