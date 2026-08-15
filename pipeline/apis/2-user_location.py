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
    # 1 is index which represent 1st argument
    # per task requirement this should be the url
    # while 0 is always the script name or file name
    # like 2-user_location.py is at 0 index and
    # the above url when fetched it will be at index 1
    # url = sys.argv[1], Gets the "https://api.github.com/users/john"
    response = requests.get(url)
    # Fetches the GitHub API
    if response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        # rate limit in api is control mechanism, to handle
        # number of http user request or client can make to
        # API within specific timeframe, e.g. per sec/min/day
        # the purpose to prevent overloading of backend infra
        # when rate limit exceeded, API reject user request with
        # msg HTTP 429 too many requests
        # X-ratelimit-limit = total allowed request
        # X-ratelimit-remaining = total remaining request
        # X-ratelimit-reset = time untill next window resets
        reset_time = int(response.headers["X-Ratelimit-Reset"])
        current_time = time.time()
        minutes = int((reset_time - current_time) / 60)
        print(f"Reset in {minutes} min")

    else:
        data = response.json()
        print(data["location"])
