from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi import docs
from fastapi.openapi import utils

from sqlalchemy.orm import Session

from . import db_config
from . import models

app = FastAPI()

# Set up Swagger
@app.get("/docs")
async def swagger():
    return docs.get_swagger_ui_html(
        openapi_url="/openapi.json", title="docs"
    )

@app.get("/openapi.json")
def openapi():
    return utils.get_openapi(
        title="FastAPI"
    )


def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}