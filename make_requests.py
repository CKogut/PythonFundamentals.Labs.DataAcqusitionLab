import requests
import json
import config

# limit and offset are included in the URL
offset = 1
limit = 1000
token = config.NOAA_TOKEN

for i in range(39):
    url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?offset={offset}&limit={limit}'
    response = requests.get(url, headers={'token': token})

    with open(f'output_{i}.json', 'w') as file:
        json.dump(response.json(), file)

    offset += limit


