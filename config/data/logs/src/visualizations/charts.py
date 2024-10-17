import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def plot_temperature_trends(city):
    conn = sqlite3.connect('data/weather_data.db')
    query = f"SELECT timestamp, temp FROM weather WHERE city='{city}'"
    df = pd.read_sql(query, conn)
    conn.close()

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s')
    plt.plot(df["timestamp"], df["temp"])
    plt.title(f"Temperature Trend for {city}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.show()
