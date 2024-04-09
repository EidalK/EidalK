# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:54:40 2024

@author: Krista.Eidal
"""

#Using Basemap. Be sure it is installed.
#Install via GitBash or other Python Console
# pip install basemap

#Further information on Basemap here: https://matplotlib.org/basemap/stable/

#Be sure to have resolved the IPs in login_success/failure_counts.csv files.
#The IP addresses need to be resolved before mapping.
#Use https://www.showmyip.com/bulk-ip-lookup/
#ShowMyIp can do 100 IPs at a time
#Download csv
#Copy the IP information into login_success/failure_counts.csv
#These files should now have the column headers:
    #IP, Count, Country, City, Region, ZIP, Timezone, ISP, ASN, Lat and Long

#Import appropriate libraries
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Load login success and failure count data
success_df = pd.read_csv('login_success_counts.csv')
failure_df = pd.read_csv('login_failure_counts.csv')

### World Map ###

# Create a Basemap instance
plt.figure(figsize=(15, 10)) #alter the numbers to change image demensions
map = Basemap(projection='mill', llcrnrlat=-70, urcrnrlat=90,
              llcrnrlon=-180, urcrnrlon=180, resolution='c')

# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.
# can have resolution = 'l' for slightly better quality
# can only have high quality ('h') with paid version
# projection is the type of map. 
# See https://matplotlib.org/basemap/stable/users/mapsetup.html
#  for different map types in Basemap

# Draw coastlines, countries, and states (map.drawstates(color='gray'))
# Assign colors for land and water
land = '#f5eadf'
water = '#bad9e3'
outline = '#303030'

map.drawcoastlines(color = outline)
map.drawcountries(color = outline)
map.fillcontinents(color=land,lake_color=water) #color fills land
map.drawmapboundary(fill_color=water) #fill_color shades the oceans

# Plot login success counts

#s=success_df['Count']*10 to make dots big enough for world map
#alpha is opacity of the dot. 1 is opac, 0 is transparent
#label will be used in the legend (see below)
x_success, y_success = map(success_df['Long'].values, success_df['Lat'].values)
map.scatter(x_success, y_success, s=success_df['Count']*10, color='green', alpha=0.75, label='Login Success')

# Plot login failure counts
x_failure, y_failure = map(failure_df['Long'].values, failure_df['Lat'].values)
map.scatter(x_failure, y_failure, s=failure_df['Count']*10, color='red', alpha=0.75, label='Login Failure')

# Add legend
plt.legend()

# Give the map a title
plt.title('EZProxy Login Success and Failure Counts')

# Save the image map to your computer
# Need to save before showing otherwise image not saved properly
plt.savefig('login_success_failure_map.png', dpi=300)

# Show the plot
plt.show()

#################################################

### UK and Europe Map ###

# Load login success and failure count data
success_df = pd.read_csv('login_success_counts.csv')
failure_df = pd.read_csv('login_failure_counts.csv')

# Create a Basemap instance
plt.figure(figsize=(7, 7))
map = Basemap(projection='mill', llcrnrlat=30, urcrnrlat=70,
              llcrnrlon=-10, urcrnrlon=30, resolution='l')

# Draw coastlines, countries, and states (map.drawstates(color='gray'))
#Assign colors for land and water
land = '#f5eadf'
water = '#bad9e3'
outline = '#303030'

map.drawcoastlines(color = outline)
map.drawcountries(color = outline)
map.fillcontinents(color=land,lake_color=water) #color fills land
map.drawmapboundary(fill_color=water) #fill_color shades the oceans

# Plot login success counts
x_success, y_success = map(success_df['Long'].values, success_df['Lat'].values)
map.scatter(x_success, y_success, s=success_df['Count']*10, color='green', alpha=0.75, label='Login Success')

# Plot login failure counts
x_failure, y_failure = map(failure_df['Long'].values, failure_df['Lat'].values)
map.scatter(x_failure, y_failure, s=failure_df['Count']*10, color='red', alpha=0.75, label='Login Failure')

# Add legend
plt.legend()

# Save the image map to your computer
plt.savefig('login_map_eur.png', dpi=300)

plt.show()


###############################################
###############################################
#An example of another map style of USA with Seatle indicated
#Taken from https://jakevdp.github.io/PythonDataScienceHandbook/04.13-geographic-data-with-basemap.html

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6, 
            lat_0=45, lon_0=-100,)
m.etopo(scale=0.5, alpha=0.5)

#.etopo is topography; alpha is opacity

# Map (long, lat) to (x, y) for plotting
# NOTE longitude first
x, y = m(-122.3, 47.6)
plt.plot(x, y, 'ok', markersize=5) #marker is size of dot
plt.text(x, y, ' Seattle', fontsize=12)
