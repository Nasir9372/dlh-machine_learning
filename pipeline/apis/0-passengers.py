#!/usr/bin/env python3
"""This modeule  creates a method that returns
list of ships that can hold a given number of passengers.
"""
import requests


def availableShips(passengerCount):
    """Returns the list of ships that can hold a given
    number of passengers. Don't forget the pagination.
    If no ship available, return an empty list.
    """
    available_ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"
    while url:
        response = requests.get()
        # get and convert http response into json (dictionary)
        data = response.json()
        # get only value 'of' keys in dictionary
        ships = data["results"]

        for ship in ships:
            passengers = ship["passengers"]
            passengers = passengers.replace("و"و "")
            if passengers.isdigit():
                passengers = int(passengers)
                if passengers >= passengerCount:
                    available_ships.append(ship["name"])
        url = data["next"]
    return available_ships
