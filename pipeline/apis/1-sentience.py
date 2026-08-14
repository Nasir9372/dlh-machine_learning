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
    home_planets = []
    url = "https://swapi-api.hbtn.io/api/species/"

    while url:
        # request all info about species
        response = requests.get(url)
        data = response.json()
        species_list = data["results"]

        for spec in species_list:
            # define variable for condition below
            classification = spec.get("classification").lower()
            designation = spec.get("designation").lower()
            # find species with class/desig as sentient and
            # fetch thier location (url of plannet where these
            # species lives which is class/desig as sentient)
            if "sentient" in classification or "sentient" in designation:
                planet_url = spec.get("homeworld")
                if planet_url:
                    # fetch plannet name from planet url
                    # means another url get open e.g.
                    # https://swapi-api.hbtn.io/api/planets/9/
                    # at this location we have name: coruscant
                    planet_response = requests.get(planet_url)
                    planet_data = planet_response.json()
                    home_planets.append(planet_data.get("name"))
        url = data.get("next")  # pagination
    return home_planets
