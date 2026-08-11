# API Data Ingestion Module

This module introduces the first step in building a modern data pipeline: collecting raw data from external sources and preparing it for storage, cleaning, and analysis. Instead of manually downloading files from servers, website, databases, the goal is to automate data retrieval using Python and public APIs.

## Module Purpose
Data ingestion is the process of bringing external data into your system. In this project, that means fetching information from web services, handling API rules, and storing the results in a structured format for later use in a data lake or analytics workflow.

## What You Will Learn

- How to make HTTP requests with Python using the Requests library
- How to retrieve data from APIs efficiently
- How to handle pagination to collect large datasets
- How to manage rate limiting and retry logic
- How to parse JSON responses and transform them into usable data

## Core Concepts
- Data Injection: importing data from external sources into your system
- API Communication: sending requests to remote servers and receiving responses
- Robust Data Collection: building scripts that can handle errors, delays, and API limits
- Data Lake Preparation: storing raw data in a centralized location for future processing

## Project Workflow
1. Choose a public API
2. Send requests to retrieve data
3. Handle pagination when results span multiple pages
4. Manage errors and rate limits gracefully
5. Save the collected data for downstream use

## Repository Structure
```text
apis/
├── 0-passengers.py
├── 1-sentience.py
├── 2-user_location.py
├── 3-first_launch.py
├── 4-rocket_frequency.py
└── README.md
```

## Skills Developed
This module builds practical engineering skills in:
- HTTP GET requests
- Pagination handling
- Rate limiting awareness
- JSON parsing and manipulation
- Automated data collection pipelines

## Context
This project is part of the Holberton School Machine Learning Pipeline track and focuses on the foundational step of creating reliable data ingestion pipelines for real-world applications.
