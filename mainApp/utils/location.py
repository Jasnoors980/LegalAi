import requests

def get_country_from_ip(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        if response.status_code == 200:
            data = response.json()
            return data.get("country_name", "Unknown")
    except:
        pass
    return "Unknown"
