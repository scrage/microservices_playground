### Setup
At project source folder:
```
# create a virtual environment
python -m venv venv

# install dependencies
pip install -r requirements.txt
```

### Usage
Open up a terminal in the project folder and run:
```
uvicorn main:app --reload
```
...where `main` refers to the `main.py` file and `app` refers to the `FastAPI` instance, and `--reload` will run it in development mode, so it will reload the server any time any changes are made and saved.

### Sample
```
> uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['***REDACTED***\\llm_rest_api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [43128] using StatReload
INFO:     Started server process [33976]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:63575 - "POST /generate?prompt=%22hello%20there%22 HTTP/1.1" 200 OK
```