import requests

def get_location(ip=""):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        print("\n Location Details:")
        print(f"IP Address: {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location (Lat,Long): {data.get('loc', 'N/A')}")
        print(f"ISP/Org: {data.get('org', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")

    except Exception as e:
        print(f" Error: {e}")

print(" IP Location Tracker")
ip_input = input("Enter IP address : ").strip()
get_location(ip_input)
