
# Weather Reporter (Simulated)

A simple Python project that gives a mock weather report
for a city entered by the user.

This version doesn’t use any API — it randomly generates temperature,
humidity, and conditions for demonstration and practice.

Concepts covered:
- Random number generation
- Lists and string formatting
- Functions and modular programming

```
"""
Weather Reporter (Simulated)
-----------------------------------------
A simple Python project that gives a mock weather report
for a city entered by the user.

This version doesn’t use any API — it randomly generates temperature,
humidity, and conditions for demonstration and practice.

Concepts covered:
- Random number generation
- Lists and string formatting
- Functions and modular programming
"""

import random
import time


def get_mock_weather(city):
    """
    Generates a simulated weather report for the given city.

    Parameters:
        city (str): The name of the city

    Returns:
        dict: A dictionary containing weather details
    """

    # Randomly generated values to simulate real weather
    temperature = random.randint(15, 40)        # Temperature in °C
    humidity = random.randint(30, 90)           # Humidity in %
    wind_speed = round(random.uniform(1.5, 10.0), 1)  # Wind speed in km/h

    # Possible weather conditions
    conditions = ["Sunny", "Cloudy", "Rainy", "Windy", "Stormy", "Foggy", "Clear"]
    condition = random.choice(conditions)

    return {
        "city": city.title(),
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "condition": condition,
    }


def display_weather(report):
    """
    Displays the weather report in a formatted way.

    Parameters:
        report (dict): The dictionary containing weather info
    """
    print("\n------------------------------------")
    print(f"Weather Report for: {report['city']}")
    print("------------------------------------")
    print(f"Temperature : {report['temperature']}°C")
    print(f"Humidity    : {report['humidity']}%")
    print(f"Wind Speed  : {report['wind_speed']} km/h")
    print(f"Condition   : {report['condition']}")
    print("------------------------------------\n")


def main():
    """Main function to handle user input and display weather info."""
    print("Welcome to the Weather Reporter!")
    print("Type 'exit' anytime to quit.\n")

    while True:
        city = input("Enter city name: ").strip()

        if city.lower() == "exit":
            print("\nExiting Weather Reporter. Have a great day!")
            break

        if not city:
            print("Please enter a valid city name.\n")
            continue

        print("\nFetching weather report...")
        time.sleep(1.5)  # Simulate data loading delay

        report = get_mock_weather(city)
        display_weather(report)


if __name__ == "__main__":
    main()

```
