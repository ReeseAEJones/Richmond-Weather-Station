import requests

# An object to gather data from the National Weather Service (NWS) API
class NWS(object):
    
    def __init__(self):
        self.base_url = "https://api.weather.gov/"
        self.headers = {
            "User-Agent": "WeatherDataCollector/1.0"
        }
                    
    def get_raw_alert_count(self):
        """
        Fetches the current weather data from the National Weather Service API.
        Returns a dictionary with the weather data.
        """
        url = f"{self.base_url}/alerts/active/count"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def get_alert_count(self):
        """
        Collects the raw alert data from the National Weather Service API.
        """
        # This function is a placeholder for future implementation
        return self.get_raw_alert_count()
       

        