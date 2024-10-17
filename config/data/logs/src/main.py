import sys
import os

# Adding the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import schedule
import time
from weather_api import get_weather_data
from data_processor import save_to_database, calculate_daily_summary
from alert_system import check_alert_conditions


def job():
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
    for city in cities:
        data = get_weather_data(city)
        if data:
            save_to_database(data)
            check_alert_conditions(data)

schedule.every(5).minutes.do(job)

print("Weather Monitoring System Started...")
while True:
    schedule.run_pending()
    time.sleep(1)
