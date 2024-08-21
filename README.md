This project aims to visualize subscriber data usage during the Dallas Cowboys NFL games at AT&T Stadium. The data includes geospatial information, app usage, and data usage (upstream, downstream, and total). Various visualizations have been created to provide insights into how subscribers interact with apps during the event.

Project Overview

Key Features: 

Data Visualization: Visualize subscriber data usage through various charts and interactive maps. 
Geospatial Analysis: Map subscriber locations relative to the AT&T Stadium, including geofencing and clustering. 
Time-Based Analysis: Analyze data usage patterns over time. 
Category-Based Analysis: Explore how different app categories contribute to data usage.

Visualizations: 
Average Total Data Usage by App Category: A bar chart showing the average data usage for each app category. 
Data Usage Distribution by Category: A pie chart showing the percentage distribution of total data usage across different app categories. 
Heatmap - Data Usage Density: A heatmap indicating the density of data usage across different locations around AT&T Stadium. 
Cluster Map - Subscriber Data Usage Clusters: An interactive map showing clusters of subscriber data usage. 
Total Data Usage Over Time: A line chart displaying how data usage changes over time during the event. 
Scatter Plot - Upstream vs. Downstream Data Usage: A scatter plot showing the relationship between upstream and downstream data usage, categorized by app type.

Directory Structure: / |-- data/ # Directory containing all the data files | |-- final_verizon_subscriber_data_with_links.csv # Final merged data with hyperlinks |-- visualizations/ # Directory containing all generated visualizations | |-- average_total_data_usage_by_category.png # Bar chart visualization | |-- data_usage_distribution_by_category.png # Pie chart visualization | |-- data_usage_heatmap.html # Heatmap visualization | |-- subscriber_data_usage_cluster_map.html # Cluster map visualization | |-- total_data_usage_over_time.png # Time series line chart | |-- upstream_vs_downstream_scatter.png # Scatter plot visualization |-- scripts/ # Directory containing the scripts used for data processing and visualization | |-- generate_visualizations.py # Python script to generate visualizations |-- README.md # Project documentation (this file)

Key Data Files: 
final_verizon_subscriber_data_with_links.csv: This is the main data file that contains subscriber information, app usage data, and hyperlinks to individual maps for each subscriber.

Example Usage You can use the visualizations generated by this project to:
Identify hotspots of data usage around the stadium. Understand which app categories are most popular during the event. Analyze the time periods with the highest data usage.

Contributions: Contributions are welcome! Please feel free to open issues or submit pull requests if you have any improvements or new features to suggest.

Acknowledgments
Folium: For providing easy-to-use tools for geospatial data visualization. 
Matplotlib and Seaborn: For enabling detailed and customizable data visualizations. 
Pandas: For powerful data manipulation and analysis tools.
