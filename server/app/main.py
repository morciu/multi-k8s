from typing import Union

from fastapi import FastAPI, Depends
from fastapi.openapi import docs
from fastapi.openapi import utils

from sqlalchemy.orm import Session

from . import db_config
from . import models

try:
    models.Base.metadata.create_all(bind=db_config.engine)
    print("created stuff")
except Exception as err:
    print(f"\n{err}\n")

app = FastAPI()

# Set up Swagger
@app.get("/docs", include_in_schema=False, name="docs")
async def swagger():
    return docs.get_swagger_ui_html(
        openapi_url="/openapi.json", title="docs"
    )

@app.get("/openapi.json", include_in_schema=False)
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
async def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    print(user)
    db_user = models.User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    result = db.query(models.User).all()
    return result



@app.get("/")
def read_root():
    return {"message": "El Root"}

