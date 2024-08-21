import folium

# AT&T Stadium coordinates (latitude, longitude)
stadium_coords = (32.7473, -97.0945)

# Example device location (latitude, longitude)
device_location = (32.746, -97.095)

# Create a map centered on AT&T Stadium
m = folium.Map(location=stadium_coords, zoom_start=15)

# Add a marker for AT&T Stadium
folium.Marker(stadium_coords, popup="AT&T Stadium", icon=folium.Icon(color='green')).add_to(m)

# Add a marker for the device location
folium.Marker(device_location, popup="Device Location", icon=folium.Icon(color='red')).add_to(m)

# Add a circle representing the geofence (2000 feet radius)
folium.Circle(stadium_coords, radius=2000*0.3048, color='blue', fill=True, fill_opacity=0.1).add_to(m)

# Save the map to an HTML file
m.save("at&t_stadium_geofence_map.html")
