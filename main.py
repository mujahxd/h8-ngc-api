
from fastapi import FastAPI, HTTPException, Header, status

app = FastAPI()

API_KEY = "ngc10h8"

fake_weathers_db = {
    "new-york-city": {
        "name": "New York City",
        "temperature": "77 F",
        "humidity:": "46%",
        "wind": "5 mph"
    },
    "los-angeles": {
        "name": "Los Angeles",
        "temperature": "67 F",
        "humidity:": "82%",
        "wind": "2 mph"
    },
    "chicago": {
        "name": "Chicago",
        "temperature": "64 F",
        "humidity:": "83%",
        "wind": "7 mph"
    }
}

@app.get("/weather/{location}")
def get_weather(location: str):
    if location in fake_weathers_db:
        return fake_weathers_db[location]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location not found.")


@app.get("/authenticate")
def auth(api_key: str = Header(None)):

    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")
    
    return {
        "message": "You used a valid API key."
    }