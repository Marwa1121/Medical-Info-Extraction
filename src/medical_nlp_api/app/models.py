from pydantic import BaseModel, Field
from typing import List
from .schema import EntityType, MedicalCategory

class Entity(BaseModel):
    entity_value: str = Field(..., description="Actual name or value of the entity.")
    entity_type: EntityType = Field(..., description="Recognized entity type.")

class MedicalReportDetails(BaseModel):
    report_title: str = Field(..., min_length=5, max_length=300)
    report_keywords: List[str] = Field(..., min_items=1)
    report_summary: List[str] = Field(..., min_items=1, max_items=5)
    report_category: MedicalCategory
    report_entities: List[Entity] = Field(..., min_items=1, max_items=15)
