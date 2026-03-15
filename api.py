from fastapi import FastAPI, HTTPException, Request
import json

app = FastAPI()

API_KEY = "123456789"   # give this to Salesforce developer
FILE_NAME = "case_details.json"


@app.get("/cases")
def get_cases(api_key: str):

    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data