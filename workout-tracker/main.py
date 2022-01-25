import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = 86
HEIGHT_CM = 164
AGE = 22

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/fa178008505d0e2f7d627164243b649c/myWorkoutsPythonProject/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}",
        "Content-Type": "application/json"
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)