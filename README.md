# Teapot app
To run code
1) Create virtual environment: python3 -m venv venv
2) Activate venv: 
   Linux, Mac OS: source venv/bin/activate
   Windows: venv/Scripts/activate
3) Install requirements: pip install -r requirements.txt
4) Start server: uvicorn main:app --host 127.0.0.1 --port 8000
5) Go to documentation: open in browser 127.0.0.1:8000/docs

Additionally realized:
1) on FastAPI web framework
2) documentation
3) logging
4) .env


To update: 
1) add async logger
2) create websocket endpoint to listen logger
