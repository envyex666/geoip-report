import os
from dataclasses import dataclass
from typing import Annotated, Optional

import geoip2.database
import geoip2.errors
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()


@dataclass
class LogReport:
    ip: str
    country_code: Optional[str]


secret_token = os.environ.get("SECRET_TOKEN")


@app.middleware("http")
async def check_token(request: Request, call_next):
    token = request.headers.get("AUTH_TOKEN")
    if token != secret_token:
        return JSONResponse(content={"error": "Unauthorized"}, status_code=401)
    return await call_next(request)


@app.on_event("startup")
async def startup_event():
    if not secret_token or secret_token.isspace():
        raise ValueError(f"SECRET_TOKEN env must be set and be not empty")


@app.post("/report")
async def get_ip(request: Request):
    try:
        if request.client is None:
            return JSONResponse(
                content={"error": "Cannot determine client IP"},
                status_code=400,
            )
        client_host = request.client.host
        with geoip2.database.Reader("db/GeoLite2-Country.mmdb") as reader:
            response = reader.country(client_host)
        print(LogReport(ip=client_host, country_code=response.country.iso_code))
        return {"status": "OK"}

    except geoip2.errors.AddressNotFoundError:
        return JSONResponse(content={"error": "Get your ass there"}, status_code=400)
    except Exception as e:
        return JSONResponse(
            content={"error": f"unknown error, {str(e)}"}, status_code=503
        )
