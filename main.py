from fastapi import FastAPI
from asyncio import sleep
import logging

from models import Teapot, TurnOnParams
from config import Settings
from exceptions import HeatingInterrupt


logging.basicConfig(filename="log.txt", level=logging.INFO)

app = FastAPI()
settings = Settings()

teapot = Teapot()


async def heat_teapot(teapot):
    temperature = 0
    while temperature < settings.max_temperature:
        teapot.temperature = temperature
        await sleep(1)
        if teapot.status == "off":
            raise HeatingInterrupt
        temperature += settings.heating_per_second
        logging.info(temperature)
    teapot.temperature = settings.max_temperature


@app.post("/turn-on/")
async def turn_on(params: TurnOnParams) -> Teapot:
    logging.info("Turn on")
    teapot.status = "on"
    teapot.water = params.water

    try:
        await heat_teapot(teapot)
    except HeatingInterrupt:
        return teapot

    teapot.status = "off"
    logging.info("Boiled")
    return teapot


@app.post("/turn-off/")
async def turn_off() -> Teapot:
    logging.info("Turn off")
    teapot.status = "off"
    return teapot


@app.get("/status/")
async def status() -> Teapot:
    return teapot


# place for socket

