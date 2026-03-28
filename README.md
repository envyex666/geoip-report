# geoip reports
### description
App for making geoip reports from requests by clients.

## quick start
prepare python virtual enviroments
```bash
python3 -m venv venv
source venv/bin/activate
install requirements
pip install -r requirements.txt
```
start your server
```bash
SECRET_TOKEN="123" uvicorn server:app --host 127.0.0.1 --port 8081 --app-dir src/
```
## request example
```bash
curl -X POST -H "AUTH_TOKEN: 123" "http://127.0.0.1:8081/report"
```
