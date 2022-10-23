import json
import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()

file_path = 'app\internal\database.json'

print(file_path)

@app.get('/')
def home():
    with open(file_path) as file:
        arch = json.loads(file.read())
    return users


if __name__ == '__main__':
    uvicorn.run(app=app)