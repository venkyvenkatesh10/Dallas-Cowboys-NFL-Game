import pandas as pd
import random
import uuid

# Load the subscriber details
subscriber_details_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\verizon_subscriber_details.csv"
subscribers_df = pd.read_csv(subscriber_details_path)

# Path to the geofence script
geofence_script_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\at&t_stadium_geofence.py"

# Sample app categories and apps
apps_categories = {
    "Social Media": ["Facebook", "Instagram", "Twitter", "Snapchat"],
    "Streaming": ["Netflix", "YouTube", "Hulu", "Disney+"],
    "Shopping": ["Amazon", "eBay", "Walmart", "Target"],
    "Gaming": ["PUBG Mobile", "Call of Duty Mobile", "Clash of Clans", "Candy Crush"],
    "Productivity": ["Google Drive", "Microsoft Office", "Slack", "Trello"],
    "News": ["CNN", "BBC", "Fox News", "NY Times"],
    "Health": ["Fitbit", "MyFitnessPal", "Apple Health", "Google Fit"]
}

# Generate URL information
def generate_url(app_name):
    protocol = random.choice(["http", "https"])
    host = f"www.{app_name.lower().replace(' ', '')}.com"
    path = f"/{uuid.uuid4()}"
    return f"{protocol}://{host}{path}", protocol, host

# Generate app usage for each subscriber
app_usage_data = []
for _, subscriber in subscribers_df.iterrows():
    num_apps_used = random.randint(1, 5)  # Each subscriber uses between 1 and 5 apps
    for _ in range(num_apps_used):
        category = random.choice(list(apps_categories.keys()))
        app_name = random.choice(apps_categories[category])
        url, protocol, host = generate_url(app_name)
        
        # Generate random data usage
        upstream_gb = round(random.uniform(0.1, 2.0), 2)  # Upstream data in GB (between 0.1 and 2.0 GB)
        downstream_gb = round(random.uniform(0.5, 5.0), 2)  # Downstream data in GB (between 0.5 and 5.0 GB)
        total_gb = round(upstream_gb + downstream_gb, 2)  # Total data usage in GB

        usage_record = {
            "mdn_hash": subscriber["mdn_hash"],
            "city": subscriber["city"],
            "lat": subscriber["latitude"],
            "lon": subscriber["longitude"],
            "app_name": app_name,
            "category": category,
            "url": url,
            "protocol": protocol,
            "host": host,
            "timestamp": subscriber["entry_time"],  # Using entry time as usage time for simplicity
            "duration_minutes": random.randint(1, 60),  # Random usage duration between 1 and 60 minutes
            "upstream_gb": upstream_gb,  # Upstream data in GB
            "downstream_gb": downstream_gb,  # Downstream data in GB
            "total_gb": total_gb  # Total data in GB
        }
        app_usage_data.append(usage_record)

# Convert the app usage data to a DataFrame
app_usage_df = pd.DataFrame(app_usage_data)

# Save the app usage data to a CSV file
output_app_usage_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\verizon_subscriber_app_usage.csv"
app_usage_df.to_csv(output_app_usage_path, index=False)

print(f"App usage data saved to {output_app_usage_path}")
print(f"Geofence script path: {geofence_script_path}")
