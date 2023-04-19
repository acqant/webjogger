import logging

from importlib import resources
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from libs.simple_lib import HelperLib

app = FastAPI(docs_url=None, title="Title for Fast API")

with resources.path("sample_stuff", "statics") as path_data:
    statistics_folder = str(path_data)

app.mount("/statics", StaticFiles(directory=statistics_folder), name="statics")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.get("/")
async def root():
    """
    Redirect / to /docs
    """
    logger.debug("IN ROOT")
    return {'message': 'app message'}


@app.get("/simple_lib")
async def simple_lib():
    our_int = HelperLib.get_some_int()
    return {'out_int': our_int}

items = {}


@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]