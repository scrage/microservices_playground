from fastapi import FastAPI, Depends, HTTPException, Header
from dotenv import load_dotenv
import ollama
import os

# references:
# https://ollama.com/blog/python-javascript-libraries
# https://www.postman.com/postman-student-programs/ollama-api/documentation/suc47x8/ollama-rest-api

load_dotenv()

# read the (hard coded) API key from the environment variable and implement a very basic
# token bucket rate limiting strategy by only allowing 10 requests to start with
API_KEY_CREDITS = {os.getenv("API_KEY"): 10}

app = FastAPI()
llm_model = "llama3.1:8b" # this model here can even be a customized one too

def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code = 401, details = "Invalid API key or no credits left.")
    
    return x_api_key

@app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    response = ollama.chat(model = llm_model, messages = [{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}
