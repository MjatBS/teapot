from pydantic import BaseModel, confloat

from config import Settings


settings = Settings()


class Teapot(BaseModel):
    status: str = "off"
    temperature: confloat(ge=0, le=settings.max_temperature) = 0
    water: confloat(ge=0, le=settings.max_water) = 0


class TurnOnParams(BaseModel):
    water: confloat(ge=0, le=settings.max_water)