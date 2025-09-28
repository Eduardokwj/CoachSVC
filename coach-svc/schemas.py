from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class SetEntry(BaseModel):
    exercise_id: int
    sets: int
    reps: int
    load_kg: float
    rir: Optional[int] = None


class PlanRequest(BaseModel):
    athlete: dict | None = None
    session: List[SetEntry] = Field(default_factory=list)


class PlanItem(BaseModel):
    exercise_id: int
    sets: int
    reps: str
    load_kg: float


class PlanWeek(BaseModel):
    week: int
    target: List[PlanItem] | None = None
    deload: bool | None = None
    note: str | None = None


class OneRMRequest(BaseModel):
    load_kg: float
    reps: int
    method: Literal["epley", "brzycki"] = "epley"


class VolumeRequest(BaseModel):
    session: List[SetEntry]
