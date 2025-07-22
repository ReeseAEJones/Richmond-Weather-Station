import sys

from datetime import datetime
from nws import NWS

# This is the default weather data for Richmond, VA. If this is used for another location, 
# the latitude and longitude should be updated or used a command line argument.
richmond_latiutude = 37.541290
richmond_longitude = -77.434769

# Function to get the latitude and longitude values from command line arguments
def get_lat_and_long():
    argc = len(sys.argv)
    if argc != 3 and argc != 1:
        print("Usage: python recorddata.py <latitude> <longitude>")
        sys.exit(1)
    
    if argc == 1:
        return None, None

    try:
        lat = float(sys.argv[1])
        long = float(sys.argv[2])
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)
    
    return lat, long

# Function to get the current date and time in a specific format
def get_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# An object to gather data from the National Weather Service (NWS) API
def append_to_output_file(data):
    with open("output.txt", "a") as file:
        file.write(f"{data}\n")

# Main function to gather weather data and append it to the output file
def main():
    # Use default Richmond, VA coordinates if no command line arguments are provided
    lat, long = get_lat_and_long()
    if lat is None or long is None:
        lat, long = richmond_latiutude, richmond_longitude

    nws_api = NWS(lat, long)
    
    append_to_output_file(f"Date: {get_date()}, Weather: {nws_api.get_weather()}")

 
if __name__ == "__main__":
    main()
