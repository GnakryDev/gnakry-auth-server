import hashlib
from fastapi import FastAPI, HTTPException, Request, APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional
from .router.crud import router
import json
import requests
from datetime import datetime, timezone
import yaml
import logging
# from IPQualityScore.DBReader import DBReader

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_app():
    app = FastAPI(title="Gnakry Auth-Server")
    return app


app = get_app()
security = HTTPBasic()
app.include_router(router)


@app.get("/auth/basic")
def user_auth(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    valid_user = False
    with open("config/users_list.yml") as file:
        user_list = yaml.load(file, Loader=yaml.FullLoader)
    for user in user_list["user_list"]:
        if credentials.username == user["username"] and hashlib.sha512(credentials.password.encode('utf-8')).hexdigest().lower() == user["password"].lower():
            valid_user = True
            break
    if valid_user:
        return {"client_host": client_host, "auth": "OK"}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


def ipValidator(request: Request):
    client_host = request.client.host
    print("################################################## ")
    print("################################################## ")
    # u = DBReader(
    #     "IPQualityScore-IP-Reputation-Database-IPv4.ipqs").Fetch(request.headers.get(
    #         "x-forwarded-for"))
    # print("IsVPN: " + u.IsVPN())
    # print("IsProxy: " + u.IsProxy())
    # print("ActiveVPN: " + u.ActiveVPN())
    # print("Country: " + u.Country())
    # print("City: " + u.City())
    # print("ISP: " + u.ISP())
    # print("Organization: " + u.Organization())
    # print("IsCrawler: " + u.IsCrawler())
    print(" ################################################## ")
    print("################################################## ")
    print({"client_host": client_host, "auth": "OK"})
    print("################################################## ")
    print("################################################## ")
    params = ['query', 'status', 'country',
              'countryCode', 'city', 'timezone', 'mobile']
    resp = requests.get('http://ip-api.com/json/' + request.headers.get(
        "x-forwarded-for"), params={'fields': ','.join(params)})
    # read response as JSON (converts to Python dict)
    info = resp.json()
    # display the response
    print(info)
    print("################################################## ")
    print("################################################## ")
    print(request.headers)
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    return True
