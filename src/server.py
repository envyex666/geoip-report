from typing import Annotated
import geoip2.database
import uvicorn
from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

secret_token = os.environ.get('SECRET_TOKEN')
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    if token != secret_token:
      raise(HTTPException(status_code=401))
    else:
      return token

@app.post("/report")
async def get_ip(request: Request, token: Annotated[str, Depends(oauth2_scheme)]):
    await read_items(token)
    client_host = request.client.host

    with geoip2.database.Reader("db/GeoLite2-Country.mmdb") as reader:
        response = reader.country(client_host)
        print(
            "report_recieved ",
            "IP:",
            client_host,
            "Country_Code:",
            response.country.iso_code,
            "Country_name:",
            response.country.name
        )

    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
