from fastapi import FastAPI
import ollama

# references:
# https://ollama.com/blog/python-javascript-libraries
# https://www.postman.com/postman-student-programs/ollama-api/documentation/suc47x8/ollama-rest-api

app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
    response = ollama.chat(model="llama3.1:8b", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}