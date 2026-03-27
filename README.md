# GEOIP REPORTS
## App for making geoip reports from requests by clients

## QUICK START

### add your token in .env
```bash
echo "SECRET_TOKEN=secret_example" > .env
```
### make python virtual enviroments
```bash
python3 -m venv venv
```
### activate your venv
```bash
source venv/bin/activate
```
### install requirements
```bash
pip install -r requirements/requirements.txt
```
### go to src dir and start your server
```bash
cd src && uvicorn server:app --host 0.0.0.0 --port 8081
```
## Request example
```bash
curl -X POST "http://SERVER_IP:SERVER_PORT/report"   -H "Authorization: YOUR_TOKEN"
```
