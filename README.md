# Weather Monitoring System

A Python-based weather monitoring system that fetches weather data for multiple cities at regular intervals, processes the data, and checks for alert conditions.

## Features

- Fetches current weather data from the OpenWeatherMap API.
- Supports monitoring multiple cities (e.g., Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- Saves weather data to a database (to be implemented).
- Checks for alert conditions based on specified thresholds (to be implemented).
- Scheduled data retrieval every 5 minutes using the `schedule` library.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- `requests` library for making HTTP requests
- `schedule` library for scheduling tasks

You can install the required libraries using pip:

```bash
pip install requests schedule
