from config import *
from datetime import date, datetime
from email_file import send_report_email
from file_handling import handle_file
from get_data import get_data, get_date_from_offset
import pandas as pd
import time


''' Reworking of the original script to run this report. This version operates in a CLI, taking a retroactive date
    as input from the user. This date is then used to offset the get_data function, pulling the hourly sales from the 
    exact date requested. This is necessary because there have been times when the server was down and the report did 
    not run, and the report had to be manually generated for previous days. 
    
    This process involved usually just setting the Windows settings back to the required date, but when those dates 
    exceeded the current year, it would fail. There have been requests for going back as far as a year for one of these 
    reports.'''

''' This project is designed to pull data from the Revel Hourly Sales API endpoint. This project is necessary
    because there is no single report that can pull this data for all establishments at once. The unnamed 
    corporation in this example runs these reports daily for all establishments. They would then take the data
    from those reports and put them in an Excel file for analysis. This turned into a time consuming process.
    
    Pulling the data from the API endpoint, a dataframe is used to store everything. The data is then filtered 
    based on a few conditions, including the hours of operation for the establishments and the filters that they 
    include when running the numbers. Filtered data is then output to an .xlsx file to generate a report.
    
    The report is generated from a linked .xlsx file using pivot tables for formatting. Overwriting the file directly
    would have removed formatting, so data linkage was the best option. 
    
    The report is handled to ensure that the data connection is updating and that the file is saving, which is all
    done through controlling the operating system (Windows in this case).
    
    Once completed, the report is emailed to the requested recipients. This runs as an .exe file linked to a 
    scheduled task on the operating system daily.  '''


# Main application logic
def main(date_offset):
    # Getting the data. Returns a filtered dataframe
    df = get_data(date_offset)

    # Export to Excel file
    output_path = 'output.xlsx'
    with pd.ExcelWriter(output_path) as writer:
        df.to_excel(writer, index=False)

    # Handle the file (OS operations to update report file with output.xlsx data)
    handle_file(PATH)
    time.sleep(5)

    # Email the file
    send_report_email(PATH, f"{ABR_EST_NAME} Hourly Sales File " + get_date_from_offset(date_offset))


if __name__ == "__main__":
    # Boolean check to see if the date is valid
    valid_date = None

    print("Pull data from a specific date")

    # For as long as we need to, get user input on date parameters (YYYY, MM, DD)
    while True:
        # Until we get an int as the input, keep asking for the year
        while True:
            try:
                year = int(input("Year: "))
                break
            # Throw error each time one is applicable
            except Exception as e:
                print(e)
        # Do the same thing for month...
        while True:
            try:
                month = int(input("Month: "))
                break
            except Exception as e:
                print(e)
        # And for day
        while True:
            try:
                day = int(input("Day: "))
                break
            except Exception as e:
                print(e)
        # Checking to see if the date is valid by passing to datetime. Will throw Exception if not
        try:
            datetime(year, month, day)
            valid_date = True
        # Print exception thrown, start at the top of the loop
        except Exception as e:
            valid_date = False
            print(f"Exception was thrown: {e}")

        # If it is a valid date...
        if valid_date:
            # Get a date object from params
            target_date = date(year, month, day)

            # Get today's date
            today = datetime.now().date()

            # Find how many days it has been since the requested date
            offset = today - target_date
            offset = offset.days

            # Pass this parameter to main function
            main(offset)

            # Break the while loop (can be removed to allow for reports to be run one after another)
            break
