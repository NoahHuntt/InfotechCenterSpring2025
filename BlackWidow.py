import random
from time import sleep

print("\n**************************************\n")
print("Gasoline Branch - Developer: Noah Hunt\n")


def gasLevelGauge():
    gas_levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gas_levels)


def gasStation():
    stations = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"]
    return random.choice(stations)


def gasLevelAlert():
    gas_level = gasLevelGauge()  # Get current gas level

    if gas_level == "Empty":
        print("**** WARNING - YOU ARE OUT OF GAS ****\n")
        sleep(1.25)
        print("Calling AAA...")
    elif gas_level in ["Low", "Quarter Tank"]:
        miles_to_station = round(random.uniform(1, 25), 1)  # Generate a random distance
        station = gasStation()  # Get a random gas station

        print(f"Your gas tank is {gas_level.lower()}, checking GPS for the closest gas station...")
        sleep(1.25)
        print(f"The closest gas station is {station}, which is {miles_to_station} miles away.")


# Run the alert function
gasLevelAlert()