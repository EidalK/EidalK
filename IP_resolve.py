# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:18:47 2024

@author: Krista.Eidal
"""
#Import from appropriate libraries

import pandas as pd

#Copy tabular data from EZProxy Audit Logs into Excel and save as CSV
""" In Excel clean up the logs by removing:
    Top four rows
    Remove extra blank lines (F5, Special, Blank, right click, delete row)
        If multiple days remove:
        Audit Events (Find All, Select all, delete rows)
        Extra Date/Time (as above)
    Save file as Cleaned_EZProxy.csv
    """
#   read the IPs from the csv file

df = pd.read_csv("Cleaned_EZProxy.csv") #change name/location as needed

#Check data loaded properly (can put a number in .head(x) to see more rows)
print(df.head())

# Check if 'IP' column exists in the DataFrame
if 'IP' in df.columns:
    # Filter DataFrame for successful and failed login attempts
    success_df = df[df['Event'] == 'Login.Success']
    failure_df = df[df['Event'] == 'Login.Failure']

    # Count the occurrences of each IP address for successful and failed login attempts
    success_counts = success_df['IP'].value_counts().reset_index()
    success_counts.columns = ['IP', 'Count']
    failure_counts = failure_df['IP'].value_counts().reset_index()
    failure_counts.columns = ['IP', 'Count']

    # Write the results to CSV files (change file names/location as needed)
    success_counts.to_csv('login_success_counts.csv', index=False)
    failure_counts.to_csv('login_failure_counts.csv', index=False)
else:
    print("'IP' column not found in the DataFrame.")
    
#You should now have 2 files.
#The IP addresses need to be resolved before mapping.
#Use https://www.showmyip.com/bulk-ip-lookup/
#ShowMyIp can do 100 IPs at a time
#Download csv
#Copy the IP information into login_success/failure_counts.csv
#These files should now have the column headers:
    #IP, Count, Country, City, Region, ZIP, Timezone, ISP, ASN, Lat and Long
#Create the maps with Mapping.py
