import requests

# An object to gather data from the National Weather Service (NWS) API
class NWS(object):
    
    def __init__(self, lat, long):
        # Set the latitude and longitude for the location of interest
        self.latiutude = lat
        self.longitude = long

        self.base_url = "https://api.weather.gov/"
        self.headers = {
            "User-Agent": "WeatherDataCollector/1.0"
        }
                    

    def get_raw_weather(self):
        """
        Fetches the current weather data from the National Weather Service API.
        Returns a dictionary with the weather data.
        """
        url = f"{self.base_url}points/{self.latiutude},{self.longitude}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def get_weather(self):
        """
        Processes the raw weather data to extract relevant information.
        Returns a JSON string with the current weather conditions.
        """
        # TODO - Implement the logic to extract and format the weather data
        return self.get_raw_weather()
        