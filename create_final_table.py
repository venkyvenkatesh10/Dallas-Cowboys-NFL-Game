import pandas as pd

# Load the subscriber details
subscriber_details_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\verizon_subscriber_details.csv"
subscribers_df = pd.read_csv(subscriber_details_path)

# Load the app usage data
app_usage_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\verizon_subscriber_app_usage.csv"
app_usage_df = pd.read_csv(app_usage_path)

# Merge the two DataFrames on the 'mdn_hash' column
final_df = pd.merge(app_usage_df, subscribers_df, on='mdn_hash', how='inner')

# Fix latitude, longitude, and city to AT&T Stadium coordinates
fixed_lat = 32.7473
fixed_lon = -97.0945
fixed_city = "Arlington"

# Add fixed latitude, longitude, and city as new columns on the right side
final_df['fixed_latitude'] = fixed_lat
final_df['fixed_longitude'] = fixed_lon
final_df['fixed_city'] = fixed_city

# Remove the original 'city_y', 'latitude', and 'longitude' columns
final_df = final_df.drop(columns=['city_y', 'latitude', 'longitude'])

# Save the final table to a new CSV file
final_table_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\final_verizon_subscriber_data.csv"
final_df.to_csv(final_table_path, index=False)

print(f"Final table saved to {final_table_path}")
