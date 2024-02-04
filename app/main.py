
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.groups import api as groups


def create_app():
    app = FastAPI()
    app.mount("/images",StaticFiles(directory="static/images"))
    app.include_router(groups.router)

    return app

app = create_app()    