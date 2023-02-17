from pydantic import BaseSettings


class Settings(BaseSettings):
    max_temperature: float
    max_water: float
    heating_per_second: float

    class Config:
        env_file = ".env"