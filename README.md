# Richmond Weather Station
A small repo to process/store daily alert data blasts from the National Weather Service (NWS) API for the Richmond, VA area. 
This is a tiny personal project to manually save and convert free data, so that I can calculate alert frequency of the NWS for the US and any upward or downward trends in alerts. 
That seperate project will be completed after some data is collected, and will compare the NWS daily alert data to the historical weather data.

## Data Source
This repo soureces data from the Public API and Datasource from the National Weather Service (NWS) provided [here](https://www.weather.gov/documentation/services-web-api).

The data contains prediction links which have an expiration datw within the year of 2200, so is assumed that the links will not change or be deleted. THis data is not retroactively searchable using the NWS API.

## Operations
I have a bash script running on my computer to commit + push based on two buttons I have on my desktop. This may mean intermittent data updates and skips in data. 
I could host this on a server (even a RaspberryPi), but I don't have one available at the moment. 
So I will just run this on my computer for now. 

This means that the data will be updated when I run the script, and not on a set schedule.
This could be considered a randomized sampling of the data, though my actions are not totally random so there will likely be some affect on the data.
