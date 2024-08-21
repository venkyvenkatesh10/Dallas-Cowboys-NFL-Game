import pandas as pd
import random
import uuid
from datetime import datetime, timedelta
import numpy as np

# Load the ZIP to CMA mapping from the CSV file
zip_to_cma_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\dallas_zip_to_cma.csv"
zip_to_cma_df = pd.read_csv(zip_to_cma_path)

# Define the geofence around AT&T Stadium
stadium_center = (32.7473, -97.0945)  # Latitude and Longitude of AT&T Stadium
radius_in_meters = 600  # 600 meters around the stadium

# Function to generate a random point within the circular geofence
def random_point_in_circle(radius, center):
    angle = 2 * np.pi * random.random()
    r = radius * np.sqrt(random.random())
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    return (center[0] + y / 111300, center[1] + x / (111300 * np.cos(center[0])))

# List of cities in the Dallas metropolitan area
cities = [
    "Dallas", "Frisco", "Irving", "Denton", "Arlington", "Celina", "Princeton",
    "McKinney", "Gunter", "Prosper", "Rockwall", "Murphy", "Garland", "DFW",
    "Richardson", "Plano", "Southlake"
]

# Sample list of subscribers
num_subscribers = 1000

# Game time window
game_start_time = datetime.strptime("2024-09-14 12:00:00", "%Y-%m-%d %H:%M:%S")
game_end_time = datetime.strptime("2024-09-14 20:00:00", "%Y-%m-%d %H:%M:%S")

# Sample Data: Generating random subscriber data
subscribers = []
for _ in range(num_subscribers):
    zip_code = random.choice(zip_to_cma_df['ZIP5_CD'])
    city = random.choice(cities)
    entry_time = game_start_time + timedelta(seconds=random.randint(0, int((game_end_time - game_start_time).total_seconds())))
    exit_time = entry_time + timedelta(seconds=random.randint(600, 14400))  # Random exit time between 10 min to 4 hours after entry

    # Ensure exit time doesn't exceed game end time
    if exit_time > game_end_time:
        exit_time = game_end_time

    lat, lon = random_point_in_circle(radius_in_meters, stadium_center)
    
    subscriber = {
        "mdn_hash": str(uuid.uuid4()),  # Unique identifier for the subscriber
        "device_make": random.choice(["Apple", "Samsung", "Google", "Kyocera", "Motorola"]),
        "device_model": random.choice(["iPhone 13", "Galaxy S21", "Pixel 6", "DuraForce PRO 2", "Moto G Power"]),
        "entry_time": entry_time.strftime("%Y-%m-%d %H:%M:%S"),
        "exit_time": exit_time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration": int((exit_time - entry_time).total_seconds() / 60),  # Duration in minutes
        "timeZone": "CST",
        "state": "TX",
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "ZIP5_CD": zip_code
    }
    subscribers.append(subscriber)

# Convert to DataFrame
subscribers_df = pd.DataFrame(subscribers)

# Merge with the ZIP to CMA mapping to get CMA codes
detailed_df = pd.merge(subscribers_df, zip_to_cma_df, on='ZIP5_CD', how='left')

# Drop the `ZIP5_CD` column from the final DataFrame if you don't want to include it
detailed_df = detailed_df.drop(columns=['ZIP5_CD'])

# Display the resulting DataFrame
print(detailed_df)

# Save the detailed subscriber data to a CSV file
output_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\verizon_subscriber_details.csv"
detailed_df.to_csv(output_path, index=False)
