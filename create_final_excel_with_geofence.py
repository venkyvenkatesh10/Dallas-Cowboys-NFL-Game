import pandas as pd
import folium
import os

# Load the final subscriber data
final_data_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\final_verizon_subscriber_data.csv"
final_df = pd.read_csv(final_data_path)

# Directory to save the HTML files
html_dir = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\maps"
os.makedirs(html_dir, exist_ok=True)

# AT&T Stadium coordinates
stadium_coords = (32.7473, -97.0945)

# Create a new column for the hyperlinks
final_df['Show Location'] = ''

# Loop through the DataFrame and generate an HTML map for each location
for index, row in final_df.iterrows():
    lat = row['lat']
    lon = row['lon']
    
    # Create the Mapbox map centered on the subscriber's location
    m = folium.Map(location=[lat, lon], zoom_start=15)
    
    # Add the AT&T Stadium marker with a green icon
    folium.Marker(stadium_coords, popup="AT&T Stadium", icon=folium.Icon(color='green')).add_to(m)
    
    # Add a circular polygon (5000 feet radius) around the AT&T Stadium
    folium.Circle(stadium_coords, radius=25000*0.3048, color='blue', fill=True, fill_opacity=0.1).add_to(m)
    
    # Add the subscriber's location marker
    folium.Marker([lat, lon], popup=row['app_name'], icon=folium.Icon(color='red')).add_to(m)
    
    # Save to an HTML file
    map_file = f"map_{index}.html"
    map_path = os.path.join(html_dir, map_file)
    m.save(map_path)
    
    # Create the hyperlink
    final_df.at[index, 'Show Location'] = f'=HYPERLINK("{map_path}", "Show Location")'

# Save the final table to a new CSV file
final_table_path = r"C:\Users\venka\Desktop\Dallas Cowboys NFL game\final_verizon_subscriber_data_with_links.csv"
final_df.to_csv(final_table_path, index=False)

print(f"Final table saved to {final_table_path}")
