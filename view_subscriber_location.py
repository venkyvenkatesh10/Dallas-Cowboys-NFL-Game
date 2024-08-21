import pandas as pd
import folium
import webbrowser
import os

# Path to your Excel file
excel_file_path = "C:/Users/venka/Desktop/Dallas Cowboys NFL game/final_verizon_subscriber_data.xlsx"

# Load Excel data
df = pd.read_excel(excel_file_path)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    lat = row['lat']  # Assuming 'lat' is the column name for latitude
    lon = row['lon']  # Assuming 'lon' is the column name for longitude
    
    # Generate the map centered on the subscriber's location
    map_ = folium.Map(location=[lat, lon], zoom_start=15)
    
    # Add a marker for the subscriber's location
    folium.Marker([lat, lon], popup='Subscriber Location', icon=folium.Icon(color='blue')).add_to(map_)
    
    # Add AT&T Stadium marker
    stadium_lat, stadium_lon = 32.7473, -97.0945
    folium.Marker([stadium_lat, stadium_lon], popup='AT&T Stadium', icon=folium.Icon(color='green')).add_to(map_)
    
    # Add a circle for the 2000 feet radius around the stadium
    folium.Circle([stadium_lat, stadium_lon], radius=609.6, color='blue', fill=True, fill_opacity=0.2).add_to(map_)
    
    # Save the map to an HTML file
    map_file = "temp_map.html"
    map_.save(map_file)
    
    # Open the HTML map in the default web browser
    webbrowser.open('file://' + os.path.realpath(map_file))
    
    # Wait for user to manually close the map (infinite loop until they do)
    input("Press Enter to close the map and delete the file...")

    # Remove the temporary file after viewing
    os.remove(map_file)
    
    # Break after the first map to prevent looping through all rows
    break  # Remove this line if you want to view maps for all rows
