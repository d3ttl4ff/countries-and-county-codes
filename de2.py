import json
import csv

with open('countryCodes.json', 'r') as json_file:
    data = json.load(json_file)

csv_data = []
for key, value in data.items():
    csv_data.append([key, value['country'], value['ISO2'], value['countryCode']])

with open('countryCodes.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Code', 'Country', 'ISO2', 'Country Code'])  # Write header row
    csv_writer.writerows(csv_data)  # Write data rows
