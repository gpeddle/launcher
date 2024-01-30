from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import string
import secrets

from data.display_repository import DisplayRepository
from models.display import Display, DisplayStatusEnum

app = FastAPI()
data = DisplayRepository('displays.db')
data.load_initial_data('initial-data.json')



# Get a list of displays


@app.get("/displays")
async def list_displays():
    # Return a list of displays
    displays: List = data.get_all()
    result = [display.json() for display in displays]

    return result

# Get details about a specific display


@app.get("/display/{id}")
async def get_display(id: str):
    display: Display = data.get_by_id(id)
    if display:
        return display.json()
    else:
        return {"message": "Display not found"}

# Check display status and provide an activation challenge code if necessary


@app.get("/auth/{id}/{web_app}/{api_key}")
async def check_display_auth(id: str, web_app: str, api_key: str):

    if id is None:
        return {"status": "Failure", "message": "No Display id parameter provided"}
    if web_app is None:
        return {"status": "Failure", "message": "No Display web_app parameter provided"}
    if api_key is None:
        return {"status": "Failure", "message": "No Display api_key parameter provided"}

    display: Display = data.get_by_id(id)

    # Fail if the display is not found
    if display is None:
        return {"status": "Failure", "message": "Display not found"}

    # Fail if the display is not associated with the given web app
    if display.web_app != web_app:
        return {"status": "Failure", "message": "Display not found"}

    # Check if the display is authorized
    status = None
    if display.api_key == api_key:
        status = {"status": "Success"}
    else:
        status = {"status": "Failure"}
        display.status = DisplayStatusEnum.pending
        display.challenge_code = generate_challenge_code()
        data.update(display)
        status['challenge_code'] = display.challenge_code

    return status

# Activate a display with a challenge code


@app.put("/activate/{id}/{web_app}/{challenge_code}")
async def activate_display(id: str, web_app: str, challenge_code: str):

    if id is None:
        return {"status": "Failure", "message": "No Display id parameter provided"}
    if web_app is None:
        return {"status": "Failure", "message": "No Display web_app parameter provided"}
    if challenge_code is None:
        return {"status": "Failure", "message": "No Display challenge_code parameter provided"}

    display: Display = data.get_by_id(id)

    # Fail if the display is not found
    if display is None:
        return {"status": "Failure", "message": "Display not found"}

    # Fail if the display is not associated with the given web app
    if display.web_app != web_app:
        return {"status": "Failure", "message": "Display not found"}

    if challenge_code != display.challenge_code:
        return {"status": "Failure", "message": "Invalid challenge code"}

    # Check if the challenge code matches the expected code for activation
    status = None
    if challenge_code == display.challenge_code:
        display.status = DisplayStatusEnum.active
        display.challenge_code = None
        display.api_key = generate_api_key()  
        data.update(display)
        status = {
            "status": "Success",
            "message": "Display activated successfully",
            "api_key": display.api_key  
        }
    return status


@app.put("/disable/{id}")
async def disable_display(id: str):

    if id is None:
        return {"status": "Failure", "message": "No Display id parameter provided"}

    display: Display = data.get_by_id(id)

    # Fail if the display is not found
    if display is None:
        return {"status": "Failure", "message": "Display not found"}

    display.api_key = None
    display.challenge_code = None
    display.status = 'disabled'
    data.update(display)
    return {"status": "Success", "message": "Display disabled successfully"}



def generate_challenge_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(characters) for _ in range(6)).upper()
    return code

def generate_api_key():
    characters = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(characters) for _ in range(32))
    return key


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
