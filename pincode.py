import requests


# Define the URL of the endpoint
url = 'https://nominatim.openstreetmap.org/reverse'

# Parameters to send in the query string
params = {
    'lat': '33.417880',
    'lon': '-111.912036',
    'format': 'json'
}

# Define headers with a valid User-Agent
headers = {
    'User-Agent': 'YourAppName/1.0 (your.email@example.com)'
}

# Make the request with headers and parameters
response = requests.get(url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
    print("##############################################################")
    print("Machanne Machanne")
    print(data['address']['postcode'])
else:
    print(f"Error: {response.status_code}")
    print(response.text) 

