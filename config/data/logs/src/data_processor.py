import pandas as pd
import sqlite3
from datetime import datetime

def save_to_database(data):
    conn = sqlite3.connect('data/weather_data.db')
    df = pd.DataFrame([data])
    df.to_sql('weather', conn, if_exists='append', index=False)
    conn.close()

def calculate_daily_summary():
    conn = sqlite3.connect('data/weather_data.db')
    query = """
    SELECT city, date(timestamp, 'unixepoch') as day, 
           AVG(temp) as avg_temp, 
           MAX(temp) as max_temp, 
           MIN(temp) as min_temp, 
           weather, COUNT(weather) as frequency 
    FROM weather
    GROUP BY city, day, weather
    ORDER BY frequency DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_dominant_weather(city, day):
    df = calculate_daily_summary()
    day_weather = df[(df["city"] == city) & (df["day"] == day)]
    dominant = day_weather.iloc[0]["weather"] if not day_weather.empty else "N/A"
    return dominant
