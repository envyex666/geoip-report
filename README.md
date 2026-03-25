Server is getting POST request and converts IP into client location data

How to works:

Server start
uvicorn server:app --host 0.0.0.0 --port 8081  

Client send POST request to server:port/report

Server converts IP into client location data

to get report do:
uvicorn server:app --host 0.0.0.0 --port 8081 | grep -E recieved

