import requests

def get_location_ip(ip_address):
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip={ip_address}"
    response = requests.get(url)
    data = response.json()
    return data

# Example usage
ip_address = "127.0.0.1"  # Example IP address
location_data = get_location_ip(ip_address)

print(f"Location for IP address {ip_address}:")
print(f"City: {location_data['city']}")
print(f"Region: {location_data['region']}")
print(f"Country: {location_data['country_name']}")
print(f"Latitude: {location_data['latitude']}")
print(f"Longitude: {location_data['longitude']}")
