import time
import json

def load_config():
    with open('config/config.json') as f:
        return json.load(f)

def check_alert_conditions(data):
    config = load_config()
    threshold_temp = config["threshold_temp"]
    duration = config["threshold_duration"]
    
    if data["temp"] > threshold_temp:
        print(f"ALERT: Temperature in {data['city']} exceeded {threshold_temp}°C!")
        with open("logs/alerts.log", "a") as log_file:
            log_file.write(f"{time.ctime()} - ALERT: {data['city']} temp {data['temp']}°C\n")

