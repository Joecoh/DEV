import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

# Read the shapefile
fp = r'Maps_with_python\india-polygon.shp'
map_df = gpd.read_file(fp)

# Copy the dataframe
map_df_copy = gpd.read_file(fp)

# Create a GeoDataFrame for landslide data
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Plot the map
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_title('Number of landslides in India state-wise', fontdict={'fontsize': 20, 'fontweight': 10})

# Plot the country borders
ax.add_geometries(map_df['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=1)

# Plot the landslides
gdf.plot(ax=ax, color='red', markersize=5, alpha=0.7, label='Landslides')

# Display the legend
ax.legend()

# Show the plot
plt.show()
