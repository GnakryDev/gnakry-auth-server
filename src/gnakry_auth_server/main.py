import hashlib
from fastapi import FastAPI, HTTPException, Request, APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional
from .router.crud import router
import json
import requests
from datetime import datetime, timezone
import yaml


def get_app():
    app = FastAPI(title="Gnakry Auth-Server")
    return app


app = get_app()
security = HTTPBasic()
app.include_router(router)


@app.get("/auth/basic")
def user_auth(credentials: HTTPBasicCredentials = Depends(security)):
    valid_user = False
    with open("config/users_list.yml") as file:
        user_list = yaml.load(file, Loader=yaml.FullLoader)
    for user in user_list["user_list"]:
        if credentials.username == user["username"] and hashlib.sha512(credentials.password.encode('utf-8')).hexdigest().lower() == user["password"].lower():
            valid_user = True
            break
    if valid_user:
        return {"auth": "OK"}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
