import requests

# Set your New Relic API key
API_KEY = "YOUR API KEY"

# New Relic Alerts API endpoint
url = "https://api.newrelic.com/v2/alerts_incidents.json"

# Set up headers with API key
headers = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json"
}

# Make a GET request to the New Relic Alerts API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract incident GUIDs from the JSON response
    incidents = response.json().get("incidents", [])
    guids = [incident.get("id") for incident in incidents]

    # Print the GUIDs
    for guid in guids:
        print(guid)
    print(guids)
else:
    print("Error:", response.status_code, response.text)
