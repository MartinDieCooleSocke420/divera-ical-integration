from flask import Flask, Response
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DIVERA_ACCESS_KEY = os.getenv('DIVERA_ACCESS_KEY')

# The URL of the API that returns the .ics file
API_URL = 'https://app.divera247.com/api/v2/events/ics?accesskey=' + DIVERA_ACCESS_KEY


@app.route('/DiveraCalendar.ics')
def get_calendar():
    # Fetch the .ics file from the API
    api_response = requests.get(API_URL)
    api_response.raise_for_status()  # Ensure the request was successful

    # Serve the .ics content directly
    return Response(
        api_response.content,
        mimetype='text/calendar',
        headers={
            "Content-Disposition": "attachment; filename=calendar.ics"
        }
    )

if __name__ == '__main__':
    app.run(port=80)
