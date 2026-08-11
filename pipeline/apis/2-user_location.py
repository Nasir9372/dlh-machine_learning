#!/usr/bin/env python3
"""
This module prints the location of a specific user.
"""
import requests
import sys
import time


if __name__ == '__main__':
    """
    Prints the location of a specific user.
    """
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        reset_time = int(response.headers["X-Ratelimit-Reset"])
        current_time = time.time()
        minutes = int((reset_time - current_time) / 60)
        print(f"Reset in {minutes} min")

    else:
        data = response.json()
        print(data["location"])
