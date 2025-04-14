from typing import Literal

EntityType = Literal[
    "person-male", "person-female", "location", "organization", "event", "time",
    "quantity", "money", "product", "law", "disease", "treatment", "medication",
    "procedure", "symptom", "body_part", "medical_condition", "diagnosis",
    "clinical_measurement", "lab_test", "artifact", "age", "date", "not_specified"
]

MedicalCategory = Literal[
    "health", "medical", "pharmaceutical", "clinical_trial", "not_specified"
]
