# Retroactive Hourly Sales Script (CLI Version)

This project builds upon the original Revel Hourly Sales Data Automation script, introducing a command-line interface (CLI) that allows the user to specify a retroactive date for generating hourly sales reports. This enhancement is essential for instances where the server was down, or the daily report failed to run, providing the flexibility to manually generate reports for previous days.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Improvements](#improvements)

## Introduction

This version of the script offers the additional functionality of generating sales reports for a specified date. While the original script only ran reports for the previous day, this reworked version allows the user to enter a specific date through the CLI. This was necessary because there have been occasions where reports needed to be generated manually, sometimes even up to a year in the past, due to server issues or missed report runs.

Previously, adjusting the system date was the workaround for running older reports, but this approach failed when dates exceeded the current year. The CLI version eliminates this limitation by allowing users to input any date directly, simplifying the process of generating historical reports.

## Features

- Pulls hourly sales data from the Revel API based on a user-specified date.
- Allows retroactive report generation for any past date within sites data retention plan.
- Automates filtering, formatting, and report generation processes, with the option to select any specific date.
- Exports filtered data to an .xlsx file while maintaining pivot table formatting.
- Sends the final report via email to the requested recipients.

## Installation

1. Clone the repository:
    ```sh
    git https://github.com/BLibs/Retroactive_Hourly_Sales.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Retroactive_Hourly_Sales
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Update the `config.py` file in the project directory and define the following variables:

```python
# API Key for making calls for data
API_KEY = "API key goes here"

# Excel file PW
EXCEL_PW = "Excel file password goes here"

# Path to the report file with data linkage and pivot tables. This is the one that is sent when ran
PATH = r"C:\PATH TO FILE GOES HERE"

# Email based variables
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'Gmail account address would go here (sender)'
EMAIL_PASSWORD = 'Gmail account password goes here'
RECIPIENT_EMAIL = ['Recipient email address goes here (can be a list of multiple recipients)']
```

## Usage 

The script can either be ran directly as a Python file or compiled into an .exe with Pyinstaller
- Run the script to start the automation process:
    ```sh
    python main.py
    ```
- Compile the .exe which can then be ran in any environment.
    ```sh
    pyinstaller --onefile --clean main.py

## Improvements

1. Improve handling of directory structure to allow for seamless use in any environment.
