# Teapot app
To run code
1) Create virtual environment: python3 -m venv venv
2) Activate venv: 
   Linux, Mac OS: source venv/bin/activate
   Windows: venv/Scripts/activate
3) Install requirements: pip install -r requirements.txt
4) Start server: uvicorn main:app --host 127.0.0.1 --port 8000
5) Go to documentation: open in browser 127.0.0.1:8000/docs

Realized on FastAPI
Realized documentation, logging, .env

To update: 
    add async logger
    create websocket endpoint to listen logger
