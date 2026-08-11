#!/usr/bin/env python3
"""
This module creates a method that returns the list of
names of the home planets of all sentient species.
"""
import requests


def sentientPlanets():
    """
    Returns the list of names of the home
    planets of all sentient species.
    """
    planets = []
    url = "https://swapi-api.hbtn.io/api/species/"

    while url:

        response = requests.get(url)

        data = response.json()

        species_list = data["results"]

        for species in species_list:
            classification = (species["classification"]).lower()
            designation = (species["designation"]).lower()

            if (classification == "sentient" or designation == "sentient"):
                homeworld_url = species["homeworld"]

                if homeworld_url:
                    planet_response = requests.get(homeworld_url)
                    planet_data = planet_response.json()
                    planets.append(planet_data["name"])

        url = data["next"]

    return planets
