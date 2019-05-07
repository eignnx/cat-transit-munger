import os
import csv

import parsers

FEED_URL = r"https://www.cattransit.com/GoogleTransit/Google%20Transit/GoogleTransitUpload.zip"

file_parsers = {
    "stops.txt": parsers.stop,
    "calendar_dates.txt": parsers.calendar_date,
    "agency.txt": parsers.agency,
    "trips.txt": parsers.trip,
    "stop_times.txt": parsers.stop_time,
    "routes.txt": parsers.route,
    "calendar.txt": parsers.calendar,
    "shapes.txt": parsers.shape,
}


def read_data():
    data = dict()
    for filename, parser in file_parsers.items():
        parsed_rows = []
        with open(f"./data/{filename}", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                parsed = parser.parse_row(row)
                parsed_rows.append(parsed)
        data[filename] = parsed_rows
    return data


def munge():
    for filename in os.listdir("./data"):
        print(filename)
        with open(f"./data/{filename}", "r", newline="") as file:
            reader = csv.DictReader(file)
            first = next(reader)
            print(first)
        print()



