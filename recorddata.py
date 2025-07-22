import sys

from datetime import datetime
from nws import NWS

# Function to get the current date and time in a specific format
def get_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# An object to gather data from the National Weather Service (NWS) API
def append_to_output_file(data):
    with open("output.txt", "a") as file:
        file.write(f"{data}\n")

# Main function to gather weather data and append it to the output file
def main():
    nws_api = NWS()
    
    append_to_output_file(f"Date: {get_date()}, Alerts: {nws_api.get_alert_count()}")

 
if __name__ == "__main__":
    main()
