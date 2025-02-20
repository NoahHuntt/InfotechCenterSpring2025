#Libraries HERE
import sys
import random
import time

print("Welcome Branch - Developer: Noah Hunt\n")

print("\nWelcome to InfoTechCenter V1.0")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(.5)
    if ellipsis ==4:
        ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Retina Scanned - Access Granted")

print("\n**********************\n")

print("Weather Branch - Developer: Noah Hunt\n")




# Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition



# Function to determine the weather
def weather():
    weather_forecast_list = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    return random.choice(weather_forecast_list)

# Store the weather condition once
weather_alert = weather()

# Vehicle Response System function
def vehicle_response_system():
    # Mapping weather conditions to delay and speed limits
    response_map = {
        "snowing": (30, 55),
        "blizzard": (60, 45),
        "icy": (90, 35),
        "rainy": (10, 65),
        "windy": (5, 70),
    }

    if weather_alert in response_map:
        delay, speed = response_map[weather_alert]
        print(f"\nThe National Weather Service has updated your alarm by {delay} minutes because it is {weather_alert} outside.")
        time.sleep(1)
        print(f"VRS has been engaged, allowing us to drive only {speed}MPH.")
    else:
        print(f"\nThe National Weather Service is calling for {weather_alert} skies outside. Drive safe!")

# Run the vehicle response system
vehicle_response_system()

