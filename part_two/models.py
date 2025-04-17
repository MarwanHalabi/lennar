from pydantic import BaseModel, Field, validator
from uuid import uuid4
from typing import Optional


# Truck Model
class Truck(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    length: float
    width: float
    height: float
    is_full: bool = False

    # Custom validator for positive values
    @validator("length", "width", "height")
    def check_positive_dimensions(cls, value):
        if value <= 0:
            raise ValueError("Dimensions must be greater than 0")
        return value

    def volume(self) -> float:
        return self.length * self.width * self.height


# Package Model
class Package(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    length: float
    width: float
    height: float
    truck_id: Optional[str] = None
    # Custom validator for positive values
    @validator("length", "width", "height")
    def check_positive_dimensions(cls, value):
        if value <= 0:
            raise ValueError("Dimensions must be greater than 0")
        return value

    def volume(self) -> float:
        return self.length * self.width * self.height
