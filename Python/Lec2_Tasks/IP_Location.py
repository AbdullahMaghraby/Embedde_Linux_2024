import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org/?format=json")
    return response.json()["ip"]

def get_location(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/geo")
    return response.json()


# Get public IP
public_ip = get_public_ip()
print("Your public IP:", public_ip)

# Get location based on IP
location_info = get_location(public_ip)
print("Country:", location_info.get("hostname"))
print("City:", location_info.get("city"))
print("Region:", location_info.get("region"))
print("City:", location_info.get("country"))
print("loc:", location_info.get("loc"))
print("org:", location_info.get("org"))
print("timezone:", location_info.get("timezone"))
print("readme:", location_info.get("readme"))

