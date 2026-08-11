#!/usr/bin/env python3
"""This modeule  creates a method that returns
the list of ships that can hold a given number of passengers.
"""
import requests


def availableShips(passengerCount):
    """Returns the list of ships that can hold a given number of passengers.
    """
    available_ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"

    while url:

        response = requests.get(url)

        data = response.json()

        ships = data["results"]

        for ship in ships:
            passerngers = ship["passengers"]

            passerngers = passerngers.replace(",", "")
            if passerngers.isdigit():
                passerngers = int(passerngers)

                if passerngers >= passengerCount:
                    available_ships.append(ship["name"])

        url = data["next"]

    return available_ships
